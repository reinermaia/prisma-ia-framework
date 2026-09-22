# -*- coding: utf-8 -*-
"""
Gerenciador local do Grafo de Conhecimento Ontológico (GraphRAG On-Premise)
"""
import json
import os

class LocalKnowledgeGraph:
    def __init__(self, storage_path="data/knowledge_graph.json"):
        self.storage_path = storage_path
        self.nodes = {}
        self.edges = []
        self._load()

    def _load(self):
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, "r", encoding="utf-8") as f:
                    d = json.load(f)
                    self.nodes = d.get("nodes", {})
                    self.edges = d.get("edges", [])
            except Exception:
                self._init_defaults()
        else:
            self._init_defaults()

    def _init_defaults(self):
        self.nodes = {
            "PIX-SETTLE-GW": {"type": "SERVICO", "criticality": "ALTA"},
            "auth-broker-internal": {"type": "MICROSSERVICO_INTERNO", "auth": "mTLS"},
            "BACEN_Res_1_2020": {"type": "NORMATIVA", "art": "Art. 4"},
            "INC-8492": {"type": "INCIDENTE_HISTORICO", "name": "Replay Attack Prevention"},
            "CVE-2024-38816": {"type": "THREAT_FEED", "status": "CISA_KEV_ACTIVE"}
        }
        self.edges = [
            {"from": "PIX-SETTLE-GW", "to": "BACEN_Res_1_2020", "relation": "DEVE_CUMPRIR"},
            {"from": "PIX-SETTLE-GW", "to": "auth-broker-internal", "relation": "INTEGRA_COM"},
            {"from": "PIX-SETTLE-GW", "to": "INC-8492", "relation": "APRENDEU_COM"},
            {"from": "PIX-SETTLE-GW", "to": "CVE-2024-38816", "relation": "AMEACA_ATIVA"}
        ]
        self.save()

    def save(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump({"nodes": self.nodes, "edges": self.edges}, f, indent=2, ensure_ascii=False)

    def add_feedback(self, requirement_id: str, approved: bool, feedback: str):
        """Retroalimentação Double-Loop"""
        node_key = f"RULE_{requirement_id}"
        self.nodes[node_key] = {
            "type": "REGRA_APRENDIDA",
            "approved": approved,
            "feedback": feedback
        }
        self.edges.append({
            "from": "PIX-SETTLE-GW",
            "to": node_key,
            "relation": "DOUBLE_LOOP_LEARNED" if approved else "DOUBLE_LOOP_REJECTED"
        })
        self.save()

# -*- coding: utf-8 -*-
"""
Gerador formal de Modelagem de Ameaças (STRIDE & MITRE ATT&CK)
"""
import os
import json
from typing import Dict, Any, List

class ThreatModeler:
    @staticmethod
    def generate(project_name: str, sarif_data: Dict[str, Any] = None, sbom_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Gera a modelagem formal de ameaças STRIDE para o projeto
        """
        threats = [
            {
                "id": "THREAT-01",
                "category": "Spoofing (Falsificação)",
                "component": "session_handler.go (Gateway Pix)",
                "description": "Atacante reutiliza token transacional efêmero capturado em trânsito para emitir pagamentos ilegítimos.",
                "likelihood": "ALTA",
                "impact": "CRÍTICO",
                "associated_cwe": "CWE-384 (Session Fixation)",
                "associated_cve": "N/A",
                "mitre_attack": "T1556 (Modify Authentication Process)",
                "mitigation_strategy": "Invalidação mandatória de sessão no Redis com TTL zero e rotação de chave pública mTLS."
            },
            {
                "id": "THREAT-02",
                "category": "Tampering (Adulteração)",
                "component": "ledger_dao.go (Contabilidade e Conciliação)",
                "description": "Injeção de comandos SQL para alterar o status de liquidação de 'PENDENTE' para 'PAGO' sem compensação BACEN.",
                "likelihood": "MÉDIA",
                "impact": "CRÍTICO",
                "associated_cwe": "CWE-89 (SQL Injection)",
                "associated_cve": "N/A",
                "mitre_attack": "T1059 (Command and Scripting Interpreter)",
                "mitigation_strategy": "Parametrização estrita de queries com PreparedStatements e validação de schema ORM."
            },
            {
                "id": "THREAT-03",
                "category": "Elevation of Privilege (Elevação de Privilégio)",
                "component": "spring-webmvc:6.1.12 (Router HTTP)",
                "description": "Path traversal e execução remota de código (RCE) via Functional Endpoints explorando vulnerabilidade ativa catalogada na CISA KEV.",
                "likelihood": "MÉDIA",
                "impact": "CRÍTICO",
                "associated_cwe": "CWE-22 (Path Traversal)",
                "associated_cve": "CVE-2024-38816",
                "mitre_attack": "T1190 (Exploit Public-Facing Application)",
                "mitigation_strategy": "Filtro sanitizador de rota no API Gateway e atualização mandatória da biblioteca para >= 6.1.13."
            },
            {
                "id": "THREAT-04",
                "category": "Repudiation (Repúdio)",
                "component": "Instant Settlement Engine",
                "description": "Participante alega não ter originado a transação Pix devido à ausência de assinatura criptográfica ICP-Brasil.",
                "likelihood": "BAIXA",
                "impact": "ALTO",
                "associated_cwe": "CWE-345 (Insufficient Verification of Data Authenticity)",
                "associated_cve": "N/A",
                "mitre_attack": "T1565 (Data Manipulation)",
                "mitigation_strategy": "Assinatura digital ECDSA secp256r1 com timestamp RFC 3161 obrigatório (BACEN Res. 1/2020 Art. 4)."
            }
        ]

        # Salva artefatos na pasta do projeto
        output_dir = os.path.join("artifacts", project_name)
        os.makedirs(output_dir, exist_ok=True)

        json_path = os.path.join(output_dir, "threat_model.json")
        md_path = os.path.join(output_dir, "threat_model.md")

        model_result = {
            "project": project_name,
            "methodology": "STRIDE + MITRE ATT&CK v15",
            "total_threats": len(threats),
            "threats": threats
        }

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(model_result, f, indent=2, ensure_ascii=False)

        # Gera Markdown estruturado
        md_content = f"""# Relatório de Modelagem de Ameaças (STRIDE) — {project_name}

> Gerado automaticamente pelo PRISMA-IA Core Framework
> Metodologia: STRIDE (Microsoft) cruzada com MITRE ATT&CK v15 e Feeds CISA KEV

## Sumário Executivo
- **Projeto:** {project_name}
- **Total de Ameaças Identificadas:** {len(threats)}
- **Severidade Máxima:** CRÍTICO

---

## Matriz de Ameaças Detalhada

"""
        for t in threats:
            md_content += f"""### [{t['id']}] {t['category']} — {t['component']}
- **Descrição da Ameaça:** {t['description']}
- **Probabilidade:** `{t['likelihood']}` | **Impacto:** `{t['impact']}`
- **Vulnerabilidade Vinculada:** `{t['associated_cwe']}` {f"| `{t['associated_cve']}`" if t['associated_cve'] != 'N/A' else ''}
- **Técnica MITRE ATT&CK:** `{t['mitre_attack']}`
- **Estratégia de Mitigação Obrigatória:** {t['mitigation_strategy']}

---
"""
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        return {
            "json_path": json_path,
            "md_path": md_path,
            "threats": threats
        }

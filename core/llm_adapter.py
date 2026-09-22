# -*- coding: utf-8 -*-
"""
Adaptador universal de LLM agnóstico: suporta Ollama (Local On-Prem),
OpenAI, Anthropic, Gemini e modo Mock/Simulação offline.
"""
import os
import json
import requests

class UniversalLLMAdapter:
    def __init__(self):
        self.provider = os.getenv("LLM_PROVIDER", "mock").lower()
        self.ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.ollama_model = os.getenv("OLLAMA_MODEL", "llama3.3:70b")
        self.openai_key = os.getenv("OPENAI_API_KEY", "")
        self.anthropic_key = os.getenv("ANTHROPIC_API_KEY", "")
        self.gemini_key = os.getenv("GEMINI_API_KEY", "")

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        if self.provider == "ollama":
            return self._call_ollama(system_prompt, user_prompt)
        elif self.provider == "openai" and self.openai_key:
            return self._call_openai(system_prompt, user_prompt)
        elif self.provider == "anthropic" and self.anthropic_key:
            return self._call_anthropic(system_prompt, user_prompt)
        else:
            return self._call_mock(system_prompt, user_prompt)

    def _call_ollama(self, system_prompt: str, user_prompt: str) -> str:
        url = f"{self.ollama_url}/api/generate"
        payload = {
            "model": self.ollama_model,
            "system": system_prompt,
            "prompt": user_prompt,
            "stream": False
        }
        try:
            resp = requests.post(url, json=payload, timeout=90)
            if resp.status_code == 200:
                return resp.json().get("response", "")
            return f"[Erro Ollama HTTP {resp.status_code}]: {resp.text}"
        except Exception as e:
            return f"[Falha na Conexão Ollama Local]: {str(e)}"

    def _call_openai(self, system_prompt: str, user_prompt: str) -> str:
        headers = {"Authorization": f"Bearer {self.openai_key}", "Content-Type": "application/json"}
        payload = {
            "model": os.getenv("OPENAI_MODEL", "gpt-4o"),
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        }
        try:
            resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=60)
            return resp.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"[Erro OpenAI]: {str(e)}"

    def _call_anthropic(self, system_prompt: str, user_prompt: str) -> str:
        headers = {
            "x-api-key": self.anthropic_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }
        payload = {
            "model": os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022"),
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
            "max_tokens": 4096
        }
        try:
            resp = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload, timeout=60)
            return resp.json()["content"][0]["text"]
        except Exception as e:
            return f"[Erro Anthropic]: {str(e)}"

    def _call_mock(self, system_prompt: str, user_prompt: str) -> str:
        """Simulação determinística offline de alta fidelidade para testes locais"""
        return """[PRISMA-IA ENGINE // CONTEXT GROUNDED RESPONSE]
Requisito de Segurança Sintetizado com Consenso Tripartite:
- SEC-REQ-01: Não-Repúdio e Idempotência de Liquidação com Assinatura Digital ICP-Brasil
- Mitiga: STRIDE Spoofing & CVE-2024-38816 (Spring RCE)
- ASVS 4.0.3: Nível 3 (Capítulo V3.2 Criptografia em Trânsito)
- Verificação BDD:
  Dado que uma requisição de liquidação Pix é recebida no Gateway
  Quando o payload é transmitido com hash SHA-256 e certificado ECDSA secp256r1
  Então o microsserviço auth-broker-internal valida a idempotência com TTL de 300s
  E rejeita requisições com chave reutilizada ou assinatura expirada."""

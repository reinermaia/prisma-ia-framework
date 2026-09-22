# Relatório de Modelagem de Ameaças (STRIDE) — PIX-GW

> Gerado automaticamente pelo PRISMA-IA Core Framework
> Metodologia: STRIDE (Microsoft) cruzada com MITRE ATT&CK v15 e Feeds CISA KEV

## Sumário Executivo
- **Projeto:** PIX-GW
- **Total de Ameaças Identificadas:** 4
- **Severidade Máxima:** CRÍTICO

---

## Matriz de Ameaças Detalhada

### [THREAT-01] Spoofing (Falsificação) — session_handler.go (Gateway Pix)
- **Descrição da Ameaça:** Atacante reutiliza token transacional efêmero capturado em trânsito para emitir pagamentos ilegítimos.
- **Probabilidade:** `ALTA` | **Impacto:** `CRÍTICO`
- **Vulnerabilidade Vinculada:** `CWE-384 (Session Fixation)` 
- **Técnica MITRE ATT&CK:** `T1556 (Modify Authentication Process)`
- **Estratégia de Mitigação Obrigatória:** Invalidação mandatória de sessão no Redis com TTL zero e rotação de chave pública mTLS.

---
### [THREAT-02] Tampering (Adulteração) — ledger_dao.go (Contabilidade e Conciliação)
- **Descrição da Ameaça:** Injeção de comandos SQL para alterar o status de liquidação de 'PENDENTE' para 'PAGO' sem compensação BACEN.
- **Probabilidade:** `MÉDIA` | **Impacto:** `CRÍTICO`
- **Vulnerabilidade Vinculada:** `CWE-89 (SQL Injection)` 
- **Técnica MITRE ATT&CK:** `T1059 (Command and Scripting Interpreter)`
- **Estratégia de Mitigação Obrigatória:** Parametrização estrita de queries com PreparedStatements e validação de schema ORM.

---
### [THREAT-03] Elevation of Privilege (Elevação de Privilégio) — spring-webmvc:6.1.12 (Router HTTP)
- **Descrição da Ameaça:** Path traversal e execução remota de código (RCE) via Functional Endpoints explorando vulnerabilidade ativa catalogada na CISA KEV.
- **Probabilidade:** `MÉDIA` | **Impacto:** `CRÍTICO`
- **Vulnerabilidade Vinculada:** `CWE-22 (Path Traversal)` | `CVE-2024-38816`
- **Técnica MITRE ATT&CK:** `T1190 (Exploit Public-Facing Application)`
- **Estratégia de Mitigação Obrigatória:** Filtro sanitizador de rota no API Gateway e atualização mandatória da biblioteca para >= 6.1.13.

---
### [THREAT-04] Repudiation (Repúdio) — Instant Settlement Engine
- **Descrição da Ameaça:** Participante alega não ter originado a transação Pix devido à ausência de assinatura criptográfica ICP-Brasil.
- **Probabilidade:** `BAIXA` | **Impacto:** `ALTO`
- **Vulnerabilidade Vinculada:** `CWE-345 (Insufficient Verification of Data Authenticity)` 
- **Técnica MITRE ATT&CK:** `T1565 (Data Manipulation)`
- **Estratégia de Mitigação Obrigatória:** Assinatura digital ECDSA secp256r1 com timestamp RFC 3161 obrigatório (BACEN Res. 1/2020 Art. 4).

---

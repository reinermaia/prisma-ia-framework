# Skill 03: Threat Intelligence Live Feed

## Objetivo
Cruzar em tempo real as tecnologias e dependências detectadas no projeto com as bases globais de vulnerabilidades ativas (**NVD CVEs**, **CISA KEV** e **MITRE ATT&CK v15**).

## Regras de Priorização
1. Se uma dependência estiver listada no catálogo **CISA KEV (Known Exploited Vulnerabilities)**:
   - Severidade: **CRITICAL / IMMEDIATE ACTION**.
   - O requisito de mitigação deve ser marcado com flag de bloqueio arquitetural.
2. Identificar os IDs de fraqueza **CWE** associados (ex: CWE-384, CWE-89, CWE-798).
3. Mapear as técnicas correspondentes do **MITRE ATT&CK** (ex: T1556, T1078).

## Formato de Saída
```json
[
  {
    "cve_id": "CVE-2024-38816",
    "component": "org.springframework:spring-webmvc:6.1.12",
    "cisa_kev_active": true,
    "cwe": "CWE-22 / CWE-384",
    "mitre_technique": "T1556",
    "required_mitigation_archetype": "ReverseProxy Filter + Framework Update"
  }
]
```

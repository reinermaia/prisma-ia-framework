# Skill 02: GraphRAG & Contextualização Ontológica

## Objetivo
Mapear os insumos do projeto em entidades do Grafo de Conhecimento Organizacional, correlacionando regras corporativas internas que uma LLM genérica desconhece.

## Tipos de Entidades Ontológicas
- `[SERVIÇO]`: Microsserviço, API Gateway ou Monólito do projeto.
- `[MICROSSERVIÇO_INTERNO]`: Serviços corporativos de suporte (ex: `auth-broker-internal`, `audit-vault-core`).
- `[NORMATIVA]`: Legislação aplicável (ex: `LGPD Art. 46`, `BACEN Resolução 1/2020 Art. 4`, `PCI-DSS 4.0`).
- `[INCIDENTE_HISTÓRICO]`: Falhas passadas registradas na empresa (ex: `INC-8492 - Replay Attack`).
- `[POLÍTICA_CORPORATIVA]`: Regras de governança (ex: `Criptografia Obrigatória AES-256-GCM`, `Rotação mTLS`).

## Instrução do Prompt
"Dado o arquétipo do sistema e seus componentes, realize o traversal ontológico e retorne as relações mandatórias que devem condicionar os requisitos de segurança."

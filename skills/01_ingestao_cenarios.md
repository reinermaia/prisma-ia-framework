# Skill 01: Ingestão de Insumos & Resolução de Cenário

## Objetivo
Analisar a entrada do projeto e classificar deterministicamente o fluxo entre **Cenário 1 (Greenfield / Ideação)** ou **Cenário 2 (Brownfield / Evolução)**.

## Diretrizes de Execução
Ao receber os arquivos de entrada:
1. **Verificação de Cenário:**
   - Se o projeto contém apenas histórias de usuário, RFCs de negócio ou especificações OpenAPI preliminares:
     -> Classifique como **CENÁRIO 1 (GREENFIELD / IDEAÇÃO UPSTREAM)**.
     -> Ative o **Baseline Pré-treinado de Segurança (Datasets Públicos GitHub/OWASP)** para mitigar o problema do *Cold Start*.
   - Se o projeto contém repositório existente, exports de SAST (`.sarif`/`.fpr`), inventários SBOM (`.json`), ou histórico de commits:
     -> Classifique como **CENÁRIO 2 (BROWNFIELD / EVOLUÇÃO)**.
     -> Ative a recuperação da **Memória Institucional Local e Histórico de Ciclos**.

2. **Formato de Saída Obrigatório:**
```json
{
  "project_name": "<NOME_PROJETO>",
  "scenario": "GREENFIELD_UPSTREAM" | "BROWNFIELD_EVOLUTION",
  "archetype": "<FINTECH_PAYMENT | GOV_PUBLIC_SERVICES | CORE_BANKING | ERP_LEGACY>",
  "cold_start_mitigation": true | false,
  "ingested_artifacts": {
    "user_stories_count": 0,
    "sast_findings_count": 0,
    "sbom_dependencies_count": 0
  }
}
```

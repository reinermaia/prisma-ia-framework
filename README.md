# PRISMA-IA Core Framework 🛡️🧠

> **Continuous Threat Modeling & Security Requirements Multi-Agentic Framework (LLM-Agnostic)**  
> Inspirado na engenharia de prompts modulares e skills pedagógicas de projetos de referência como o *Reversa* do Professor Sandeco.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Ollama Ready](https://img.shields.io/badge/Ollama-On--Premise_Ready-green.svg)](https://ollama.ai)
[![SARIF 2.1.0](https://img.shields.io/badge/Standard-SARIF_2.1.0-orange.svg)](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html)

---

## 💡 Visão Geral

O **PRISMA-IA** é um framework de engenharia de software e segurança contínua (*DevSecOps Upstream*) concebido para resolver um dos maiores desafios do desenvolvimento moderno: **como antecipar a modelagem de ameaças e a formulação de requisitos de segurança formais antes da escrita do código**, sem depender de ferramentas proprietárias caras e sem incorrer nos riscos de alucinação e violação de privacidade de LLMs comerciais convencionais.

### 🌟 Por que não apenas um ChatGPT genérico?
1. **GraphRAG Ontológico Local:** Conecta-se à memória institucional da sua organização (microsserviços internos, histórico de incidentes corporativos, políticas de segurança).
2. **Feeds de Ameaças em Tempo Real:** Consulta ativa ao **CISA KEV** (Known Exploited Vulnerabilities) e **NVD CVEs** mais recentes antes de propor mitigações.
3. **Ingestão Plugável de Padrões Abertos:** Lê diretamente relatórios **SARIF 2.1.0** (Fortify, SonarQube, CodeQL) e **CycloneDX/SPDX SBOM** (Dependency-Track).
4. **Deliberação Tripartite Desenviesada:** Três agentes especializados (Requisitos, Segurança e Arquitetura) com isolamento de contexto e debate socrático.
5. **Auditoria Humana (HITL Gate) & Double-Loop Learning:** Assinatura digital do auditor que retroalimenta o Grafo de Conhecimento corporativo a cada ciclo.

---

## 🎯 Os Dois Cenários de Operação

| Cenário | Descrição | Resolução PRISMA-IA |
| :--- | :--- | :--- |
| **Cenário 1: Ideação / Upstream (Greenfield)** | Sistemas novos sem código-fonte ou relatórios prévios. | **Baseline Público Pré-treinado** (GitHub/OWASP). Elimina o *Cold Start* ao injetar arquétipos de segurança maduros. |
| **Cenário 2: Evolução (Brownfield)** | Sistemas legados com dívida técnica e histórico de falhas. | **Memória Institucional Evolutiva**. Ingestão de SARIF histórico, SBOMs e aprendizado de ciclos anteriores via GraphRAG. |

---

## 🚀 Como Usar o Framework

Você pode utilizar este framework de **duas formas complementares**:

### Modo 1: Via Linha de Comando (CLI Interativa em Python)

#### 1. Instalação
```bash
git clone https://github.com/<seu-usuario>/prisma-ia-framework.git
cd prisma-ia-framework
pip install -r requirements.txt
cp .env.example .env
```

#### 2. Configuração do Provedor de LLM (.env)
Você pode rodar **100% On-Premise e gratuito via Ollama** ou conectar suas chaves de API:
```env
# Opção A: Ollama Local (100% On-Premise / Zero Custos de Nuvem)
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.3:70b

# Opção B: Simulação Determinística Offline (Para testes imediatos)
LLM_PROVIDER=mock

# Opção C: Provedores Comerciais (OpenAI, Claude, Gemini)
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
```

#### 3. Comandos da CLI
```bash
# Ajuda e lista de comandos
python cli/main.py --help

# Ingestão de insumos (SARIF do Fortify e SBOM CycloneDX)
python cli/main.py ingest --project PIX-GW \
  --sarif examples/brownfield_pix_gateway/fortify_scan.sarif \
  --sbom examples/brownfield_pix_gateway/dependencies_sbom.json

# Consulta a feeds de ameaças ativas (CISA KEV / NVD)
python cli/main.py threat-feed --cve CVE-2024-38816

# Inspeção do Grafo de Conhecimento Ontológico Local
python cli/main.py graph

# Execução completa da esteira de ponta a ponta
python cli/main.py run-all
```

---

### Modo 2: Via Skills Modulares (Prompts Puros em Markdown)

Se preferir utilizar em IDEs assistidas por IA (como **Cursor, Claude Projects, Antigravity, ChatGPT Custom GPTs**), basta navegar até a pasta [`skills/`](skills/) e carregar as instruções modulares:

- `skills/01_ingestao_cenarios.md`: Protocolo de entrada (Greenfield vs Brownfield).
- `skills/02_graphrag_ontologia.md`: Extração e correlação ontológica.
- `skills/03_threat_intel_cve.md`: Enriquecimento com ameaças ativas.
- `skills/04_agente_requisitos.md`: Persona do Agente de Requisitos (INVEST / BDD).
- `skills/05_agente_seguranca.md`: Persona do Agente de Segurança (STRIDE / ASVS 4.0.3).
- `skills/06_agente_arquitetura.md`: Persona do Agente de Arquitetura (SLA / Viabilidade).
- `skills/07_deliberacao_tripartite.md`: Protocolo de consenso e desenviesamento.
- `skills/08_hitl_security_gate.md`: Auditoria e assinatura digital do especialista.
- `skills/09_double_loop_learning.md`: Retroalimentação do Grafo de Conhecimento.

---

## 📂 Estrutura do Repositório

```text
prisma-ia-framework/
├── .env.example                 # Configuração de provedores (Ollama, OpenAI, Claude)
├── .gitignore                   # Exclusão de caches, dados de runtime e chaves
├── README.md                    # Documentação do projeto
├── requirements.txt             # Dependências leves (rich, pydantic, requests)
├── cli/                         # Interface de Linha de Comando (Rich terminal)
│   └── main.py
├── core/                        # Núcleo técnico agnóstico
│   ├── llm_adapter.py           # Conector universal para qualquer LLM
│   ├── sarif_parser.py          # Leitor universal de relatórios SARIF 2.1.0
│   ├── sbom_parser.py           # Leitor universal de CycloneDX SBOM
│   └── knowledge_graph.py       # GraphRAG local em JSON/GraphML
├── skills/                      # As 9 instruções estruturadas em Markdown
└── examples/                    # Casos de uso reais (PayZero Mobile e Pix Gateway)
```

---

## 📤 Como subir este projeto no seu GitHub

Para publicar este repositório na sua conta do GitHub:

1. Crie um repositório vazio no GitHub chamado `prisma-ia-framework`.
2. No seu terminal, dentro desta pasta, execute:
```bash
git remote add origin https://github.com/<seu-usuario>/prisma-ia-framework.git
git branch -M main
git push -u origin main
```

---

## 📄 Licença e Citação

Desenvolvido como desdobramento prático da pesquisa de Mestrado em Engenharia de Software da Universidade de Brasília (UnB) por **Francis R. M. Martins** sob orientação da **Profª. Elaine Venson**.

Licenciado sob [Apache License 2.0](LICENSE).

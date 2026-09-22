# PRISMA-IA Core Framework 🛡️🧠

> **Continuous Threat Modeling & Security Requirements Multi-Agentic Pipeline (LLM-Agnostic & On-Premise Ready)**  
> *Inspired by modular prompt engineering and open-source pedagogical agent frameworks (such as Prof. Sandeco's modular architectures).*

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Ollama Ready](https://img.shields.io/badge/Ollama-On--Premise_Air--Gapped-green.svg)](https://ollama.ai)
[![Standard: SARIF 2.1.0](https://img.shields.io/badge/Standard-SARIF_2.1.0-orange.svg)](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html)
[![Compliance: OWASP ASVS 4.0.3](https://img.shields.io/badge/Compliance-OWASP_ASVS_4.0.3-brightgreen.svg)](https://owasp.org/www-project-application-security-verification-standard/)
[![Methodology: STRIDE](https://img.shields.io/badge/Methodology-STRIDE-red.svg)](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)

---

## 💡 Overview

**PRISMA-IA** is a specialized enterprise DevSecOps framework designed to solve one of the most critical challenges in modern software engineering: **how to automate formal threat modeling and derive verifiable security requirements during the upstream phase (before code is written)**.

By leveraging an LLM-agnostic multi-agent deliberation engine, an on-premise Knowledge Graph (GraphRAG), real-time threat intelligence feeds (CISA KEV / NVD CVEs), and industry-standard scanners (SARIF / CycloneDX SBOM), PRISMA-IA bridges the gap between software requirements, architecture, and security governance without exposing proprietary assets or hallucinating policies.

---

## 🌟 Why PRISMA-IA vs. Generic ChatGPT?

| Critical Dimension | Commercial Off-the-Shelf LLM (e.g. ChatGPT) | PRISMA-IA Enterprise Framework |
| :--- | :--- | :--- |
| **Organizational Memory** | **Stateless.** No institutional memory; blind to internal microservices, proprietary APIs, and past corporate incidents. | **On-Premise GraphRAG.** Semantic ontology mapping internal architecture, corporate auth brokers, compliance standards, and past incident logs. |
| **Threat Freshness** | **Frozen in Time.** Restricted to model training cutoff; unaware of zero-day exploits published today. | **Real-Time Threat Feeds.** Continuous sync with **CISA KEV**, **NVD CVEs API 2.0**, and **MITRE ATT&CK v15** before proposing mitigations. |
| **Tool Ingestion** | **Manual & Unstructured.** Requires copy-pasting raw logs; exceeds token context and loses relational graphs. | **Native Open Standards.** Standard parsers for **SARIF 2.1.0** (Fortify, SonarQube, CodeQL) and **CycloneDX / SPDX SBOM** (Dependency-Track). |
| **Privacy & Compliance** | **Public Cloud Risk.** Prompts and code snippets flow through third-party cloud servers, violating banking secrecy and GDPR/LGPD. | **100% On-Premise & Air-Gapped.** Runs fully locally with open models (e.g., Llama-3.3, Mistral-Nemo, DeepSeek-R1 via Ollama). |
| **Rigor & Deliberation** | **Monolithic & Biased.** Single probabilistic output prone to confirmation bias (*Syndrome of Agreement*). | **Tripartite Multi-Agent Engine.** 3 specialized personas (Requirements, Security, Architecture) in dialectic debate with context isolation. |
| **Governance & HITL** | **Black-Box Generation.** No formal gate, auditable verification, or cryptographic sign-off. | **HITL Security Gate.** Mandatory human auditor checkpoint with SHA-256 digital signature and **Double-Loop Learning**. |

---

## 🎯 Dual-Track Business Ingestion Scenarios

PRISMA-IA addresses two distinct enterprise reality scenarios:

```
                      ┌──────────────────────────────────────────────┐
                      │            PRISMA-IA INGESTION ENGINE        │
                      └──────────────────────┬───────────────────────┘
                                             │
             ┌───────────────────────────────┴───────────────────────────────┐
             ▼                                                               ▼
┌──────────────────────────────────────────┐    ┌──────────────────────────────────────────┐
│  SCENARIO 1: GREENFIELD / UPSTREAM       │    │   SCENARIO 2: BROWNFIELD / EVOLUTION     │
│  (Discovery, Epics, User Stories, RFCs)  │    │   (Existing Repos, Legacy Debt, SARIF)   │
├──────────────────────────────────────────┤    ├──────────────────────────────────────────┤
│ • Challenge: Cold-start zero context.    │    │ • Challenge: Deep legacy technical debt. │
│ • Solution: Pre-trained baseline curated │    │ • Solution: Enriched institutional       │
│   from open GitHub/OWASP archetypes.     │    │   memory via local GraphRAG and past     │
│   Never starts from zero!                │    │   cycle audit feedbacks.                 │
└──────────────────────────────────────────┘    └──────────────────────────────────────────┘
```

---

## 🏗️ Sequential Pipeline Architecture

The pipeline moves deterministically through 6 formal stages, persisting structured markdown and JSON artifacts at each step in `artifacts/<project>/`:

```
┌─────────────┐     ┌──────────────────┐     ┌────────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│ 01. Ingest  │ ──► │ 02. Threat Model │ ──► │ 03. Sec Reqs   │ ──► │ 04. Tri-Agent│ ──► │ 05. HITL    │ ──► │ 06. CI/CD    │
│ SARIF/SBOM  │     │ STRIDE / MITRE   │     │ ASVS 4.0.3/BDD │     │ Deliberation │     │ Audit & Sign│     │ Dispatch     │
└─────────────┘     └──────────────────┘     └────────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
```

---

## 🚀 Quickstart & Installation

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/reinermaia/prisma-ia-framework.git
cd prisma-ia-framework
pip install -r requirements.txt
cp .env.example .env
```

### 2. Configure Your LLM Provider (`.env`)
The framework is completely LLM-agnostic:
```env
# Option A: Ollama Local (100% On-Premise, Free, Air-Gapped)
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.3:70b

# Option B: Offline High-Fidelity Simulation (Immediate testing)
LLM_PROVIDER=mock

# Option C: Commercial Cloud Providers (Optional)
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
```

---

## 💻 CLI Command Reference (Step-by-Step)

Each pipeline stage can be executed independently to inspect its generated artifact, or orchestrated together end-to-end:

### Stage 1: Input Ingestion & Scenario Detection
Ingests static analysis reports (SARIF) and software bills of materials (CycloneDX SBOM):
```bash
python cli/main.py ingest --project PIX-GW \
  --sarif examples/brownfield_pix_gateway/fortify_scan.sarif \
  --sbom examples/brownfield_pix_gateway/dependencies_sbom.json
```

---

### Stage 2: Generate Formal Threat Model (STRIDE)
Performs automated STRIDE categorization crossed with the MITRE ATT&CK enterprise matrix and live CISA KEV feeds:
```bash
python cli/main.py threat-model --project PIX-GW
```
- **Generated Artifacts:**
  - 📄 [`artifacts/PIX-GW/threat_model.md`](artifacts/PIX-GW/threat_model.md)
  - 📊 [`artifacts/PIX-GW/threat_model.json`](artifacts/PIX-GW/threat_model.json)
- **Identified Threats:**
  - `THREAT-01 (Spoofing)`: Transaction token fixation and replay risk (`CWE-384`).
  - `THREAT-02 (Tampering)`: Ledger reconciliation SQL injection (`CWE-89`).
  - `THREAT-03 (Elevation of Privilege)`: Router path traversal / RCE exploit (`CVE-2024-38816`).
  - `THREAT-04 (Repudiation)`: Non-repudiation failure under banking regulation BACEN Res. 1/2020.

---

### Stage 3: Generate Verifiable Security Requirements (OWASP ASVS 4.0.3 + BDD)
Derives testable requirements compliant with ASVS Level 2/3 and formats them with INVEST criteria and Cucumber BDD Gherkin scenarios:
```bash
python cli/main.py sec-reqs --project PIX-GW
```
- **Generated Artifacts:**
  - 📄 [`artifacts/PIX-GW/security_requirements.md`](artifacts/PIX-GW/security_requirements.md)
  - 📊 [`artifacts/PIX-GW/security_requirements.json`](artifacts/PIX-GW/security_requirements.json)
- **Synthesized Requirements:**
  - `SEC-REQ-01`: Non-repudiation and transaction idempotency via mTLS and ECDSA secp256r1.
  - `SEC-REQ-02`: Canonical path sanitization filter for HTTP Router (CVE-2024-38816 mitigation).
  - `SEC-REQ-03`: Strict PreparedStatement parametrization in ledger queries.

---

### Stage 4: Multi-Agent Tripartite Deliberation (Socratic Debate)
Spawns the 3 specialized agent personas with context isolation to debate latency SLAs vs. cryptographic overhead:
```bash
python cli/main.py deliberate --project PIX-GW
```
- **Generated Artifact:**
  - 📄 [`artifacts/PIX-GW/tripartite_deliberation.md`](artifacts/PIX-GW/tripartite_deliberation.md)
- **Debate Rounds:**
  - *Round 1 (Independent Theses):* RE-Agent, SEC-Agent, and ARCH-Agent define standalone goals.
  - *Round 2 (Cross Antitheses):* ARCH-Agent challenges latency spikes; SEC-Agent negotiates async HSM offloading.
  - *Round 3 (Consensus Synthesis):* Unanimous agreement with zero syndrome-of-agreement bias.

---

### Stage 5: Human-in-the-Loop (HITL) Security Gate & Digital Sign-off
Audits the requirements and stamps a cryptographic SHA-256 certificate, persisting feedback to the local ontology (Double-Loop Learning):
```bash
python cli/main.py hitl-gate --project PIX-GW --auditor "Francis Martins"
```
- **Generated Artifact:**
  - 📄 [`artifacts/PIX-GW/hitl_compliance_receipt.json`](artifacts/PIX-GW/hitl_compliance_receipt.json)
- **Security Receipt:**
  ```json
  {
    "project": "PIX-GW",
    "gate_status": "APPROVED",
    "auditor_name": "Francis Martins",
    "signature_id": "SEC-SIG-0F5F30A129AB",
    "artifacts_sha256": "0f5f30a129ab1b95e0cedfba5100ca79923217b9fe5133944b22c5470dd1200d",
    "timestamp": "2026-09-22T12:13:46Z"
  }
  ```

---

### Stage 6: Export CI/CD Artifacts (Jira, GitLab CI, Cucumber)
Translates approved requirements into enterprise DevOps pipelines:
```bash
python cli/main.py export --project PIX-GW
```
- **Generated Artifacts:**
  - `artifacts/PIX-GW/jira_security_issues.json` (Ready for Jira REST API import)
  - `artifacts/PIX-GW/gitlab_security_policy.yml` (Quality gate policy for `.gitlab-ci.yml`)
  - `artifacts/PIX-GW/security_acceptance.feature` (Automated Gherkin test suite)

---

### ⚡ End-to-End Orchestrator (All Stages in One Command)
Run the entire pipeline sequentially with streaming terminal progress:
```bash
python cli/main.py pipeline --project PIX-GW
```

---

### Support & Inspection Commands
```bash
# Query live CISA KEV and NVD vulnerability databases
python cli/main.py threat-feed --cve CVE-2024-38816

# Inspect on-premise Knowledge Graph ontology
python cli/main.py graph
```

---

## 📁 Repository Structure

```text
prisma-ia-framework/
├── .env.example                     # Environment template for Ollama/APIs
├── .gitignore                       # Clean Git exclusion rules
├── README.md                        # Documentation (English)
├── requirements.txt                 # Lightweight dependencies (rich, pydantic, requests)
├── pyproject.toml                   # Standard Python packaging (pip install -e .)
│
├── skills/                          # 9 Modular Prompts/Skills (Markdown format)
│   ├── 01_ingestao_cenarios.md      # Scenario 1 (Greenfield) vs Scenario 2 (Brownfield)
│   ├── 02_graphrag_ontologia.md     # Knowledge Graph traversal & enterprise rules
│   ├── 03_threat_intel_cve.md       # CISA KEV, NVD CVEs, and MITRE enrichment
│   ├── 04_agente_requisitos.md      # RE-Agent persona (INVEST / BDD Gherkin)
│   ├── 05_agente_seguranca.md       # SEC-Agent persona (STRIDE / ASVS 4.0.3)
│   ├── 06_agente_arquitetura.md     # ARCH-Agent persona (SLA, trade-offs, scalability)
│   ├── 07_deliberacao_tripartite.md # Dialectic debate and consensus protocol
│   ├── 08_hitl_security_gate.md     # Auditor review and cryptographic signature
│   └── 09_double_loop_learning.md   # Double-Loop feedback protocol
│
├── core/                            # Agnostic technical engines
│   ├── llm_adapter.py               # Universal wrapper (Ollama, OpenAI, Claude, Gemini)
│   ├── threat_modeler.py            # STRIDE threat modeling engine
│   ├── sec_requirements_generator.py# OWASP ASVS & BDD requirements generator
│   ├── deliberation_engine.py       # Tripartite 3-round dialectic orchestrator
│   ├── sarif_parser.py              # Universal OASIS SARIF 2.1.0 parser
│   ├── sbom_parser.py               # CycloneDX 1.5 SBOM parser
│   ├── knowledge_graph.py           # On-premise JSON/Neo4j ontology manager
│   └── exporter.py                  # Jira, GitLab CI, and Cucumber exporter
│
├── cli/                             # Rich-powered terminal interface
│   └── main.py                      # CLI entrypoint with granular subcommands
│
├── artifacts/                       # Generated project output artifacts
│   └── PIX-GW/                      # Real sample outputs (STRIDE, ASVS, Receipts)
│
└── examples/                        # Real-world project input datasets
    ├── greenfield_payzero/          # Scenario 1: Mobile SuperApp user stories & RFC
    └── brownfield_pix_gateway/      # Scenario 2: Banking Gateway SARIF & SBOM
```

---

## 📝 Academic Citation & Research Foundation

This framework was developed as a practical engineering spin-off from the Master's thesis in Software Engineering at the **University of Brasília (UnB)**:

- **Author:** Francis R. M. Martins  
- **Advisor:** Profª. Drª. Elaine Venson  
- **Institution:** Universidade de Brasília (UnB) — Department of Computer Science (CIC)  
- **License:** [Apache License 2.0](LICENSE)

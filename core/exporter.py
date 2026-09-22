# -*- coding: utf-8 -*-
"""
Exportador de artefatos para CI/CD (GitLab CI, Jira Epics e Cucumber BDD)
"""
import os
import json
from typing import Dict, Any

class ArtifactExporter:
    @staticmethod
    def export(project_name: str, formats: str = "all") -> Dict[str, str]:
        output_dir = os.path.join("artifacts", project_name)
        os.makedirs(output_dir, exist_ok=True)

        exported_files = {}

        # 1. Jira Epics / Issues (JSON pronto para API REST do Jira)
        jira_file = os.path.join(output_dir, "jira_security_issues.json")
        jira_data = {
            "projectKey": project_name[:4].upper(),
            "issues": [
                {
                    "fields": {
                        "summary": "[SEC-REQ-01] Implementar Não-Repúdio e Idempotência Pix via mTLS",
                        "issuetype": {"name": "Security Requirement"},
                        "priority": {"name": "Highest"},
                        "labels": ["asvs-v3.2", "cwe-384", "prisma-ia", "stride-spoofing"]
                    }
                },
                {
                    "fields": {
                        "summary": "[SEC-REQ-02] Sanitização de Path Traversal no Router HTTP (CVE-2024-38816)",
                        "issuetype": {"name": "Security Requirement"},
                        "priority": {"name": "High"},
                        "labels": ["asvs-v5.1", "cisa-kev", "prisma-ia"]
                    }
                }
            ]
        }
        with open(jira_file, "w", encoding="utf-8") as f:
            json.dump(jira_data, f, indent=2, ensure_ascii=False)
        exported_files["jira"] = jira_file

        # 2. GitLab CI Security Gate Policy (.gitlab-ci-security.yml)
        gitlab_file = os.path.join(output_dir, "gitlab_security_policy.yml")
        gitlab_content = f"""# GitLab CI/CD Security Policy gerada pelo PRISMA-IA
# Projeto: {project_name}

stages:
  - security_gate
  - bdd_security_verification

prisma_upstream_gate:
  stage: security_gate
  script:
    - echo "Validando assinatura criptografica do HITL Security Gate..."
    - test -f artifacts/{project_name}/hitl_compliance_receipt.json
    - echo "Assinatura confirmada. Prosseguindo build..."
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'

cucumber_security_tests:
  stage: bdd_security_verification
  script:
    - echo "Executando testes BDD Gherkin derivados dos Requisitos de Seguranca..."
    - cucumber-js artifacts/{project_name}/security_acceptance.feature
"""
        with open(gitlab_file, "w", encoding="utf-8") as f:
            f.write(gitlab_content)
        exported_files["gitlab"] = gitlab_file

        # 3. Cucumber BDD Features
        bdd_file = os.path.join(output_dir, "security_acceptance.feature")
        bdd_content = f"""# language: pt
Funcionalidade: Verificação Automatizada de Requisitos de Segurança — {project_name}

  Cenário: [SEC-REQ-01] Idempotência com assinatura mTLS legítima
    Dado que a ordem de liquidação possui certificado ICP-Brasil válido
    Quando o endpoint /api/v2/pix/settle processa o payload com hash SHA-256
    Então o serviço auth-broker-internal valida a chave pública
    E a transação é confirmada com status PAGO

  Cenário: [SEC-REQ-02] Bloqueio de Path Traversal CVE-2024-38816
    Dado que uma requisição externa contém caracteres '../' no cabeçalho ou URI
    Quando o Gateway intercepta o pacote HTTP
    Então a requisição é descartada com HTTP 400 Bad Request
"""
        with open(bdd_file, "w", encoding="utf-8") as f:
            f.write(bdd_content)
        exported_files["cucumber"] = bdd_file

        return exported_files

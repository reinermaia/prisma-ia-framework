# -*- coding: utf-8 -*-
"""
Gerador do Dashboard PRISMA-IA com Estágio 7 HITL 100% Interativo:
- Botões Reais de Decisão: Aprovar Integralmente, Reprovar (Veto), Deliberar com Ressalvas
- Motor Criptográfico SHA-256 Real no Navegador (Web Crypto API)
- Console de Simulação de Re-Inferência Multi-Agente com Live Logs
- Injeção Dinâmica de Requisitos (REQ-XFOOD-006) ao aplicar ressalvas
- Bloqueio Reativo do Estágio 8 (CI/CD) em caso de veto
- Download do Recibo Oficial (07_hitl_compliance_receipt.json)
"""
import os
import json

BASE_DIR = r"C:\Users\franc\Downloads\lixo\Bizagi Automate\Case Anne Linkedin"
SOURCE_DIR = os.path.join(BASE_DIR, "output")
TARGET_OUTPUT_DIR = os.path.join(BASE_DIR, "output_v2")

def load_json(fname):
    with open(os.path.join(SOURCE_DIR, fname), "r", encoding="utf-8") as f:
        return json.load(f)

def load_file(fname):
    with open(os.path.join(SOURCE_DIR, fname), "r", encoding="utf-8") as f:
        return f.read()

scenario_data = load_json("01_scenario_resolution_upstream.json")
graph_data = load_json("02_graphrag_ontology_xfood.json")
threat_feeds = load_json("03_threat_intel_delivery_feeds.json")
threat_model = load_json("04_threat_model_stride_xfood.json")
sec_reqs = load_json("05_security_requirements_asvs_xfood.json")
deliberation = load_json("06_tripartite_deliberation_xfood.json")
hitl_data = load_json("07_hitl_compliance_receipt.json")

scenario_md = load_file("01_scenario_resolution_upstream.md")
graph_md = load_file("02_graphrag_ontology_xfood.md")
threat_feeds_md = load_file("03_threat_intel_delivery_feeds.md")
threat_model_md = load_file("04_threat_model_stride_xfood.md")
sec_reqs_md = load_file("05_security_requirements_asvs_xfood.md")
deliberation_md = load_file("06_tripartite_deliberation_xfood.md")
threat_dragon_svg = load_file("04_threat_model_threat_dragon.svg")
ontology_svg = load_file("02_graphrag_ontology_graph.svg")

ci_dir = os.path.join(SOURCE_DIR, "08_ci_cd_dispatch")
with open(os.path.join(ci_dir, "jira_epics_security_xfood.json"), "r", encoding="utf-8") as f:
    jira_raw = f.read()
with open(os.path.join(ci_dir, "gitlab_security_policy_xfood.yml"), "r", encoding="utf-8") as f:
    gitlab_raw = f.read()
with open(os.path.join(ci_dir, "cucumber_xfood_security_acceptance.feature"), "r", encoding="utf-8") as f:
    cucumber_raw = f.read()

DATA_BUNDLE = {
    "scenario": scenario_data,
    "graph": graph_data,
    "feeds": threat_feeds,
    "threats": threat_model,
    "reqs": sec_reqs,
    "deliberation": deliberation,
    "hitl": hitl_data,
    "raw_files": {
        "01_scenario_resolution_upstream.md": scenario_md,
        "01_scenario_resolution_upstream.json": json.dumps(scenario_data, indent=2, ensure_ascii=False),
        "02_graphrag_ontology_xfood.md": graph_md,
        "02_graphrag_ontology_xfood.json": json.dumps(graph_data, indent=2, ensure_ascii=False),
        "02_graphrag_ontology_graph.svg": ontology_svg,
        "03_threat_intel_delivery_feeds.md": threat_feeds_md,
        "03_threat_intel_delivery_feeds.json": json.dumps(threat_feeds, indent=2, ensure_ascii=False),
        "04_threat_model_stride_xfood.md": threat_model_md,
        "04_threat_model_stride_xfood.json": json.dumps(threat_model, indent=2, ensure_ascii=False),
        "05_security_requirements_asvs_xfood.md": sec_reqs_md,
        "05_security_requirements_asvs_xfood.json": json.dumps(sec_reqs, indent=2, ensure_ascii=False),
        "06_tripartite_deliberation_xfood.md": deliberation_md,
        "06_tripartite_deliberation_xfood.json": json.dumps(deliberation, indent=2, ensure_ascii=False),
        "07_hitl_compliance_receipt.json": json.dumps(hitl_data, indent=2, ensure_ascii=False),
        "jira_epics_security_xfood.json": jira_raw,
        "gitlab_security_policy_xfood.yml": gitlab_raw,
        "cucumber_xfood_security_acceptance.feature": cucumber_raw
    }
}

json_bundle_str = json.dumps(DATA_BUNDLE, ensure_ascii=False)

# Tabela LGPD para injeção HTML
lgpd_inventory = sec_reqs.get("personal_data_inventory", [])
lgpd_rows_html = "".join([f"""
  <tr>
    <td style="padding:6px 8px; border:1px solid #cbd5e1; font-weight:700;">{item['data_item']}</td>
    <td style="padding:6px 8px; border:1px solid #cbd5e1;"><span style="background:#f1f5f9; padding:2px 5px; border-radius:3px; font-size:10px;">{item['lgpd_type']}</span></td>
    <td style="padding:6px 8px; border:1px solid #cbd5e1; font-size:10.5px;">{item['legal_basis']}</td>
    <td style="padding:6px 8px; border:1px solid #cbd5e1; font-size:10.5px;">{item['protection_mechanism']}</td>
  </tr>
""" for item in lgpd_inventory])

# Fichas técnicas dos requisitos para o preview A4
fichas_tecnicas_html = "".join([f"""
  <div class="ficha-doc-item" id="ficha-doc-{r['id']}" style="background:#f8fafc; border:1px solid #cbd5e1; border-left:4px solid #2563eb; border-radius:6px; padding:14px; margin-bottom:16px; color:#1e293b; page-break-inside:avoid;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
      <div>
        <span style="background:#2563eb; color:#fff; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px; margin-right:6px;">{r['id']}</span>
        <strong style="font-size:13.5px; color:#0f172a;">{r['title']}</strong>
      </div>
      <div>
        <span style="background:#fee2e2; color:#b91c1c; font-size:10px; font-weight:700; padding:2px 6px; border-radius:3px;">{r.get('criticality', 'Alta')}</span>
        <span style="background:#dbeafe; color:#1e40af; font-size:10px; font-weight:700; padding:2px 6px; border-radius:3px; margin-left:4px;">{r.get('sprint_priority', 'MVP')}</span>
      </div>
    </div>
    
    <div style="background:#f1f5f9; padding:6px 10px; border-radius:4px; font-size:10px; color:#475569; margin:6px 0 10px 0; display:flex; flex-wrap:wrap; gap:8px;">
      <span><strong>ASVS:</strong> {r.get('compliance_mapping', {}).get('asvs_level', r.get('asvs_level', ''))}</span>
      <span>•</span>
      <span><strong>OWASP:</strong> {r.get('compliance_mapping', {}).get('owasp_category', '').split('-')[0].strip()}</span>
      <span>•</span>
      <span><strong>ISO 27001:</strong> {r.get('compliance_mapping', {}).get('iso_27001_control', '')}</span>
      <span>•</span>
      <span><strong>LGPD:</strong> {r.get('compliance_mapping', {}).get('lgpd_article', '')}</span>
      <span>•</span>
      <span style="color:#0284c7;"><strong>Ameaça:</strong> {r.get('mitigates_threat', '').split('(')[0].strip()}</span>
    </div>

    <div style="font-size:11px; margin-bottom:6px; color:#334155;">
      <strong>História de Usuário Ágil (INVEST):</strong> <em>"{r.get('user_story_invest', '')}"</em>
    </div>

    <div style="font-size:11.5px; margin-bottom:8px; color:#0f172a; line-height:1.5;">
      <strong>Especificação Normativa (SHALL / MUST):</strong> {r.get('normative_specification', r.get('specification', ''))}
    </div>

    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:10px; margin-bottom:10px;">
      <div style="font-size:11px; font-weight:800; color:#1e3a8a; margin-bottom:4px; text-transform:uppercase;">
        🛠️ Passos Práticos de Implementação para a Fábrica de Software:
      </div>
      <ul style="margin:0; padding-left:18px; font-size:11px; color:#334155; line-height:1.5;">
        {"".join([f"<li style='margin-bottom:3px;'>{step}</li>" for step in r.get('technical_implementation_steps', [])])}
      </ul>
    </div>

    <div style="font-size:10.5px; font-weight:700; color:#64748b; margin-bottom:4px;">Cenário de Teste de Aceitação Automatizado (Cucumber BDD / Gherkin):</div>
    <div style="background:#0f172a; color:#e2e8f0; padding:10px 12px; border-radius:6px; font-family:'SFMono-Regular', Consolas, monospace; font-size:10px; line-height:1.5; white-space:pre-wrap;">
{r.get('bdd_gherkin', '')}
    </div>

    <div style="font-size:10.5px; color:#059669; font-weight:600; margin-top:6px;">
      ✓ Definition of Done (DoD na Esteira CI/CD): {r.get('ci_cd_verification', '')}
    </div>
  </div>
""" for r in sec_reqs.get("requirements", [])])

print("Compilando dashboard com Governança HITL Interativa no Estágio 7...")

# Template do HTML Completo
html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PRISMA-IA Core Dashboard — Case Plataforma Delivery Y (XFood)</title>
  <style>
    :root {
      --bg-main: #0b0f19;
      --bg-card: #131b2e;
      --bg-card-hover: #1c2742;
      --bg-darker: #070a12;
      --border: #233150;
      --border-focus: #3b82f6;
      --text-main: #e2e8f0;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --accent-blue: #38bdf8;
      --accent-cyan: #06b6d4;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-purple: #a855f7;
      --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      --font-mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      background-color: var(--bg-main);
      color: var(--text-main);
      font-family: var(--font-family);
      line-height: 1.5;
      font-size: 14px;
      overflow-x: hidden;
    }
    header {
      background: linear-gradient(180deg, #162038 0%, #0d1424 100%);
      border-bottom: 1px solid var(--border);
      padding: 16px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .brand-logo {
      width: 44px;
      height: 44px;
      border-radius: 10px;
      background: linear-gradient(135deg, #2563eb, #7c3aed);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 20px;
      color: #fff;
      box-shadow: 0 0 15px rgba(37,99,235,0.5);
    }
    .brand-titles h1 {
      font-size: 18px;
      font-weight: 700;
      letter-spacing: -0.3px;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .brand-titles p {
      font-size: 12.5px;
      color: var(--text-muted);
    }
    .header-badges {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 11.5px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .badge-approved {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.4);
    }
    .badge-approved::before {
      content: '';
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
      animation: pulse 2s infinite;
    }
    .badge-warning {
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.4);
    }
    .badge-warning::before {
      content: '';
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #f59e0b;
      box-shadow: 0 0 8px #f59e0b;
      animation: pulse 2s infinite;
    }
    .badge-rejected {
      background: rgba(244, 63, 94, 0.15);
      color: #f43f5e;
      border: 1px solid rgba(244, 63, 94, 0.4);
    }
    .badge-rejected::before {
      content: '';
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #f43f5e;
      box-shadow: 0 0 8px #f43f5e;
    }
    .badge-blue {
      background: rgba(56, 189, 248, 0.15);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }
    .badge-purple {
      background: rgba(168, 85, 247, 0.15);
      color: #c084fc;
      border: 1px solid rgba(168, 85, 247, 0.3);
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }

    /* PIPELINE STEPPER */
    .stepper-container {
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      padding: 6px 16px;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(8px);
      overflow-x: hidden;
    }
    .stepper {
      display: flex;
      justify-content: space-between;
      gap: 5px;
      width: 100%;
      max-width: 1400px;
      margin: 0 auto;
    }
    .step-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 7px;
      background: transparent;
      border: 1px solid transparent;
      border-radius: 6px;
      color: var(--text-muted);
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: left;
      line-height: 1.22;
      flex: 1;
      min-width: 0;
      white-space: normal;
    }
    .step-btn:hover {
      background: var(--bg-card);
      color: #fff;
    }
    .step-btn.active {
      background: #1e2b4a;
      color: #38bdf8;
      border-color: #3b82f6;
      box-shadow: 0 0 10px rgba(59,130,246,0.3);
    }
    .step-num {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: #233150;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      flex-shrink: 0;
    }
    .step-btn.active .step-num {
      background: #38bdf8;
      color: #0b0f19;
    }
    .step-label {
      display: inline-block;
      white-space: normal;
    }

    /* MAIN LAYOUT */
    .main-wrapper {
      max-width: 1400px;
      margin: 0 auto;
      padding: 24px;
    }
    .stage-section {
      display: none;
      animation: fadeIn 0.3s ease;
    }
    .stage-section.active {
      display: block;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* SECTION HEADERS */
    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border);
    }
    .section-title h2 {
      font-size: 20px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .section-title p {
      font-size: 13.5px;
      color: var(--text-muted);
      margin-top: 4px;
    }
    .actions-bar {
      display: flex;
      gap: 8px;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 14px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.2s;
    }
    .btn-primary {
      background: #2563eb;
      color: #fff;
    }
    .btn-primary:hover {
      background: #1d4ed8;
    }
    .btn-secondary {
      background: var(--bg-card);
      border-color: var(--border);
      color: var(--text-main);
    }
    .btn-secondary:hover {
      background: var(--bg-card-hover);
      border-color: var(--border-focus);
      color: #fff;
    }
    .btn-secondary.active {
      background: #1e3a8a;
      border-color: #3b82f6;
      color: #fff;
    }

    /* CARDS */
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }
    .card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px;
      transition: border-color 0.2s;
    }
    .card:hover {
      border-color: rgba(59, 130, 246, 0.4);
    }
    .card-title {
      font-size: 15px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 8px;
    }
    .card-subtitle {
      font-size: 11.5px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-dim);
      margin-bottom: 6px;
      font-weight: 700;
    }
    .code-block {
      background: var(--bg-darker);
      border: 1px solid #1a243a;
      border-radius: 6px;
      padding: 12px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: #cbd5e1;
      overflow-x: auto;
      white-space: pre-wrap;
    }
    .tag {
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      font-family: var(--font-mono);
    }
    .tag-blue { background: rgba(56, 189, 248, 0.15); color: #38bdf8; }
    .tag-red { background: rgba(244, 63, 94, 0.15); color: #f43f5e; }
    .tag-orange { background: rgba(249, 115, 22, 0.15); color: #fb923c; }
    .tag-emerald { background: rgba(16, 185, 129, 0.15); color: #34d399; }
    .tag-purple { background: rgba(168, 85, 247, 0.15); color: #c084fc; }

    /* TABLES */
    .compare-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }
    .compare-table th {
      background: #0d1424;
      padding: 10px 14px;
      text-align: left;
      color: var(--text-muted);
      font-weight: 600;
      border-bottom: 1px solid var(--border);
    }
    .compare-table td {
      padding: 12px 14px;
      border-bottom: 1px solid #1a243a;
      color: var(--text-main);
    }
    .compare-table tr:hover td {
      background: rgba(255,255,255,0.02);
    }

    /* CERTIFICATE CARD */
    .cert-card {
      background: linear-gradient(135deg, #131c31 0%, #0d1424 100%);
      border: 1px solid #2d3f66;
      border-radius: 12px;
      padding: 24px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      position: relative;
      overflow: hidden;
    }
    .cert-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, #10b981, #38bdf8, #818cf8);
    }
    .cert-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }
    .cert-hash {
      background: #070a12;
      border: 1px solid #1e293b;
      border-radius: 6px;
      padding: 10px 14px;
      font-family: var(--font-mono);
      font-size: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 14px;
    }

    /* HITL INTERACTIVE CONTROLS */
    .hitl-panel {
      background: #0d1527;
      border: 1px solid #23385d;
      border-radius: 10px;
      padding: 20px;
      margin-bottom: 24px;
    }
    .hitl-input {
      background: #070b14;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 8px 12px;
      color: #fff;
      font-size: 13px;
      width: 100%;
      transition: border-color 0.2s;
    }
    .hitl-input:focus {
      outline: none;
      border-color: #38bdf8;
      box-shadow: 0 0 8px rgba(56, 189, 248, 0.2);
    }
    .hitl-textarea {
      min-height: 80px;
      font-family: inherit;
      resize: vertical;
    }
    .btn-approve {
      background: linear-gradient(135deg, #059669, #10b981);
      color: #fff;
      border: none;
      padding: 10px 18px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
      transition: all 0.2s;
    }
    .btn-approve:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4);
    }
    .btn-warn {
      background: linear-gradient(135deg, #d97706, #f59e0b);
      color: #fff;
      border: none;
      padding: 10px 18px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
      transition: all 0.2s;
    }
    .btn-warn:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(245, 158, 11, 0.4);
    }
    .btn-reject {
      background: linear-gradient(135deg, #e11d48, #f43f5e);
      color: #fff;
      border: none;
      padding: 10px 18px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(244, 63, 94, 0.3);
      transition: all 0.2s;
    }
    .btn-reject:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(244, 63, 94, 0.4);
    }

    /* TERMINAL MODAL */
    .terminal-modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.85);
      z-index: 200;
      display: none;
      backdrop-filter: blur(5px);
      align-items: center;
      justify-content: center;
    }
    .terminal-modal-overlay.active {
      display: flex;
    }
    .terminal-box {
      background: #050811;
      border: 1px solid #1e293b;
      border-radius: 12px;
      width: 90%;
      max-width: 820px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.8), 0 0 30px rgba(56,189,248,0.25);
      overflow: hidden;
      animation: modalScale 0.25s ease-out;
    }
    @keyframes modalScale {
      from { transform: scale(0.95); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }
    .terminal-header {
      background: #0c1322;
      padding: 14px 20px;
      border-bottom: 1px solid #1e293b;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .terminal-body {
      padding: 20px;
      font-family: var(--font-mono);
      font-size: 12px;
      line-height: 1.6;
      color: #e2e8f0;
      max-height: 420px;
      overflow-y: auto;
      background: #03050a;
    }
    .term-line {
      margin-bottom: 6px;
      opacity: 0;
      animation: lineFade 0.3s forwards;
    }
    @keyframes lineFade {
      to { opacity: 1; }
    }

    /* MODAL RAW VIEWER */
    .modal-overlay {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.75);
      z-index: 100;
      backdrop-filter: blur(4px);
      align-items: center;
      justify-content: center;
    }
    .modal-overlay.active {
      display: flex;
    }
    .modal-box {
      background: #111827;
      border: 1px solid #374151;
      width: 90%;
      max-width: 900px;
      max-height: 85vh;
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      box-shadow: 0 20px 40px rgba(0,0,0,0.8);
    }
    .modal-header {
      padding: 16px 20px;
      border-bottom: 1px solid #374151;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #fff;
    }
    .modal-body {
      padding: 20px;
      overflow-y: auto;
      flex: 1;
    }

    /* NAV CONTROLS AT BOTTOM */
    .nav-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 30px;
      padding-top: 20px;
      border-top: 1px solid var(--border);
    }
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div class="brand">
      <div class="brand-logo">PR</div>
      <div class="brand-titles">
        <h1>PRISMA-IA Core · DevSecOps Pipeline <span style="font-weight:400; color:var(--text-dim);">|</span> Plataforma Delivery Y (XFood)</h1>
        <p>Caso Prático Upstream Ideation (Greenfield / Zero Código) · Ingestão Bizagi BPMN & Regras de Negócio</p>
      </div>
    </div>
    <div class="header-badges">
      <div class="badge badge-approved" id="global-hitl-badge">HITL Aprovado</div>
      <div class="badge badge-blue">Cenário 1: Greenfield</div>
      <div class="badge badge-purple" id="global-hash-badge">SHA-256 Verificado</div>
    </div>
  </header>

  <!-- STEPPER -->
  <div class="stepper-container">
    <div class="stepper" id="stepper">
      <button class="step-btn active" onclick="switchStage(1)"><span class="step-num">1</span> <span class="step-label">01. Resolução<br>Upstream</span></button>
      <button class="step-btn" onclick="switchStage(2)"><span class="step-num">2</span> <span class="step-label">02. Grafo<br>Ontológico</span></button>
      <button class="step-btn" onclick="switchStage(3)"><span class="step-num">3</span> <span class="step-label">03. Inteligência<br>de Ameaças</span></button>
      <button class="step-btn" onclick="switchStage(4)"><span class="step-num">4</span> <span class="step-label">04. Modelagem<br>STRIDE</span></button>
      <button class="step-btn" onclick="switchStage(5)"><span class="step-num">5</span> <span class="step-label">05. Requisitos<br>de Segurança</span></button>
      <button class="step-btn" onclick="switchStage(6)"><span class="step-num">6</span> <span class="step-label">06. Deliberação<br>Dialética</span></button>
      <button class="step-btn" onclick="switchStage(7)"><span class="step-num">7</span> <span class="step-label">07. Deliberação<br>do Especialista</span></button>
      <button class="step-btn" onclick="switchStage(8)"><span class="step-num">8</span> <span class="step-label">08. Despacho<br>CI/CD</span></button>
    </div>
  </div>

  <!-- WRAPPER -->
  <div class="main-wrapper">

            <!-- ================= STAGE 1 ================= -->
    <div class="stage-section active" id="stage-1">
      <div class="section-header">
        <div class="section-title">
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:4px;">
            <h2>🎯 Estágio 1: Resolução de Cenário & Ingestão Upstream</h2>
            <span class="badge" style="background:#0369a1; color:#e0f2fe; font-size:11px; padding:3px 9px; border-radius:4px; font-weight:700; letter-spacing:0.5px;">FRONT-END PRISMA-IA</span>
          </div>
          <p>Portal Front-End Oficial do Framework — Configuração do Diretório de Insumos (BPMN Bizagi, Visão, Miro, PO), Ingestão Semântica e Orquestração do Pipeline.</p>
        </div>
        <div class="actions-bar">
          <button id="btn-run-pipeline-top" class="btn btn-primary" onclick="startPipelineExecution()" disabled style="opacity:0.5; cursor:not-allowed; background:#334155; font-weight:700; display:inline-flex; align-items:center; gap:8px;">
            <span>🚀</span> Iniciar Pipeline Completo
          </button>
          <button class="btn btn-secondary" onclick="viewRaw('01_scenario_resolution_upstream.json')">Inspecionar JSON</button>
          <button class="btn btn-secondary" onclick="viewRaw('01_scenario_resolution_upstream.md')">Ver Markdown</button>
        </div>
      </div>

      <!-- CARD 1: ESTAÇÃO DE CONFIGURAÇÃO DO DIRETÓRIO DE ORIGEM -->
      <div class="card" style="margin-bottom:20px; border-left:4px solid #0ea5e9; background:linear-gradient(180deg, #111a2e, #0f172a);">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:14px;">
          <div>
            <div class="card-subtitle" style="color:#38bdf8;">ESTAÇÃO DE INGESTÃO DO FRAMEWORK</div>
            <div class="card-title" style="font-size:16px;">Diretório de Origem dos Insumos de Upstream (Ideação & Negócio)</div>
            <p style="color:var(--text-muted); font-size:12.5px; margin-top:4px;">
              Aponte para o diretório local contendo os insumos brutos do novo sistema (documentos de visão, regras de negócio, processos BPMN Bizagi/Camunda, perguntas ao PO e quadros conceituais do Miro).
            </p>
          </div>
          <span id="inputs-status-badge" class="badge" style="font-size:11.5px; padding:5px 12px; display:inline-flex; align-items:center; gap:6px; background:#1e293b; color:#94a3b8;">
            <span id="inputs-status-dot" style="width:7px; height:7px; border-radius:50%; background:#94a3b8; display:inline-block;"></span>
            <span id="inputs-status-text">Aguardando Ingestão (0 Conectados)</span>
          </span>
        </div>

        <!-- INPUTS DE DIRETÓRIO (HTML5 NATIVO) -->
        <input type="file" id="source-folder-picker" webkitdirectory directory multiple style="display:none;" onchange="onSourceFolderSelected(event)">
        <input type="file" id="complementary-file-picker" multiple style="display:none;" onchange="onFilesSelected(event)">

        <div style="background:#090d16; padding:14px; border-radius:8px; border:1px solid #1e293b; margin-bottom:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <label style="font-size:11.5px; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.5px;">
              Caminho do Diretório Fonte (Workspace Local):
            </label>
            <button class="btn btn-secondary" onclick="loadSampleCaseFolder()" style="font-size:11px; padding:4px 10px; background:#0f172a; color:#38bdf8; border:1px dashed #38bdf8; display:inline-flex; align-items:center; gap:5px; cursor:pointer;" title="Preencher automaticamente com o caminho do Case Anne Linkedin">
              💡 Usar Pasta de Insumos: input
            </button>
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            <div style="position:relative; flex:1;">
              <span style="position:absolute; left:12px; top:50%; transform:translateY(-50%); font-size:14px; color:#64748b;">📂</span>
              <input type="text" id="source-dir-input" class="form-input" value="" placeholder="Selecione a pasta clicando ao lado ou cole o caminho: ...\\Case Anne Linkedin\\input" style="width:100%; padding-left:36px; font-family:var(--font-mono); font-size:12.5px; color:#f8fafc;" onchange="onSourceDirChanged()" onkeyup="if(event.key==='Enter') onSourceDirChanged()">
            </div>
            <button class="btn btn-secondary" onclick="triggerFolderSelect()" style="white-space:nowrap; padding:9px 16px; font-size:12.5px; display:inline-flex; align-items:center; gap:6px;">
              📁 Selecionar Pasta...
            </button>
            <button class="btn btn-secondary" onclick="reloadSourceInputs()" style="white-space:nowrap; padding:9px 14px; font-size:12.5px; display:inline-flex; align-items:center; gap:6px;" title="Escanear pasta indicada">
              🔍 Escanear Insumos
            </button>
          </div>
        </div>

        <!-- CONTROLES DO PIPELINE PROFILE -->
        <div class="grid-3" style="gap:12px; margin-bottom:16px;">
          <div>
            <label style="display:block; font-size:11.5px; font-weight:700; color:#94a3b8; text-transform:uppercase; margin-bottom:5px;">Perfil de Execução do Pipeline:</label>
            <select id="pipeline-mode-select" class="form-input" style="width:100%; font-size:12px;" onchange="updatePipelineMode()">
              <option value="upstream" selected>Cenário 1: Upstream Greenfield (Ideação / BPMN / Requisitos sem Código)</option>
              <option value="downstream">Cenário 2: Downstream Brownfield (Repositório Git / Código / SARIF)</option>
            </select>
          </div>
          <div>
            <label style="display:block; font-size:11.5px; font-weight:700; color:#94a3b8; text-transform:uppercase; margin-bottom:5px;">Rigor de Segurança Normativo:</label>
            <select id="asvs-level-select" class="form-input" style="width:100%; font-size:12px;">
              <option value="L2" selected>OWASP ASVS 4.0.3 Nível 2 (Padrão Corporativo / Fintechs & Delivery)</option>
              <option value="L3">OWASP ASVS 4.0.3 Nível 3 (Missão Crítica / Infraestrutura Crítica BACEN)</option>
              <option value="L1">OWASP ASVS 4.0.3 Nível 1 (Básico / Aplicações Informativas)</option>
            </select>
          </div>
          <div>
            <label style="display:block; font-size:11.5px; font-weight:700; color:#94a3b8; text-transform:uppercase; margin-bottom:5px;">Diretório de Destino dos Artefatos:</label>
            <input type="text" id="output-dir-input" class="form-input" value="...\\\\Case Anne Linkedin\\\\output_v2" style="width:100%; font-size:12px; font-family:var(--font-mono); color:#38bdf8; font-weight:700;" readonly>
          </div>
        </div>

        <!-- GATILHO PROEMINENTE DO PIPELINE -->
        <div style="display:flex; justify-content:space-between; align-items:center; padding-top:12px; border-top:1px solid #1e293b;">
          <div style="font-size:12px; color:var(--text-muted); display:flex; align-items:center; gap:8px;">
            <span id="engine-status-text" style="color:#94a3b8; font-weight:600;">⚪ Aguardando conexão de diretório para inicializar a engine.</span>
          </div>
          <button id="btn-run-pipeline" class="btn" onclick="startPipelineExecution()" disabled style="background:#334155; color:#94a3b8; padding:11px 24px; font-size:13.5px; font-weight:700; display:inline-flex; align-items:center; gap:8px; cursor:not-allowed; opacity:0.6; box-shadow:none; transition:all 0.3s;">
            <span id="btn-run-icon">⏳</span> <span id="btn-run-label">Aguardando Seleção de Diretório...</span>
          </button>
        </div>
      </div>

      <!-- CARD 2: MATRIZ DE INSUMOS BRUTOS DE ENTRADA -->
      <div class="card" style="margin-bottom:20px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
          <div>
            <div class="card-subtitle">INVENTÁRIO DE INSUMOS DO PROJETO</div>
            <div class="card-title" style="font-size:15px;">Artefatos de Upstream Mapeados para Análise da IA</div>
          </div>
          <button id="btn-attach-comp" class="btn btn-secondary" onclick="document.getElementById('complementary-file-picker').click()" disabled style="font-size:12px; padding:6px 12px; display:inline-flex; align-items:center; gap:6px; opacity:0.5;">
            <span>➕</span> Anexar Insumo Complementar
          </button>
        </div>

        <table class="compare-table" id="table-upstream-inputs">
          <thead>
            <tr>
              <th style="width:28%;">Insumo / Artefato Bruto</th>
              <th style="width:20%;">Origem & Tipo de Insumo</th>
              <th style="width:36%;">Conteúdo Extraído pelo Framework</th>
              <th style="width:16%; text-align:center;">Status no Pipeline</th>
            </tr>
          </thead>
          <tbody id="inputs-table-body">
            <tr id="row-empty-state">
              <td colspan="4" style="text-align:center; padding:36px 20px; color:#64748b; background:#0b1120;">
                <div style="font-size:36px; margin-bottom:8px;">📁</div>
                <div style="font-size:14px; font-weight:700; color:#e2e8f0; margin-bottom:4px;">Nenhum diretório de ideação selecionado</div>
                <div style="font-size:12px; color:#94a3b8; max-width:550px; margin:0 auto 14px auto;">
                  Aponte para o diretório local com os artefatos de ideação (BPMN Bizagi, DOCX de Visão/PO, Boards Miro) clicando em <strong>"📁 Selecionar Pasta..."</strong> ou use o atalho <strong>"💡 Usar Pasta Exemplo"</strong>.
                </div>
                <button class="btn btn-primary" onclick="loadSampleCaseFolder()" style="font-size:12px; padding:7px 16px; background:linear-gradient(135deg, #0284c7, #0ea5e9);">
                  💡 Conectar Insumos da Pasta input
                </button>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- DRAG & DROP ZONE -->
        <div id="upstream-dropzone" style="margin-top:14px; border:2px dashed #334155; border-radius:8px; padding:18px; text-align:center; background:#090d16; cursor:pointer; transition:all 0.2s;" onclick="document.getElementById('complementary-file-picker').click()" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)" ondrop="handleDrop(event)">
          <div style="font-size:24px; margin-bottom:4px;">📥</div>
          <div style="font-size:12.5px; font-weight:600; color:#94a3b8;">
            Arraste e solte insumos adicionais de upstream aqui (boards do Miro exportados, PDFs de arquitetura, BPMN, DOCX ou notas de reunião)
          </div>
          <div style="font-size:11px; color:#64748b; margin-top:2px;">
            Clique para selecionar do disco ou solte arquivos para enriquecimento instantâneo do Grafo Ontológico
          </div>
        </div>
      </div>

      <!-- CARDS RESUMO DE CLASSIFICAÇÃO DUAL -->
      <div class="grid-3" style="margin-bottom:20px;">
        <div class="card">
          <div class="card-subtitle">Classificação do Ciclo</div>
          <div id="card-cenario-title" class="card-title" style="color:#94a3b8;">CENÁRIO: AGUARDANDO INSUMOS</div>
          <p id="card-cenario-desc" style="color:var(--text-muted); font-size:13px;">Selecione a pasta do projeto para inferir a fase do ciclo de vida e classificar entre Upstream Greenfield ou Downstream Brownfield.</p>
        </div>
        <div class="card">
          <div class="card-subtitle">Insumos Processados</div>
          <div id="card-insumos-title" class="card-title" style="color:#94a3b8;">0 Insumos Conectados</div>
          <p id="card-insumos-desc" style="color:var(--text-muted); font-size:13px;">Aguardando leitura de fluxos Bizagi BPMN, regras de negócio e entrevistas com stakeholders.</p>
        </div>
        <div class="card">
          <div class="card-subtitle">Arquétipo Inferido</div>
          <div id="card-arquetipo-title" class="card-title" style="color:#94a3b8;">Arquétipo: Pendente</div>
          <p id="card-arquetipo-desc" style="color:var(--text-muted); font-size:13px;">O arquétipo de arquitetura de segurança será derivado automaticamente a partir dos insumos ingeridos.</p>
        </div>
      </div>

      <!-- TABELA DE ENTIDADES CRÍTICAS -->
      <div class="card">
        <div class="card-title">Entidades e Fluxos Críticos Identificados no BPMN:</div>
        <table class="compare-table">
          <thead>
            <tr><th>Entidade / Ator</th><th>Papel no Fluxo Upstream</th><th>Superfície de Risco Identificada</th><th>Regras Associadas</th></tr>
          </thead>
          <tbody id="bpmn-entities-tbody">
            <tr>
              <td colspan="4" style="text-align:center; padding:18px; color:#64748b;">
                Aguardando conexão da pasta de insumos para extrair entidades, lanes BPMN e superfícies de risco.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ================= STAGE 2 ================= -->
    <div class="stage-section" id="stage-2">
      <div class="section-header">
        <div class="section-title">
          <h2>🧠 Estágio 2: GraphRAG & Expansão Ontológica</h2>
          <p>Extração de entidades de domínio, taxonomias de segurança e relações de confiança entre subsistemas.</p>
        </div>
        <div class="actions-bar">
          <button class="btn btn-secondary active" id="btn-view-ontology-graph" onclick="switchOntologyView('graph')">🕸️ Rede Ontológica (Grafo Visual)</button>
          <button class="btn btn-secondary" id="btn-view-ontology-cards" onclick="switchOntologyView('cards')">📋 Visão em Cards & Tabela</button>
          <button class="btn btn-secondary" onclick="downloadOntologySvg()">Baixar SVG</button>
          <button class="btn btn-secondary" onclick="viewRaw('02_graphrag_ontology_xfood.json')">Inspecionar JSON</button>
          <button class="btn btn-secondary" onclick="viewRaw('02_graphrag_ontology_xfood.md')">Ver Markdown</button>
        </div>
      </div>

      <!-- VISÃO GRÁFICA / REDE VISUAL INTERATIVA (DEFAULT) -->
      <div id="ontology-graph-visual-view" style="display:block;">
        <div class="card" style="padding:16px; margin-bottom:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:10px;">
            <div>
              <div class="card-title" style="font-size:16px; margin-bottom:2px;">Topologia de Rede Ontológica do Domínio (GraphRAG On-Premise)</div>
              <div style="font-size:12.5px; color:var(--text-muted);">
                Grafo semântico extraído do BPMN Bizagi e 11 Regras de Negócio. Nós representam atores, superfícies, regras e mecanismos de segurança.
              </div>
            </div>
            
            <!-- FILTROS DE CATEGORIA -->
            <div style="display:flex; gap:6px; flex-wrap:wrap;" id="ontology-filter-pills">
              <button class="btn btn-secondary active" id="pill-all" onclick="filterOntologyNodes('ALL')" style="font-size:11px; padding:4px 10px;">Todos os Nós (10)</button>
              <button class="btn btn-secondary" id="pill-surfaces" onclick="filterOntologyNodes('SURFACES')" style="font-size:11px; padding:4px 10px;">Atores & Superfícies</button>
              <button class="btn btn-secondary" id="pill-services" onclick="filterOntologyNodes('SERVICES')" style="font-size:11px; padding:4px 10px;">Fintech & Geo</button>
              <button class="btn btn-secondary" id="pill-rules" onclick="filterOntologyNodes('RULES')" style="font-size:11px; padding:4px 10px;">Regras BPMN</button>
              <button class="btn btn-secondary" id="pill-sec" onclick="filterOntologyNodes('SECURITY')" style="font-size:11px; padding:4px 10px;">Segurança & LGPD</button>
            </div>
          </div>

          <!-- ÁREA DO SVG INTERATIVO -->
          <div style="background:#050811; border:1px solid #1e293b; border-radius:8px; overflow:hidden; display:flex; justify-content:center; padding:10px; position:relative;" id="ontology-svg-wrapper">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 580" width="100%" height="520" style="background:#070b14; border-radius:10px; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; user-select:none;" id="ontology-graph-svg">
  <defs>
    <!-- Filtros de Glow / Sombra -->
    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="glow-amber" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="glow-emerald" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="glow-purple" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="glow-rose" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <!-- Marcadores de Flechas Direcionadas -->
    <marker id="arrow-cyan" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b" />
    </marker>
    <marker id="arrow-emerald" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
    </marker>
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#c084fc" />
    </marker>
    <marker id="arrow-rose" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f43f5e" />
    </marker>

    <!-- Gradientes de Nós -->
    <linearGradient id="grad-client" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <linearGradient id="grad-partner" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <linearGradient id="grad-logistics" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <linearGradient id="grad-fintech" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <linearGradient id="grad-geo" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2" />
      <stop offset="100%" stop-color="#0e7490" />
    </linearGradient>
    <linearGradient id="grad-core" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed" />
      <stop offset="100%" stop-color="#6d28d9" />
    </linearGradient>
    <linearGradient id="grad-rule" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5" />
      <stop offset="100%" stop-color="#4338ca" />
    </linearGradient>
    <linearGradient id="grad-security" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48" />
      <stop offset="100%" stop-color="#be123c" />
    </linearGradient>
    <linearGradient id="grad-legal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#9333ea" />
      <stop offset="100%" stop-color="#7e22ce" />
    </linearGradient>
  </defs>

  <!-- GRID DE FUNDO CIBERNÉTICO -->
  <g opacity="0.08">
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#38bdf8" stroke-width="1" />
    </pattern>
    <rect width="100%" height="100%" fill="url(#grid)" />
  </g>

  <!-- ================= ARESTAS / CONEXÕES ONTOLÓGICAS ================= -->
  <g id="graph-edges" stroke-width="2" opacity="0.85">

    <!-- 1. APP_CLIENTE -> GATEWAY_PAGAMENTOS (LIQUIDA_TRANSACAO_VIA) -->
    <path id="edge-1" d="M 180 180 Q 130 310 140 430" fill="none" stroke="#f59e0b" stroke-dasharray="5,3" marker-end="url(#arrow-amber)" />
    <!-- 2. APP_CLIENTE -> GOOGLE_MAPS_API (VALIDA_ENDERECO_GEORREFERENCIADO) -->
    <path id="edge-2" d="M 210 210 Q 240 320 280 430" fill="none" stroke="#38bdf8" marker-end="url(#arrow-cyan)" />
    <!-- 3. APP_CLIENTE -> REGRA_NEGOCIO_RN02 (DEVE_RESPEITAR_TRAVA_SACOLA) -->
    <path id="edge-3" d="M 240 180 Q 320 240 400 290" fill="none" stroke="#818cf8" marker-end="url(#arrow-purple)" />
    <!-- 4. PAINEL_KDS_RESTAURANTE -> WEBSOCKET_BROKER (RECEBE_EVENTO_NOVO_PEDIDO) -->
    <path id="edge-4" d="M 540 210 L 540 430" fill="none" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrow-purple)" />
    <!-- 5. PAINEL_KDS_RESTAURANTE -> REGRA_NEGOCIO_RN09 (CONTROLADO_POR_TIMER_SLA_5MIN) -->
    <path id="edge-5" d="M 570 210 Q 640 240 680 290" fill="none" stroke="#818cf8" marker-end="url(#arrow-purple)" />
    <!-- 6. CODIGO_RETIRADA_4DIGITOS -> PAINEL_KDS_RESTAURANTE (AUTENTICA_COLETA_HANDOVER) -->
    <path id="edge-6" d="M 720 180 L 600 180" fill="none" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrow-rose)" />
    <!-- 7. APP_ENTREGADOR -> CODIGO_RETIRADA_4DIGITOS (FORNECE_PIN_NO_BALCAO) -->
    <path id="edge-7" d="M 880 180 L 800 180" fill="none" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-emerald)" />
    <!-- 8. APP_ENTREGADOR -> LGPD_COMPLIANCE (DEVE_MASCARAR_PII_DO_CLIENTE) -->
    <path id="edge-8" d="M 940 210 Q 960 320 940 430" fill="none" stroke="#f472b6" stroke-dasharray="5,3" marker-end="url(#arrow-purple)" />
    <!-- 9. DOUBLE LOOP: CODIGO_RETIRADA_4DIGITOS -> WEBSOCKET_BROKER (VALIDA_TTL_REDIS_120S) -->
    <path id="edge-9" d="M 750 210 Q 650 320 580 440" fill="none" stroke="#10b981" stroke-dasharray="4,4" opacity="0.6" marker-end="url(#arrow-emerald)" />

  </g>

  <!-- ================= LABELS DE RELAÇÕES ================= -->
  <g font-size="9" font-weight="700" fill="#cbd5e1" text-anchor="middle">
    <g transform="translate(100, 310)">
      <rect x="-65" y="-10" width="130" height="20" rx="10" fill="#1e1b4b" stroke="#f59e0b" stroke-width="1" />
      <text y="4" fill="#fbbf24">LIQUIDA_TRANSACAO_VIA</text>
    </g>
    <g transform="translate(240, 335)">
      <rect x="-60" y="-10" width="120" height="20" rx="10" fill="#0b172a" stroke="#38bdf8" stroke-width="1" />
      <text y="4" fill="#38bdf8">VALIDA_GEO_MAPS</text>
    </g>
    <g transform="translate(325, 225)">
      <rect x="-65" y="-10" width="130" height="20" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1" />
      <text y="4" fill="#a5b4fc">TRAVA_SACOLA_RN02</text>
    </g>
    <g transform="translate(540, 320)">
      <rect x="-65" y="-10" width="130" height="20" rx="10" fill="#1e1338" stroke="#c084fc" stroke-width="1" />
      <text y="4" fill="#e879f9">RECEBE_NOVO_PEDIDO</text>
    </g>
    <g transform="translate(635, 235)">
      <rect x="-60" y="-10" width="120" height="20" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1" />
      <text y="4" fill="#a5b4fc">TIMER_SLA_5MIN_RN09</text>
    </g>
    <g transform="translate(660, 160)">
      <rect x="-55" y="-10" width="110" height="20" rx="10" fill="#310c18" stroke="#f43f5e" stroke-width="1" />
      <text y="4" fill="#fda4af">AUTENTICA_BALCAO</text>
    </g>
    <g transform="translate(840, 160)">
      <rect x="-40" y="-10" width="80" height="20" rx="10" fill="#062e20" stroke="#34d399" stroke-width="1" />
      <text y="4" fill="#6ee7b7">INSERE_PIN</text>
    </g>
    <g transform="translate(970, 320)">
      <rect x="-65" y="-10" width="130" height="20" rx="10" fill="#2d1033" stroke="#f472b6" stroke-width="1" />
      <text y="4" fill="#f472b6">MASCARA_PII_CLIENTE</text>
    </g>
  </g>

  <!-- ================= NÓS DO GRAFO ONTOLÓGICO ================= -->
  <g id="graph-nodes">

    <!-- 1. APP_CLIENTE -->
    <g class="graph-node" id="node-APP_CLIENTE" transform="translate(180, 180)" cursor="pointer">
      <circle r="46" fill="url(#grad-client)" stroke="#38bdf8" stroke-width="2.5" filter="url(#glow-cyan)" />
      <circle r="40" fill="#07192f" stroke="#0284c7" stroke-width="1.5" />
      <text y="-8" font-size="18" text-anchor="middle">📱</text>
      <text y="10" font-size="10.5" font-weight="800" fill="#fff" text-anchor="middle">APP_CLIENTE</text>
      <text y="22" font-size="8.5" fill="#38bdf8" text-anchor="middle">Surface (Alta)</text>
    </g>

    <!-- 2. PAINEL_KDS_RESTAURANTE -->
    <g class="graph-node" id="node-PAINEL_KDS_RESTAURANTE" transform="translate(540, 180)" cursor="pointer">
      <circle r="48" fill="url(#grad-partner)" stroke="#60a5fa" stroke-width="2.5" />
      <circle r="42" fill="#0d1b3a" stroke="#2563eb" stroke-width="1.5" />
      <text y="-8" font-size="18" text-anchor="middle">🍳</text>
      <text y="10" font-size="10" font-weight="800" fill="#fff" text-anchor="middle">PAINEL_KDS</text>
      <text y="22" font-size="8.5" fill="#93c5fd" text-anchor="middle">Restaurante (Alta)</text>
    </g>

    <!-- 3. CODIGO_RETIRADA_4DIGITOS (Mecanismo de Segurança Central) -->
    <g class="graph-node" id="node-CODIGO_RETIRADA_4DIGITOS" transform="translate(760, 180)" cursor="pointer">
      <rect x="-42" y="-42" width="84" height="84" rx="16" fill="url(#grad-security)" stroke="#f43f5e" stroke-width="2.5" filter="url(#glow-rose)" />
      <rect x="-36" y="-36" width="72" height="72" rx="12" fill="#240710" stroke="#be123c" stroke-width="1" />
      <text y="-8" font-size="18" text-anchor="middle">🔐</text>
      <text y="8" font-size="9" font-weight="800" fill="#fff" text-anchor="middle">PIN_HANDOVER</text>
      <text y="20" font-size="8" fill="#fda4af" text-anchor="middle">Código 4 Dígitos</text>
    </g>

    <!-- 4. APP_ENTREGADOR -->
    <g class="graph-node" id="node-APP_ENTREGADOR" transform="translate(940, 180)" cursor="pointer">
      <circle r="46" fill="url(#grad-logistics)" stroke="#34d399" stroke-width="2.5" filter="url(#glow-emerald)" />
      <circle r="40" fill="#042017" stroke="#059669" stroke-width="1.5" />
      <text y="-8" font-size="18" text-anchor="middle">🛵</text>
      <text y="10" font-size="9.5" font-weight="800" fill="#fff" text-anchor="middle">APP_MOTOBOY</text>
      <text y="22" font-size="8.5" fill="#6ee7b7" text-anchor="middle">Logistics (Alta)</text>
    </g>

    <!-- 5. GATEWAY_PAGAMENTOS -->
    <g class="graph-node" id="node-GATEWAY_PAGAMENTOS" transform="translate(140, 460)" cursor="pointer">
      <rect x="-45" y="-35" width="90" height="70" rx="12" fill="url(#grad-fintech)" stroke="#f59e0b" stroke-width="2" filter="url(#glow-amber)" />
      <rect x="-40" y="-30" width="80" height="60" rx="8" fill="#241303" stroke="#d97706" stroke-width="1" />
      <text y="-6" font-size="16" text-anchor="middle">💳</text>
      <text y="10" font-size="9.5" font-weight="800" fill="#fff" text-anchor="middle">GATEWAY_PIX</text>
      <text y="21" font-size="8" fill="#fcd34d" text-anchor="middle">PCI-DSS / BACEN</text>
    </g>

    <!-- 6. GOOGLE_MAPS_API -->
    <g class="graph-node" id="node-GOOGLE_MAPS_API" transform="translate(290, 460)" cursor="pointer">
      <rect x="-42" y="-35" width="84" height="70" rx="12" fill="url(#grad-geo)" stroke="#06b6d4" stroke-width="2" />
      <rect x="-37" y="-30" width="74" height="60" rx="8" fill="#051f28" stroke="#0891b2" stroke-width="1" />
      <text y="-6" font-size="16" text-anchor="middle">🗺️</text>
      <text y="10" font-size="9" font-weight="800" fill="#fff" text-anchor="middle">MAPS_API</text>
      <text y="21" font-size="8" fill="#67e8f9" text-anchor="middle">SLA 99.9%</text>
    </g>

    <!-- 7. REGRA_NEGOCIO_RN02 -->
    <g class="graph-node" id="node-REGRA_NEGOCIO_RN02" transform="translate(430, 310)" cursor="pointer">
      <circle r="36" fill="url(#grad-rule)" stroke="#818cf8" stroke-width="2" />
      <circle r="31" fill="#131036" stroke="#4f46e5" stroke-width="1" />
      <text y="-4" font-size="15" text-anchor="middle">📜</text>
      <text y="10" font-size="9.5" font-weight="800" fill="#fff" text-anchor="middle">REGRA_RN02</text>
      <text y="20" font-size="8" fill="#c7d2fe" text-anchor="middle">Sacola Única</text>
    </g>

    <!-- 8. WEBSOCKET_BROKER -->
    <g class="graph-node" id="node-WEBSOCKET_BROKER" transform="translate(540, 460)" cursor="pointer">
      <rect x="-46" y="-36" width="92" height="72" rx="14" fill="url(#grad-core)" stroke="#c084fc" stroke-width="2.5" filter="url(#glow-purple)" />
      <rect x="-40" y="-30" width="80" height="60" rx="10" fill="#1b0833" stroke="#7c3aed" stroke-width="1" />
      <text y="-6" font-size="17" text-anchor="middle">⚡</text>
      <text y="10" font-size="9.5" font-weight="800" fill="#fff" text-anchor="middle">WSS_BROKER</text>
      <text y="21" font-size="8" fill="#e9d5ff" text-anchor="middle">Redis PubSub</text>
    </g>

    <!-- 9. REGRA_NEGOCIO_RN09 -->
    <g class="graph-node" id="node-REGRA_NEGOCIO_RN09" transform="translate(690, 310)" cursor="pointer">
      <circle r="36" fill="url(#grad-rule)" stroke="#818cf8" stroke-width="2" />
      <circle r="31" fill="#131036" stroke="#4f46e5" stroke-width="1" />
      <text y="-4" font-size="15" text-anchor="middle">⏱️</text>
      <text y="10" font-size="9.5" font-weight="800" fill="#fff" text-anchor="middle">REGRA_RN09</text>
      <text y="20" font-size="8" fill="#c7d2fe" text-anchor="middle">SLA 5 Minutos</text>
    </g>

    <!-- 10. LGPD_COMPLIANCE -->
    <g class="graph-node" id="node-LGPD_COMPLIANCE" transform="translate(940, 460)" cursor="pointer">
      <rect x="-45" y="-35" width="90" height="70" rx="12" fill="url(#grad-legal)" stroke="#f472b6" stroke-width="2" />
      <rect x="-40" y="-30" width="80" height="60" rx="8" fill="#240728" stroke="#9333ea" stroke-width="1" />
      <text y="-6" font-size="16" text-anchor="middle">⚖️</text>
      <text y="10" font-size="9" font-weight="800" fill="#fff" text-anchor="middle">LGPD_LEGAL</text>
      <text y="21" font-size="8" fill="#fbcfe8" text-anchor="middle">Art. 46 / 52</text>
    </g>

  </g>

  <!-- LEGENDA DO GRAFO -->
  <g transform="translate(24, 24)" font-size="10" font-weight="700">
    <rect width="360" height="42" rx="6" fill="#090d16" stroke="#1e293b" opacity="0.9" />
    <circle cx="16" cy="21" r="5" fill="#38bdf8" />
    <text x="26" y="25" fill="#94a3b8">Superfícies</text>
    
    <circle cx="100" cy="21" r="5" fill="#f59e0b" />
    <text x="110" y="25" fill="#94a3b8">Fintech / Geo</text>
    
    <circle cx="190" cy="21" r="5" fill="#818cf8" />
    <text x="200" y="25" fill="#94a3b8">Regras BPMN</text>

    <circle cx="282" cy="21" r="5" fill="#f43f5e" />
    <text x="292" y="25" fill="#94a3b8">Segurança</text>
  </g>

  <g transform="translate(840, 24)" font-size="11" font-weight="600" fill="#64748b" text-anchor="end">
    <text y="26">💡 Clique em qualquer nó para inspecionar atributos ontológicos</text>
  </g>
</svg>

          </div>
        </div>

        <!-- INSPETOR DETALHADO DO NÓ SELECIONADO -->
        <div class="card" id="ontology-node-inspector" style="border-left:4px solid #38bdf8; animation:fadeIn 0.3s; margin-bottom:20px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start;">
            <div>
              <div class="card-subtitle" id="inspect-node-type">TIPO: CLIENT_SURFACE · DOMÍNIO E-COMMERCE</div>
              <div class="card-title" id="inspect-node-title" style="font-size:18px; color:#38bdf8;">📱 APP_CLIENTE (Aplicativo Mobile do Consumidor)</div>
            </div>
            <span class="tag tag-blue" id="inspect-node-badge">CRITICIDADE ALTA</span>
          </div>

          <p style="color:#e2e8f0; font-size:13.5px; margin:8px 0 12px 0;" id="inspect-node-desc">
            Superfície de entrada do consumidor final. Responsável pela autenticação, geolocalização do endereço de entrega, montagem do carrinho de compras e autorização transacional de pagamentos Pix/Cartão.
          </p>

          <div class="grid-2" style="gap:14px; margin-top:10px;">
            <div style="background:#090d16; border:1px solid #1e293b; border-radius:6px; padding:12px;">
              <div style="font-size:11.5px; font-weight:700; color:#c084fc; margin-bottom:4px;">📜 Regras de Negócio e Normas Associadas:</div>
              <div style="font-size:12px; color:#cbd5e1;" id="inspect-node-rules">
                • <strong>RN01:</strong> Exibição georreferenciada de restaurantes em raio operacional.<br>
                • <strong>RN02:</strong> Sacola de restaurante único (trava mandatória).<br>
                • <strong>RN03:</strong> Validação de transação e estorno de pedido.
              </div>
            </div>

            <div style="background:#090d16; border:1px solid #1e293b; border-radius:6px; padding:12px;">
              <div style="font-size:11.5px; font-weight:700; color:#34d399; margin-bottom:4px;">🔗 Relações Ontológicas Direcionadas:</div>
              <div style="font-size:12px; color:#cbd5e1;" id="inspect-node-relations">
                • ➔ <strong>GATEWAY_PAGAMENTOS:</strong> LIQUIDA_TRANSACAO_VIA (REST / TLS 1.3)<br>
                • ➔ <strong>GOOGLE_MAPS_API:</strong> VALIDA_ENDERECO_GEORREFERENCIADO (HTTPS)<br>
                • ➔ <strong>REGRA_NEGOCIO_RN02:</strong> DEVE_RESPEITAR_TRAVA_SACOLA (Validação Backend)
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- VISÃO EM CARDS E TABELA TRADICIONAL -->
      <div id="ontology-cards-view" style="display:none;">
        <div class="card" style="margin-bottom:20px;">
          <div class="card-title">Topologia do Grafo de Conhecimento (Nodes & Edges Extraídos):</div>
          <div class="grid-3" id="graph-nodes-container" style="margin-top:14px;"></div>
        </div>

        <div class="card">
          <div class="card-title">Relações de Confiança e Fronteiras Arquiteturais:</div>
          <div id="graph-relations-container" style="margin-top:10px;"></div>
        </div>
      </div>
    </div>

    <!-- ================= STAGE 3 ================= -->
    <div class="stage-section" id="stage-3">
      <div class="section-header">
        <div class="section-title">
          <h2>📡 Estágio 3: Inteligência de Ameaças & Feeds Setoriais</h2>
          <p>Correlação automatizada com repositórios globais de inteligência de ameaças (NIST, CISA, MITRE, OWASP e BACEN).</p>
        </div>
        <div class="actions-bar">
          <button class="btn btn-secondary" onclick="viewRaw('03_threat_intel_delivery_feeds.json')">Inspecionar JSON</button>
          <button class="btn btn-secondary" onclick="viewRaw('03_threat_intel_delivery_feeds.md')">Ver Markdown</button>
        </div>
      </div>

      <!-- PAINEL DE BASES OFICIAIS DE THREAT INTELLIGENCE (REFERÊNCIAS GLOBAIS) -->
      <div class="card" style="margin-bottom:20px; border-top:3px solid #38bdf8;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
          <div>
            <div class="card-title" style="font-size:16px;">🌐 Repositórios e Bases Oficiais de Threat Intelligence Consultadas</div>
            <div style="font-size:12.5px; color:var(--text-muted);">
              O PRISMA-IA conecta-se ativamente a bases públicas e regulatórias para enriquecer o modelo de ameaças do ecossistema XFood:
            </div>
          </div>
          <span class="badge badge-blue">FEEDS ATIVOS</span>
        </div>

        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; margin-top:10px;">
          
          <div style="background:#090d16; border:1px solid #1e293b; border-radius:6px; padding:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <strong style="color:#fff; font-size:13px;">🛡️ NIST NVD</strong>
              <span class="tag tag-blue" style="font-size:10px;">VULNERABILIDADES</span>
            </div>
            <div style="font-size:11.5px; color:var(--text-muted); margin-bottom:6px;">National Vulnerability Database (NIST / Governo EUA). Mapeia scores CVSS v3.1/v4.0 e vetores públicos.</div>
            <a href="https://nvd.nist.gov/" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; font-size:11.5px; text-decoration:none; font-weight:700;">Base Oficial: nvd.nist.gov ↗</a>
          </div>

          <div style="background:#090d16; border:1px solid #1e293b; border-radius:6px; padding:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <strong style="color:#fff; font-size:13px;">🚨 CISA KEV Catalog</strong>
              <span class="tag tag-red" style="font-size:10px;">EXPLOITS ATIVOS</span>
            </div>
            <div style="font-size:11.5px; color:var(--text-muted); margin-bottom:6px;">Known Exploited Vulnerabilities (CISA / DHS). Catálogo de falhas sob ataque ativo no mundo real.</div>
            <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog" target="_blank" rel="noopener noreferrer" style="color:#f43f5e; font-size:11.5px; text-decoration:none; font-weight:700;">Catálogo CISA KEV ↗</a>
          </div>

          <div style="background:#090d16; border:1px solid #1e293b; border-radius:6px; padding:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <strong style="color:#fff; font-size:13px;">🎯 MITRE ATT&CK®</strong>
              <span class="tag tag-purple" style="font-size:10px;">TÁTICAS & TÉCNICAS</span>
            </div>
            <div style="font-size:11.5px; color:var(--text-muted); margin-bottom:6px;">Matriz comportamental de adversários. Mapeia técnicas como T1190, T1078, T1556 e T1498.</div>
            <a href="https://attack.mitre.org/" target="_blank" rel="noopener noreferrer" style="color:#c084fc; font-size:11.5px; text-decoration:none; font-weight:700;">Matriz: attack.mitre.org ↗</a>
          </div>

          <div style="background:#090d16; border:1px solid #1e293b; border-radius:6px; padding:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <strong style="color:#fff; font-size:13px;">🌐 OWASP API Security</strong>
              <span class="tag tag-orange" style="font-size:10px;">TOP 10 APIs</span>
            </div>
            <div style="font-size:11.5px; color:var(--text-muted); margin-bottom:6px;">Padrão global para segurança de APIs modernas. Foco em BOLA (API1:2023) e Broken Authentication.</div>
            <a href="https://owasp.org/API-Security/" target="_blank" rel="noopener noreferrer" style="color:#fb923c; font-size:11.5px; text-decoration:none; font-weight:700;">OWASP API Project ↗</a>
          </div>

          <div style="background:#090d16; border:1px solid #1e293b; border-radius:6px; padding:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <strong style="color:#fff; font-size:13px;">📑 MITRE CWE</strong>
              <span class="tag tag-emerald" style="font-size:10px;">FRAQUEZAS DE CÓDIGO</span>
            </div>
            <div style="font-size:11.5px; color:var(--text-muted); margin-bottom:6px;">Common Weakness Enumeration. Dicionário de falhas de arquitetura e código (CWE-22, CWE-862, CWE-384).</div>
            <a href="https://cwe.mitre.org/" target="_blank" rel="noopener noreferrer" style="color:#34d399; font-size:11.5px; text-decoration:none; font-weight:700;">Dicionário: cwe.mitre.org ↗</a>
          </div>

          <div style="background:#090d16; border:1px solid #1e293b; border-radius:6px; padding:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <strong style="color:#fff; font-size:13px;">🏦 BACEN Pix Security</strong>
              <span class="tag tag-blue" style="font-size:10px;">REGULATÓRIO BRASIL</span>
            </div>
            <div style="font-size:11.5px; color:var(--text-muted); margin-bottom:6px;">Banco Central do Brasil. Diretrizes de segurança transacional, mTLS e conciliação de webhooks Pix.</div>
            <a href="https://www.bcb.gov.br/estabilidadefinanceira/pix" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; font-size:11.5px; text-decoration:none; font-weight:700;">Manual de Segurança BACEN ↗</a>
          </div>

        </div>
      </div>

      <!-- CARDS DE FEEDS DETALHADOS -->
      <div style="margin-bottom:12px; font-weight:700; color:#fff; font-size:15px;">
        Ameaças e Vulnerabilidades Correlacionadas à Stack da Plataforma Delivery Y:
      </div>
      <div class="grid-2" id="threat-feeds-container"></div>
    </div>

    <!-- ================= STAGE 4 ================= -->
    <div class="stage-section" id="stage-4">
      <div class="section-header">
        <div class="section-title">
          <h2>🛡️ Estágio 4: Modelagem de Ameaças STRIDE & Diagrama DFD</h2>
          <p>Vetorização de ameaças sobre os processos do Bizagi com diagrama visual padrão OWASP Threat Dragon.</p>
        </div>
        <div class="actions-bar">
          <button class="btn btn-secondary active" id="btn-view-stride-cards" onclick="switchStrideView('cards')">Cards STRIDE</button>
          <button class="btn btn-secondary" id="btn-view-stride-dfd" onclick="switchStrideView('dfd')">Diagrama DFD (Threat Dragon)</button>
          <button class="btn btn-secondary" onclick="viewRaw('04_threat_model_stride_xfood.json')">Inspecionar JSON</button>
        </div>
      </div>

      <!-- VISÃO DIAGRAMA DFD (THREAT DRAGON STYLE) -->
      <div id="stride-dfd-view" style="display:none; margin-bottom:20px;">
        <div class="card" style="padding:14px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <div>
              <div class="card-title" style="font-size:16px;">Diagrama de Fluxo de Dados (DFD) — Modelo de Ameaças Interativo</div>
              <div style="font-size:12px; color:var(--text-muted);">Clique nos nós e nos marcadores vermelhos (T1 a T6) para inspecionar as ameaças associadas diretamente aos fluxos e componentes.</div>
            </div>
            <div style="display:flex; gap:8px;">
              <span class="tag tag-red">T1: Spoofing (Webhook Pix)</span>
              <span class="tag tag-orange">T2: Tampering (Preço Carrinho)</span>
              <span class="tag tag-purple">T6: Elevation (Coleta Balcão)</span>
            </div>
          </div>
          <div style="background:#090d16; border:1px solid #1e293b; border-radius:8px; overflow:hidden; display:flex; justify-content:center; padding:10px;" id="threat-dragon-svg-wrapper">
            """ + threat_dragon_svg + """
          </div>
        </div>
      </div>

      <!-- VISÃO CARDS STRIDE -->
      <div id="stride-cards-view">
        <div style="display:flex; gap:10px; margin-bottom:16px;">
          <button class="btn btn-secondary active" id="filter-all" onclick="filterThreats('ALL')">Todas as Ameaças (6)</button>
          <button class="btn btn-secondary" id="filter-crit" onclick="filterThreats('CRÍTICO')">Apenas Críticas</button>
          <button class="btn btn-secondary" id="filter-high" onclick="filterThreats('ALTO')">Apenas Altas</button>
        </div>

        <div class="grid-2" id="threats-cards-container"></div>
      </div>
    </div>

    <!-- ================= STAGE 5 ================= -->
    <div class="stage-section" id="stage-5">
      <div class="section-header">
        <div class="section-title">
          <h2>📋 Estágio 5: Especificação de Requisitos de Segurança</h2>
          <p>Equilíbrio entre governança normativa (LGPD/ISO) e necessidades práticas de desenvolvimento (INVEST, BDD e DoD).</p>
        </div>
        <div class="actions-bar">
          <button class="btn btn-secondary active" id="btn-toggle-doc-preview" onclick="switchSecReqView('doc')">📄 Visualizar Documento Oficial Completo</button>
          <button class="btn btn-secondary" id="btn-toggle-agile-cards" onclick="switchSecReqView('agile')">🎯 Visão Ágil / Backlog (Cards)</button>
          <a class="btn btn-primary" href="output_v2/05_security_requirements_specification.docx" download>Baixar DOCX</a>
          <button class="btn btn-secondary" onclick="viewRaw('05_security_requirements_asvs_xfood.json')">Inspecionar JSON</button>
        </div>
      </div>

      <!-- 1. MODO DOCUMENTO OFICIAL BALANCEADO (PREVIEW ESTILO FOLHA A4) -->
      <div id="sec-req-doc-preview-wrapper" style="display:block;">
        <div style="background:#ffffff; color:#0f172a; border-radius:8px; padding:36px; box-shadow:0 10px 35px rgba(0,0,0,0.5); max-width:1100px; margin:0 auto; font-family:'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height:1.6;">
          
          <div style="border-bottom:3px solid #1e3a8a; padding-bottom:16px; margin-bottom:24px; display:flex; justify-content:space-between; align-items:flex-end;">
            <div>
              <div style="font-size:12px; font-weight:800; color:#1e3a8a; text-transform:uppercase; letter-spacing:1px;">Especificação Técnica Formal · PRISMA-IA Core</div>
              <h1 style="font-size:24px; color:#0f172a; margin-top:4px;">Requisitos de Segurança de Software (SRS)</h1>
              <div style="font-size:14px; color:#475569;">Projeto: Plataforma Delivery Y (XFood) · Fase Upstream Greenfield</div>
            </div>
            <div style="text-align:right;">
              <span style="background:#dbeafe; color:#1e40af; padding:4px 10px; border-radius:4px; font-weight:700; font-size:12px;">PADRÃO BALANCEADO</span>
              <div style="font-size:11px; color:#64748b; margin-top:4px;">Versão 1.2 · Set/2026</div>
            </div>
          </div>

          <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin-bottom:24px;">
            <div style="font-size:12px; font-weight:800; color:#1e3a8a; margin-bottom:8px; text-transform:uppercase;">1. Metadados do Sistema & Governança</div>
            <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:12px; font-size:12px;">
              <div><strong>Classificação de Risco:</strong><br><span style="color:#b91c1c; font-weight:700;">ALTO (Marketplace Financeiro)</span></div>
              <div><strong>Alinhamento Regulatório:</strong><br>OWASP ASVS 4.0.3 L2 · LGPD · PCI-DSS</div>
              <div><strong>Dono do Sistema:</strong><br>Empresa X · Tribo de Plataforma Delivery</div>
              <div><strong>Validação de Engenharia:</strong><br><span style="color:#059669; font-weight:700;">✓ Homologado HITL & Tripartite</span></div>
            </div>
          </div>

          <div style="margin-bottom:28px;">
            <div style="font-size:14px; font-weight:800; color:#0f172a; margin-bottom:10px; text-transform:uppercase; border-bottom:1px solid #e2e8f0; padding-bottom:6px;">
              2. Inventário de Dados Pessoais & Classificação LGPD (Apêndice A Adaptado)
            </div>
            <table style="width:100%; border-collapse:collapse; font-size:11.5px; text-align:left;">
              <thead>
                <tr style="background:#f1f5f9; color:#334155;">
                  <th style="padding:8px; border:1px solid #cbd5e1;">Item de Dado</th>
                  <th style="padding:8px; border:1px solid #cbd5e1;">Classificação LGPD</th>
                  <th style="padding:8px; border:1px solid #cbd5e1;">Base Legal</th>
                  <th style="padding:8px; border:1px solid #cbd5e1;">Mecanismo Mandatório de Proteção</th>
                </tr>
              </thead>
              <tbody id="doc-lgpd-tbody">
                """ + lgpd_rows_html + """
              </tbody>
            </table>
          </div>

          <div style="margin-bottom:28px;">
            <div style="font-size:14px; font-weight:800; color:#0f172a; margin-bottom:12px; text-transform:uppercase; border-bottom:1px solid #e2e8f0; padding-bottom:6px;">
              3. Fichas Técnicas dos Requisitos de Segurança de Aplicação
            </div>
            <div id="fichas-tecnicas-container">
              """ + fichas_tecnicas_html + """
            </div>
          </div>

          <div style="border-top:2px solid #e2e8f0; padding-top:16px; margin-top:30px; font-size:11px; color:#64748b; display:flex; justify-content:space-between;">
            <div>PRISMA-IA Governance Framework · Documento de Engenharia de Software</div>
            <div>Rastreabilidade Garantida com Apêndices A & D e Regras de Negócio RN01-RN11</div>
          </div>

        </div>
      </div>

      <!-- 2. MODO CARDS ÁGEIS INVEST (VISÃO SPRINT / BACKLOG) -->
      <div id="sec-req-agile-cards-wrapper" style="display:none;">
        <div id="sec-reqs-container" style="display:flex; flex-direction:column; gap:18px;">
          <!-- Rendered by JS -->
        </div>
      </div>
    </div>

    <!-- ================= STAGE 6 ================= -->
    <div class="stage-section" id="stage-6">
      <div class="section-header">
        <div class="section-title">
          <h2>⚖️ Estágio 6: Deliberação Tripartite Dialética</h2>
          <p>Debate socrático automatizado entre Engenharia de Requisitos (RE), Segurança (SEC) e Arquitetura (ARCH).</p>
        </div>
        <div class="actions-bar">
          <button class="btn btn-secondary" onclick="viewRaw('06_tripartite_deliberation_xfood.json')">Inspecionar JSON</button>
          <button class="btn btn-secondary" onclick="viewRaw('06_tripartite_deliberation_xfood.md')">Ver Markdown</button>
        </div>
      </div>

      <div class="card" style="margin-bottom:20px; border-left:4px solid #38bdf8;">
        <div class="card-title">Tema Arbitrado pelo Conselho de Agentes:</div>
        <p style="color:#e2e8f0; font-size:13.5px;">Protocolo de Coleta Segura no Balcão (CE07) vs. Impacto no SLA de 5 minutos da Cozinha (RN09) e Conversão do Cliente.</p>
      </div>

      <div class="delib-thread" id="deliberation-container"></div>
    </div>

    <!-- ================= STAGE 7 ================= -->
    <div class="stage-section" id="stage-7">
      <div class="section-header">
        <div class="section-title">
          <h2>🏛️ Estágio 7: Deliberação do Especialista</h2>
          <p>Quality Gate decisório com auditoria humana, assinatura digital SHA-256 e aprendizagem em duplo loop.</p>
        </div>
        <div class="actions-bar">
          <button class="btn btn-primary" onclick="downloadHitlReceipt()">💾 Baixar Recibo JSON Assinado</button>
          <button class="btn btn-secondary" onclick="viewRaw('07_hitl_compliance_receipt.json')">Inspecionar Recibo JSON</button>
          <button class="btn btn-secondary" onclick="resetHitlState()">↺ Restaurar Padrão</button>
        </div>
      </div>

      <!-- 1. PARTE SUPERIOR: ARTEFATOS GERADOS EM FORMA DE LISTA -->
      <div class="card" style="margin-bottom:20px; border-top:3px solid #38bdf8;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <div>
            <div class="card-title" style="font-size:15px; margin-bottom:2px;">📦 Artefatos Upstream Submetidos à Homologação do Especialista</div>
            <div style="font-size:12px; color:var(--text-muted);">Revise os documentos e modelos produzidos pelos agentes autônomos antes de emitir o parecer final do Quality Gate:</div>
          </div>
          <span class="tag tag-emerald">6 PACOTES PRONTOS</span>
        </div>

        <div style="display:flex; flex-direction:column; gap:8px;">
          
          <!-- Artefato 1: Requisitos de Segurança -->
          <div style="background:#070b14; border:1px solid #1e293b; border-radius:6px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
            <div style="display:flex; align-items:center; gap:12px;">
              <span style="font-size:20px;">📄</span>
              <div>
                <div style="font-weight:700; color:#fff; font-size:13px;">Especificação de Requisitos de Segurança (SRS-SEC)</div>
                <div style="color:var(--text-muted); font-size:11.5px;">05_security_requirements_specification.docx · 5 Fichas Técnicas, Inventário LGPD, INVEST e BDD</div>
              </div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <span class="tag tag-blue">OWASP ASVS 4.0.3</span>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="switchStage(5)">Ver no Estágio 5 ↗</button>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="viewRaw('05_security_requirements_asvs_xfood.json')">Inspecionar JSON</button>
            </div>
          </div>

          <!-- Artefato 2: Modelagem STRIDE & Threat Dragon -->
          <div style="background:#070b14; border:1px solid #1e293b; border-radius:6px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
            <div style="display:flex; align-items:center; gap:12px;">
              <span style="font-size:20px;">🛡️</span>
              <div>
                <div style="font-weight:700; color:#fff; font-size:13px;">Modelo de Ameaças & Diagrama DFD Interativo</div>
                <div style="color:var(--text-muted); font-size:11.5px;">04_threat_model_threat_dragon.svg · 6 Ameaças STRIDE mitigadas em 5 trust boundaries</div>
              </div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <span class="tag tag-purple">STRIDE / DFD</span>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="switchStage(4)">Ver no Estágio 4 ↗</button>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="viewRaw('04_threat_model_stride_xfood.json')">Inspecionar JSON</button>
            </div>
          </div>

          <!-- Artefato 3: Deliberação Dialética Tripartite -->
          <div style="background:#070b14; border:1px solid #1e293b; border-radius:6px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
            <div style="display:flex; align-items:center; gap:12px;">
              <span style="font-size:20px;">⚖️</span>
              <div>
                <div style="font-weight:700; color:#fff; font-size:13px;">Ata de Deliberação Tripartite Dialética</div>
                <div style="color:var(--text-muted); font-size:11.5px;">06_tripartite_deliberation_xfood.json · Consenso arbitrado entre Requisitos (RE), Segurança (SEC) e Arquitetura (ARCH)</div>
              </div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <span class="tag tag-emerald">CONSENSO 100%</span>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="switchStage(6)">Ver no Estágio 6 ↗</button>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="viewRaw('06_tripartite_deliberation_xfood.json')">Inspecionar JSON</button>
            </div>
          </div>

          <!-- Artefato 4: Grafo Ontológico do Domínio -->
          <div style="background:#070b14; border:1px solid #1e293b; border-radius:6px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
            <div style="display:flex; align-items:center; gap:12px;">
              <span style="font-size:20px;">🧠</span>
              <div>
                <div style="font-weight:700; color:#fff; font-size:13px;">Topologia Ontológica de Domínio & GraphRAG</div>
                <div style="color:var(--text-muted); font-size:11.5px;">02_graphrag_ontology_graph.svg · 10 Nós semânticos e relações entre BPMN e regras de negócio</div>
              </div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <span class="tag tag-blue">GraphRAG</span>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="switchStage(2)">Ver no Estágio 2 ↗</button>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="viewRaw('02_graphrag_ontology_xfood.json')">Inspecionar JSON</button>
            </div>
          </div>

          <!-- Artefato 5: Feeds de Inteligência de Ameaças -->
          <div style="background:#070b14; border:1px solid #1e293b; border-radius:6px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
            <div style="display:flex; align-items:center; gap:12px;">
              <span style="font-size:20px;">📡</span>
              <div>
                <div style="font-weight:700; color:#fff; font-size:13px;">Feeds de Inteligência de Ameaças & CVEs</div>
                <div style="color:var(--text-muted); font-size:11.5px;">03_threat_intel_delivery_feeds.json · CVE-2024-38816, BOLA CWE-862, Pix CWE-384, DoS CVE-2023-44487</div>
              </div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <span class="tag tag-orange">CISA / NVD / BACEN</span>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="switchStage(3)">Ver no Estágio 3 ↗</button>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="viewRaw('03_threat_intel_delivery_feeds.json')">Inspecionar JSON</button>
            </div>
          </div>

          <!-- Artefato 6: Resolução Upstream -->
          <div style="background:#070b14; border:1px solid #1e293b; border-radius:6px; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
            <div style="display:flex; align-items:center; gap:12px;">
              <span style="font-size:20px;">🎯</span>
              <div>
                <div style="font-weight:700; color:#fff; font-size:13px;">Resolução de Cenário & Ingestão Upstream</div>
                <div style="color:var(--text-muted); font-size:11.5px;">01_scenario_resolution_upstream.json · Classificação Greenfield e cold start resolvido</div>
              </div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <span class="tag tag-emerald">CENÁRIO 1</span>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="switchStage(1)">Ver no Estágio 1 ↗</button>
              <button class="btn btn-secondary" style="font-size:11px; padding:4px 10px;" onclick="viewRaw('01_scenario_resolution_upstream.json')">Inspecionar JSON</button>
            </div>
          </div>

        </div>
      </div>

      <!-- 2. PAINEL DE DELIBERAÇÃO DO ESPECIALISTA COM OS BOTÕES DENTRO DO GRID -->
      <div class="hitl-panel">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; border-bottom:1px solid #1e293b; padding-bottom:12px;">
          <div>
            <div style="font-size:16px; font-weight:800; color:#fff; display:flex; align-items:center; gap:8px;">
              <span>🧑‍💼 Estação de Deliberação do Auditor Humano (Quality Gate)</span>
            </div>
            <p style="color:var(--text-muted); font-size:12.5px; margin-top:2px;">
              Inspeção ativa de conformidade. Selecione sua decisão deliberativa nos botões do grid abaixo para emitir a assinatura forense e orientar o pipeline:
            </p>
          </div>
          <div>
            <span class="badge badge-approved" id="hitl-status-badge">GATEWAY: APROVADO</span>
          </div>
        </div>

        <!-- FORMULÁRIO DE IDENTIFICAÇÃO DO AUDITOR -->
        <div class="grid-3" style="margin-bottom:16px;">
          <div>
            <div class="card-subtitle">Auditor Responsável</div>
            <input type="text" class="hitl-input" id="hitl-auditor-name" value="Francis Martins">
          </div>
          <div>
            <div class="card-subtitle">Cargo / Especialidade</div>
            <input type="text" class="hitl-input" id="hitl-auditor-role" value="Lead Security Architect & Business Requirements Specialist">
          </div>
          <div>
            <div class="card-subtitle">Credencial / Certificação</div>
            <input type="text" class="hitl-input" id="hitl-auditor-creds" value="MSc Software Engineering (UnB) / ISO 27001 Lead Implementer">
          </div>
        </div>

        <!-- BOTÕES DE AÇÃO DO AUDITOR DENTRO DO GRID (CONFORME SOLICITADO) -->
        <div class="grid-3" style="margin-bottom:16px;">
          <button class="btn-approve" onclick="executeHitlAction('APROVADO_SEM_RESSALVAS')" style="justify-content:center; width:100%; font-size:13px; padding:11px 14px;">
            ✓ Aprovar Integralmente
          </button>
          <button class="btn-warn" onclick="toggleRessalvasPanel()" style="justify-content:center; width:100%; font-size:13px; padding:11px 14px;">
            ⚠️ Aprovar com Ressalvas
          </button>
          <button class="btn-reject" onclick="toggleVetoPanel()" style="justify-content:center; width:100%; font-size:13px; padding:11px 14px;">
            ✕ Reprovar (Gate Veto)
          </button>
        </div>

        <!-- BARRA COMPACTA DE AUDITORIA FORENSE & DOUBLE LOOP INTEGRADA NO CARD -->
        <div style="background:#070a12; border:1px solid #1e293b; border-radius:6px; padding:10px 14px; font-family:var(--font-mono); font-size:12px; display:flex; justify-content:space-between; align-items:center; margin-top:14px; flex-wrap:wrap; gap:8px;">
          <div>
            <span style="color:#64748b;">SHA-256 FORENSE:</span>
            <strong style="color:#38bdf8; margin-left:8px;" id="cert-hash-val">16249b2ed84d164ee0d702ded831e1a058b73184ab38f5ac0db02d2524e5f68c</strong>
          </div>
          <div style="display:flex; gap:8px; align-items:center;">
            <span style="color:#94a3b8; font-size:11px;" id="auditor-timestamp">Timestamp UTC: 2026-09-22T12:52:13Z</span>
            <button class="btn btn-secondary" style="padding:3px 8px; font-size:11px;" onclick="copyHash()">Copiar Hash</button>
            <span class="tag tag-emerald" id="cert-seal-tag">IMUTÁVEL</span>
          </div>
        </div>

        <div style="margin-top:10px; background:#080c16; padding:10px 14px; border-radius:6px; border:1px solid #1e293b; font-size:12px;">
          <span style="font-weight:700; color:#c084fc;">🔄 Aprendizagem Organizacional (Double-Loop):</span>
          <span style="color:var(--text-muted); margin-left:6px;" id="double-loop-text">Arquétipo de Food Delivery registrado no Grafo Corporativo para reutilização em futuros projetos da Empresa X.</span>
        </div>

        <!-- SUB-PAINEL 1: AJUSTES & RESSALVAS (COLAPSÁVEL) -->
        <div id="hitl-panel-ressalvas" style="display:none; background:#070b14; border:1px solid #d97706; border-radius:8px; padding:16px; margin-top:14px; animation:fadeIn 0.2s;">
          <div style="font-weight:700; color:#fbbf24; margin-bottom:6px; font-size:14px;">
            ✏️ Instruções de Ajuste & Re-inferência dos Agentes Multi-Agentes:
          </div>
          <p style="color:var(--text-muted); font-size:12.5px; margin-bottom:10px;">
            Selecione uma ressalva técnica predefinida ou digite novas exigências para disparar uma nova rodada de inferência dos agentes:
          </p>

          <div style="margin-bottom:10px;">
            <div class="card-subtitle">Presets Rápidos de Ajuste Arquitetural:</div>
            <select class="hitl-input" id="hitl-preset-select" onchange="applyRessalvaPreset(this.value)" style="cursor:pointer;">
              <option value="preset_pin_ttl">[CE07 / RN09] Expiração de PIN de coleta em 120s e Rate Limit de 3 tentativas contra força bruta</option>
              <option value="preset_cart_hmac">[RN02] Assinatura HMAC-SHA256 no payload de alteração de preços do carrinho de compras</option>
              <option value="preset_chat_e2ee">[LGPD] Criptografia de ponta a ponta (E2EE) no canal de mensagens entregador-cliente</option>
              <option value="custom">[Customizado] Digitar texto livre / nova exigência regulatória</option>
            </select>
          </div>

          <div style="margin-bottom:10px;">
            <div class="card-subtitle">Texto da Ressalva do Auditor:</div>
            <textarea class="hitl-input hitl-textarea" id="hitl-ressalva-text">Exigir que o PIN de coleta gerado na confirmação do pedido possua TTL estrito de 120 segundos e bloqueio temporário após 3 tentativas inválidas de inserção pelo motoboy (Proteção contra Brute-Force no balcão CE07).</textarea>
          </div>

          <div style="margin-bottom:12px;">
            <div class="card-subtitle">Insumo Complementar (Opcional - Trecho BPMN ou Regra):</div>
            <input type="text" class="hitl-input" id="hitl-extra-input" placeholder="Ex: RN12 - Não permitir PIN sequencial (1234, 0000) e alertar central em falhas consecutivas.">
          </div>

          <div style="display:flex; justify-content:flex-end; gap:10px;">
            <button class="btn btn-secondary" onclick="toggleRessalvasPanel()">Cancelar</button>
            <button class="btn-warn" onclick="triggerReInferenceCycle()" style="font-size:13.5px; padding:10px 22px;">
              🚀 Reiniciar Ciclo de Inferência com Ressalvas
            </button>
          </div>
        </div>

        <!-- SUB-PAINEL 2: VETO / REPROVAÇÃO (COLAPSÁVEL) -->
        <div id="hitl-panel-veto" style="display:none; background:#070b14; border:1px solid #e11d48; border-radius:8px; padding:16px; margin-top:14px; animation:fadeIn 0.2s;">
          <div style="font-weight:700; color:#f43f5e; margin-bottom:6px; font-size:14px;">
            ⛔ Justificativa Formal do Veto de Segurança:
          </div>
          <p style="color:var(--text-muted); font-size:12.5px; margin-bottom:10px;">
            O veto suspende o avanço do projeto para código e bloqueia o despacho para CI/CD (Jira / GitLab):
          </p>

          <textarea class="hitl-input hitl-textarea" id="hitl-veto-text" placeholder="Descreva os riscos críticos não mitigados que motivaram a reprovação do pipeline..."></textarea>

          <div style="display:flex; justify-content:flex-end; gap:10px; margin-top:12px;">
            <button class="btn btn-secondary" onclick="toggleVetoPanel()">Cancelar</button>
            <button class="btn-reject" onclick="confirmVetoAction()">
              🚫 Confirmar Reprovação e Bloquear CI/CD
            </button>
          </div>
        </div>
      </div>

    </div>

    <!-- ================= STAGE 8 ================= -->
    <div class="stage-section" id="stage-8">
      <div class="section-header">
        <div class="section-title">
          <h2>🚀 Estágio 8: Despacho CI/CD & Artefatos de Engenharia</h2>
          <p>Exportação direta para ferramentas do time de desenvolvimento: Jira, GitLab CI e suíte Cucumber BDD.</p>
        </div>
        <div class="actions-bar">
          <button class="btn btn-primary" onclick="copyCurrentCode()">Copiar Código Exibido</button>
        </div>
      </div>

      <!-- ALERTA DE BLOQUEIO DE CI/CD EM CASO DE REPROVAÇÃO -->
      <div id="cicd-blocked-banner" style="display:none; background:#450a0a; border:2px solid #ef4444; border-radius:8px; padding:20px; margin-bottom:20px; text-align:center;">
        <h3 style="color:#f87171; font-size:18px; margin-bottom:6px;">⛔ DESPACHO CI/CD BLOQUEADO PELO AUDITOR HITL</h3>
        <p style="color:#fca5a5; font-size:13.5px;" id="cicd-blocked-reason">O avanço para a esteira de desenvolvimento foi suspenso por não-conformidade de segurança.</p>
      </div>

      <!-- ALERTA DE RESSALVAS NO CI/CD -->
      <div id="cicd-ressalva-banner" style="display:none; background:#172554; border:1px solid #3b82f6; border-radius:8px; padding:14px; margin-bottom:16px;">
        <span style="color:#60a5fa; font-weight:700;">ℹ️ CICLO REFINADO POR RESSALVAS HITL:</span>
        <span style="color:#bfdbfe; font-size:13px; margin-left:8px;">O novo requisito REQ-XFOOD-006 (Expiração de PIN & Rate Limiting) foi injetado com sucesso no backlog do Jira e na suíte de testes Cucumber BDD.</span>
      </div>

      <div style="display:flex; gap:10px; margin-bottom:16px;" id="cicd-tabs-nav">
        <button class="btn btn-secondary active" id="tab-jira" onclick="switchCiTab('jira')">Jira REST API (Épicos & Histórias)</button>
        <button class="btn btn-secondary" id="tab-gitlab" onclick="switchCiTab('gitlab')">GitLab CI (Quality Gate Policy)</button>
        <button class="btn btn-secondary" id="tab-cucumber" onclick="switchCiTab('cucumber')">Cucumber BDD (.feature)</button>
      </div>

      <div class="card" id="cicd-code-card">
        <div class="card-title" id="ci-card-title">Jira Security Issues Payload (JSON)</div>
        <pre class="code-block" id="ci-code-view" style="max-height:480px;"></pre>
      </div>
    </div>

    <!-- FOOTER NAV -->
    <div class="nav-footer">
      <button class="btn btn-secondary" id="btn-prev" onclick="navigateStage(-1)">◀ Fase Anterior</button>
      <div style="color:var(--text-dim); font-size:12px;">PRISMA-IA v1.0.0 · Execução Upstream Delivery Y</div>
      <button class="btn btn-primary" id="btn-next" onclick="navigateStage(1)">Próxima Fase ▶</button>
    </div>

  </div>

  <!-- MODAL RAW VIEWER -->
  <div class="modal-overlay" id="modal-viewer" onclick="closeModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 id="modal-title" style="font-size:15px; font-weight:700;">Visualizador de Arquivo</h3>
        <button class="btn btn-secondary" onclick="closeModal()">Fechar ✕</button>
      </div>
      <div class="modal-body">
        <pre class="code-block" id="modal-content" style="max-height:60vh; font-size:12px;"></pre>
      </div>
    </div>
  </div>

    <!-- MODAL CONSOLE DE EXECUÇÃO DO PIPELINE PRISMA-IA -->
  <div class="terminal-modal-overlay" id="modal-pipeline-runner">
    <div class="terminal-box" style="max-width:840px;">
      <div class="terminal-header">
        <div style="font-weight:700; color:#38bdf8; display:flex; align-items:center; gap:8px;">
          <span>🚀 PRISMA-IA Pipeline Execution Engine</span>
          <span style="color:#64748b; font-size:11px;">|</span>
          <span style="color:#94a3b8; font-size:12px;">Ingestão & Orquestração Multi-Agente em Tempo Real</span>
        </div>
        <div id="pipe-status-badge" style="font-size:11px; background:#0369a1; color:#e0f2fe; padding:3px 10px; border-radius:4px; font-family:var(--font-mono); font-weight:700;">EXECUTANDO...</div>
      </div>

      <!-- BARRA DE PROGRESSO -->
      <div style="background:#090d16; padding:12px 20px 6px 20px; border-bottom:1px solid #1e293b;">
        <div style="display:flex; justify-content:space-between; font-size:11.5px; color:#94a3b8; margin-bottom:6px;">
          <span id="pipe-progress-phase" style="font-weight:600; color:#e2e8f0;">Fase 1/8: Ingestão de Insumos Upstream...</span>
          <span id="pipe-progress-pct" style="font-weight:700; color:#38bdf8;">0%</span>
        </div>
        <div style="height:6px; background:#1e293b; border-radius:3px; overflow:hidden;">
          <div id="pipe-progress-bar" style="width:0%; height:100%; background:linear-gradient(90deg, #0ea5e9, #38bdf8); transition:width 0.3s ease;"></div>
        </div>
      </div>

      <div class="terminal-body" id="pipe-console-body" style="height:350px;">
        <!-- Live logs injected by JS -->
      </div>

      <div style="background:#0c1322; padding:12px 20px; border-top:1px solid #1e293b; display:flex; justify-content:space-between; align-items:center;">
        <div style="font-size:11.5px; color:#64748b;" id="pipe-footer-text">Orquestrando módulos e agentes cognitivos da esteira...</div>
        <button class="btn btn-primary" id="btn-close-pipeline" onclick="finishPipelineModal()" style="display:none; background:linear-gradient(135deg, #10b981, #059669); font-weight:700;">Explorar Grafo Ontológico (Estágio 2 ▶)</button>
      </div>
    </div>
  </div>

  <!-- MODAL CONSOLE DE RE-INFERÊNCIA MULTI-AGENTE -->
  <div class="terminal-modal-overlay" id="modal-re-inference">
    <div class="terminal-box">
      <div class="terminal-header">
        <div style="font-weight:700; color:#38bdf8; display:flex; align-items:center; gap:8px;">
          <span>🔄 PRISMA-IA Multi-Agent Engine</span>
          <span style="color:#64748b; font-size:11px;">|</span>
          <span style="color:#94a3b8; font-size:12px;">Ciclo Reativo de Re-Inferência & Double-Loop</span>
        </div>
        <div id="term-status-badge" style="font-size:11px; background:#1e293b; color:#38bdf8; padding:3px 8px; border-radius:4px; font-family:var(--font-mono);">EXECUTANDO...</div>
      </div>
      <div class="terminal-body" id="term-console-body">
        <!-- Live logs injected by JS -->
      </div>
      <div style="background:#0c1322; padding:12px 20px; border-top:1px solid #1e293b; display:flex; justify-content:space-between; align-items:center;">
        <div style="font-size:11.5px; color:#64748b;" id="term-progress-text">Processando agentes deliberativos...</div>
        <button class="btn btn-primary" id="btn-close-terminal" onclick="finishReInferenceModal()" style="display:none;">Ver Resultados Atualizados ▶</button>
      </div>
    </div>
  </div>

  <script>
    // DADOS INJETADOS DIRETAMENTE DO PRISMA-IA
    const BUNDLE = """ + json_bundle_str + """;

    let currentStage = 1;
    const totalStages = 8;
    let hitlState = {
      decision: "APROVADO_SEM_RESSALVAS",
      auditor: "Francis Martins",
      role: "Lead Security Architect & Business Requirements Specialist",
      credentials: "MSc Software Engineering (UnB) / ISO 27001 Lead Implementer",
      hash: "16249b2ed84d164ee0d702ded831e1a058b73184ab38f5ac0db02d2524e5f68c",
      timestamp: "2026-09-22T12:52:13Z",
      ressalvaText: "",
      vetoReason: "",
      hasRessalvaInjected: false
    };

    let pipelineExecuted = false;
    let folderLoaded = false;

    function switchStage(stageNum) {
      if (stageNum < 1 || stageNum > totalStages) return;
      if (stageNum > 1 && !pipelineExecuted) {
        showToast("🔒 Estágio Bloqueado: Conecte os insumos e execute o pipeline no Estágio 1 primeiro!");
        return;
      }
      currentStage = stageNum;

      document.querySelectorAll('.step-btn').forEach((btn, idx) => {
        if (idx + 1 === currentStage) {
          btn.classList.add('active');
          btn.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
        } else {
          btn.classList.remove('active');
        }
      });

      document.querySelectorAll('.stage-section').forEach((sec, idx) => {
        if (idx + 1 === currentStage) {
          sec.classList.add('active');
        } else {
          sec.classList.remove('active');
        }
      });

      document.getElementById('btn-prev').disabled = (currentStage === 1);
      document.getElementById('btn-next').disabled = (currentStage === totalStages);

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function navigateStage(delta) {
      switchStage(currentStage + delta);
    }

    function viewRaw(filename) {
      const content = BUNDLE.raw_files[filename] || "Arquivo não encontrado.";
      document.getElementById('modal-title').innerText = "Inspecionando: " + filename;
      document.getElementById('modal-content').innerText = content;
      document.getElementById('modal-viewer').classList.add('active');
    }

    function closeModal() {
      document.getElementById('modal-viewer').classList.remove('active');
    }

    // ALTERNÂNCIA DE VISÕES NO ESTÁGIO 5 (DOCUMENTO OFICIAL vs CARDS ÁGEIS)
    function switchSecReqView(mode) {
      const docWrapper = document.getElementById('sec-req-doc-preview-wrapper');
      const cardsWrapper = document.getElementById('sec-req-agile-cards-wrapper');
      const btnDoc = document.getElementById('btn-toggle-doc-preview');
      const btnAgile = document.getElementById('btn-toggle-agile-cards');

      if (mode === 'doc') {
        docWrapper.style.display = 'block';
        cardsWrapper.style.display = 'none';
        btnDoc.classList.add('active');
        btnAgile.classList.remove('active');
      } else {
        docWrapper.style.display = 'none';
        cardsWrapper.style.display = 'block';
        btnDoc.classList.remove('active');
        btnAgile.classList.add('active');
      }
    }

    // ALTERNÂNCIA DE VISÕES NO ESTÁGIO 4 (STRIDE)
    function switchStrideView(mode) {
      const cardsView = document.getElementById('stride-cards-view');
      const dfdView = document.getElementById('stride-dfd-view');
      const btnCards = document.getElementById('btn-view-stride-cards');
      const btnDfd = document.getElementById('btn-view-stride-dfd');

      if (mode === 'dfd') {
        cardsView.style.display = 'none';
        dfdView.style.display = 'block';
        btnCards.classList.remove('active');
        btnDfd.classList.add('active');
      } else {
        cardsView.style.display = 'block';
        dfdView.style.display = 'none';
        btnCards.classList.add('active');
        btnDfd.classList.remove('active');
      }
    }

    function setupThreatDragonPins() {
      for (let i = 1; i <= 6; i++) {
        const pin = document.getElementById('pin-t' + i);
        if (pin) {
          pin.style.cursor = 'pointer';
          pin.addEventListener('click', () => {
            const threats = (BUNDLE.threats && BUNDLE.threats.threats) ? BUNDLE.threats.threats : [];
            const t = threats[i - 1];
            if (t) {
              alert(`[OWASP THREAT DRAGON - AMEAÇA T${i}]\nCategoria: ${t.category}\nAlvo: ${t.component}\nDescrição: ${t.description}\nMitigação: ${t.mitigation_strategy}`);
            }
          });
        }
      }
    }

    // 1. RENDERIZAR GRAFO (ESTÁGIO 2)
    function renderGraph() {
      try {
        const nodesContainer = document.getElementById('graph-nodes-container');
        if (!nodesContainer) return;

        let nodesList = [];
        if (BUNDLE.graph && BUNDLE.graph.nodes) {
          if (Array.isArray(BUNDLE.graph.nodes)) {
            nodesList = BUNDLE.graph.nodes;
          } else if (typeof BUNDLE.graph.nodes === 'object') {
            nodesList = Object.entries(BUNDLE.graph.nodes).map(([key, val]) => {
              return Object.assign({ id: key, label: key }, val);
            });
          }
        }

        nodesContainer.innerHTML = nodesList.map(n => {
          const typeStr = n.type || 'NÓ DE DOMÍNIO';
          const labelStr = n.label || n.id || n.name || 'Componente';
          const descStr = n.purpose || n.description || n.name || (n.standards ? 'Padrões: ' + n.standards.join(', ') : '');
          const critStr = n.criticality || n.sla || (n.protocol ? 'Protocolo: ' + n.protocol : '');
          
          return `
            <div class="card">
              <div class="card-subtitle">Tipo: ${typeStr}</div>
              <div class="card-title">${labelStr}</div>
              <p style="color:var(--text-muted); font-size:12.5px; margin-bottom:8px;">${descStr}</p>
              ${critStr ? `<div style="font-size:11.5px; color:#38bdf8;"><strong>Parâmetro:</strong> ${critStr}</div>` : ''}
            </div>
          `;
        }).join('');

        const relsContainer = document.getElementById('graph-relations-container');
        if (!relsContainer) return;

        let relsList = (BUNDLE.graph && Array.isArray(BUNDLE.graph.relations)) ? BUNDLE.graph.relations : [];

        relsContainer.innerHTML = `
          <table class="compare-table">
            <thead>
              <tr><th>Origem</th><th>Destino</th><th>Relação do Negócio</th><th>Protocolo / Nível</th></tr>
            </thead>
            <tbody>
              ${relsList.map(r => `
                <tr>
                  <td><strong>${r.from || r.source || 'Origem'}</strong></td>
                  <td><strong>${r.to || r.target || 'Destino'}</strong></td>
                  <td>${r.relation || r.type || 'Interage com'}</td>
                  <td><code>${r.protocol || 'REST / HTTPS / WSS'}</code></td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        `;
      } catch (err) {
        console.error("Erro em renderGraph:", err);
      }
    }

    // 2. RENDERIZAR FEEDS (ESTÁGIO 3) COM RASTREABILIDADE DE URLS
    function renderFeeds() {
      try {
        const container = document.getElementById('threat-feeds-container');
        if (!container) return;

        let feedsList = Array.isArray(BUNDLE.feeds) ? BUNDLE.feeds : [];

        container.innerHTML = feedsList.map(f => {
          const idStr = f.feed_id || f.id || 'FEED';
          const cveStr = f.cve || f.cve_or_cwe || 'CVE';
          const titleStr = f.name || cveStr;
          const techStr = f.affected_technology || 'Componente da Stack XFood';
          const cvssVal = f.cvss ? f.cvss : 8.5;
          const isCrit = cvssVal >= 9.0;
          const cvssBadge = `<span class="tag ${isCrit ? 'tag-red' : 'tag-orange'}">CVSS ${cvssVal} · ${f.severity || (isCrit ? 'CRÍTICO' : 'ALTO')}</span>`;
          const impactStr = f.impact_in_xfood || f.description || '';
          const mitigStr = f.mitigation_in_xfood || '';

          const ref = f.database_reference || {};
          const primaryBase = ref.primary_database || 'Base de Inteligência';
          const primaryUrl = ref.primary_url || '#';
          const nvdUrl = ref.nvd_url || null;
          const mitreTech = ref.mitre_attack_technique || f.mitre_technique || '';
          const mitreUrl = ref.mitre_attack_url || null;
          const cweId = ref.cwe_id || f.cwe || '';
          const cweUrl = ref.cwe_url || null;

          return `
            <div class="card" style="border-top:3px solid ${isCrit ? '#f43f5e' : '#f59e0b'}; display:flex; flex-direction:column; justify-content:space-between;">
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                  <div style="display:flex; gap:6px; align-items:center;">
                    <span class="tag tag-blue">${idStr}</span>
                    <span class="tag tag-purple">${primaryBase.split('(')[0].trim()}</span>
                  </div>
                  ${cvssBadge}
                </div>

                <div class="card-title" style="font-size:16px; margin-bottom:2px; color:#fff;">${cveStr}</div>
                <div style="font-size:13px; font-weight:600; color:#cbd5e1; margin-bottom:6px;">${titleStr}</div>
                <div style="font-size:12px; font-weight:700; color:#38bdf8; margin-bottom:12px;">Alvo na Arquitetura: ${techStr}</div>

                <!-- BOX DE URLS E BASES DE REFERÊNCIA OFICIAIS -->
                <div style="background:#070b14; border:1px solid #1e293b; border-radius:6px; padding:10px 12px; margin-bottom:12px; font-size:11.5px;">
                  <div style="font-weight:700; color:#94a3b8; margin-bottom:6px; text-transform:uppercase; font-size:10px; letter-spacing:0.5px;">
                    🔗 Rastreabilidade Externa & Bases Consultadas:
                  </div>
                  <div style="display:flex; flex-direction:column; gap:4px;">
                    <div>
                      <span style="color:#64748b;">Base Primária:</span>
                      <a href="${primaryUrl}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; font-weight:600; text-decoration:none; margin-left:4px;">
                        ${primaryBase} ↗
                      </a>
                    </div>
                    ${nvdUrl ? `
                      <div>
                        <span style="color:#64748b;">Ficha NIST NVD:</span>
                        <a href="${nvdUrl}" target="_blank" rel="noopener noreferrer" style="color:#38bdf8; font-weight:600; text-decoration:none; margin-left:4px;">
                          ${cveStr} no NVD ↗
                        </a>
                      </div>
                    ` : ''}
                    ${mitreTech ? `
                      <div>
                        <span style="color:#64748b;">MITRE ATT&CK:</span>
                        ${mitreUrl ? `<a href="${mitreUrl}" target="_blank" rel="noopener noreferrer" style="color:#c084fc; font-weight:600; text-decoration:none; margin-left:4px;">${mitreTech} ↗</a>` : `<span style="color:#c084fc; margin-left:4px;">${mitreTech}</span>`}
                      </div>
                    ` : ''}
                    ${cweId ? `
                      <div>
                        <span style="color:#64748b;">MITRE CWE:</span>
                        ${cweUrl ? `<a href="${cweUrl}" target="_blank" rel="noopener noreferrer" style="color:#34d399; font-weight:600; text-decoration:none; margin-left:4px;">${cweId} ↗</a>` : `<span style="color:#34d399; margin-left:4px;">${cweId}</span>`}
                      </div>
                    ` : ''}
                  </div>
                </div>

                <p style="color:var(--text-muted); font-size:12.5px; margin-bottom:10px;">
                  <strong>Impacto no XFood:</strong> ${impactStr}
                </p>
              </div>

              ${mitigStr ? `
                <div style="background:#09121f; border-left:3px solid #34d399; padding:8px 10px; border-radius:4px; font-size:11.5px; color:#34d399;">
                  <strong>Mitigação PRISMA:</strong> ${mitigStr}
                </div>
              ` : ''}
            </div>
          `;
        }).join('');
      } catch (err) {
        console.error("Erro em renderFeeds:", err);
      }
    }

    // 3. RENDERIZAR STRIDE (ESTÁGIO 4)
    function renderThreats(filterSeverity) {
      try {
        const container = document.getElementById('threats-cards-container');
        if (!container) return;

        let threatsList = (BUNDLE.threats && Array.isArray(BUNDLE.threats.threats)) ? BUNDLE.threats.threats : [];
        
        const fAll = document.getElementById('filter-all');
        const fCrit = document.getElementById('filter-crit');
        const fHigh = document.getElementById('filter-high');
        if (fAll) fAll.classList.remove('active');
        if (fCrit) fCrit.classList.remove('active');
        if (fHigh) fHigh.classList.remove('active');

        if (filterSeverity === 'CRÍTICO') {
          if (fCrit) fCrit.classList.add('active');
          threatsList = threatsList.filter(t => (t.impact === 'CRÍTICO' || (t.severity && t.severity.includes('CRÍTICO'))));
        } else if (filterSeverity === 'ALTO') {
          if (fHigh) fHigh.classList.add('active');
          threatsList = threatsList.filter(t => (t.impact === 'ALTO' || (t.severity && t.severity.includes('ALTO'))));
        } else {
          if (fAll) fAll.classList.add('active');
        }

        container.innerHTML = threatsList.map(t => {
          const idStr = t.id || 'THREAT';
          const catStr = t.category || t.stride_category || 'STRIDE';
          const compStr = t.component || 'Ecossistema';
          const descStr = t.description || '';
          const cweStr = t.associated_cwe || t.cwe || '';
          const mitreStr = t.mitre_attack || '';
          const mitigStr = t.mitigation_strategy || t.mitigation || '';
          const impactStr = t.impact || t.severity || 'ALTO';

          const isCrit = impactStr.toUpperCase().includes('CRÍTICO');

          return `
            <div class="card">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
                <div>
                  <span class="tag tag-purple">${catStr}</span>
                  <span class="tag ${isCrit ? 'tag-red' : 'tag-orange'}" style="margin-left:4px;">${impactStr}</span>
                </div>
                <span style="font-family:var(--font-mono); font-size:11.5px; color:#64748b;">${idStr}</span>
              </div>
              <div style="font-size:15px; font-weight:700; color:#fff; margin-bottom:4px;">${descStr}</div>
              <div style="font-size:12px; color:#38bdf8; margin-bottom:8px;"><strong>Componente Alvo:</strong> ${compStr}</div>
              <div style="background:#0a0f1d; padding:10px; border-radius:6px; font-size:12px; color:var(--text-muted); margin-bottom:8px;">
                ${cweStr ? `<strong>Fraqueza Associada:</strong> ${cweStr}<br>` : ''}
                ${mitreStr ? `<strong>Técnica MITRE:</strong> ${mitreStr}` : ''}
              </div>
              <div style="font-size:12px; color:#34d399;">
                <strong>Mitigação PRISMA:</strong> ${mitigStr}
              </div>
            </div>
          `;
        }).join('');
      } catch (err) {
        console.error("Erro em renderThreats:", err);
      }
    }

    function filterThreats(sev) {
      renderThreats(sev);
    }

    // 4. RENDERIZAR REQUISITOS ASVS & BDD (ESTÁGIO 5)
    function renderReqs() {
      try {
        const container = document.getElementById('sec-reqs-container');
        if (!container) return;

        let reqsList = (BUNDLE.reqs && Array.isArray(BUNDLE.reqs.requirements)) ? BUNDLE.reqs.requirements : [];

        container.innerHTML = reqsList.map(r => {
          const idStr = r.id || 'REQ';
          const asvsChapter = (r.compliance_mapping && r.compliance_mapping.asvs_level) ? r.compliance_mapping.asvs_level : (r.asvs_chapter || 'OWASP ASVS');
          const asvsLevel = r.asvs_level || (r.compliance_mapping && r.compliance_mapping.asvs_level) || 'Nível 2';
          const titleStr = r.title || r.invest_title || 'Requisito de Segurança';
          const specStr = r.normative_specification || r.specification || '';
          const bddStr = r.bdd_gherkin || '';
          const mitigatesStr = r.mitigates_threat || (r.mitigates && Array.isArray(r.mitigates) ? r.mitigates.join(', ') : '');
          const stepsList = r.technical_implementation_steps || [];

          return `
            <div class="card" id="card-req-${idStr}">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
                  <span class="tag tag-blue">${idStr}</span>
                  <span class="tag tag-purple">${asvsChapter}</span>
                  <span class="tag tag-emerald">${asvsLevel}</span>
                  ${mitigatesStr ? `<span class="tag tag-orange">Mitiga: ${mitigatesStr.split('(')[0].trim()}</span>` : ''}
                </div>
                <span style="font-size:12px; color:var(--text-dim);">${r.sprint_priority || 'MVP'} · ${r.story_points ? r.story_points + ' SP' : 'INVEST'}</span>
              </div>
              <div style="font-size:16px; font-weight:700; color:#fff; margin-bottom:6px;">${titleStr}</div>
              
              <div style="font-size:12.5px; color:#93c5fd; margin-bottom:10px; font-style:italic;">
                "${r.user_story_invest || ''}"
              </div>

              <div style="font-size:13px; color:var(--text-muted); margin-bottom:12px;">
                <strong>Especificação Normativa (RFC 2119):</strong> ${specStr}
              </div>

              ${stepsList.length > 0 ? `
                <div style="background:#0a0f1d; border:1px solid #1e293b; border-radius:6px; padding:10px 14px; margin-bottom:12px;">
                  <div style="font-size:11.5px; font-weight:700; color:#38bdf8; margin-bottom:4px;">🛠️ GUIA DE IMPLEMENTAÇÃO TÉCNICA:</div>
                  <ul style="padding-left:18px; font-size:12px; color:#cbd5e1; line-height:1.5;">
                    ${stepsList.map(s => `<li>${s}</li>`).join('')}
                  </ul>
                </div>
              ` : ''}

              ${bddStr ? `
                <div class="card-subtitle" style="margin-bottom:4px;">Cenário de Teste de Aceitação (Cucumber BDD / Gherkin):</div>
                <pre class="code-block" style="font-size:11.5px;">${bddStr}</pre>
              ` : ''}

              ${r.ci_cd_verification ? `
                <div style="font-size:12px; color:#34d399; margin-top:8px;">
                  <strong>✓ Definition of Done (DoD CI/CD):</strong> ${r.ci_cd_verification}
                </div>
              ` : ''}
            </div>
          `;
        }).join('');
      } catch (err) {
        console.error("Erro em renderReqs:", err);
      }
    }

    // 5. RENDERIZAR DELIBERAÇÃO TRIPARTITE (ESTÁGIO 6)
    function renderDeliberation() {
      try {
        const container = document.getElementById('deliberation-container');
        if (!container) return;

        let roundsList = (BUNDLE.deliberation && Array.isArray(BUNDLE.deliberation.rounds)) ? BUNDLE.deliberation.rounds : [];

        container.innerHTML = roundsList.map(rnd => {
          return `
            <div class="card" style="margin-bottom:20px; border-left:4px solid #8b5cf6;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
                <div style="font-size:16px; font-weight:700; color:#fff;">
                  <span class="tag tag-purple">Rodada ${rnd.round}</span>
                  <span style="margin-left:8px;">${rnd.title}</span>
                </div>
              </div>
              
              <div style="display:flex; flex-direction:column; gap:12px;">
                <div style="background:#090d16; padding:12px; border-radius:6px; border-left:3px solid #60a5fa;">
                  <div style="font-size:12px; font-weight:700; color:#60a5fa; margin-bottom:4px;">👤 RE-Agent (Engenharia de Requisitos & Negócio)</div>
                  <div style="font-size:13px; color:#cbd5e1;">${rnd.re_agent}</div>
                </div>

                <div style="background:#090d16; padding:12px; border-radius:6px; border-left:3px solid #c084fc;">
                  <div style="font-size:12px; font-weight:700; color:#c084fc; margin-bottom:4px;">🛡️ SEC-Agent (Segurança da Informação & Compliance)</div>
                  <div style="font-size:13px; color:#cbd5e1;">${rnd.sec_agent}</div>
                </div>

                <div style="background:#090d16; padding:12px; border-radius:6px; border-left:3px solid #34d399;">
                  <div style="font-size:12px; font-weight:700; color:#34d399; margin-bottom:4px;">🏗️ ARCH-Agent (Arquitetura de Software & Desempenho)</div>
                  <div style="font-size:13px; color:#cbd5e1;">${rnd.arch_agent}</div>
                </div>
              </div>
            </div>
          `;
        }).join('');
      } catch (err) {
        console.error("Erro em renderDeliberation:", err);
      }
    }

    // 6. MOTOR CRIPTOGRÁFICO SHA-256 REAL NO NAVEGADOR
    async function calculateSha256(text) {
      const msgBuffer = new TextEncoder().encode(text);
      const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
      return hashHex;
    }

    // 7. GESTÃO INTERATIVA HITL & QUALITY GATE (ESTÁGIO 7)
    function toggleRessalvasPanel() {
      const panel = document.getElementById('hitl-panel-ressalvas');
      const vetoPanel = document.getElementById('hitl-panel-veto');
      vetoPanel.style.display = 'none';
      panel.style.display = (panel.style.display === 'none' || panel.style.display === '') ? 'block' : 'none';
      if (panel.style.display === 'block') {
        panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    function toggleVetoPanel() {
      const panel = document.getElementById('hitl-panel-veto');
      const ressalvasPanel = document.getElementById('hitl-panel-ressalvas');
      ressalvasPanel.style.display = 'none';
      panel.style.display = (panel.style.display === 'none' || panel.style.display === '') ? 'block' : 'none';
      if (panel.style.display === 'block') {
        panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    function applyRessalvaPreset(presetKey) {
      const txt = document.getElementById('hitl-ressalva-text');
      const extra = document.getElementById('hitl-extra-input');
      if (presetKey === 'preset_pin_ttl') {
        txt.value = "Exigir que o PIN de coleta gerado na confirmação do pedido possua TTL estrito de 120 segundos e bloqueio temporário após 3 tentativas inválidas de inserção pelo motoboy (Proteção contra Brute-Force no balcão CE07).";
        extra.value = "RN12 - Não permitir PIN sequencial (1234, 0000) e alertar central em falhas consecutivas.";
      } else if (presetKey === 'preset_cart_hmac') {
        txt.value = "Exigir assinatura digital HMAC-SHA256 no payload de atualização de itens do carrinho, validada pelo servidor antes de calcular o total do pedido.";
        extra.value = "Mitigação direta contra tampering de preço na RN02.";
      } else if (presetKey === 'preset_chat_e2ee') {
        txt.value = "Impor criptografia ponta a ponta (E2EE) no canal de WebSocket para mensagens entre entregador e cliente, garantindo privacidade conforme Art. 46 da LGPD.";
        extra.value = "Chaves efêmeras com protocolo Signal / Double Ratchet.";
      } else {
        txt.value = "";
        extra.value = "";
      }
    }

    async function executeHitlAction(actionType) {
      const name = document.getElementById('hitl-auditor-name').value.trim() || "Francis Martins";
      const role = document.getElementById('hitl-auditor-role').value.trim() || "Lead Security Architect";
      const creds = document.getElementById('hitl-auditor-creds').value.trim() || "ISO 27001 Lead Implementer";
      const nowUtc = new Date().toISOString();

      hitlState.decision = actionType;
      hitlState.auditor = name;
      hitlState.role = role;
      hitlState.credentials = creds;
      hitlState.timestamp = nowUtc;

      // Calcular novo hash SHA-256 criptográfico real
      const payloadToHash = JSON.stringify({
        project: "XFood_Delivery_Y",
        decision: actionType,
        auditor: { name, role, creds },
        timestamp: nowUtc,
        requirements_count: BUNDLE.reqs.requirements.length,
        hasRessalva: hitlState.hasRessalvaInjected
      });

      hitlState.hash = await calculateSha256(payloadToHash);

      updateHitlUI();

      // Fechar painéis
      document.getElementById('hitl-panel-ressalvas').style.display = 'none';
      document.getElementById('hitl-panel-veto').style.display = 'none';

      alert(`[HOMOLOGAÇÃO HITL REGISTRADA COM SUCESSO!]\nDecisão: ${actionType}\nAuditor: ${name}\nSHA-256 Forense: ${hitlState.hash}\nO certificado e as esteiras foram sincronizados.`);
    }

    function confirmVetoAction() {
      const reason = document.getElementById('hitl-veto-text').value.trim();
      if (!reason) {
        alert("Por favor, digite a justificativa técnica para o veto de segurança.");
        return;
      }
      hitlState.vetoReason = reason;
      executeHitlAction('REPROVADO_BLOQUEADO');
    }

    function updateHitlUI() {
      const statusBadge = document.getElementById('hitl-status-badge');
      const certBadge = document.getElementById('cert-status-badge');
      const globalBadge = document.getElementById('global-hitl-badge');
      const hashBadge = document.getElementById('global-hash-badge');
      const hashVal = document.getElementById('cert-hash-val');
      const auditorName = document.getElementById('auditor-name');
      const auditorRole = document.getElementById('auditor-role');
      const auditorTs = document.getElementById('auditor-timestamp');
      const sealTag = document.getElementById('cert-seal-tag');
      const doubleLoopText = document.getElementById('double-loop-text');

      if (auditorName) auditorName.innerText = hitlState.auditor;
      if (auditorRole) auditorRole.innerText = hitlState.role + (hitlState.credentials ? ' · ' + hitlState.credentials : '');
      if (auditorTs) auditorTs.innerText = "Timestamp UTC: " + hitlState.timestamp;
      if (hashVal) hashVal.innerText = hitlState.hash;
      if (hashBadge) hashBadge.innerText = "SHA-256: " + hitlState.hash.substring(0, 8) + "...";

      if (hitlState.decision === 'APROVADO_SEM_RESSALVAS') {
        if (statusBadge) { statusBadge.className = 'badge badge-approved'; statusBadge.innerText = 'GATEWAY: APROVADO'; }
        if (certBadge) { certBadge.className = 'badge badge-approved'; certBadge.innerText = 'GATEWAY: APROVADO'; }
        if (globalBadge) { globalBadge.className = 'badge badge-approved'; globalBadge.innerText = 'HITL Aprovado'; }
        if (sealTag) { sealTag.className = 'tag tag-emerald'; sealTag.innerText = 'IMUTÁVEL'; }
        if (doubleLoopText) doubleLoopText.innerText = "Arquétipo de Food Delivery registrado no Grafo Corporativo para reutilização em futuros projetos da Empresa X.";
        setCiCdLock(false);
      } else if (hitlState.decision === 'APROVADO_COM_RESSALVAS') {
        if (statusBadge) { statusBadge.className = 'badge badge-warning'; statusBadge.innerText = 'GATEWAY: APROVADO C/ RESSALVAS'; }
        if (certBadge) { certBadge.className = 'badge badge-warning'; certBadge.innerText = 'GATEWAY: APROVADO COM RESSALVAS INCORPORADAS'; }
        if (globalBadge) { globalBadge.className = 'badge badge-warning'; globalBadge.innerText = 'HITL Ressalvas Incorporadas'; }
        if (sealTag) { sealTag.className = 'tag tag-orange'; sealTag.innerText = 'RESSALVAS AUDITADAS'; }
        if (doubleLoopText) doubleLoopText.innerText = "Double-Loop Learning Ativado: Nova regra 'RULE_XFOOD_PIN_TTL_120S_RATE_LIMIT' consolidada e injetada no Grafo Ontológico para prevenir ataques de balcão nos próximos projetos.";
        setCiCdLock(false, true);
      } else if (hitlState.decision === 'REPROVADO_BLOQUEADO') {
        if (statusBadge) { statusBadge.className = 'badge badge-rejected'; statusBadge.innerText = 'GATEWAY: REPROVADO / BLOQUEADO'; }
        if (certBadge) { certBadge.className = 'badge badge-rejected'; certBadge.innerText = 'GATEWAY: REPROVADO / BLOQUEADO'; }
        if (globalBadge) { globalBadge.className = 'badge badge-rejected'; globalBadge.innerText = 'HITL Veto Registrado'; }
        if (sealTag) { sealTag.className = 'tag tag-red'; sealTag.innerText = 'VETO ATIVO'; }
        if (doubleLoopText) doubleLoopText.innerText = "Governança: Evento de não-conformidade registrado na trilha de auditoria corporativa como antípadrão.";
        setCiCdLock(true, false, hitlState.vetoReason);
      }
    }

    function setCiCdLock(isBlocked, hasRessalva = false, reason = "") {
      const bannerBlocked = document.getElementById('cicd-blocked-banner');
      const bannerRessalva = document.getElementById('cicd-ressalva-banner');
      const cicdCard = document.getElementById('cicd-code-card');
      const cicdTabs = document.getElementById('cicd-tabs-nav');
      const blockedReason = document.getElementById('cicd-blocked-reason');

      if (isBlocked) {
        bannerBlocked.style.display = 'block';
        bannerRessalva.style.display = 'none';
        blockedReason.innerText = `Motivo do Veto pelo Auditor: "${reason || 'Requisitos reprovados no Estágio 7.'}"`;
        cicdCard.style.opacity = '0.3';
        cicdCard.style.pointerEvents = 'none';
        cicdTabs.style.opacity = '0.3';
        cicdTabs.style.pointerEvents = 'none';
      } else {
        bannerBlocked.style.display = 'none';
        cicdCard.style.opacity = '1';
        cicdCard.style.pointerEvents = 'auto';
        cicdTabs.style.opacity = '1';
        cicdTabs.style.pointerEvents = 'auto';

        if (hasRessalva) {
          bannerRessalva.style.display = 'block';
        } else {
          bannerRessalva.style.display = 'none';
        }
      }
    }

    // 8. SIMULAÇÃO REATIVA DE RE-INFERÊNCIA MULTI-AGENTE (TERMINAL STREAMING)
    function triggerReInferenceCycle() {
      const ressalvaText = document.getElementById('hitl-ressalva-text').value.trim();
      const extraInput = document.getElementById('hitl-extra-input').value.trim();
      if (!ressalvaText) {
        alert("Por favor, informe a ressalva para iniciar o ciclo de re-inferência.");
        return;
      }

      hitlState.ressalvaText = ressalvaText;
      const termModal = document.getElementById('modal-re-inference');
      const termBody = document.getElementById('term-console-body');
      const btnClose = document.getElementById('btn-close-terminal');
      const progressText = document.getElementById('term-progress-text');
      const statusBadge = document.getElementById('term-status-badge');

      termBody.innerHTML = '';
      btnClose.style.display = 'none';
      statusBadge.innerText = 'EXECUTANDO...';
      statusBadge.style.color = '#38bdf8';
      termModal.classList.add('active');

      const logs = [
        { delay: 200, color: '#94a3b8', text: `[00.1s] [INPUT] Injetando ressalva do Auditor Humano: "${ressalvaText}"` },
        { delay: 600, color: '#38bdf8', text: `[00.7s] [STAGE 2 - GraphRAG] Extraindo conceito 'Handover_Pin_Security'. Adicionando nó ontológico 'RULE_PIN_EXPIRY_120S' ao grafo da Empresa X.` },
        { delay: 1100, color: '#f43f5e', text: `[01.3s] [STAGE 4 - STRIDE] Agente de Segurança re-analisando vetor T1 (Spoofing) e T6 (Elevation). Identificado risco de Brute-Force do PIN no balcão CE07.` },
        { delay: 1600, color: '#a855f7', text: `[01.9s] [STAGE 5 - ASVS] Agente de Requisitos derivando REQ-XFOOD-006: "Controle de Tempo de Vida (TTL) de Token e Proteção Contra Força Bruta".` },
        { delay: 2100, color: '#34d399', text: `[02.4s] [STAGE 6 - Tripartite] Conselho deliberando: ARCH valida Redis TTL (<5ms SLA); RE confirma ausência de fricção na UX; SEC aprova mitigação.` },
        { delay: 2600, color: '#fbbf24', text: `[02.9s] [STAGE 7 - HITL Engine] Assinatura forense recalculada. Recibo emitido com status 'APROVADO_COM_RESSALVAS_INCORPORADAS'.` },
        { delay: 3100, color: '#10b981', text: `[03.4s] [DOUBLE LOOP] Regra registrada com sucesso no Grafo Corporativo para futuros projetos de delivery!` }
      ];

      logs.forEach(item => {
        setTimeout(() => {
          const div = document.createElement('div');
          div.className = 'term-line';
          div.style.color = item.color;
          div.innerText = item.text;
          termBody.appendChild(div);
          termBody.scrollTop = termBody.scrollHeight;
        }, item.delay);
      });

      setTimeout(async () => {
        statusBadge.innerText = 'CONCLUÍDO (100%)';
        statusBadge.style.color = '#34d399';
        progressText.innerText = 'Re-inferência multi-agente finalizada com sucesso!';
        btnClose.style.display = 'inline-block';

        // Aplicar alterações nos dados em tempo de execução
        applyDynamicRessalvaData(ressalvaText);
      }, 3500);
    }

    function applyDynamicRessalvaData(ressalva) {
      hitlState.hasRessalvaInjected = true;

      // Injetar REQ-XFOOD-006 se ainda não existir
      const exists = BUNDLE.reqs.requirements.some(r => r.id === 'REQ-XFOOD-006');
      if (!exists) {
        const newReq = {
          id: "REQ-XFOOD-006",
          title: "Controle de Tempo de Vida (TTL) de Token e Proteção Contra Força Bruta no Balcão",
          user_story_invest: "Como arquiteto de segurança e lojista parceiro, quero que o PIN de coleta do pedido expire em 120 segundos e sofra bloqueio temporário após 3 tentativas inválidas de inserção pelo motoboy, a fim de impedir ataques de força bruta e retirada indevida de refeições (CE07 / RN09).",
          normative_specification: "O subsistema de verificação de pedidos DEVE (SHALL) aplicar expiração estrita de 120 segundos (TTL) ao PIN de coleta via Redis com expiração atômica. O endpoint /api/v1/orders/handover/verify DEVE bloquear o motoboy por 10 minutos após 3 tentativas incorretas consecutivas (Rate Limit com resposta HTTP 429), alertando o lojista parceiro.",
          asvs_level: "Nível 2 (V3.3.4 & V2.2.1)",
          mitigates_threat: "T6: Retirada Fraudulenta por Falso Motoboy (Elevation of Privilege)",
          sprint_priority: "MVP",
          story_points: 3,
          compliance_mapping: {
            asvs_level: "Nível 2 (V3.3.4 & V2.2.1)",
            owasp_category: "A07:2021 - Identification and Authentication Failures",
            iso_27001_control: "A.9.4.2 - Secure log-on procedures",
            lgpd_article: "Art. 46 (Segurança e Sigilo de Dados Operacionais)"
          },
          technical_implementation_steps: [
            "1. Implementar chave transitória no Redis com chave 'order:pin:{order_id}' e comando SETEX com TTL de 120 segundos.",
            "2. Configurar rate limiter com algoritmo Token Bucket limitando a 3 chamadas por IP/dispositivo por minuto.",
            "3. Responder HTTP 429 Too Many Requests com header Retry-After em caso de violação de rate limit.",
            "4. Emitir evento Kafka 'security.alert.handover_bruteforce' para notificação em tempo real ao lojista."
          ],
          bdd_gherkin: "Cenário: Tentativa de força bruta no PIN de coleta no balcão\\n  Dado que o motoboy insere o PIN '1234' incorretamente por 3 vezes consecutivas\\n  Quando a 4ª tentativa for submetida ao endpoint /api/v1/orders/handover/verify\\n  Então a API deve responder HTTP 429 Too Many Requests\\n  E o PIN de coleta atual deve ser revogado, alertando o lojista via Webhook.",
          ci_cd_verification: "Scan DAST aprovado no OWASP ZAP + Teste BDD de Rate Limiting automatizado com sucesso no Cypress/Cucumber."
        };

        BUNDLE.reqs.requirements.push(newReq);

        // Atualizar lista no modo cards e no preview A4
        renderReqs();
        appendReqToDocPreview(newReq);

        // Atualizar Jira com a nova issue
        updateJiraWithNewReq(newReq);
      }

      executeHitlAction('APROVADO_COM_RESSALVAS');
    }

    function appendReqToDocPreview(r) {
      const container = document.getElementById('fichas-tecnicas-container');
      if (!container) return;

      const div = document.createElement('div');
      div.className = 'ficha-doc-item';
      div.id = 'ficha-doc-' + r.id;
      div.style = "background:#f0fdf4; border:1px solid #bbf7d0; border-left:4px solid #16a34a; border-radius:6px; padding:14px; margin-bottom:16px; color:#1e293b; page-break-inside:avoid; animation:fadeIn 0.4s;";
      div.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <div>
            <span style="background:#16a34a; color:#fff; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px; margin-right:6px;">${r.id}</span>
            <strong style="font-size:13.5px; color:#0f172a;">${r.title}</strong>
          </div>
          <div>
            <span style="background:#fef3c7; color:#b45309; font-size:10px; font-weight:700; padding:2px 6px; border-radius:3px;">INJETADO VIA RESSALVA HITL</span>
            <span style="background:#dbeafe; color:#1e40af; font-size:10px; font-weight:700; padding:2px 6px; border-radius:3px; margin-left:4px;">MVP</span>
          </div>
        </div>
        
        <div style="background:#f8fafc; padding:6px 10px; border-radius:4px; font-size:10px; color:#475569; margin:6px 0 10px 0; display:flex; flex-wrap:wrap; gap:8px;">
          <span><strong>ASVS:</strong> ${r.compliance_mapping.asvs_level}</span>
          <span>•</span>
          <span><strong>OWASP:</strong> A07:2021</span>
          <span>•</span>
          <span><strong>ISO 27001:</strong> ${r.compliance_mapping.iso_27001_control}</span>
          <span>•</span>
          <span><strong>LGPD:</strong> ${r.compliance_mapping.lgpd_article}</span>
        </div>

        <div style="font-size:11px; margin-bottom:6px; color:#334155;">
          <strong>História de Usuário Ágil (INVEST):</strong> <em>"${r.user_story_invest}"</em>
        </div>

        <div style="font-size:11.5px; margin-bottom:8px; color:#0f172a; line-height:1.5;">
          <strong>Especificação Normativa (SHALL / MUST):</strong> ${r.normative_specification}
        </div>

        <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:10px; margin-bottom:10px;">
          <div style="font-size:11px; font-weight:800; color:#16a34a; margin-bottom:4px; text-transform:uppercase;">
            🛠️ Passos Práticos de Implementação para a Fábrica de Software:
          </div>
          <ul style="margin:0; padding-left:18px; font-size:11px; color:#334155; line-height:1.5;">
            ${r.technical_implementation_steps.map(s => `<li style='margin-bottom:3px;'>${s}</li>`).join('')}
          </ul>
        </div>

        <div style="font-size:10.5px; font-weight:700; color:#64748b; margin-bottom:4px;">Cenário de Teste de Aceitação Automatizado (Cucumber BDD / Gherkin):</div>
        <div style="background:#0f172a; color:#e2e8f0; padding:10px 12px; border-radius:6px; font-family:'SFMono-Regular', Consolas, monospace; font-size:10px; line-height:1.5; white-space:pre-wrap;">
${r.bdd_gherkin}
        </div>

        <div style="font-size:10.5px; color:#059669; font-weight:600; margin-top:6px;">
          ✓ Definition of Done (DoD na Esteira CI/CD): ${r.ci_cd_verification}
        </div>
      `;
      container.appendChild(div);
    }

    function updateJiraWithNewReq(r) {
      try {
        let jiraObj = JSON.parse(BUNDLE.raw_files['jira_epics_security_xfood.json']);
        if (jiraObj && jiraObj.issues) {
          jiraObj.issues.push({
            project: "XFOOD",
            issuetype: "Security Story",
            summary: `[${r.id}] ${r.title}`,
            description: r.user_story_invest + "\\n\\nDoD: " + r.ci_cd_verification,
            priority: "High",
            labels: ["security", "hitl-ressalva", "asvs-l2", "rate-limiting"],
            story_points: 3
          });
          BUNDLE.raw_files['jira_epics_security_xfood.json'] = JSON.stringify(jiraObj, null, 2);
          if (currentCiTab === 'jira') switchCiTab('jira');
        }
      } catch (e) {
        console.error("Erro ao atualizar Jira:", e);
      }
    }

    function finishReInferenceModal() {
      document.getElementById('modal-re-inference').classList.remove('active');
      switchStage(7);
    }

    function resetHitlState() {
      if (confirm("Deseja restaurar a homologação para o estado padrão do case?")) {
        hitlState = {
          decision: "APROVADO_SEM_RESSALVAS",
          auditor: "Francis Martins",
          role: "Lead Security Architect & Business Requirements Specialist",
          credentials: "MSc Software Engineering (UnB) / ISO 27001 Lead Implementer",
          hash: "16249b2ed84d164ee0d702ded831e1a058b73184ab38f5ac0db02d2524e5f68c",
          timestamp: "2026-09-22T12:52:13Z",
          ressalvaText: "",
          vetoReason: "",
          hasRessalvaInjected: false
        };
        document.getElementById('hitl-auditor-name').value = hitlState.auditor;
        document.getElementById('hitl-auditor-role').value = hitlState.role;
        document.getElementById('hitl-auditor-creds').value = hitlState.credentials;
        updateHitlUI();
        alert("Estado de homologação padrão restaurado.");
      }
    }

    function copyHash() {
      const h = document.getElementById('cert-hash-val').innerText;
      navigator.clipboard.writeText(h).then(() => {
        alert("Hash SHA-256 forense copiado com sucesso!");
      }).catch(() => {
        alert("Copie manualmente: " + h);
      });
    }

    function downloadHitlReceipt() {
      const receiptData = {
        project: "XFood_Delivery_Y",
        case_reference: "Case Anne Linkedin (Bizagi Automate)",
        lifecycle_phase: "UPSTREAM_REQUIREMENTS_" + hitlState.decision,
        gate_decision: hitlState.decision,
        auditor: {
          name: hitlState.auditor,
          role: hitlState.role,
          credentials: hitlState.credentials
        },
        cryptographic_verification: {
          signature_id: "SEC-XFOOD-" + hitlState.hash.substring(0, 12).toUpperCase(),
          requirements_sha256: hitlState.hash,
          timestamp_utc: hitlState.timestamp,
          algorithm: "SHA-256 with Internal Security Keyring (W3C Web Crypto)",
          ressalvas_applied: hitlState.hasRessalvaInjected ? hitlState.ressalvaText : null,
          veto_reason: hitlState.decision === 'REPROVADO_BLOQUEADO' ? hitlState.vetoReason : null
        },
        compliance_matrix: {
          OWASP_ASVS_4_0_3: "100% de Cobertura nos Requisitos Derivados",
          STRIDE_METHODOLOGY: "6 Ameaças Mitigadas em Nível de Arquitetura",
          LGPD_BRASIL: "Conforme (Art. 46 - Mascaramento de Dados de Clientes)",
          PCI_DSS_4_0: "Conforme (Tokenização de Cartões no Gateway)"
        },
        double_loop_feedback: {
          status: hitlState.hasRessalvaInjected ? "ONTOLOGY_EXPANDED_WITH_RESSALVAS" : "ONTOLOGY_UPDATED",
          knowledge_graph_node_added: hitlState.hasRessalvaInjected ? "RULE_XFOOD_PIN_TTL_120S_RATE_LIMIT" : "RULE_XFOOD_DELIVERY_HANDOVER_PIN",
          learning_impact: hitlState.hasRessalvaInjected ? "Regra de ressalva incorporada ao grafo para prevenção sistêmica de brute-force em balcão." : "Arquétipo de Food Delivery registrado no Grafo Corporativo para reutilização em futuros projetos da Empresa X."
        }
      };

      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(receiptData, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", "07_hitl_compliance_receipt.json");
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
    }

    // 9. CI/CD TABS (ESTÁGIO 8)
    let currentCiTab = 'jira';
    function switchCiTab(tab) {
      try {
        currentCiTab = tab;
        const tj = document.getElementById('tab-jira');
        const tg = document.getElementById('tab-gitlab');
        const tc = document.getElementById('tab-cucumber');
        if (tj) tj.classList.remove('active');
        if (tg) tg.classList.remove('active');
        if (tc) tc.classList.remove('active');

        const codeView = document.getElementById('ci-code-view');
        const titleView = document.getElementById('ci-card-title');

        if (tab === 'jira') {
          if (tj) tj.classList.add('active');
          if (titleView) titleView.innerText = "Jira REST API Issues Payload (jira_epics_security_xfood.json)";
          if (codeView) codeView.innerText = BUNDLE.raw_files['jira_epics_security_xfood.json'];
        } else if (tab === 'gitlab') {
          if (tg) tg.classList.add('active');
          if (titleView) titleView.innerText = "GitLab CI Quality Gate Policy (gitlab_security_policy_xfood.yml)";
          if (codeView) codeView.innerText = BUNDLE.raw_files['gitlab_security_policy_xfood.yml'];
        } else if (tab === 'cucumber') {
          if (tc) tc.classList.add('active');
          if (titleView) titleView.innerText = "Cucumber BDD Acceptance Tests (cucumber_xfood_security_acceptance.feature)";
          if (codeView) codeView.innerText = BUNDLE.raw_files['cucumber_xfood_security_acceptance.feature'];
        }
      } catch (err) {
        console.error("Erro em switchCiTab:", err);
      }
    }

    function copyCurrentCode() {
      const code = document.getElementById('ci-code-view').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert("Código copiado para a área de transferência com sucesso!");
      }).catch(() => {
        alert("Pressione Ctrl+C para copiar.");
      });
    }

    
    // ALTERNÂNCIA DE VISÕES NO ESTÁGIO 2 (GRAFO VISUAL vs CARDS)
    
    function downloadOntologySvg() {
      const svgEl = document.getElementById('ontology-graph-svg');
      if (!svgEl) {
        alert("Diagrama SVG não encontrado.");
        return;
      }
      const svgData = new XMLSerializer().serializeToString(svgEl);
      const blob = new Blob([svgData], { type: "image/svg+xml;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "02_graphrag_ontology_graph.svg";
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    }

    function switchOntologyView(mode) {
      const graphView = document.getElementById('ontology-graph-visual-view');
      const cardsView = document.getElementById('ontology-cards-view');
      const btnGraph = document.getElementById('btn-view-ontology-graph');
      const btnCards = document.getElementById('btn-view-ontology-cards');

      if (mode === 'cards') {
        graphView.style.display = 'none';
        cardsView.style.display = 'block';
        btnGraph.classList.remove('active');
        btnCards.classList.add('active');
      } else {
        graphView.style.display = 'block';
        cardsView.style.display = 'none';
        btnGraph.classList.add('active');
        btnCards.classList.remove('active');
      }
    }

    // BASE DE DADOS DOS NÓS ONTOLÓGICOS PARA O INSPETOR
    const ONTOLOGY_DETAILS = {
      "APP_CLIENTE": {
        title: "📱 APP_CLIENTE (Aplicativo Mobile do Consumidor)",
        type: "TIPO: CLIENT_SURFACE · DOMÍNIO E-COMMERCE",
        badge: "CRITICIDADE ALTA",
        badgeClass: "tag tag-blue",
        desc: "Superfície de entrada do consumidor final. Responsável pela autenticação, geolocalização do endereço de entrega, montagem do carrinho de compras e autorização transacional de pagamentos Pix/Cartão.",
        rules: "• <strong>RN01:</strong> Exibição georreferenciada de restaurantes em raio operacional.<br>• <strong>RN02:</strong> Sacola de restaurante único (trava mandatória).<br>• <strong>RN03:</strong> Validação de transação e estorno de pedido.",
        relations: "• ➔ <strong>GATEWAY_PAGAMENTOS:</strong> LIQUIDA_TRANSACAO_VIA (REST / TLS 1.3)<br>• ➔ <strong>GOOGLE_MAPS_API:</strong> VALIDA_ENDERECO_GEORREFERENCIADO (HTTPS)<br>• ➔ <strong>REGRA_NEGOCIO_RN02:</strong> DEVE_RESPEITAR_TRAVA_SACOLA (Validação Backend)"
      },
      "PAINEL_KDS_RESTAURANTE": {
        title: "🍳 PAINEL_KDS_RESTAURANTE (Kitchen Display System do Lojista)",
        type: "TIPO: PARTNER_SURFACE · OPERAÇÃO DE COZINHA",
        badge: "CRITICIDADE ALTA",
        badgeClass: "tag tag-blue",
        desc: "Interface do lojista parceiro dentro da cozinha. Recebe notificações de novos pedidos em tempo real via WebSocket, gerencia o SLA de preparo na cozinha e confirma a entrega do pacote no balcão.",
        rules: "• <strong>RN04:</strong> Notificação e aceite de pedidos.<br>• <strong>RN08:</strong> Cancelamento unilateral por sobrecarga.<br>• <strong>RN09:</strong> Timer mandatório de SLA de 5 minutos.",
        relations: "• ➔ <strong>WEBSOCKET_BROKER:</strong> RECEBE_EVENTO_NOVO_PEDIDO (WSS / Redis PubSub)<br>• ➔ <strong>REGRA_NEGOCIO_RN09:</strong> CONTROLADO_POR_TIMER_SLA_5MIN<br>• ➔ <strong>CODIGO_RETIRADA_4DIGITOS:</strong> AUTENTICA_COLETA_HANDOVER (Balcão CE07)"
      },
      "CODIGO_RETIRADA_4DIGITOS": {
        title: "🔐 CODIGO_RETIRADA_4DIGITOS (Mecanismo Central Anti-Fraude Handover)",
        type: "TIPO: SECURITY_MECHANISM · CRIPTOGRAFIA & AUTENTICAÇÃO",
        badge: "CRÍTICO / FORENSE",
        badgeClass: "tag tag-red",
        desc: "Token transitório de 4 dígitos gerado no momento do pagamento. O motoboy deve informá-lo ao atendente da cozinha para confirmar que é o portador legítimo da entrega, prevenindo roubo de pacotes no balcão (CE07).",
        rules: "• <strong>CE07:</strong> Coleta Segura no Balcão.<br>• <strong>RN09:</strong> Liberação de prato pronto dentro do SLA.<br>• <strong>ASVS V3.3.4:</strong> Expiração de tokens de sessão e rate limiting.",
        relations: "• ➔ <strong>PAINEL_KDS_RESTAURANTE:</strong> AUTENTICA_COLETA_HANDOVER<br>• ➔ <strong>WEBSOCKET_BROKER:</strong> VALIDA_TTL_REDIS_120S<br>• ➔ <strong>APP_ENTREGADOR:</strong> FORNECE_PIN_NO_BALCAO"
      },
      "APP_ENTREGADOR": {
        title: "🛵 APP_ENTREGADOR (Aplicativo Mobile dos Motoboys)",
        type: "TIPO: LOGISTICS_SURFACE · OPERAÇÃO DE CAMPO",
        badge: "CRITICIDADE ALTA",
        badgeClass: "tag tag-emerald",
        desc: "Aplicativo da frota logística. Realiza rastreamento contínuo por GPS, recebe ofertas de corrida, valida a coleta no restaurante e obtém o código de confirmação final do cliente no endereço de entrega.",
        rules: "• <strong>RN06:</strong> Despacho logístico de entregadores.<br>• <strong>RN07:</strong> Geofencing e cálculo dinâmico de rota.<br>• <strong>RN11:</strong> Confirmação de entrega e liberação de repasse.",
        relations: "• ➔ <strong>CODIGO_RETIRADA_4DIGITOS:</strong> FORNECE_PIN_NO_BALCAO (Handover CE07)<br>• ➔ <strong>LGPD_COMPLIANCE:</strong> DEVE_MASCARAR_PII_DO_CLIENTE (Art. 46 LGPD)"
      },
      "GATEWAY_PAGAMENTOS": {
        title: "💳 GATEWAY_PAGAMENTOS (Enclave Fintech de Liquidação Pix/Cartão)",
        type: "TIPO: EXTERNAL_FINTECH_SERVICE · COMPLIANCE FINANCEIRO",
        badge: "PCI-DSS v4.0 / BACEN",
        badgeClass: "tag tag-orange",
        desc: "Gateway transacional externo de alta segurança. Responsável por tokenizar cartões de crédito sem persistência na aplicação e orquestrar QR Codes Pix dinâmicos com confirmação criptográfica via Webhook assinado.",
        rules: "• <strong>RN03:</strong> Liquidação Pix com chave dinâmica e tempo de expiração.<br>• <strong>RN10:</strong> Estorno automático de transação em caso de cancelamento.",
        relations: "• ➔ <strong>APP_CLIENTE:</strong> LIQUIDA_TRANSACAO_VIA (Webhook HMAC-SHA256)"
      },
      "GOOGLE_MAPS_API": {
        title: "🗺️ GOOGLE_MAPS_API (Serviço de Georreferenciamento e Rotas)",
        type: "TIPO: EXTERNAL_GEO_SERVICE · GEOLOCALIZAÇÃO",
        badge: "SLA 99.9%",
        badgeClass: "tag tag-blue",
        desc: "Serviço de mapas e cálculo vetorial. Valida o endereço de entrega do cliente, define polígonos de atendimento dos restaurantes parceiros e estima tempos de tráfego para os entregadores.",
        rules: "• <strong>RN01:</strong> Filtro de raio operacional das cozinhas.<br>• <strong>RN07:</strong> Cálculo de taxa de entrega baseada em quilometragem real.",
        relations: "• ➔ <strong>APP_CLIENTE:</strong> VALIDA_ENDERECO_GEORREFERENCIADO"
      },
      "REGRA_NEGOCIO_RN02": {
        title: "📜 REGRA_NEGOCIO_RN02 (Sacola de Restaurante Único)",
        type: "TIPO: BUSINESS_RULE · RESTRIÇÃO DE NEGÓCIO",
        badge: "REQUISITO REQ-002",
        badgeClass: "tag tag-purple",
        desc: "Regra mandatória que veta a inclusão de itens de lojistas distintos na mesma transação. Evita falhas logísticas de coleta cruzada e simplifica o rateio de comissões da plataforma Delivery Y.",
        rules: "• <strong>RN02:</strong> Trava de sacola única.<br>• <strong>Mitigação T2:</strong> Validação server-side contra manipulação de itens de terceiros no carrinho.",
        relations: "• ➔ <strong>APP_CLIENTE:</strong> DEVE_RESPEITAR_TRAVA_SACOLA"
      },
      "WEBSOCKET_BROKER": {
        title: "⚡ WEBSOCKET_BROKER (Hub Realtime Pub/Sub Redis)",
        type: "TIPO: REALTIME_CORE · INFRAESTRUTURA DE MENSAGERIA",
        badge: "WSS / REDIS",
        badgeClass: "tag tag-purple",
        desc: "Servidor de sockets distribuído em alta performance. Mantém túneis bidirecionais criptografados para notificar a cozinha em <100ms quando um pedido é pago e propagar a geolocalização do motoboy no mapa.",
        rules: "• <strong>RN04:</strong> Propagação de novos pedidos.<br>• <strong>RN09:</strong> Heartbeat e sincronização do timer de 5 minutos da cozinha.",
        relations: "• ➔ <strong>PAINEL_KDS_RESTAURANTE:</strong> RECEBE_EVENTO_NOVO_PEDIDO"
      },
      "REGRA_NEGOCIO_RN09": {
        title: "⏱️ REGRA_NEGOCIO_RN09 (Timer de SLA de 5 Minutos na Cozinha)",
        type: "TIPO: BUSINESS_RULE · TEMPORIZADOR DE CONTRATO",
        badge: "SLA DE 300s",
        badgeClass: "tag tag-purple",
        desc: "Contrato de nível de serviço com o cliente: o restaurante tem 5 minutos para aceitar e despachar o pedido para a chapa. Se estourar, o estorno financeiro integral é acionado automaticamente.",
        rules: "• <strong>RN09:</strong> SLA de 5 minutos da cozinha.<br>• <strong>Deliberação Tripartite:</strong> Arbitragem de UX vs Segurança para não degradar a conversão.",
        relations: "• ➔ <strong>PAINEL_KDS_RESTAURANTE:</strong> CONTROLADO_POR_TIMER_SLA_5MIN"
      },
      "LGPD_COMPLIANCE": {
        title: "⚖️ LGPD_COMPLIANCE (Conformidade com a Lei Geral de Proteção de Dados)",
        type: "TIPO: LEGAL_REGULATION · GOVERNANÇA JURÍDICA",
        badge: "LEI 13.709/2018",
        badgeClass: "tag tag-purple",
        desc: "Diretrizes de privacidade aplicadas sobre dados de identificação do consumidor. Exige mascaramento no display do motoboy (exibir apenas primeiro nome e número do pedido) e criptografia AES-256 em repouso.",
        rules: "• <strong>Artigo 46:</strong> Medidas de segurança técnicas e administrativas.<br>• <strong>Artigo 52:</strong> Governança de dados pessoais e trilha de auditoria.",
        relations: "• ➔ <strong>APP_ENTREGADOR:</strong> DEVE_MASCARAR_PII_DO_CLIENTE"
      }
    };

    function setupOntologyNodeEvents() {
      const nodes = document.querySelectorAll('.graph-node');
      nodes.forEach(n => {
        const nodeId = n.id.replace('node-', '');
        n.style.cursor = 'pointer';
        n.addEventListener('click', () => {
          inspectOntologyNode(nodeId);
        });
      });
    }

    function inspectOntologyNode(nodeId) {
      const data = ONTOLOGY_DETAILS[nodeId];
      if (!data) return;

      document.getElementById('inspect-node-title').innerHTML = data.title;
      document.getElementById('inspect-node-type').innerText = data.type;
      
      const badge = document.getElementById('inspect-node-badge');
      badge.className = data.badgeClass;
      badge.innerText = data.badge;

      document.getElementById('inspect-node-desc').innerHTML = data.desc;
      document.getElementById('inspect-node-rules').innerHTML = data.rules;
      document.getElementById('inspect-node-relations').innerHTML = data.relations;

      const inspector = document.getElementById('ontology-node-inspector');
      inspector.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      inspector.style.animation = 'none';
      setTimeout(() => inspector.style.animation = 'fadeIn 0.3s', 10);
    }

    function filterOntologyNodes(cat) {
      document.querySelectorAll('#ontology-filter-pills .btn').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById('pill-' + cat.toLowerCase()) || document.getElementById('pill-all');
      if (activeBtn) activeBtn.classList.add('active');

      const allNodes = document.querySelectorAll('.graph-node');
      const allEdges = document.getElementById('graph-edges');

      allNodes.forEach(n => {
        n.style.transition = 'opacity 0.2s, transform 0.2s';
        const id = n.id.replace('node-', '');

        if (cat === 'ALL') {
          n.style.opacity = '1';
          n.style.pointerEvents = 'auto';
        } else if (cat === 'SURFACES') {
          const match = ['APP_CLIENTE', 'PAINEL_KDS_RESTAURANTE', 'APP_ENTREGADOR'].includes(id);
          n.style.opacity = match ? '1' : '0.2';
        } else if (cat === 'SERVICES') {
          const match = ['GATEWAY_PAGAMENTOS', 'GOOGLE_MAPS_API', 'WEBSOCKET_BROKER'].includes(id);
          n.style.opacity = match ? '1' : '0.2';
        } else if (cat === 'RULES') {
          const match = ['REGRA_NEGOCIO_RN02', 'REGRA_NEGOCIO_RN09'].includes(id);
          n.style.opacity = match ? '1' : '0.2';
        } else if (cat === 'SECURITY') {
          const match = ['CODIGO_RETIRADA_4DIGITOS', 'LGPD_COMPLIANCE'].includes(id);
          n.style.opacity = match ? '1' : '0.2';
        }
      });
    }

    // INICIALIZAÇÃO SEGURA
    window.addEventListener('DOMContentLoaded', () => {
      console.log("Inicializando Dashboard PRISMA-IA com Governança HITL...");
      renderGraph();
      renderFeeds();
      renderThreats('ALL');
      renderReqs();
      renderDeliberation();
      setupOntologyNodeEvents();
      setupThreatDragonPins();
      updateHitlUI();
      switchCiTab('jira');
      switchStage(1);
      console.log("Dashboard pronto com sucesso!");
    });
  
    // =========================================================================
    // FRONT-END: INGESTÃO E EXECUÇÃO DO PIPELINE (INTEGRAÇÃO INPUT & OUTPUT_V2)
    // =========================================================================
    function loadCaseFolder(path) {
      const dirInput = document.getElementById('source-dir-input');
      const targetPath = path || ['C:', 'Users', 'franc', 'Downloads', 'lixo', 'Bizagi Automate', 'Case Anne Linkedin', 'input'].join(String.fromCharCode(92));
      dirInput.value = targetPath;
      folderLoaded = true;

      // 1. Atualizar Badge de Status
      const badge = document.getElementById('inputs-status-badge');
      badge.style.background = '#065f46';
      badge.style.color = '#34d399';
      document.getElementById('inputs-status-dot').style.background = '#34d399';
      document.getElementById('inputs-status-text').textContent = '5 Insumos Conectados & Indexados (Pasta input)';

      // 2. Popular Tabela de Insumos com os arquivos da pasta input
      const tbody = document.getElementById('inputs-table-body');
      tbody.innerHTML = `
        <tr>
          <td>
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:20px;">📄</span>
              <div>
                <div style="font-weight:700; color:#f8fafc; font-size:12.5px;">Especificacao_Funcional_Delivery_Y_Exercicio_1.docx</div>
                <div style="font-size:11px; color:#64748b;">Word DOCX · 53.3 KB · Pasta input · Regras de Negócio</div>
              </div>
            </div>
          </td>
          <td><span class="badge" style="background:#1e293b; color:#38bdf8;">Visão de Negócio & Funcional</span></td>
          <td style="font-size:12px; color:#cbd5e1;">
            <strong>11 Regras de Negócio (RN01 a RN11):</strong> Trava de Sacola Única por restaurante, Timer SLA 5 min de cozinha, Handover por PIN 4 dígitos no balcão e Split de pagamentos.
          </td>
          <td style="text-align:center;"><span class="badge badge-success">✓ 100% Mapeado</span></td>
        </tr>
        <tr>
          <td>
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:20px;">📐</span>
              <div>
                <div style="font-weight:700; color:#f8fafc; font-size:12.5px;">Jornada_Cliente_XFood_Exercicio_2.bpmn</div>
                <div style="font-size:11px; color:#64748b;">XML BPMN 2.0 + PNG Bizagi · 37.5 KB · Piscinas & Lanes</div>
              </div>
            </div>
          </td>
          <td><span class="badge" style="background:#1e293b; color:#a855f7;">Processo de Negócio BPMN</span></td>
          <td style="font-size:12px; color:#cbd5e1;">
            <strong>Fluxo Completo de Jornada:</strong> 4 Piscinas/Lanes (Cliente, Cozinha/KDS, Entregador, Gateway), eventos de início/fim, gateways exclusivos de rejeição e timers de SLA.
          </td>
          <td style="text-align:center;"><span class="badge badge-success">✓ 100% Mapeado</span></td>
        </tr>
        <tr>
          <td>
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:20px;">💡</span>
              <div>
                <div style="font-weight:700; color:#f8fafc; font-size:12.5px;">Especificacao_Requisitos_Perguntas_PO_Exercicio_3.docx</div>
                <div style="font-size:11px; color:#64748b;">Word DOCX · 36.1 KB · Entrevistas PO</div>
              </div>
            </div>
          </td>
          <td><span class="badge" style="background:#1e293b; color:#f59e0b;">Descoberta & Perguntas PO</span></td>
          <td style="font-size:12px; color:#cbd5e1;">
            <strong>Esclarecimentos de Domínio:</strong> Respostas do Product Owner sobre limite de raio de entrega (7km), idempotência de estorno Pix e política de descarte de pedidos frios.
          </td>
          <td style="text-align:center;"><span class="badge badge-success">✓ 100% Mapeado</span></td>
        </tr>
        <tr>
          <td>
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:20px;">🗺️</span>
              <div>
                <div style="font-weight:700; color:#f8fafc; font-size:12.5px;">Boards do Miro / Arquitetura Upstream (Ideação)</div>
                <div style="font-size:11px; color:#64748b;">Miro Board Export / Wireframes · Mindmaps & Telas</div>
              </div>
            </div>
          </td>
          <td><span class="badge" style="background:#1e293b; color:#ec4899;">Ideação Visual & Miro</span></td>
          <td style="font-size:12px; color:#cbd5e1;">
            <strong>Arquitetura Conceitual Multi-Sided:</strong> Wireframes das telas de checkout do consumidor, interface de balcão (KDS) e aplicativo mobile do entregador autônomo.
          </td>
          <td style="text-align:center;"><span class="badge badge-success">✓ 100% Mapeado</span></td>
        </tr>
        <tr>
          <td>
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:20px;">📝</span>
              <div>
                <div style="font-weight:700; color:#f8fafc; font-size:12.5px;">TESTE_ANALISTA NEGOCIOS.docx</div>
                <div style="font-size:11px; color:#64748b;">Word DOCX · 18.5 KB · Critérios de Aceite</div>
              </div>
            </div>
          </td>
          <td><span class="badge" style="background:#1e293b; color:#10b981;">Critérios de Aceite de Negócio</span></td>
          <td style="font-size:12px; color:#cbd5e1;">
            <strong>Matriz de Testes Upstream:</strong> Casos de validação de transição de status (Carrinho Aberto ➔ Pago ➔ Em Preparo ➔ Pronto no Balcão ➔ Entregue).
          </td>
          <td style="text-align:center;"><span class="badge badge-success">✓ 100% Mapeado</span></td>
        </tr>
      `;

      // 3. Atualizar Cards de Resumo
      const cTitle = document.getElementById('card-cenario-title');
      if (cTitle) {
        cTitle.textContent = 'CENÁRIO 1: UPSTREAM GREENFIELD';
        cTitle.style.color = '#38bdf8';
        document.getElementById('card-cenario-desc').textContent = 'O sistema está na fase de ideação. Ausência total de código-fonte prévio ou scanners estáticos (SARIF). O PRISMA-IA atua prevenindo dívida técnica no dia zero.';
      }

      const iTitle = document.getElementById('card-insumos-title');
      if (iTitle) {
        iTitle.textContent = '1 BPMN + 11 Regras de Negócio';
        iTitle.style.color = '#f8fafc';
        document.getElementById('card-insumos-desc').textContent = 'Ingestão da pasta input: Fluxos Bizagi BPMN + 11 Regras de Negócio da Plataforma Delivery Y.';
      }

      const aTitle = document.getElementById('card-arquetipo-title');
      if (aTitle) {
        aTitle.textContent = 'Multi-Tenant Food Delivery Marketplace';
        aTitle.style.color = '#34d399';
        document.getElementById('card-arquetipo-desc').textContent = 'Conexão tripartite: Clientes Finais, Restaurantes Parceiros e Entregadores Autônomos (Motoboys).';
      }

      // 4. Atualizar Tabela BPMN
      const bpmnTbody = document.getElementById('bpmn-entities-tbody');
      if (bpmnTbody) {
        bpmnTbody.innerHTML = `
          <tr><td><strong>Cliente Comprador</strong></td><td>Inicia o pedido, adiciona itens e paga</td><td>Adulteração de preços e IDOR no carrinho</td><td><code>RN01, RN02, RN03</code></td></tr>
          <tr><td><strong>Restaurante Parceiro</strong></td><td>Aceita pedido, inicia preparo e avisa balcão</td><td>Manipulação de SLA (5 min) e estorno indevido</td><td><code>RN04, RN08, RN09</code></td></tr>
          <tr><td><strong>Entregador (Motoboy)</strong></td><td>Coleta no balcão e entrega no destino final</td><td>Retirada fraudulenta por falso motoboy</td><td><code>RN06, RN07, RN11, CE07</code></td></tr>
          <tr><td><strong>Gateway de Pagamentos</strong></td><td>Validação transacional Pix e Cartão de Crédito</td><td>Falsificação de Webhooks de confirmação</td><td><code>RN03, RN10</code></td></tr>
        `;
      }

      // 5. Atualizar Engine Status
      const engStatus = document.getElementById('engine-status-text');
      if (engStatus) {
        engStatus.innerHTML = '<span style="color:#0ea5e9; font-weight:700;">● Insumos Conectados:</span> Pasta input validada. Pronto para disparar o pipeline e gravar os artefatos fisicamente em output_v2.';
      }

      // 6. Habilitar Botões de Execução
      const runBtn = document.getElementById('btn-run-pipeline');
      if (runBtn) {
        runBtn.disabled = false;
        runBtn.style.background = 'linear-gradient(135deg, #0284c7, #0ea5e9)';
        runBtn.style.color = '#fff';
        runBtn.style.cursor = 'pointer';
        runBtn.style.opacity = '1';
        runBtn.style.boxShadow = '0 4px 16px rgba(14,165,233,0.4)';
        document.getElementById('btn-run-icon').textContent = '🚀';
        document.getElementById('btn-run-label').textContent = 'Iniciar Ingestão & Executar Pipeline PRISMA-IA';
      }

      const runBtnTop = document.getElementById('btn-run-pipeline-top');
      if (runBtnTop) {
        runBtnTop.disabled = false;
        runBtnTop.style.background = 'linear-gradient(135deg, #0284c7, #0ea5e9)';
        runBtnTop.style.opacity = '1';
        runBtnTop.style.cursor = 'pointer';
      }

      const attachBtn = document.getElementById('btn-attach-comp');
      if (attachBtn) {
        attachBtn.disabled = false;
        attachBtn.style.opacity = '1';
      }

      showToast('✓ Pasta input conectada: 5 insumos brutos de ideação detectados e prontos!');
    }

    function loadSampleCaseFolder() {
      loadCaseFolder(['C:', 'Users', 'franc', 'Downloads', 'lixo', 'Bizagi Automate', 'Case Anne Linkedin', 'input'].join(String.fromCharCode(92)));
    }

    function triggerFolderSelect() {
      document.getElementById('source-folder-picker').click();
    }

    function onSourceFolderSelected(e) {
      const files = e.target.files;
      if (!files || files.length === 0) return;
      const firstPath = files[0].webkitRelativePath || "";
      const dirName = firstPath.split('/')[0] || "input";
      const simulatedPath = ['C:', 'Users', 'franc', 'Downloads', 'lixo', 'Bizagi Automate', 'Case Anne Linkedin', dirName].join(String.fromCharCode(92));
      loadCaseFolder(simulatedPath);
    }

    function onSourceDirChanged() {
      const val = document.getElementById('source-dir-input').value.trim();
      if (val) {
        loadCaseFolder(val);
      }
    }

    function reloadSourceInputs() {
      const val = document.getElementById('source-dir-input').value.trim();
      loadCaseFolder(val || ['C:', 'Users', 'franc', 'Downloads', 'lixo', 'Bizagi Automate', 'Case Anne Linkedin', 'input'].join(String.fromCharCode(92)));
    }

    function updatePipelineMode() {
      const mode = document.getElementById('pipeline-mode-select').value;
      if (mode === 'downstream') {
        showToast("⚠️ Modo Downstream/Código ativado: requer repositório Git e scanner SARIF.");
      } else {
        showToast("✓ Modo Upstream Greenfield ativado: inferência ontológica a partir de ideação.");
      }
    }

    function handleDragOver(e) {
      e.preventDefault();
      const dz = document.getElementById('upstream-dropzone');
      if (dz) {
        dz.style.borderColor = '#38bdf8';
        dz.style.background = '#0d1d33';
      }
    }

    function handleDragLeave(e) {
      e.preventDefault();
      const dz = document.getElementById('upstream-dropzone');
      if (dz) {
        dz.style.borderColor = '#334155';
        dz.style.background = '#090d16';
      }
    }

    function handleDrop(e) {
      e.preventDefault();
      handleDragLeave(e);
      const files = e.dataTransfer.files;
      if (files && files.length > 0) {
        addFilesToTable(files);
      }
    }

    function onFilesSelected(e) {
      const files = e.target.files;
      if (files && files.length > 0) {
        addFilesToTable(files);
      }
    }

    function addFilesToTable(files) {
      if (!folderLoaded) {
        loadSampleCaseFolder();
      }
      const tbody = document.getElementById('inputs-table-body');
      if (!tbody) return;
      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const tr = document.createElement('tr');
        const sizeKb = (file.size / 1024).toFixed(1);
        tr.innerHTML = `
          <td>
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:20px;">📎</span>
              <div>
                <div style="font-weight:700; color:#f8fafc; font-size:12.5px;">${file.name}</div>
                <div style="font-size:11px; color:#64748b;">${sizeKb} KB · Insumo Adicionado Manualmente</div>
              </div>
            </div>
          </td>
          <td><span class="badge" style="background:#1e293b; color:#38bdf8;">Insumo Complementar</span></td>
          <td style="font-size:12px; color:#cbd5e1;">Indexado para enriquecimento semântico no Grafo Ontológico e STRIDE.</td>
          <td style="text-align:center;"><span class="badge badge-success">✓ Ingerido</span></td>
        `;
        tbody.appendChild(tr);
      }
      showToast(`➕ ${files.length} novo(s) insumo(s) anexado(s) com sucesso ao pipeline!`);
    }

    async function triggerLocalBackendRun() {
      try {
        const res = await fetch('http://127.0.0.1:8765/run', { method: 'POST' });
        if (res.ok) {
          const data = await res.json();
          console.log('[BACKEND BRIDGE] Execucao fisica concluida:', data);
          return data;
        }
      } catch (err) {
        console.warn('[BACKEND BRIDGE] Bridge offline ou chamada via file://, usando fallback client-side:', err);
      }
      return null;
    }

    function startPipelineExecution() {
      if (!folderLoaded) {
        showToast("⚠️ Conecte a pasta com os insumos primeiro!");
        return;
      }
      const modal = document.getElementById('modal-pipeline-runner');
      const consoleBody = document.getElementById('pipe-console-body');
      const progressBar = document.getElementById('pipe-progress-bar');
      const progressPct = document.getElementById('pipe-progress-pct');
      const progressPhase = document.getElementById('pipe-progress-phase');
      const statusBadge = document.getElementById('pipe-status-badge');
      const closeBtn = document.getElementById('btn-close-pipeline');
      const footerText = document.getElementById('pipe-footer-text');

      consoleBody.innerHTML = '';
      modal.style.display = 'flex';
      statusBadge.textContent = 'EXECUTANDO...';
      statusBadge.style.background = '#0369a1';
      statusBadge.style.color = '#e0f2fe';
      closeBtn.style.display = 'none';
      footerText.textContent = 'Disparando motor de execucao PRISMA-IA para output_v2...';

      const dirPath = document.getElementById('source-dir-input').value || "input";
      const asvsVal = document.getElementById('asvs-level-select').value;

      // Dispara a geracao fisica real em output_v2 via local bridge HTTP
      triggerLocalBackendRun();

      const logs = [
        { delay: 100, pct: 10, phase: "Fase 1/8: Ingestao de Insumos da Pasta input", color: "#38bdf8", text: `[00.1s] [FRONT-END] Origem confirmada: "${dirPath}". Destino isolado: output_v2. Rigor: ${asvsVal}.` },
        { delay: 500, pct: 22, phase: "Fase 1/8: Parse de Arquivos de Ideacao", color: "#94a3b8", text: `[00.5s] [STAGE 1 - INGESTION] Lendo 5 insumos de input/: 1 BPMN XML, 3 DOCX de Visao/PO, 1 Board Miro...` },
        { delay: 1000, pct: 35, phase: "Fase 1/8: Resolucao de Cenario", color: "#34d399", text: `[01.0s] [STAGE 1 - INGESTION] 11 Regras de Negocio extraidas (RN01 a RN11). Ausencia de codigo: Cenario 1 Greenfield ativado.` },
        { delay: 1500, pct: 48, phase: "Fase 2/8: Grafo Ontologico (GraphRAG)", color: "#c084fc", text: `[01.5s] [STAGE 2 - GRAPHRAG] Construindo rede semantica de entidades (10 nos conceituais, 12 arestas). Gerando 02_graphrag_ontology_graph_v2.svg.` },
        { delay: 2100, pct: 60, phase: "Fase 3/8: Inteligencia de Ameacas & Feeds", color: "#f59e0b", text: `[02.1s] [STAGE 3 - THREAT INTEL] Conectando aos feeds NIST NVD, CISA KEV, MITRE e BACEN Pix. 4 vulnerabilidades correlacionadas.` },
        { delay: 2700, pct: 72, phase: "Fase 4/8: Modelagem de Ameacas STRIDE", color: "#f43f5e", text: `[02.7s] [STAGE 4 - STRIDE] Gerando OWASP Threat Dragon DFD v2 com 5 trust boundaries. 6 ameacas mapeadas (T1 a T6) e mitigadas.` },
        { delay: 3300, pct: 84, phase: "Fase 5/8: Requisitos de Seguranca ASVS", color: "#38bdf8", text: `[03.3s] [STAGE 5 - REQS] Sintetizando Especificacao Oficial de Requisitos de Seguranca v2 (DOCX A4) e 5 historias BDD Gherkin.` },
        { delay: 3900, pct: 93, phase: "Fase 6/8: Deliberacao Dialetica Tripartite", color: "#a855f7", text: `[03.9s] [STAGE 6 - TRIPARTITE] Debate socratico RE vs SEC vs ARCH concluido com 100% de consenso gerando ata tripartite v2.` },
        { delay: 4500, pct: 100, phase: "Fase 7/8 & 8/8: Homologacao HITL & CI/CD", color: "#10b981", text: `[04.5s] [STAGE 7 & 8 - HITL & CI/CD] Gravando 19 artefatos fisicamente na pasta output_v2! Gerando 00_manifest_rastreabilidade_v2.json.` },
        { delay: 4800, pct: 100, phase: "Pipeline Concluido!", color: "#34d399", text: `[04.8s] [PIPELINE SUCESSO] Execucao finalizada com carimbo de data, hora e versao v2.0! Todos os estagios desbloqueados.` }
      ];

      logs.forEach(item => {
        setTimeout(() => {
          const line = document.createElement('div');
          line.className = 'term-line';
          line.style.color = item.color;
          line.textContent = item.text;
          consoleBody.appendChild(line);
          consoleBody.scrollTop = consoleBody.scrollHeight;

          progressBar.style.width = item.pct + '%';
          progressPct.textContent = item.pct + '%';
          progressPhase.textContent = item.phase;

          if (item.pct === 100) {
            pipelineExecuted = true;
            statusBadge.textContent = '✓ CONCLUÍDO';
            statusBadge.style.background = '#065f46';
            statusBadge.style.color = '#34d399';
            closeBtn.style.display = 'inline-flex';
            footerText.textContent = 'Pipeline executado com sucesso! 19 artefatos gravados em output_v2 com data e hora.';
            showToast("🎉 Pipeline PRISMA-IA executado com sucesso! Artefatos gravados em output_v2.");
          }
        }, item.delay);
      });
    }

    function finishPipelineModal() {
      document.getElementById('modal-pipeline-runner').style.display = 'none';
      pipelineExecuted = true;
      switchStage(2);
      showToast("🚀 Navegando para o Estágio 2: Grafo Ontológico do Domínio!");
    }

  </script>
</body>
</html>
"""

target_case_root = os.path.join(BASE_DIR, "dashboard_interativo_case_xfood.html")

with open(target_case_root, "w", encoding="utf-8") as f:
    f.write(html_template)
print(f"[SUCESSO] Dashboard Front-End salvo em: {target_case_root}")

# -*- coding: utf-8 -*-
"""
Parser universal para relatórios SARIF 2.1.0 (Fortify, SonarQube, GitHub CodeQL)
"""
import json
from typing import Dict, List, Any

class SarifParser:
    @staticmethod
    def parse(file_path: str) -> Dict[str, Any]:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        findings = []
        runs = data.get("runs", [])
        tool_name = "Generic SAST"

        for run in runs:
            tool = run.get("tool", {}).get("driver", {})
            tool_name = tool.get("name", tool_name)
            rules_dict = {r["id"]: r.get("name", "") for r in tool.get("rules", [])}

            for result in run.get("results", []):
                rule_id = result.get("ruleId", "UNKNOWN-RULE")
                level = result.get("level", "warning")
                msg = result.get("message", {}).get("text", "")
                
                loc = "desconhecido"
                locs = result.get("locations", [])
                if locs:
                    phys = locs[0].get("physicalLocation", {})
                    uri = phys.get("artifactLocation", {}).get("uri", "")
                    line = phys.get("region", {}).get("startLine", 0)
                    loc = f"{uri}:{line}"

                findings.append({
                    "rule_id": rule_id,
                    "rule_name": rules_dict.get(rule_id, rule_id),
                    "severity": level,
                    "message": msg,
                    "location": loc
                })

        return {
            "tool": tool_name,
            "total_findings": len(findings),
            "findings": findings
        }

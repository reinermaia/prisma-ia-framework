# -*- coding: utf-8 -*-
"""
Parser universal de CycloneDX SBOM (Dependency-Track / OWASP Dependency-Check)
"""
import json
from typing import Dict, Any

class SbomParser:
    @staticmethod
    def parse(file_path: str) -> Dict[str, Any]:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        components = []
        vulnerabilities = []

        for comp in data.get("components", []):
            purl = comp.get("purl", comp.get("name", ""))
            vulns = comp.get("vulnerabilities", [])
            for v in vulns:
                vulnerabilities.append({
                    "component": purl,
                    "cve": v.get("id", "N/A"),
                    "severity": v.get("ratings", [{}])[0].get("severity", "medium"),
                    "desc": v.get("description", "")
                })
            components.append({
                "name": comp.get("name"),
                "version": comp.get("version"),
                "purl": purl,
                "vuln_count": len(vulns)
            })

        return {
            "format": data.get("bomFormat", "CycloneDX"),
            "spec_version": data.get("specVersion", "1.5"),
            "total_components": len(components),
            "total_vulnerabilities": len(vulnerabilities),
            "vulnerabilities": vulnerabilities,
            "components": components
        }

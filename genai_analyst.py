import os
from pathlib import Path
import requests
log = Path("test.log").read_text() if Path("test.log").exists() else "Log indisponível"
codigo = Path("app.py").read_text()
key = os.getenv("GEMINI_API_KEY")
if key:
    response = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/" + os.getenv("GEMINI_MODEL", "gemini-2.5-flash") + ":generateContent",
        headers={"x-goog-api-key": key},
        json={"contents": [{"parts": [{"text": "Explique o erro, a causa e a correção sugerida. Não altere código.\n" + codigo + "\n" + log}]}]},
        timeout=40)
    response.raise_for_status()
    result = response.json()["candidates"][0]["content"]["parts"][0]["text"]
else:
    result = "Configure GEMINI_API_KEY no GitLab CI/CD Variables para habilitar a análise."
Path("relatorio_ia.md").write_text("# Diagnóstico\n\n" + result)
print(result)

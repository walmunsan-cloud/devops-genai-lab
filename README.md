# DevOps com GenAI — Unidade 5

Miniprojeto acadêmico com falha intencional de tipo em Python, teste pytest e pipeline GitLab CI/CD.

## Arquivos
- `app.py`: código com bug proposital.
- `test_app.py`: teste automatizado.
- `.gitlab-ci.yml`: jobs `unit_test` e `ai_debugger`.
- `genai_analyst.py`: análise opcional via Gemini.
- `requirements.txt`: dependências.

## Como executar
```bash
pip install -r requirements.txt
pytest -v
```
O teste deve falhar com `TypeError`, pois o código concatena `str` e `float`.

## Publicação no GitLab
Crie um projeto público vazio chamado `devops-genai-lab`, envie os arquivos à raiz e configure `GEMINI_API_KEY` em Settings > CI/CD > Variables (mascarada). Abra um Merge Request para acionar o pipeline conforme as regras do seu projeto.

## Correção a validar
```python
def formatar_recibo(total):
    return f"Total: R$ {total:.2f}"
```
A correção depende do requisito de formatação monetária.

**Atenção:** projeto preparado como exemplo; execução no GitLab e integração real com IA ainda precisam ser verificadas. O agente não comenta automaticamente no MR. Nunca envie chaves ou dados sensíveis nos logs.

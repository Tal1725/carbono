# IA LIVRE — modo local

O arquivo `ia-livre-local.py` cria um pequeno servidor local para evitar o problema de CORS entre o navegador e o Ollama.

## Uso

1. Deixe o Ollama aberto.
2. Execute **INICIAR-IA-LIVRE.bat**.
3. Abra **http://127.0.0.1:8765** no navegador.

O servidor encaminha:
- `GET /api/tags` → Ollama
- `POST /api/chat` → Ollama

Nenhuma chave de API é necessária para o chat local.

## Vídeo

A interface já possui a área de vídeo. A geração real de vídeo exige um motor local compatível, como ComfyUI com um modelo de vídeo. O navegador sozinho/GitHub Pages não executa esse modelo. GitHub Pages hospeda arquivos estáticos, não um servidor Python. 

A prioridade é manter o chat local simples e depois conectar o motor de vídeo sem alterar a interface.

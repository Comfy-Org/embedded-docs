# Google Gemini

Gere respostas de texto com os modelos Gemini do Google. Forneça um prompt de texto e, opcionalmente, uma ou mais imagens, clipes de áudio, vídeos ou arquivos como contexto multimodal.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `prompt` | Entrada de texto para o modelo. Inclua instruções detalhadas, perguntas ou contexto. | STRING | Sim |  |
| `model` | O modelo Gemini usado para gerar a resposta. | COMBO | Sim | `"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `seed` | Semente para amostragem. Defina como 0 para uma semente aleatória. A saída determinística não é garantida. (padrão: 42) | INT | Sim | 0 a 2147483647 |
| `system_prompt` | Instruções fundamentais que determinam o comportamento do modelo. (padrão: "") | STRING | Não |  |

**Observação:** Ao fornecer imagens, áudio ou vídeo como contexto multimodal, o nó faz upload da mídia como URLs para as primeiras 10 entradas. Qualquer mídia adicional é enviada inline como dados base64, com um payload inline máximo de 18 MB. Se o payload inline exceder esse limite, um erro será gerado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `output` | A resposta de texto gerada pelo modelo Gemini. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ec9921f218a726082eb8987cf94b3575f61a3c6cf55fb33aeb81d42fad35d302`

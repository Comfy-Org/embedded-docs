> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/pt-BR.md)

Este nó permite que usuários interajam com os modelos de IA Gemini do Google para gerar respostas de texto. Você pode fornecer vários tipos de entradas, incluindo texto, imagens, áudio, vídeo e arquivos como contexto para o modelo gerar respostas mais relevantes e significativas. O nó gerencia automaticamente toda a comunicação com a API e a análise das respostas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | - | Entradas de texto para o modelo, usadas para gerar uma resposta. Você pode incluir instruções detalhadas, perguntas ou contexto para o modelo. Padrão: string vazia. |
| `model` | COMBO | Sim | `gemini-2.5-pro-preview-05-06`<br>`gemini-2.5-flash-preview-04-17`<br>`gemini-2.5-pro`<br>`gemini-2.5-flash`<br>`gemini-3-pro-preview`<br>`gemini-3-1-pro`<br>`gemini-3-1-flash-lite` | O modelo Gemini a ser usado para gerar respostas. Padrão: gemini-3-1-pro. |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Quando a semente é fixada em um valor específico, o modelo faz o melhor esforço para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou as configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo quando você usa o mesmo valor de semente. Por padrão, um valor de semente aleatório é usado. Padrão: 42. |
| `images` | IMAGE | Não | - | Imagem(ns) opcional(is) para usar como contexto para o modelo. Para incluir várias imagens, você pode usar o nó Batch Images. Padrão: Nenhum. |
| `audio` | AUDIO | Não | - | Áudio opcional para usar como contexto para o modelo. Padrão: Nenhum. |
| `video` | VIDEO | Não | - | Vídeo opcional para usar como contexto para o modelo. Padrão: Nenhum. |
| `files` | GEMINI_INPUT_FILES | Não | - | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. Padrão: Nenhum. |
| `system_prompt` | STRING | Não | - | Instruções fundamentais que ditam o comportamento de uma IA. Padrão: string vazia. Este é um parâmetro avançado. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `STRING` | STRING | A resposta de texto gerada pelo modelo Gemini. |

---
**Source fingerprint (SHA-256):** `6addc7c0bc0c5889ddd6dbcb72b0b608ab738189990c591eb7160f849f6b5374`

# Google Gemini

Este nó permite que usuários interajam com os modelos de IA Gemini do Google para gerar respostas de texto. Você pode fornecer vários tipos de entradas, incluindo texto, imagens, áudio, vídeo e arquivos como contexto para o modelo gerar respostas mais relevantes e significativas. O nó gerencia automaticamente toda a comunicação com a API e a análise das respostas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Entradas de texto para o modelo, usadas para gerar uma resposta. Você pode incluir instruções detalhadas, perguntas ou contexto para o modelo. Padrão: string vazia. | STRING | Sim | - |
| `modelo` | O modelo Gemini a ser usado para gerar respostas. Padrão: gemini-3-1-pro. | COMBO | Sim | `gemini-2.5-pro-preview-05-06`<br>`gemini-2.5-flash-preview-04-17`<br>`gemini-2.5-pro`<br>`gemini-2.5-flash`<br>`gemini-3-pro-preview`<br>`gemini-3-1-pro`<br>`gemini-3-1-flash-lite` |
| `semente` | Quando a semente é fixada em um valor específico, o modelo faz o melhor esforço para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou as configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo quando você usa o mesmo valor de semente. Por padrão, um valor de semente aleatório é usado. Padrão: 42. | INT | Sim | 0 a 18446744073709551615 |
| `imagens` | Imagem(ns) opcional(is) para usar como contexto para o modelo. Para incluir várias imagens, você pode usar o nó Batch Images. Padrão: Nenhum. | IMAGE | Não | - |
| `áudio` | Áudio opcional para usar como contexto para o modelo. Padrão: Nenhum. | AUDIO | Não | - |
| `vídeo` | Vídeo opcional para usar como contexto para o modelo. Padrão: Nenhum. | VIDEO | Não | - |
| `arquivos` | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. Padrão: Nenhum. | GEMINI_INPUT_FILES | Não | - |
| `system_prompt` | Instruções fundamentais que ditam o comportamento de uma IA. Padrão: string vazia. Este é um parâmetro avançado. | STRING | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `STRING` | A resposta de texto gerada pelo modelo Gemini. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6addc7c0bc0c5889ddd6dbcb72b0b608ab738189990c591eb7160f849f6b5374`

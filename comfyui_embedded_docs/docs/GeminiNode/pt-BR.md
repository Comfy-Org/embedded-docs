# Google Gemini

Este nó permite que os usuários interajam com os modelos de IA Gemini do Google para gerar respostas de texto. Você pode fornecer vários tipos de entradas, incluindo texto, imagens, áudio, vídeo e arquivos como contexto para o modelo gerar respostas mais relevantes e significativas. O nó lida automaticamente com toda a comunicação com a API e o parsing das respostas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Entradas de texto para o modelo, usadas para gerar uma resposta. Você pode incluir instruções detalhadas, perguntas ou contexto para o modelo. Padrão: string vazia. | STRING | Sim | - |
| `model` | O modelo Gemini a ser usado para gerar respostas. Padrão: gemini-3-1-pro. | COMBO | Sim | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `seed` | Quando a seed é fixada em um valor específico, o modelo faz o melhor esforço para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou as configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo quando você usa o mesmo valor de seed. Por padrão, um valor de seed aleatório é usado. Padrão: 42. | INT | Sim | 0 a 18446744073709551615 |
| `images` | Imagem(ns) opcional(is) para usar como contexto para o modelo. Para incluir várias imagens, você pode usar o nó Batch Images. Padrão: Nenhum. | IMAGE | Não | - |
| `audio` | Áudio opcional para usar como contexto para o modelo. Padrão: Nenhum. | AUDIO | Não | - |
| `video` | Vídeo opcional para usar como contexto para o modelo. Padrão: Nenhum. | VIDEO | Não | - |
| `files` | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. Padrão: Nenhum. | GEMINI_INPUT_FILES | Não | - |
| `system_prompt` | Instruções fundamentais que determinam o comportamento de uma IA. Padrão: string vazia. Este é um parâmetro avançado. | STRING | Não | - |

Nota: Este nó está marcado como obsoleto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `STRING` | A resposta de texto gerada pelo modelo Gemini. Se o modelo não retornar texto, o nó gera "Empty response from Gemini model...". | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`

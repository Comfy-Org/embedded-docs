> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/pt-BR.md)

Este nó permite que os usuários interajam com os modelos de IA Gemini do Google para gerar respostas em texto. Você pode fornecer múltiplos tipos de entrada, incluindo texto, imagens, áudio, vídeo e arquivos como contexto para que o modelo gere respostas mais relevantes e significativas. O nó gerencia toda a comunicação com a API e a análise das respostas automaticamente.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Entradas de texto para o modelo, usadas para gerar uma resposta. Você pode incluir instruções detalhadas, perguntas ou contexto para o modelo. Padrão: string vazia. |
| `model` | COMBO | Sim | `gemini-2.0-flash-exp`<br>`gemini-2.0-flash-thinking-exp`<br>`gemini-2.5-pro-exp`<br>`gemini-2.0-flash`<br>`gemini-2.0-flash-thinking`<br>`gemini-2.5-pro`<br>`gemini-2.0-flash-lite`<br>`gemini-1.5-flash`<br>`gemini-1.5-flash-8b`<br>`gemini-1.5-pro`<br>`gemini-1.0-pro` | O modelo Gemini a ser usado para gerar as respostas. Padrão: gemini-2.5-pro. |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Quando o *seed* é fixado em um valor específico, o modelo faz o melhor esforço para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo quando se usa o mesmo valor de *seed*. Por padrão, um valor de *seed* aleatório é usado. Padrão: 42. |
| `images` | IMAGE | Não | - | Imagem(s) opcional(is) para usar como contexto para o modelo. Para incluir múltiplas imagens, você pode usar o nó Batch Images. Padrão: Nenhum. |
| `audio` | AUDIO | Não | - | Áudio opcional para usar como contexto para o modelo. Padrão: Nenhum. |
| `video` | VIDEO | Não | - | Vídeo opcional para usar como contexto para o modelo. Padrão: Nenhum. |
| `files` | GEMINI_INPUT_FILES | Não | - | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files. Padrão: Nenhum. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `STRING` | STRING | A resposta em texto gerada pelo modelo Gemini. |

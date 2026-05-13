> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImageNode/pt-BR.md)

O nó GeminiImage gera respostas de texto e imagem dos modelos de IA Gemini do Google. Ele permite que você forneça entradas multimodais, incluindo prompts de texto, imagens e arquivos para criar saídas coerentes de texto e imagem. O nó gerencia toda a comunicação com a API e a análise das respostas com os modelos Gemini mais recentes.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Faixa | Descrição |
|-----------|---------------|-----------------|--------|-------|-----------|
| `prompt` | STRING | obrigatório | "" | - | Prompt de texto para geração |
| `model` | COMBO | obrigatório | gemini_2_5_flash_image_preview | Modelos Gemini disponíveis<br>Opções extraídas do enum GeminiImageModel | O modelo Gemini a ser usado para gerar respostas |
| `seed` | INT | obrigatório | 42 | 0 a 18446744073709551615 | Quando a semente é fixada em um valor específico, o modelo faz o melhor possível para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou as configurações de parâmetros, como a temperatura, pode causar variações na resposta, mesmo usando o mesmo valor de semente. Por padrão, um valor de semente aleatório é usado |
| `images` | IMAGE | opcional | Nenhum | - | Imagem(ns) opcional(is) para usar como contexto para o modelo. Para incluir várias imagens, você pode usar o nó Batch Images |
| `files` | GEMINI_INPUT_FILES | opcional | Nenhum | - | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó Gemini Generate Content Input Files |

*Nota: O nó inclui parâmetros ocultos (`auth_token`, `comfy_api_key`, `unique_id`) que são tratados automaticamente pelo sistema e não exigem entrada do usuário.*

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `IMAGE` | IMAGE | A resposta de imagem gerada pelo modelo Gemini |
| `STRING` | STRING | A resposta de texto gerada pelo modelo Gemini |
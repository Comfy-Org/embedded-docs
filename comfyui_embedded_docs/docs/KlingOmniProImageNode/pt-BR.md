> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/pt-BR.md)

O nó Kling Omni Image (Pro) gera ou edita imagens usando o modelo Kling AI. Ele cria imagens com base em uma descrição textual e permite que você forneça imagens de referência para orientar o estilo ou conteúdo. O nó envia uma solicitação para uma API externa, que processa a tarefa e retorna a imagem final.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `model_name` | COMBO | Sim | `"kling-image-o1"` | O modelo específico do Kling AI a ser usado para a geração de imagem. |
| `prompt` | STRING | Sim | - | Um prompt de texto descrevendo o conteúdo da imagem. Pode incluir descrições positivas e negativas. O texto deve ter entre 1 e 2500 caracteres. |
| `resolution` | COMBO | Sim | `"1K"`<br>`"2K"` | A resolução alvo para a imagem gerada. |
| `aspect_ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` | A proporção de aspecto (largura para altura) desejada para a imagem gerada. |
| `reference_images` | IMAGE | Não | - | Até 10 imagens de referência adicionais. Cada imagem deve ter pelo menos 300 pixels em largura e altura, e sua proporção de aspecto deve estar entre 1:2,5 e 2,5:1. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
| :--- | :--- | :--- |
| `image` | IMAGE | A imagem final gerada ou editada pelo modelo Kling AI. |

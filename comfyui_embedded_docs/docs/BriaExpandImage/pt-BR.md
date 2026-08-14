# BriaExpandImage

Bria Expand Image expande uma imagem além de suas bordas originais, gerando novo conteúdo com a Bria. Permite escolher uma proporção alvo, uma proporção personalizada ou definir uma tela com posicionamento manual da imagem original. A expansão pode ser guiada por um prompt de texto, e a Bria gerará um automaticamente se o prompt for deixado vazio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser expandida. | IMAGE | Sim | — |
| `expand_mode` | Formato alvo da imagem expandida: uma proporção predefinida, uma proporção personalizada ou posicionamento manual da imagem original em uma tela. O modo manual é o único que pode alcançar uma tela mais alta que 1:2. Selecionar `custom_ratio` revela `ratio_width` e `ratio_height`. Selecionar `manual` revela os parâmetros de tela e posicionamento da imagem. | COMBO | Sim | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `ratio_width` | Lado da largura da proporção alvo: 21 e 9 resultam em 21:9. Padrão: 21. | INT | Condicional | 1–100 |
| `ratio_height` | Lado da altura da proporção alvo: 21 e 9 resultam em 21:9. A Bria só aceita largura/altura entre 0,5 e 3,0, portanto qualquer coisa mais alta que 1:2 exige o modo manual. Padrão: 9. | INT | Condicional | 1–100 |
| `canvas_width` | Largura da tela de saída em pixels. Padrão: 1000. | INT | Condicional | 64–5000 |
| `canvas_height` | Altura da tela de saída em pixels. Padrão: 1000. | INT | Condicional | 64–5000 |
| `image_width` | Largura da imagem original dentro da tela. Padrão: 500. | INT | Condicional | 1–5000 |
| `image_height` | Altura da imagem original dentro da tela. Padrão: 500. | INT | Condicional | 1–5000 |
| `image_x` | Posição X do canto superior esquerdo da imagem dentro da tela; pode ficar fora da tela, cortando a imagem. Padrão: 250. | INT | Condicional | -5000–5000 |
| `image_y` | Posição Y do canto superior esquerdo da imagem dentro da tela; pode ficar fora da tela, cortando a imagem. Padrão: 250. | INT | Condicional | -5000–5000 |
| `prompt` | Descrição opcional da cena expandida; quando vazio, a Bria gera uma a partir da imagem. Padrão: string vazia. | STRING | Não | Qualquer string |
| `negative_prompt` | Um prompt negativo opcional para a expansão. Padrão: string vazia. | STRING | Não | Qualquer string |
| `seed` | Semente para o processo de geração aleatória. Padrão: 42. | INT | Não | 1–2147483647 |
| `moderation` | Configurações de moderação. Quando definido como `true`, opções adicionais de moderação são exibidas. | COMBO | Não | `"false"`<br>`"true"` |
| `prompt_content_moderation` | Se ativado, modera o conteúdo do prompt. Padrão: false. Disponível apenas quando `moderation` é `true`. | BOOLEAN | Condicional | true/false |
| `visual_input_moderation` | Se ativado, modera a entrada visual. Padrão: false. Disponível apenas quando `moderation` é `true`. | BOOLEAN | Condicional | true/false |
| `visual_output_moderation` | Se ativado, modera a saída visual. Padrão: false. Disponível apenas quando `moderation` é `true`. | BOOLEAN | Condicional | true/false |

Quando `expand_mode` é `custom_ratio`, `ratio_width` e `ratio_height` definem uma proporção alvo. A Bria só aceita proporções largura/altura entre 0,5 e 3,0. Se a proporção estiver fora desse intervalo, um erro é gerado e o modo `manual` deve ser usado.

Quando `expand_mode` é `manual`, a imagem original é posicionada em uma tela no tamanho e na posição especificados. A imagem pode se estender para fora da tela; nesse caso, a parte externa é cortada.

Quando `moderation` é `true`, os três booleanos de moderação são enviados para a Bria. Quando `moderation` é `false`, eles são ignorados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem expandida gerada pela Bria. | IMAGE |
| `prompt` | O prompt usado para a expansão; gerado automaticamente pela Bria quando a entrada de prompt está vazia. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d2c9431837f200ccbcb39037f7b26013494c4dea3d40d899db4e717ddbbea71c`

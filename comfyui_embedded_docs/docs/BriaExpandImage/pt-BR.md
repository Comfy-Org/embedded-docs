# Bria Expand Image

Bria Expand Image expande uma imagem além de suas bordas originais gerando novo conteúdo com o Bria. Permite escolher uma proporção de aspecto desejada, uma proporção personalizada ou definir um canvas com posicionamento manual da imagem original. A expansão pode ser guiada por um prompt de texto, e o Bria gerará um automaticamente se o prompt for deixado vazio.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser expandida. | IMAGE | Sim | — |
| `expand_mode` | Forma desejada da imagem expandida: uma proporção de aspecto predefinida, uma proporção personalizada ou posicionamento manual da imagem original em um canvas. O modo manual é o único que pode alcançar um canvas mais alto que 1:2. Selecionar `custom_ratio` revela `ratio_width` e `ratio_height`. Selecionar `manual` revela os parâmetros de canvas e posicionamento da imagem. | DYNAMIC_COMBO | Sim | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `prompt` | Descrição opcional da cena expandida; quando vazio, o Bria gera uma a partir da imagem. Padrão: string vazia. | STRING | Sim | Qualquer string |
| `negative_prompt` | Um prompt negativo opcional para a expansão. Padrão: string vazia. | STRING | Sim | Qualquer string |
| `seed` | Seed para o processo de geração aleatória. Padrão: 42. | INT | Sim | 1–2147483647 |
| `moderation` | Configurações de moderação. Quando definido como `true`, opções adicionais de moderação são exibidas. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |

### Entradas de proporção personalizada

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `ratio_width` | Lado da largura da proporção desejada: 21 e 9 resultam em 21:9. Padrão: 21. | INT | Sim | 1–100 |
| `ratio_height` | Lado da altura da proporção desejada: 21 e 9 resultam em 21:9. O Bria só aceita largura/altura entre 0,5 e 3,0, então qualquer coisa mais alta que 1:2 precisa do modo manual. Padrão: 9. | INT | Sim | 1–100 |

### Entradas manuais

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `canvas_width` | Largura do canvas de saída em pixels. Padrão: 1000. | INT | Sim | 64–5000 |
| `canvas_height` | Altura do canvas de saída em pixels. Padrão: 1000. | INT | Sim | 64–5000 |
| `image_width` | Largura da imagem original dentro do canvas. Padrão: 500. | INT | Sim | 1–5000 |
| `image_height` | Altura da imagem original dentro do canvas. Padrão: 500. | INT | Sim | 1–5000 |
| `image_x` | Posição X do canto superior esquerdo da imagem dentro do canvas; pode ficar fora do canvas, cortando a imagem. Padrão: 250. | INT | Sim | -5000–5000 |
| `image_y` | Posição Y do canto superior esquerdo da imagem dentro do canvas; pode ficar fora do canvas, cortando a imagem. Padrão: 250. | INT | Sim | -5000–5000 |

### Entradas de moderação

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Se habilitado, modera o conteúdo do prompt. Padrão: false. Disponível apenas quando `moderation` é `true`. | BOOLEAN | Sim | true/false |
| `visual_input_moderation` | Se habilitado, modera a entrada visual. Padrão: false. Disponível apenas quando `moderation` é `true`. | BOOLEAN | Sim | true/false |
| `visual_output_moderation` | Se habilitado, modera a saída visual. Padrão: false. Disponível apenas quando `moderation` é `true`. | BOOLEAN | Sim | true/false |

As opções de proporção de aspecto predefinidas (`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`) não têm entradas adicionais.

Quando `expand_mode` é `custom_ratio`, `ratio_width` e `ratio_height` definem uma proporção de aspecto desejada. O Bria só aceita proporções largura-altura entre 0,5 e 3,0. Se a proporção estiver fora desse intervalo, um erro é gerado e o modo `manual` deve ser usado em vez disso.

Quando `expand_mode` é `manual`, a imagem original é colocada em um canvas no tamanho e posição especificados. A imagem pode se estender para fora do canvas; nesse caso, a parte externa é cortada.

Quando `moderation` é `true`, os três booleanos de moderação são enviados ao Bria. Quando `moderation` é `false`, eles são ignorados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem expandida gerada pelo Bria. | IMAGE |
| `prompt` | O prompt usado para a expansão; gerado automaticamente pelo Bria quando a entrada de prompt está vazia. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d2c9431837f200ccbcb39037f7b26013494c4dea3d40d899db4e717ddbbea71c`

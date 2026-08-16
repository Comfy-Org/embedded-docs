# Grok Image Edit

Modifique uma imagem existente com base em um prompt de texto. Este nó envia suas imagens e uma descrição de texto para a API Grok, que edita as imagens de acordo com suas instruções e retorna o resultado.
## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `model` | O modelo de imagem Grok a ser usado. Os subparâmetros exibidos abaixo mudam dependendo do modelo selecionado. | DYNAMIC_COMBO | Sim | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | O prompt de texto usado para gerar a imagem. (padrão: "") | STRING | Sim | N/A |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos, independentemente da semente. (padrão: 0) | INT | Sim | 0 to 2147483647 |

### Entradas do grok-imagine-image-2.0

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `resolution` | Resolução de saída das imagens editadas. | COMBO | Sim | "1K"<br>"2K" |
| `number_of_images` | Número de imagens editadas a serem geradas. (padrão: 1) | INT | Sim | 1 to 10 |
| `quality` | Nível de qualidade das imagens geradas. | COMBO | Sim | "medium"<br>"low" |
| `aspect_ratio` | Proporção de aspecto da imagem editada. (padrão: "auto") | COMBO | Sim | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Entradas do grok-imagine-image-quality e do grok-imagine-image

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `resolution` | Resolução de saída das imagens editadas. | COMBO | Sim | "1K"<br>"2K" |
| `number_of_images` | Número de imagens editadas a serem geradas. (padrão: 1) | INT | Sim | 1 to 10 |
| `aspect_ratio` | Permitido apenas quando várias imagens estão conectadas. (padrão: "auto") | COMBO | Sim | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Entradas do grok-imagine-image-pro

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `resolution` | Resolução de saída das imagens editadas. | COMBO | Sim | "1K"<br>"2K" |
| `number_of_images` | Número de imagens editadas a serem geradas. (padrão: 1) | INT | Sim | 1 to 10 |

### Entradas de referência

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `images` | Slot expansível: conecte 1 ou mais imagens de referência para edição. Slots numerados como `image_1`, `image_2`, `image_3` podem ser adicionados. O número máximo de imagens depende do modelo selecionado (consulte as seções de modelos acima). | IMAGE | Sim | 1 image for `grok-imagine-image-pro`<br>1 to 3 images for `grok-imagine-image-2.0`, `grok-imagine-image-quality`, and `grok-imagine-image` |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---|---|---|
| `IMAGE` | The edited image(s) returned by the Grok API. If a single image is generated, it is returned directly. If multiple images are generated, they are concatenated into a single batch tensor. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`

# Grok Image Edit

Modifique uma ou mais imagens existentes com base em um prompt de texto. O nó envia a(s) imagem(ns) de referência conectada(s) e o prompt para a API de edição de imagens do Grok usando o modelo selecionado e, em seguida, retorna a(s) imagem(ns) editada(s).

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de imagem do Grok a ser usado. Os subparâmetros mostrados abaixo mudam dependendo do modelo selecionado. | DYNAMIC_COMBO | Sim | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | O prompt de texto usado para gerar a imagem. (padrão: "") | STRING | Sim | N/A |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |

### Entradas do grok-imagine-image-2.0

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Resolução de saída das imagens editadas. | COMBO | Sim | "1K"<br>"2K" |
| `number_of_images` | Número de imagens editadas a serem geradas. (padrão: 1) | INT | Sim | 1 a 10 |
| `quality` | Nível de qualidade das imagens geradas. | COMBO | Sim | "medium"<br>"low" |
| `aspect_ratio` | Proporção de aspecto da imagem editada. (padrão: "auto") | COMBO | Sim | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Entradas do grok-imagine-image-quality e do grok-imagine-image

Compartilhado por grok-imagine-image-quality e grok-imagine-image.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Resolução de saída das imagens editadas. | COMBO | Sim | "1K"<br>"2K" |
| `number_of_images` | Número de imagens editadas a serem geradas. (padrão: 1) | INT | Sim | 1 a 10 |
| `aspect_ratio` | Permitido apenas quando várias imagens estão conectadas. (padrão: "auto") | COMBO | Sim | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Entradas do grok-imagine-image-pro

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Resolução de saída das imagens editadas. | COMBO | Sim | "1K"<br>"2K" |
| `number_of_images` | Número de imagens editadas a serem geradas. (padrão: 1) | INT | Sim | 1 a 10 |

### Entradas de referência

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot expansível: conecte de 1 a N imagens de referência para editar. Os slots usam os nomes de template `image_1`, `image_2`, `image_3`; o número máximo de slots depende do modelo selecionado. | IMAGE | Sim | 1 imagem para `grok-imagine-image-pro`<br>1 a 3 imagens para `grok-imagine-image-2.0`, `grok-imagine-image-quality` e `grok-imagine-image` |

**Nota sobre restrições:**
- `prompt` deve conter pelo menos 1 caractere que não seja espaço em branco.
- Pelo menos uma imagem de referência é obrigatória para edição; o nó lança um erro se nenhuma imagem estiver conectada.
- O número máximo de imagens de entrada é 1 para `grok-imagine-image-pro` e 3 para `grok-imagine-image-2.0`, `grok-imagine-image-quality` e `grok-imagine-image`. Conectar mais imagens do que o modelo suporta lança um erro.
- O limite de imagens conta cada imagem nas entradas conectadas, portanto, um lote contendo várias imagens conta como várias imagens para o limite.
- Para `grok-imagine-image-quality` e `grok-imagine-image`, um `aspect_ratio` personalizado (qualquer valor diferente de "auto") só é permitido quando várias imagens estão conectadas. Com uma única imagem, `aspect_ratio` deve ser "auto".
- Para `grok-imagine-image-2.0`, `aspect_ratio` pode ser definido livremente mesmo com uma única imagem.
- O subparâmetro `quality` só está disponível com `grok-imagine-image-2.0`.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `IMAGE` | A(s) imagem(ns) editada(s) retornada(s) pela API do Grok. Se uma única imagem for gerada, ela é retornada diretamente. Se várias imagens forem geradas, elas são concatenadas em um único tensor de lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`

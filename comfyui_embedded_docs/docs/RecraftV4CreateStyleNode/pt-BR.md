# Recraft V4 Criar Estilo

Este nó cria um estilo Recraft V4 reutilizável a partir de 1 a 10 imagens de referência. O ID de estilo retornado funciona com todos os modelos Recraft V4 e V4.1 do mesmo tipo de saída e pode ser reutilizado em etapas posteriores de geração de imagens. O tamanho total de todas as imagens de referência é limitado a 10 MB.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Tipo de saída para o qual o estilo é criado: recraftv4_styles para imagens raster, recraftv4_styles_vector para SVG. | COMBO | Sim | "recraftv4_styles"<br>"recraftv4_styles_vector" |
| `images` | Imagens de referência que definem o estilo. Referências semelhantes aprimoram a correspondência; referências variadas ampliam-na. Slot expansível: conecte de 1 a 10 imagens (`image_1` a `image_10`). | IMAGE | Sim | 1 a 10 imagens |

### Notas

- É necessária pelo menos uma imagem de referência; o nó gera um erro se nenhuma for fornecida.
- São permitidas no máximo 10 imagens de referência.
- O tamanho total codificado de todas as imagens de referência não deve exceder 10 MB; o nó gera um erro se o limite for excedido.
- Cada imagem de referência é reduzida para no máximo 2048×2048 pixels e codificada como WebP antes de ser enviada à API Recraft.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `style_id` | Identificador único do estilo criado, utilizável com todos os modelos Recraft V4 e V4.1 do mesmo tipo de saída. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `63b31ff08d5cfe7c0d4de6987f2ee5a34bd491237ed0fb4c93c225e33b7cede3`

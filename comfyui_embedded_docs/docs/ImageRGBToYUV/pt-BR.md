# Converter RGB para YUV

O nó ImageRGBToYUV converte uma imagem RGB em componentes de cor no estilo YUV usando uma conversão de cor RGB para YCbCr. Ele divide o resultado em três imagens separadas — Y (luminância, ou brilho), U (croma de diferença azul) e V (croma de diferença vermelha) — e retorna cada componente com a mesma largura e altura da entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem RGB de entrada a ser convertida em componentes Y, U e V. Se a imagem contiver um canal alfa, apenas os três primeiros canais (RGB) serão usados. | IMAGE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `Y` | O componente de luminância (brilho) do espaço de cor YUV, retornado como uma imagem de três canais | IMAGE |
| `U` | O componente de croma de diferença azul do espaço de cor YUV, retornado como uma imagem de três canais | IMAGE |
| `V` | O componente de croma de diferença vermelha do espaço de cor YUV, retornado como uma imagem de três canais | IMAGE |

Cada saída tem a mesma largura e altura da imagem de entrada. O componente Y, U ou V correspondente é repetido em todos os três canais, de modo que cada saída seja retornada como uma imagem padrão de três canais.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`

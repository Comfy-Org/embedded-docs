# ImageYUVToRGB

O nó ImageYUVToRGB converte imagens do espaço de cores YUV para o espaço de cores RGB. Ele recebe três imagens de entrada separadas representando os componentes Y (luma), U (projeção azul) e V (projeção vermelha) e as combina em uma única imagem RGB.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `Y` | A imagem de entrada do componente Y (luminância). Se a imagem tiver mais de três canais, somente os três primeiros serão usados e a média deles será calculada em um único canal. | IMAGE | Sim | - |
| `U` | A imagem de entrada do componente U (projeção azul). Se a imagem tiver mais de três canais, somente os três primeiros serão usados e a média deles será calculada em um único canal. | IMAGE | Sim | - |
| `V` | A imagem de entrada do componente V (projeção vermelha). Se a imagem tiver mais de três canais, somente os três primeiros serão usados e a média deles será calculada em um único canal. | IMAGE | Sim | - |

**Nota:** Todas as três imagens de entrada (Y, U e V) devem ser fornecidas em conjunto e devem ter dimensões compatíveis (altura, largura e tamanho do lote correspondentes) para que a conversão seja bem-sucedida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A imagem RGB convertida | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/pt-BR.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`

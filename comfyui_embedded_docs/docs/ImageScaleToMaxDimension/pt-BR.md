# ImageScaleToMaxDimension

O nó ImageScaleToMaxDimension redimensiona imagens para caber dentro de uma dimensão máxima especificada, mantendo a proporção original. Ele calcula se a imagem está orientada no modo retrato ou paisagem, então dimensiona a maior dimensão para corresponder ao tamanho alvo, ajustando proporcionalmente a dimensão menor. O nó suporta múltiplos métodos de upscaling para diferentes requisitos de qualidade e desempenho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada a ser redimensionada | IMAGE | Sim | - |
| `método de upscaling` | O método de interpolação usado para redimensionar a imagem (padrão: "area") | STRING | Sim | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bilinear"<br>"bicubic" |
| `maior tamanho` | A dimensão máxima para a imagem redimensionada (padrão: 512) | INT | Sim | 0 a 16384 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem redimensionada com a maior dimensão correspondendo ao tamanho especificado | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/pt-BR.md)

---
**Source fingerprint (SHA-256):** `be113c1a98ab9d884b2c728b790c41fb236857d59af567e43e2be0ef0362cc5e`

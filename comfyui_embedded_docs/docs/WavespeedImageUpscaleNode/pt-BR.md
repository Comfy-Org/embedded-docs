# WaveSpeed Image Upscale

O nó WaveSpeed Image Upscale utiliza um serviço de IA externo para aumentar a resolução e a qualidade de uma imagem. Ele recebe uma única foto de entrada e a redimensiona para uma resolução alvo mais alta, como 2K, 4K ou 8K, produzindo um resultado mais nítido e detalhado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de IA a ser usado para o redimensionamento. "SeedVR2" e "Ultimate" oferecem diferentes níveis de qualidade e preços. | STRING | Sim | `"SeedVR2"`<br>`"Ultimate"` |
| `imagem` | A imagem de entrada a ser redimensionada. | IMAGE | Sim |  |
| `resolução_alvo` | A resolução de saída desejada para a imagem redimensionada. | STRING | Sim | `"2K"`<br>`"4K"`<br>`"8K"` |

**Nota:** Este nó requer exatamente uma imagem de entrada. Fornecer um lote de imagens resultará em um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagem` | A imagem de saída redimensionada em alta resolução. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b14056f981f6e34c67d8126391acc11878f92f5f406559afbac803c86da42bcc`

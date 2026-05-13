> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/pt-BR.md)

O nó WaveSpeed Image Upscale utiliza um serviço de IA externo para aumentar a resolução e a qualidade de uma imagem. Ele recebe uma única foto de entrada e a redimensiona para uma resolução alvo mais alta, como 2K, 4K ou 8K, produzindo um resultado mais nítido e detalhado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model` | STRING | Sim | `"SeedVR2"`<br>`"Ultimate"` | O modelo de IA a ser usado para o redimensionamento. "SeedVR2" e "Ultimate" oferecem diferentes níveis de qualidade e preços. |
| `image` | IMAGE | Sim | | A imagem de entrada a ser redimensionada. |
| `target_resolution` | STRING | Sim | `"2K"`<br>`"4K"`<br>`"8K"` | A resolução de saída desejada para a imagem redimensionada. |

**Nota:** Este nó requer exatamente uma imagem de entrada. Fornecer um lote de imagens resultará em um erro.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `image` | IMAGE | A imagem de saída redimensionada em alta resolução. |

---
**Source fingerprint (SHA-256):** `b14056f981f6e34c67d8126391acc11878f92f5f406559afbac803c86da42bcc`

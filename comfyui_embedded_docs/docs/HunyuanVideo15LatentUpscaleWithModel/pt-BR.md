# Hunyuan Video 15 Latent Upscale With Model

O nó Hunyuan Video 15 Latent Upscale With Model aumenta a resolução de uma representação latente de imagem. Ele primeiro amplia as amostras latentes para um tamanho especificado usando um método de interpolação escolhido e, em seguida, refina o resultado ampliado usando um modelo especializado de upscale do Hunyuan Video 1.5 para melhorar a qualidade.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de upscale latente do Hunyuan Video 1.5 usado para refinar as amostras ampliadas. | LATENT_UPSCALE_MODEL | Sim | N/A |
| `samples` | A representação latente de imagem a ser ampliada. | LATENT | Sim | N/A |
| `upscale_method` | O algoritmo de interpolação usado para a etapa inicial de ampliação (padrão: `"bilinear"`). | COMBO | Sim | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | A largura desejada para o latente ampliado, em pixels. Um valor de 0 calculará a largura automaticamente com base na altura desejada e na proporção original. A largura final de saída será um múltiplo de 16 (padrão: 1280). | INT | Sim | 0 a 16384 (passo: 8) |
| `height` | A altura desejada para o latente ampliado, em pixels. Um valor de 0 calculará a altura automaticamente com base na largura desejada e na proporção original. A altura final de saída será um múltiplo de 16 (padrão: 720). | INT | Sim | 0 a 16384 (passo: 8) |
| `crop` | Determina como o latente ampliado é cortado para se ajustar às dimensões desejadas. | COMBO | Sim | `"disabled"`<br>`"center"` |

**Nota sobre dimensões:** Se ambos `width` e `height` forem definidos como 0, o nó retorna o `samples` de entrada sem alterações. Se apenas uma dimensão for definida como 0, a outra dimensão será calculada para preservar a proporção original. Ambos os valores são limitados a um mínimo de 64, e o alvo de ampliação passado para a etapa de interpolação é `width // 16` por `height // 16`, portanto, as dimensões solicitadas são efetivamente arredondadas para baixo para múltiplos de 16.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | A representação latente de imagem ampliada e refinada pelo modelo, retornada como um tensor float na CPU. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`

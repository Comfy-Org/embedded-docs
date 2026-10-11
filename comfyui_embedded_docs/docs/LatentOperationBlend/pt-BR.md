# Latent Operation Blend

Este nó cria uma operação de latent que mescla um latent em direção a um latent de referência e retorna essa operação para que ela possa ser conectada a nós como Latent Apply Operation ou Latent Apply Operation CFG. Quando a referência tem um tamanho espacial diferente, ela é redimensionada para o latent de destino com interpolação por vizinho mais próximo, e uma referência com um lote menor é repetida para corresponder ao tamanho do lote de destino. Um valor de `strength` de 0 deixa o latent inalterado. Este nó está marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `reference` | O latent em direção ao qual mesclar. Suas amostras são convertidas para o dispositivo e o dtype do latent sendo processado, depois redimensionadas e repetidas para corresponder a ele. | LATENT | Sim | - |
| `strength` | O quanto mesclar em direção à referência: 0 deixa o latent inalterado, 1 corresponde ao latent de referência redimensionado (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.0001) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `operation` | Uma operação de mesclagem que pode ser aplicada a amostras de latent. | LATENT_OPERATION |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationBlend/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5890089afddf83ddd4edd992606509b118aac9ef13eb89589f73fa75e0b9dd5a`

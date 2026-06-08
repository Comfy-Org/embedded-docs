# Pré-Processamento da Entrada do SeedVR2

Este nó adiciona bordas a uma imagem redimensionada para prepará-la para o modelo SeedVR2. Ele remove o canal alfa durante o processamento, que posteriormente é restaurado pelo nó complementar Pós-Processamento da Saída do SeedVR2 usando a imagem redimensionada original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `resized_images` | A imagem redimensionada a ser processada. | IMAGE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `images` | A imagem com bordas adicionadas, pronta para o processamento do SeedVR2. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b8135d0e27f75a673f52d080c6704de8cc86d15b5d16eca055d55e2d20837dc7`

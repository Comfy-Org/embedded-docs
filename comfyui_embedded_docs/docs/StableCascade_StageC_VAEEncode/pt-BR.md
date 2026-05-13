> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/pt-BR.md)

O nó **StableCascade_StageC_VAEEncode** processa imagens através de um codificador VAE para gerar representações latentes para os modelos Stable Cascade. Ele recebe uma imagem de entrada e a comprime usando o modelo VAE especificado, em seguida, gera duas representações latentes: uma para o estágio C e um placeholder para o estágio B. O parâmetro de compressão controla o quanto a imagem é reduzida antes da codificação.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser codificada no espaço latente |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar a imagem |
| `compression` | INT | Não | 4-128 | O fator de compressão aplicado à imagem antes da codificação (padrão: 42) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `stage_c` | LATENT | A representação latente codificada para o estágio C do modelo Stable Cascade |
| `stage_b` | LATENT | Uma representação latente placeholder para o estágio B (atualmente retorna zeros) |

---
**Source fingerprint (SHA-256):** `e7b9bd83d263903567ab06c00324575e01b79b50881fa807cd6f006955935c63`

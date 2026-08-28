# StableCascade_EmptyLatentImage

O nó StableCascade_EmptyLatentImage cria tensores latentes vazios para modelos Stable Cascade. Ele gera duas representações latentes separadas — uma para o estágio C e outra para o estágio B — com dimensões apropriadas com base na resolução de entrada e nas configurações de compressão. Este nó fornece o ponto de partida para o pipeline de geração do Stable Cascade.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `largura` | A largura da imagem de saída em pixels (padrão: 1024, passo: 8) | INT | Sim | 256 a MAX_RESOLUTION |
| `altura` | A altura da imagem de saída em pixels (padrão: 1024, passo: 8) | INT | Sim | 256 a MAX_RESOLUTION |
| `compressão` | O fator de compressão que determina as dimensões latentes para o estágio C (padrão: 42, passo: 1). Este é um parâmetro avançado. | INT | Sim | 4 a 128 |
| `tamanho_do_lote` | O número de amostras latentes a serem geradas em um lote (padrão: 1) | INT | Não | 1 a 4096 |

Nota: O valor de `compression` controla o tamanho latente do estágio C: sua altura e largura são a `height` e a `width` de entrada divididas por `compression`. O latente do estágio B sempre usa uma compressão fixa de 4.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `stage_c` | O tensor latente do estágio C com dimensões [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | O tensor latente do estágio B com dimensões [batch_size, 4, height//4, width//4] | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`

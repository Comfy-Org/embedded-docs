> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/pt-BR.md)

O nó **StableCascade_EmptyLatentImage** cria tensores latentes vazios para modelos Stable Cascade. Ele gera duas representações latentes separadas — uma para o estágio C e outra para o estágio B — com dimensões apropriadas com base na resolução de entrada e nas configurações de compressão. Este nó fornece o ponto de partida para o pipeline de geração do Stable Cascade.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `width` | INT | Sim | 256 a MAX_RESOLUTION | A largura da imagem de saída em pixels (padrão: 1024, passo: 8) |
| `height` | INT | Sim | 256 a MAX_RESOLUTION | A altura da imagem de saída em pixels (padrão: 1024, passo: 8) |
| `compression` | INT | Sim | 4 a 128 | O fator de compressão que determina as dimensões latentes para o estágio C (padrão: 42, passo: 1) |
| `batch_size` | INT | Não | 1 a 4096 | O número de amostras latentes a serem geradas em um lote (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `stage_c` | LATENT | O tensor latente do estágio C com dimensões [batch_size, 16, altura//compressão, largura//compressão] |
| `stage_b` | LATENT | O tensor latente do estágio B com dimensões [batch_size, 4, altura//4, largura//4] |

---
**Source fingerprint (SHA-256):** `ba5347f522b661993e540bc5775737cae88bd5f7a87c1b91715f8c1858e8e81a`

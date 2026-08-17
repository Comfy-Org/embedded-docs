# Empty Flux 2 Latent

O nó EmptyFlux2LatentImage cria uma representação latente vazia e em branco. Ele gera um tensor preenchido com zeros, que serve como ponto de partida para o processo de remoção de ruído (denoising) do modelo Flux. As dimensões do latente são determinadas pela largura e altura de entrada, reduzidas por um fator de 16.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `width` | A largura da imagem final a ser gerada. A largura latente será este valor dividido por 16. O valor padrão é 1024. | INT | Sim | 16 a 16384 |
| `height` | A altura da imagem final a ser gerada. A altura latente será este valor dividido por 16. O valor padrão é 1024. | INT | Sim | 16 a 16384 |
| `batch_size` | O número de amostras latentes a serem geradas em um único lote. O valor padrão é 1. | INT | Não | 1 a 4096 |

**Nota:** As entradas `width` e `height` devem ser divisíveis por 16, pois o nó internamente as divide por esse fator para criar as dimensões latentes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `samples` | Um tensor latente preenchido com zeros. A forma é `[batch_size, 128, height // 16, width // 16]`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`

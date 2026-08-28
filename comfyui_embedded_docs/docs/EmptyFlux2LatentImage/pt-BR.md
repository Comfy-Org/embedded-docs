# Empty Flux 2 Latent

O nó Empty Flux 2 Latent cria uma representação latente vazia e em branco. Ele gera um tensor preenchido com zeros, que serve como ponto de partida para o processo de remoção de ruído (denoising) do modelo Flux. As dimensões do latente são determinadas pela largura e altura de entrada, reduzidas por um fator de 16.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `largura` | A largura da imagem final a ser gerada. A largura do latente será este valor dividido por 16. O valor padrão é 1024. | INT | Sim | 16 a 8192 |
| `altura` | A altura da imagem final a ser gerada. A altura do latente será este valor dividido por 16. O valor padrão é 1024. | INT | Sim | 16 a 8192 |
| `tamanho_do_lote` | O número de amostras latentes a serem geradas em um único lote. O valor padrão é 1. | INT | Não | 1 a 4096 |

**Nota:** As entradas `width` e `height` devem ser divisíveis por 16, pois o nó as divide internamente por esse fator para criar as dimensões do latente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `samples` | Um tensor latente preenchido com zeros. O formato é `[batch_size, 128, height // 16, width // 16]`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`

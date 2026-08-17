# EmptyLTXVLatentVideo

O nó EmptyLTXVLatentVideo cria um tensor latente vazio para geração de vídeo. Ele produz uma representação latente preenchida com zeros, com largura, altura, comprimento e tamanho de lote especificados, pronta para ser usada como ponto de partida em fluxos de trabalho de vídeo LTXV. O latente armazena o vídeo em uma forma comprimida: as dimensões espaciais são divididas por 32 e o número de quadros é reduzido por um fator de 8.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `width` | A largura do vídeo latente em pixels (padrão: 768, passo: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `height` | A altura do vídeo latente em pixels (padrão: 512, passo: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `length` | O número de quadros no vídeo latente (padrão: 97, passo: 8) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | O número de vídeos latentes a serem gerados em um lote (padrão: 1) | INT | Não | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | O tensor latente vazio gerado, preenchido com zeros. O latente também carrega um valor `downscale_ratio_spacial` de 32, que descreve a redução de escala espacial aplicada à largura e à altura. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`

# Empty HunyuanVideo 1.0 Latent

O nó `EmptyHunyuanLatentVideo` é semelhante ao nó `EmptyLatentImage`. Você pode considerá-lo como uma tela em branco para geração de vídeo, onde largura, altura e comprimento definem as propriedades da tela, e o tamanho do lote determina a quantidade de telas a serem criadas. Este nó cria telas vazias prontas para tarefas subsequentes de geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `largura` | Largura do vídeo, padrão 848, mínimo 16, máximo `nodes.MAX_RESOLUTION`, tamanho do passo 16. | `INT` |
| `altura` | Altura do vídeo, padrão 480, mínimo 16, máximo `nodes.MAX_RESOLUTION`, tamanho do passo 16. | `INT` |
| `duração` | Comprimento do vídeo, padrão 25, mínimo 1, máximo `nodes.MAX_RESOLUTION`, tamanho do passo 4. | `INT` |
| `tamanho_do_lote` | Tamanho do lote, padrão 1, mínimo 1, máximo 4096. | `INT` |

## Saídas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `samples` | Amostras de vídeo latente geradas contendo tensores zero, prontas para tarefas de processamento e geração. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/pt-BR.md)

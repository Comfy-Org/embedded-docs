> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/pt-BR.md)

Este nó salva um conjunto de dados de treinamento preparado no disco rígido do seu computador. Ele recebe dados codificados, que incluem latentes de imagem e seu condicionamento de texto correspondente, e os organiza em vários arquivos menores chamados *shards* para facilitar o gerenciamento. O nó cria automaticamente uma pasta no seu diretório de saída e salva tanto os arquivos de dados quanto um arquivo de metadados que descreve o conjunto de dados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Sim | N/A | Lista de dicionários de latentes do nó MakeTrainingDataset. |
| `conditioning` | CONDITIONING | Sim | N/A | Lista de listas de condicionamento do nó MakeTrainingDataset. |
| `folder_name` | STRING | Não | N/A | Nome da pasta para salvar o conjunto de dados (dentro do diretório de saída). (padrão: "training_dataset") |
| `shard_size` | INT | Não | 1 a 100000 | Número de amostras por arquivo *shard*. (padrão: 1000) |

**Observação:** O número de itens na lista `latents` deve corresponder exatamente ao número de itens na lista `conditioning`. O nó gerará um erro se essas contagens não coincidirem.

## Saídas

Este nó não produz nenhum dado de saída. Sua função é salvar arquivos no seu disco.

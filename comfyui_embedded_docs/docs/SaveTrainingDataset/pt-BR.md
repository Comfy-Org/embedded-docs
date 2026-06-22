# Salvar Conjunto de Dados de Treinamento

Este nó salva um conjunto de dados de treinamento preparado no disco rígido do seu computador. Ele recebe dados codificados, que incluem latentes de imagem e seus respectivos condicionamentos de texto, e os organiza em vários arquivos menores chamados *shards* para facilitar o gerenciamento. O nó cria automaticamente uma pasta no diretório de saída e salva tanto os arquivos de dados quanto um arquivo de metadados descrevendo o conjunto de dados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latents` | Lista de dicionários latentes do MakeTrainingDataset. | LATENT | Sim | N/A |
| `condicionamento` | Lista de listas de condicionamento do MakeTrainingDataset. | CONDITIONING | Sim | N/A |
| `nome_da_pasta` | Nome da pasta para salvar o conjunto de dados (dentro do diretório de saída). (padrão: "training_dataset") | STRING | Não | N/A |
| `tamanho_do_fragmento` | Número de amostras por arquivo *shard*. (padrão: 1000) | INT | Não | 1 a 100000 |

**Observação:** O número de itens na lista `latents` deve corresponder exatamente ao número de itens na lista `conditioning`. O nó gerará um erro se essas contagens não coincidirem.

## Saídas

Este nó não produz nenhum dado de saída. Sua função é salvar arquivos no seu disco.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1b0108be7362c0cb8ba16ffbf94cf42be2d04159aacbabe1ff0890083d1733b3`

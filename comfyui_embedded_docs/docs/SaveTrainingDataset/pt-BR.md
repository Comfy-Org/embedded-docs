# Salvar Conjunto de Dados de Treinamento

Este nó salva um conjunto de dados de treinamento codificado em disco para carregamento eficiente durante o treinamento. Ele recebe os latentes de imagem e o respectivo condicionamento de texto, divide-os em arquivos menores chamados shards e os armazena em uma pasta dentro do diretório datasets. Ele também grava um arquivo de metadados que descreve o conjunto de dados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latents` | Lista de dicionários latentes do MakeTrainingDataset. | LATENT | Sim | N/A |
| `condicionamento` | Lista de listas de condicionamento do MakeTrainingDataset. | CONDITIONING | Sim | N/A |
| `nome_da_pasta` | Nome da pasta para salvar o conjunto de dados, dentro do diretório datasets. Subpastas como 'project/run1' são permitidas. (padrão: "training_dataset") | STRING | Sim | N/A |
| `tamanho_do_fragmento` | Número de amostras por arquivo de shard. (padrão: 1000) | INT | Sim | 1 a 100000 |

**Nota:** O número de itens em `latents` deve corresponder exatamente ao número de itens em `conditioning`; o nó gera um erro se essas contagens não coincidirem. O `folder_name` deve nomear uma subpasta do diretório datasets (por exemplo, `my_dataset`) — não pode ser o próprio diretório datasets, e nomes de pasta que resultariam em um caminho fora do diretório datasets são rejeitados.

## Saídas

Este nó não produz nenhum dado de saída. Sua função é salvar arquivos no seu disco. Cada shard é salvo como um arquivo `shard_XXXX.pkl` na pasta escolhida, e um arquivo `metadata.json` registra o número total de amostras, o número de shards e o tamanho do shard.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`

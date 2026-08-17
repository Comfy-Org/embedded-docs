# Salvar Conjunto de Dados de Treinamento

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latents` | Lista de dicionários de latentes do MakeTrainingDataset. | LATENT | Sim | N/A |
| `conditioning` | Lista de listas de condicionamento do MakeTrainingDataset. | CONDITIONING | Sim | N/A |
| `folder_name` | Nome da pasta para salvar o conjunto de dados, dentro do diretório datasets. Subpastas como 'project/run1' são permitidas. (padrão: "training_dataset") | STRING | Sim | N/A |
| `shard_size` | Número de amostras por arquivo de fragmento. (padrão: 1000) | INT | Sim | 1 a 100000 |

**Nota:** O número de itens na lista `latents` deve corresponder exatamente ao número de itens na lista `conditioning`. O nó lança um erro se essas contagens não corresponderem. O `folder_name` deve especificar uma subpasta do diretório datasets: a própria pasta raiz do diretório datasets, bem como qualquer caminho que escape dela (como '..' ou um caminho absoluto), é rejeitada.

## Saídas

Este nó não produz nenhum dado de saída. Ele salva o conjunto de dados como arquivos de fragmentos numerados (por exemplo, `shard_0000.pkl`) e um arquivo `metadata.json` dentro da pasta escolhida no diretório datasets.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`

# Carregar Conjunto de Dados de Treinamento

Este nó carrega um dataset de treinamento codificado (latents e condicionamento) que foi previamente salvo em disco. Ele lê todos os arquivos de shard de dados `shard_*.pkl` de uma pasta de dataset selecionada no diretório datasets e retorna os vetores latentes combinados e os dados de condicionamento para uso em fluxos de trabalho de treinamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `nome_da_pasta` | Dataset salvo a ser carregado, do diretório datasets. | COMBO | Sim | Uma opção por pasta de dataset encontrada no diretório datasets |

Nota: As opções de `folder_name` são criadas automaticamente ao escanear o diretório datasets. Uma subpasta é listada como um dataset quando contém um arquivo `metadata.json` ou pelo menos um arquivo `.safetensors` (a varredura não entra em uma pasta que corresponda a esse critério). A pasta de dataset selecionada é pesquisada em todos os diretórios raiz de datasets configurados, e o nome da pasta deve resolver para uma subpasta dentro de um desses diretórios raiz. O nó lê todos os arquivos chamados `shard_*.pkl` na pasta selecionada, em ordem classificada, e gera um erro se nenhum arquivo shard for encontrado ou se a pasta não puder ser localizada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latents` | Lista de dicionários de latentes (lista de saída), em que cada dicionário contém uma chave `"samples"` com um tensor. | LATENT |
| `conditioning` | Lista de listas de condicionamento (lista de saída), em que cada lista interna contém dados de condicionamento para a amostra correspondente. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`

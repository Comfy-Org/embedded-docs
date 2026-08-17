# Carregar Conjunto de Dados de Treinamento

Este nó carrega um conjunto de dados de treinamento codificado (latentes e condicionamento) do disco para uso no treinamento. Após selecionar uma pasta de conjunto de dados salva anteriormente, ele lê todos os arquivos de shard dentro dela e retorna os vetores latentes combinados e os dados de condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `folder_name` | Conjunto de dados salvo para carregar, a partir do diretório de datasets. | COMBO | Sim | Preenchido dinamicamente com todas as pastas de conjuntos de dados encontradas nos diretórios de datasets registrados. Somente pastas que contenham um arquivo `metadata.json` ou arquivos `.safetensors` são listadas. |

**Nota:** A pasta do conjunto de dados selecionada deve ser uma subpasta de um diretório de datasets registrado e deve conter pelo menos um arquivo de shard chamado `shard_*.pkl`; caso contrário, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latents` | Lista de dicionários de latentes carregados dos shards do conjunto de dados, cada um contendo um tensor `samples`. | LATENT |
| `conditioning` | Lista de listas de condicionamento carregadas dos shards do conjunto de dados, uma por amostra. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`

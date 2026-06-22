# Carregar Conjunto de Dados de Treinamento

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/en.md)

Este nó carrega um conjunto de dados de treinamento codificado que foi previamente salvo em disco. Ele procura e lê todos os arquivos de fragmentos de dados de uma pasta especificada dentro do diretório de saída do ComfyUI e, em seguida, retorna os vetores latentes combinados e os dados de condicionamento para uso em fluxos de trabalho de treinamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `nome_da_pasta` | Nome da pasta que contém o conjunto de dados salvo, localizada dentro do diretório de saída do ComfyUI (padrão: "training_dataset"). | STRING | Sim | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latents` | Uma lista de dicionários latentes, onde cada dicionário contém uma chave `"samples"` com um tensor. | LATENT |
| `conditioning` | Uma lista de listas de condicionamento, onde cada lista interna contém dados de condicionamento para uma amostra correspondente. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0a07c97e2c6a32f77cd21ea7dbdd33e06fad82285696b88122fef369307e133d`

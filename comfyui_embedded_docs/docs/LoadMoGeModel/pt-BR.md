Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/en.md)

## Visão Geral

Carrega um modelo MoGe (Geometria Monocular) a partir de um arquivo e o prepara para uso em tarefas de estimativa geométrica. Este nó lê um arquivo de modelo da pasta `geometry_estimation` e inicializa o modelo MoGe com seus pesos treinados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | O nome do arquivo do modelo MoGe a ser carregado. Selecione entre os arquivos de modelo disponíveis na sua instalação do ComfyUI. | STRING | Sim | Lista de arquivos de modelo disponíveis na pasta `geometry_estimation` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MOGE_MODEL` | A instância do modelo MoGe carregada, pronta para uso em fluxos de trabalho de estimativa geométrica. | MOGE_MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4707002565181ca17936ecf87ea8059630c97c44c17facfecd04053d9581b7d1`

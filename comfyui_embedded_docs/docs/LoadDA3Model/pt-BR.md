# Carregar Depth Anything 3

Este nó carrega um modelo Depth Anything 3 a partir de um arquivo, preparando-o para uso em tarefas de estimativa de profundidade. Ele permite selecionar o arquivo do modelo e, opcionalmente, especificar a precisão numérica (tipo de dado) para os pesos do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `model_name` | O nome do arquivo do modelo Depth Anything 3 a ser carregado. | STRING | Sim | Lista de arquivos de modelo disponíveis na pasta `geometry_estimation` |
| `weight_dtype` | A precisão numérica (tipo de dado) para os pesos do modelo. A opção "default" usa a precisão original do modelo. (padrão: "default") | STRING | Não | `"default"`<br>`"fp16"`<br>`"bf16"`<br>`"fp32"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `DA3_MODEL` | O modelo Depth Anything 3 carregado, pronto para uso em fluxos de trabalho de estimativa de profundidade. | DA3_MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadDA3Model/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b1b3f4075cd9172bc1f274848b9300bca20d3cbd53b23d3c4a9f0986b36e409e`

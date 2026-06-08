# Visão Geral

Seleciona objetos rastreados específicos de uma sessão de rastreamento SAM3 por seus números de índice e os combina em uma única máscara de saída. Isso permite que você escolha quais objetos manter e quais ignorar dos resultados do rastreamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `dados_de_rastreamento` | Os dados de rastreamento gerados por um nó rastreador SAM3, contendo as máscaras empacotadas e o tamanho original da imagem. | SAM3TRACKDATA | Sim | N/A |
| `índices_de_objetos` | Índices de objetos separados por vírgula para incluir na máscara de saída (ex.: '0,2,3'). Se deixado vazio, todos os objetos rastreados são incluídos. | STRING | Não | Qualquer lista de inteiros separados por vírgula |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `masks` | Uma única máscara binária para cada quadro, onde os objetos selecionados são combinados em uma máscara. Se nenhum objeto for selecionado ou não houver dados de rastreamento, retorna uma máscara zero. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2da82effc4cdc6655d0d37e281858bf33f7b62d9056629ec810e3ff9b2e7b5a6`

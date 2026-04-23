> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/pt-BR.md)

# Visão Geral

Seleciona objetos rastreados específicos de uma sessão de rastreamento SAM3 por seus números de índice e os combina em uma única máscara de saída. Isso permite que você escolha quais objetos manter e quais ignorar dos resultados do rastreamento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `track_data` | SAM3TRACKDATA | Sim | N/A | Os dados de rastreamento provenientes de um nó rastreador SAM3, contendo as máscaras empacotadas e o tamanho original da imagem. |
| `object_indices` | STRING | Não | Qualquer lista de inteiros separados por vírgula | Índices de objetos separados por vírgula a serem incluídos na máscara de saída (ex.: '0,2,3'). Se deixado vazio, todos os objetos rastreados são incluídos. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `masks` | MASK | Uma única máscara binária para cada quadro, onde os objetos selecionados são combinados em uma máscara. Se nenhum objeto for selecionado ou não houver dados de rastreamento, retorna uma máscara zero. |
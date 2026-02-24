> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/pt-BR.md)

O nó WanMoveConcatTrack combina dois conjuntos de dados de rastreamento de movimento em uma única sequência mais longa. Ele funciona unindo os caminhos de rastreamento e as máscaras de visibilidade dos rastreamentos de entrada ao longo de suas respectivas dimensões. Se apenas uma entrada de rastreamento for fornecida, ele simplesmente repassa esses dados sem alterações.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `tracks_1` | TRACKS | Sim | | O primeiro conjunto de dados de rastreamento de movimento a ser concatenado. |
| `tracks_2` | TRACKS | Não | | Um segundo conjunto opcional de dados de rastreamento de movimento. Se não for fornecido, `tracks_1` é repassado diretamente para a saída. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `tracks` | TRACKS | Os dados de rastreamento de movimento concatenados, contendo o `track_path` e o `track_visibility` combinados das entradas. |

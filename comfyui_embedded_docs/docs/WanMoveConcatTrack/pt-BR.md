# WanMoveConcatTrack

O nó WanMoveConcatTrack combina dois conjuntos de dados de rastreamento de movimento em uma única sequência mais longa. Ele funciona unindo os caminhos de rastreamento e as máscaras de visibilidade dos rastreamentos de entrada ao longo de suas respectivas dimensões. Se apenas uma entrada de rastreamento for fornecida, ele simplesmente repassa esses dados sem alterações.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tracks_1` | O primeiro conjunto de dados de rastreamento de movimento a ser concatenado. | TRACKS | Sim |  |
| `tracks_2` | Um segundo conjunto opcional de dados de rastreamento de movimento. Se não for fornecido, `tracks_1` é passado diretamente para a saída. | TRACKS | Não |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `tracks` | Os dados de rastreamento de movimento concatenados, contendo o `track_path` e o `track_visibility` combinados das entradas. | TRACKS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`

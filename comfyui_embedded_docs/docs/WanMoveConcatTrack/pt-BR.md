# WanMoveConcatTrack

O nó WanMoveConcatTrack combina dois conjuntos de dados de rastreamento de movimento em uma única sequência mais longa. Ele funciona unindo os caminhos de rastreamento e as máscaras de visibilidade das faixas de entrada ao longo de suas respectivas dimensões. Se apenas uma faixa de entrada for fornecida, ele simplesmente repassa esses dados sem alterações.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `tracks_1` | O primeiro conjunto de dados de rastreamento de movimento a ser concatenado. | TRACKS | Sim |  |
| `tracks_2` | Um segundo conjunto opcional de dados de rastreamento de movimento. Se não for fornecido, `tracks_1` é passado diretamente para a saída. | TRACKS | Não |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `tracks` | Os dados de rastreamento de movimento concatenados, contendo o `track_path` e o `track_visibility` combinados das entradas. | TRACKS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d9b4c00291c6fa8e17bf54ecdcd16f7f6874159fe8cebebe66568dc2a744868f`

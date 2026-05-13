> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/pt-BR.md)

O nó WanMoveConcatTrack combina dois conjuntos de dados de rastreamento de movimento em uma única sequência mais longa. Ele funciona unindo os caminhos de rastreamento e as máscaras de visibilidade das faixas de entrada ao longo de suas respectivas dimensões. Se apenas uma faixa de entrada for fornecida, ele simplesmente repassa esses dados sem alterações.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `tracks_1` | TRACKS | Sim | | O primeiro conjunto de dados de rastreamento de movimento a ser concatenado. |
| `tracks_2` | TRACKS | Não | | Um segundo conjunto opcional de dados de rastreamento de movimento. Se não for fornecido, `tracks_1` é passado diretamente para a saída. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `tracks` | TRACKS | Os dados de rastreamento de movimento concatenados, contendo o `track_path` e o `track_visibility` combinados das entradas. |

---
**Source fingerprint (SHA-256):** `d9b4c00291c6fa8e17bf54ecdcd16f7f6874159fe8cebebe66568dc2a744868f`

# Dividir Imagem em Lista de Blocos

O nó Dividir Imagem em Lista de Blocos divide uma única imagem de entrada em uma série de seções retangulares menores e sobrepostas, chamadas blocos. Ele cria uma lista em lote desses blocos, que podem ser processados individualmente por outros nós. O tamanho de cada bloco e a quantidade de sobreposição entre eles podem ser especificados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada a ser dividida em blocos. | IMAGE | Sim | - |
| `tile_width` | A largura de cada bloco de saída em pixels (padrão: 1024). | INT | Sim | 64 a 1048576 |
| `tile_height` | A altura de cada bloco de saída em pixels (padrão: 1024). | INT | Sim | 64 a 1048576 |
| `overlap` | O número de pixels que blocos adjacentes irão sobrepor (padrão: 128). | INT | Sim | 0 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | Uma lista em lote contendo todos os blocos de imagem individuais. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/pt-BR.md)

---
**Source fingerprint (SHA-256):** `26991a325b7b9358cd7338348e93c57695b1ed1aa1983962794f889c94c34547`

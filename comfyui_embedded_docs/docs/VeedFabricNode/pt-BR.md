# VEED Fabric 1.0

Transforme uma imagem estática e uma faixa de fala em um vídeo falado com sincronia labial usando o VEED Fabric. Funciona com fotos, ilustrações e mascotes, desde que o rosto esteja claramente visível; o vídeo mantém a proporção de aspecto da imagem e tem a mesma duração do áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a usar. Selecionar um modelo revela os parâmetros específicos dele: `image`, `audio` e `resolution`. | DYNAMIC_COMBO | Sim | `"fabric-1.0"` |
| `image` | Imagem com um rosto claramente visível. O vídeo mantém a proporção de aspecto da imagem. | IMAGE | Sim | - |
| `audio` | Fala para sincronia labial, com até 300 segundos. Define a duração do vídeo. | AUDIO | Sim | Até 300 segundos |
| `resolution` | Classe de tamanho da saída: cerca de 0,4 megapixels em `"480p"` (864x480 em 16:9) e 0,9 megapixels em `"720p"` (1312x736 em 16:9). (padrão: `"720p"`) | COMBO | Sim | `"480p"`<br>`"720p"` |

O nó para com um erro quando a faixa de fala tem mais de 300 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `VIDEO` | O vídeo com fala: a imagem de entrada animada para corresponder à faixa de fala. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedFabricNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `69cabfa5f03885ce770e8502419305dacee49d7e89a748f31abe3775d682a33a`

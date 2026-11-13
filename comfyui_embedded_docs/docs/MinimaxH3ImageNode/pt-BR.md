# MiniMax H3 Image

Gera imagens a partir de texto com o MiniMax H3 Image, ou edita e combina até 16 imagens de referência. O prompt refere-se às referências pela ordem de conexão: `@Image1`, `@Image2` e assim por diante.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Range |
| --- | --- | --- | --- | --- |
| `model` | `MiniMax-H3-Image` ou `MiniMax-H3-Image-Highspeed` para execuções mais rápidas. Padrão: `"MiniMax-H3-Image"`. | COMBO | Sim | `"MiniMax-H3-Image"`<br>`"MiniMax-H3-Image-Highspeed"` |
| `prompt` | O que gerar, ou como editar as referências. Com imagens de referência conectadas, pode ter no máximo 8.000 caracteres. Padrão: vazio. | STRING | Sim | 1 a 8000 caracteres |
| `size` | `2K` e `4K` derivam o tamanho a partir de uma proporção de aspecto; `custom` define largura e altura exatas. Padrão: `"2K"`. | DYNAMIC_COMBO | Sim | `"2K"`<br>`"4K"`<br>`"custom"` |
| `enhance_prompt` | O MiniMax reescreve o prompt em uma descrição de cena detalhada antes de gerar. Edições de imagem são sempre aprimoradas. Quando desativado, escolha uma proporção de aspecto fixa ou um tamanho personalizado. Padrão: true. | BOOLEAN | Não | true<br>false |
| `seed` | Controla se o nó é executado novamente; os resultados não são determinísticos independentemente da seed. Padrão: 42. | INT | Não | 0 a 2147483647 |
| `images` | Imagens de referência para editar ou combinar, referenciadas no prompt como `@Image1` a `@Image16` na ordem de conexão. | AUTOGROW | Não | Até 16 imagens |

### Entradas de tamanho "2K" e "4K"

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Range |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Com `auto`, o MiniMax escolhe a proporção a partir do prompt, ou segue a imagem de referência quando uma está conectada. Texto para imagem com `enhance_prompt` desativado precisa de uma proporção fixa. Padrão: `"auto"`. | COMBO | Sim | Várias opções disponíveis |

### Entradas de tamanho "custom"

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Range |
| --- | --- | --- | --- | --- |
| `width` | Largura de saída em pixels. Padrão: 2048. | INT | Sim | 512 a 7680 (passo 16) |
| `height` | Altura de saída em pixels. Padrão: 2048. | INT | Sim | 512 a 7680 (passo 16) |

Observação: Para um tamanho personalizado, a largura multiplicada pela altura deve estar entre 655.360 e 20.000.000 pixels, com uma proporção de aspecto de no máximo 3:1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem gerada ou editada, como PNG. | IMAGE |
| `revised_prompt` | O prompt reescrito que o MiniMax usou, quando o aprimoramento de prompt estava ativado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxH3ImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `723eb4c2d3b303ece041f98bd5b773c669affb9a7b3da0c08ffcac4ee89f8e11`

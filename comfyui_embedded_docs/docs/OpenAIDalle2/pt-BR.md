# OpenAI DALL·E 2

Gera imagens de forma síncrona por meio do endpoint DALL·E 2 da OpenAI.

## Como Funciona

Este nó se conecta à API DALL·E 2 da OpenAI para criar imagens baseadas em descrições textuais. Quando você fornece um prompt de texto, o nó o envia aos servidores da OpenAI, que geram as imagens correspondentes e as retornam ao ComfyUI. O nó pode operar em dois modos: geração padrão de imagens usando apenas um prompt de texto, ou modo de edição de imagens quando tanto uma imagem quanto uma máscara são fornecidas. No modo de edição, ele usa a máscara para determinar quais partes da imagem original devem ser modificadas, mantendo as outras áreas inalteradas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto para o DALL·E | STRING | obrigatória | "" | - |
| `seed` | ainda não implementado no backend | INT | opcional | 0 | 0 a 2147483647 |
| `size` | Tamanho da imagem | COMBO | opcional | "1024x1024" | "256x256", "512x512", "1024x1024" |
| `n` | Quantas imagens gerar | INT | opcional | 1 | 1 a 8 |
| `image` | Imagem de referência opcional para edição de imagem | IMAGE | opcional | None | - |
| `mask` | Máscara opcional para inpainting (áreas brancas serão substituídas) | MASK | opcional | None | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A(s) imagem(ns) gerada(s) ou editada(s) pelo DALL·E 2 | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ad10b149ac28559ad18c09e0f071286509680603d953833106ad6a2d578f7efe`

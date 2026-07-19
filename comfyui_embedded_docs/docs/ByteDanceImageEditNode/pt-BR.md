# ByteDanceImageEditNode

O nó ByteDance Image Edit permite modificar imagens usando os modelos de IA da ByteDance por meio de uma API. Você fornece uma imagem de entrada e um prompt de texto descrevendo as alterações desejadas, e o nó processa a imagem de acordo com suas instruções. O nó gerencia a comunicação com a API automaticamente e retorna a imagem editada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `model` | Nome do modelo | MODEL | COMBO | seededit_3 | Opções Image2ImageModelName |
| `image` | A imagem base para editar | IMAGE | IMAGE | - | - |
| `prompt` | Instrução para editar a imagem | STRING | STRING | "" | - |
| `seed` | Semente a ser usada para geração | INT | INT | 0 | 0-2147483647 |
| `guidance_scale` | Valor mais alto faz a imagem seguir o prompt mais fielmente | FLOAT | FLOAT | 5.5 | 1.0-10.0 |
| `watermark` | Se deve adicionar uma marca d'água "gerado por IA" à imagem | BOOLEAN | BOOLEAN | True | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A imagem editada retornada pela API da ByteDance | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`

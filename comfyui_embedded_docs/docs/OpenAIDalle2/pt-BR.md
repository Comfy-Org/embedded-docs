# OpenAIDalle2

Gera imagens de forma síncrona por meio do endpoint DALL·E 2 da OpenAI. O nó envia um prompt de texto para a API DALL·E 2 da OpenAI e retorna a(s) imagem(ns) resultante(s) para o ComfyUI. Ele também pode editar uma imagem existente quando um `image` e uma `mask` são fornecidos em conjunto.

## Como funciona

Este nó se conecta à API DALL·E 2 da OpenAI para criar imagens com base em descrições de texto. Ao fornecer um prompt de texto, o nó o envia aos servidores da OpenAI, que geram as imagens correspondentes e as retornam ao ComfyUI. O nó pode operar em dois modos: geração padrão de imagens usando apenas um prompt de texto, ou modo de edição de imagem quando tanto uma imagem quanto uma máscara são fornecidas. No modo de edição, ele usa a máscara para determinar quais partes da imagem original devem ser modificadas, mantendo as demais áreas inalteradas.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto para o DALL·E (padrão: vazio) | STRING | Sim | - |
| `seed` | ainda não implementado no backend (padrão: 0) | INT | Não | 0 a 2147483647 |
| `size` | Tamanho da imagem (padrão: "1024x1024") | COMBO | Não | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Quantas imagens gerar (padrão: 1) | INT | Não | 1 a 8 |
| `image` | Imagem de referência opcional para edição de imagem. | IMAGE | Não | - |
| `mask` | Máscara opcional para inpainting (áreas brancas serão substituídas) | MASK | Não | - |

**Observação:** O modo de edição de imagem é ativado somente quando `image` e `mask` são fornecidos em conjunto. Se apenas um deles for fornecido, um erro será gerado. A `mask` deve ter o mesmo tamanho da `image`; caso contrário, um erro será gerado. No modo de edição, as áreas brancas da máscara indicam as regiões que serão substituídas.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `IMAGE` | A(s) imagem(ns) gerada(s) ou editada(s) pelo DALL·E 2 | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`

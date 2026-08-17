# OpenAI DALL·E 2

OpenAI DALL·E 2 gera imagens de forma síncrona por meio do endpoint DALL·E 2 da OpenAI. Forneça um prompt de texto para criar novas imagens, ou forneça uma imagem e uma máscara para editar uma imagem existente.

## Como Funciona

Este nó conecta-se à API DALL·E 2 da OpenAI para criar imagens com base em descrições de texto. Quando você fornece um prompt de texto, o nó o envia aos servidores da OpenAI, que geram as imagens correspondentes e as retornam ao ComfyUI. O nó pode operar em dois modos: geração padrão de imagens usando apenas um prompt de texto, ou modo de edição de imagens quando uma imagem e uma máscara são fornecidas. No modo de edição, ele usa a máscara para determinar quais partes da imagem original devem ser modificadas, mantendo as outras áreas inalteradas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para o DALL·E (padrão: vazio) | STRING | Sim | - |
| `seed` | ainda não implementado no backend (padrão: 0) | INT | Não | 0 to 2147483647 |
| `size` | Tamanho da imagem (padrão: "1024x1024") | COMBO | Não | "256x256"<br>"512x512"<br>"1024x1024" |
| `n` | Quantas imagens gerar (padrão: 1) | INT | Não | 1 to 8 |
| `image` | Imagem de referência opcional para edição de imagens. | IMAGE | Não | - |
| `mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas) | MASK | Não | - |

Nota: `image` e `mask` devem ser fornecidos juntos. Quando ambos são fornecidos, o nó alterna para o modo de edição de imagens. Se apenas um deles for fornecido, um erro será gerado. A `mask` deve ter o mesmo tamanho que a `image`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `IMAGE` | A(s) imagem(ns) gerada(s) ou editada(s) pelo DALL·E 2 | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`

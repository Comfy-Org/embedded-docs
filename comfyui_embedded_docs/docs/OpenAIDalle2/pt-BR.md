> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/pt-BR.md)

Gera imagens de forma síncrona através do endpoint DALL·E 2 da OpenAI.

## Como Funciona

Este nó se conecta à API DALL·E 2 da OpenAI para criar imagens com base em descrições textuais. Quando você fornece um prompt de texto, o nó o envia para os servidores da OpenAI, que geram as imagens correspondentes e as retornam para o ComfyUI. O nó pode operar em dois modos: geração padrão de imagens usando apenas um prompt de texto, ou modo de edição de imagem quando tanto uma imagem quanto uma máscara são fornecidas. No modo de edição, ele usa a máscara para determinar quais partes da imagem original devem ser modificadas, mantendo as outras áreas inalteradas.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Range | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `prompt` | STRING | obrigatório | "" | - | Prompt de texto para o DALL·E |
| `seed` | INT | opcional | 0 | 0 a 2147483647 | ainda não implementado no backend |
| `size` | COMBO | opcional | "1024x1024" | "256x256", "512x512", "1024x1024" | Tamanho da imagem |
| `n` | INT | opcional | 1 | 1 a 8 | Quantas imagens gerar |
| `image` | IMAGE | opcional | None | - | Imagem de referência opcional para edição de imagem. |
| `mask` | MASK | opcional | None | - | Máscara opcional para inpainting (as áreas em branco serão substituídas) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | A(s) imagem(ns) gerada(s) ou editada(s) pelo DALL·E 2 |

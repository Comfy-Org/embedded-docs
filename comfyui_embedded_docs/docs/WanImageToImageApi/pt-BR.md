> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/pt-BR.md)

O nó Wan Image to Image gera uma imagem a partir de uma ou duas imagens de entrada e um prompt de texto. Ele transforma suas imagens de entrada com base na descrição fornecida, criando uma nova imagem que mantém a proporção de aspecto da sua entrada original. A imagem de saída tem uma resolução fixa de 1,6 megapixels, independentemente do tamanho da entrada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Range | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | "wan2.5-i2i-preview" | Modelo a ser utilizado (padrão: "wan2.5-i2i-preview"). |
| `image` | IMAGE | Sim | - | Edição de imagem única ou fusão de múltiplas imagens, máximo de 2 imagens. |
| `prompt` | STRING | Sim | - | Prompt usado para descrever os elementos e características visuais, suporta inglês/chinês (padrão: vazio). |
| `negative_prompt` | STRING | Não | - | Prompt de texto negativo para orientar o que evitar (padrão: vazio). |
| `seed` | INT | Não | 0 a 2147483647 | Semente a ser usada para a geração (padrão: 0). |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água "AI generated" ao resultado (padrão: true). |

**Observação:** Este nó aceita exatamente 1 ou 2 imagens de entrada. Se você fornecer mais de 2 imagens ou nenhuma imagem, o nó retornará um erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem gerada com base nas imagens de entrada e prompts de texto. |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/pt-BR.md)

O nó Wan Image to Image gera uma imagem a partir de uma ou duas imagens de entrada e um prompt de texto. Ele transforma suas imagens de entrada com base na descrição fornecida, criando uma nova imagem que mantém a proporção da sua entrada original. A imagem de saída é fixada em 1,6 megapixels, independentemente do tamanho da entrada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | COMBO | Sim | "wan2.5-i2i-preview" | Modelo a ser usado (padrão: "wan2.5-i2i-preview"). |
| `imagem` | IMAGE | Sim | - | Edição de imagem única ou fusão de múltiplas imagens, máximo de 2 imagens. |
| `prompt` | STRING | Sim | - | Prompt descrevendo os elementos e características visuais. Suporta inglês e chinês (padrão: vazio). |
| `prompt negativo` | STRING | Não | - | Prompt negativo descrevendo o que evitar (padrão: vazio). |
| `semente` | INT | Não | 0 a 2147483647 | Semente a ser usada para geração (padrão: 0). |
| `marca d'água` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: falso). |

**Observação:** Este nó aceita exatamente 1 ou 2 imagens de entrada. Se você fornecer mais de 2 imagens ou nenhuma imagem, o nó retornará um erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `imagem` | IMAGE | A imagem gerada com base nas imagens de entrada e prompts de texto. |

---
**Source fingerprint (SHA-256):** `d69811ddaba718e5468f539fb9b25827efdf79f3ee9cbf31ad8f9387cea9b9be`

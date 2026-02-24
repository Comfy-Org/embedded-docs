> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/pt-BR.md)

O nó Wan Text to Image gera imagens com base em descrições textuais. Ele utiliza modelos de IA para criar conteúdo visual a partir de prompts escritos, suportando entrada de texto em inglês e chinês. O nó oferece vários controles para ajustar o tamanho, a qualidade e as preferências de estilo da imagem de saída.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | "wan2.5-t2i-preview" | Modelo a ser utilizado (padrão: "wan2.5-t2i-preview") |
| `prompt` | STRING | Sim | - | Prompt usado para descrever os elementos e características visuais, suporta inglês/chinês (padrão: vazio) |
| `negative_prompt` | STRING | Não | - | Prompt de texto negativo para orientar o que evitar (padrão: vazio) |
| `width` | INT | Não | 768-1440 | Largura da imagem em pixels (padrão: 1024, incremento: 32) |
| `height` | INT | Não | 768-1440 | Altura da imagem em pixels (padrão: 1024, incremento: 32) |
| `seed` | INT | Não | 0-2147483647 | Semente a ser usada para a geração (padrão: 0) |
| `prompt_extend` | BOOLEAN | Não | - | Se deve aprimorar o prompt com assistência de IA (padrão: Verdadeiro) |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água "Gerado por IA" ao resultado (padrão: Verdadeiro) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A imagem gerada com base no prompt de texto |

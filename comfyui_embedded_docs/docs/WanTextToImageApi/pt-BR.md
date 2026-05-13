> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/pt-BR.md)

O nó Wan Text to Image gera imagens com base em descrições textuais. Ele utiliza modelos de IA para criar conteúdo visual a partir de instruções escritas, suportando entrada de texto em inglês e chinês. O nó oferece vários controles para ajustar o tamanho, a qualidade e as preferências de estilo da imagem de saída.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | "wan2.5-t2i-preview" | Modelo a ser utilizado (padrão: "wan2.5-t2i-preview") |
| `prompt` | STRING | Sim | - | Instrução descrevendo os elementos e características visuais. Suporta inglês e chinês (padrão: vazio) |
| `negative_prompt` | STRING | Não | - | Instrução negativa descrevendo o que deve ser evitado (padrão: vazio) |
| `width` | INT | Não | 768-1440 | Largura da imagem em pixels (padrão: 1024, passo: 32) |
| `height` | INT | Não | 768-1440 | Altura da imagem em pixels (padrão: 1024, passo: 32) |
| `seed` | INT | Não | 0-2147483647 | Semente a ser usada para a geração (padrão: 0) |
| `prompt_extend` | BOOLEAN | Não | - | Se deve aprimorar a instrução com assistência de IA (padrão: Verdadeiro) |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: Falso) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A imagem gerada com base na instrução de texto |

---
**Source fingerprint (SHA-256):** `2a59551d7ff0fc0553f41561afd94092d2d950ac3e1aa3f6402436540da7d6fb`

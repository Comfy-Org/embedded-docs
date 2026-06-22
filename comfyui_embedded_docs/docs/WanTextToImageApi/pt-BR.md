# Wan Texto para Imagem

O nó Wan Text to Image gera imagens com base em descrições textuais. Ele utiliza modelos de IA para criar conteúdo visual a partir de instruções escritas, suportando entrada de texto em inglês e chinês. O nó oferece vários controles para ajustar o tamanho, a qualidade e as preferências de estilo da imagem de saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | Modelo a ser utilizado (padrão: "wan2.5-t2i-preview") | COMBO | Sim | "wan2.5-t2i-preview" |
| `prompt` | Instrução descrevendo os elementos e características visuais. Suporta inglês e chinês (padrão: vazio) | STRING | Sim | - |
| `prompt_negativo` | Instrução negativa descrevendo o que deve ser evitado (padrão: vazio) | STRING | Não | - |
| `largura` | Largura da imagem em pixels (padrão: 1024, passo: 32) | INT | Não | 768-1440 |
| `altura` | Altura da imagem em pixels (padrão: 1024, passo: 32) | INT | Não | 768-1440 |
| `semente` | Semente a ser usada para a geração (padrão: 0) | INT | Não | 0-2147483647 |
| `estender_prompt` | Se deve aprimorar a instrução com assistência de IA (padrão: Verdadeiro) | BOOLEAN | Não | - |
| `marca_d'água` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: Falso) | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A imagem gerada com base na instrução de texto | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2a59551d7ff0fc0553f41561afd94092d2d950ac3e1aa3f6402436540da7d6fb`

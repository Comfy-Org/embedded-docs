# Wan Texto para Imagem

O nó Wan Text to Image gera imagens com base em descrições de texto. Ele usa modelos de IA para criar conteúdo visual a partir de prompts escritos, com suporte a entrada de texto em inglês e chinês. O nó oferece vários controles para ajustar o tamanho, a qualidade e as preferências de estilo da imagem de saída.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a usar (padrão: "wan2.5-t2i-preview") | STRING | Sim | "wan2.5-t2i-preview" |
| `prompt` | Prompt que descreve os elementos e as características visuais. Suporta inglês e chinês (padrão: vazio) | STRING | Sim | - |
| `prompt_negativo` | Prompt negativo que descreve o que evitar (padrão: vazio) | STRING | Não | - |
| `largura` | Largura da imagem em pixels (padrão: 1024, passo: 32) | INT | Não | 768-1440 |
| `altura` | Altura da imagem em pixels (padrão: 1024, passo: 32) | INT | Não | 768-1440 |
| `semente` | Semente a usar para geração (padrão: 0) | INT | Não | 0-2147483647 |
| `estender_prompt` | Se deve aprimorar o prompt com assistência de IA (padrão: True) | BOOLEAN | Não | - |
| `marca_d'água` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False) | BOOLEAN | Não | - |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `output` | A imagem gerada com base no prompt de texto | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `208b7c839da45316aeb1a14a3e9d176eeb09b2f931f764fb8a296da15ae3bd4e`

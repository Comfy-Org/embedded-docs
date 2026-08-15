# Wan 2.7 Continuação de Vídeo

O nó Wan 2.7 Video Continuation gera um novo segmento de vídeo que continua a partir do final de um clipe de vídeo de entrada. Ele usa o modelo Wan 2.7 para sintetizar a continuação com base em um prompt de texto e pode, opcionalmente, orientar o final em direção a um quadro-alvo específico.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo de geração de vídeo a ser usado. | DYNAMIC_COMBO | Sim | `"wan2.7-i2v"` |
| `primeiro_clip` | Vídeo de entrada a partir do qual continuar. Duração: 2s–10s. A proporção de aspecto da saída é derivada deste vídeo. | VIDEO | Sim | 2 a 10 s |
| `último_quadro` | Imagem do último quadro. A continuação fará a transição em direção a este quadro. | IMAGE | Não | - |
| `semente` | Semente a ser usada para geração. (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `estender_prompt` | Se deve aprimorar o prompt com assistência de IA. (padrão: True) | BOOLEAN | Sim | - |
| `marca_d'água` | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: False) | BOOLEAN | Sim | - |

### Entradas wan2.7-i2v

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt que descreve os elementos e recursos visuais. Suporta inglês e chinês. (padrão: string vazia) | STRING | Sim | - |
| `prompt_negativo` | Prompt negativo que descreve o que evitar. (padrão: string vazia) | STRING | Sim | - |
| `resolução` | A resolução para o vídeo de saída. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `duração` | Duração total da saída em segundos. O modelo gera continuação para preencher o tempo restante após o clipe de entrada. (padrão: 5) | INT | Sim | 2 a 15 |

**Nota:** O vídeo de entrada `first_clip` deve ter entre 2 e 10 segundos de duração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A continuação do vídeo gerada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `591e551676969bc1fedb5f820f6866512c132bb98ee8ef1766d1e0b389e2dc11`

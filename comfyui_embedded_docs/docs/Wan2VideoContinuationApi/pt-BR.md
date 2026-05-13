> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/pt-BR.md)

Aqui está a tradução da documentação para português brasileiro, seguindo todas as regras estabelecidas:

O nó Wan 2.7 Video Continuation gera um novo segmento de vídeo que continua perfeitamente a partir do final de um clipe de vídeo de entrada. Ele utiliza o modelo Wan 2.7 para sintetizar a continuação com base em um prompt de texto e pode, opcionalmente, guiar o final em direção a um quadro alvo específico.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | Sim | `"wan2.7-i2v"` | O modelo de geração de vídeo a ser usado. |
| `model.prompt` | STRING | Sim | - | Prompt descrevendo os elementos e características visuais. Suporta inglês e chinês. (padrão: string vazia) |
| `model.negative_prompt` | STRING | Sim | - | Prompt negativo descrevendo o que evitar. (padrão: string vazia) |
| `model.resolution` | COMBO | Sim | `"720P"`<br>`"1080P"` | A resolução do vídeo de saída. |
| `model.duration` | INT | Sim | 2 a 15 | Duração total da saída em segundos. O modelo gera a continuação para preencher o tempo restante após o clipe de entrada. (padrão: 5) |
| `first_clip` | VIDEO | Sim | - | Vídeo de entrada a ser continuado. Duração: 2s-10s. A proporção de aspecto da saída é derivada deste vídeo. |
| `last_frame` | IMAGE | Não | - | Imagem do último quadro. A continuação fará a transição em direção a este quadro. |
| `seed` | INT | Sim | 0 a 2147483647 | Semente a ser usada para a geração. (padrão: 0) |
| `prompt_extend` | BOOLEAN | Sim | - | Se deve aprimorar o prompt com assistência de IA. (padrão: True) |
| `watermark` | BOOLEAN | Sim | - | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: False) |

**Nota:** O vídeo de entrada `first_clip` deve ter duração entre 2 e 10 segundos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
| :--- | :--- | :--- |
| `output` | VIDEO | A continuação do vídeo gerada. |

---
**Source fingerprint (SHA-256):** `5e9d2c7800603660f5f994d125e1e32f2b310234c4b6a24d502c764d91be49e8`

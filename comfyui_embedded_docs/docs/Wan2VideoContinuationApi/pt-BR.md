Aqui está a tradução da documentação para português brasileiro, seguindo todas as regras estabelecidas:

O nó Wan 2.7 Video Continuation gera um novo segmento de vídeo que continua perfeitamente a partir do final de um clipe de vídeo de entrada. Ele utiliza o modelo Wan 2.7 para sintetizar a continuação com base em um prompt de texto e pode, opcionalmente, guiar o final em direção a um quadro alvo específico.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de geração de vídeo a ser usado. | COMBO | Sim | `"wan2.7-i2v"` |
| `model.prompt` | Prompt descrevendo os elementos e características visuais. Suporta inglês e chinês. (padrão: string vazia) | STRING | Sim | - |
| `model.negative_prompt` | Prompt negativo descrevendo o que evitar. (padrão: string vazia) | STRING | Sim | - |
| `model.resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `model.duration` | Duração total da saída em segundos. O modelo gera a continuação para preencher o tempo restante após o clipe de entrada. (padrão: 5) | INT | Sim | 2 a 15 |
| `primeiro_clip` | Vídeo de entrada a ser continuado. Duração: 2s-10s. A proporção de aspecto da saída é derivada deste vídeo. | VIDEO | Sim | - |
| `último_quadro` | Imagem do último quadro. A continuação fará a transição em direção a este quadro. | IMAGE | Não | - |
| `semente` | Semente a ser usada para a geração. (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `estender_prompt` | Se deve aprimorar o prompt com assistência de IA. (padrão: True) | BOOLEAN | Sim | - |
| `marca_d'água` | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: False) | BOOLEAN | Sim | - |

**Nota:** O vídeo de entrada `first_clip` deve ter duração entre 2 e 10 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A continuação do vídeo gerada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5e9d2c7800603660f5f994d125e1e32f2b310234c4b6a24d502c764d91be49e8`

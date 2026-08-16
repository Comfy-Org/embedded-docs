# Wan 2.7 Imagem para Vídeo

O nó Wan 2.7 Image to Video gera um vídeo a partir de uma imagem de primeiro quadro. Opcionalmente, você pode fornecer uma imagem de último quadro para criar uma transição entre os dois, ou fornecer um arquivo de áudio para orientar o movimento e o ritmo do vídeo. O nó usa um modelo de IA para animar a cena com base na sua descrição em texto.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de IA usado para a geração de vídeo. | DYNAMIC_COMBO | Sim | `"wan2.7-i2v"` |
| `first_frame` | Imagem do primeiro quadro. A proporção de aspecto da saída é derivada desta imagem. | IMAGE | Sim | - |
| `last_frame` | Imagem do último quadro. O modelo gera um vídeo com transição do primeiro para o último quadro. | IMAGE | Não | - |
| `audio` | Áudio para orientar a geração de vídeo (ex.: sincronização labial, movimento sincronizado com batida). Duração: 2s-30s. Se não for fornecido, o modelo gera automaticamente música de fundo ou efeitos sonoros correspondentes. | AUDIO | Não | - |
| `seed` | Semente a ser usada para a geração (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA (padrão: True). Esta é uma configuração avançada. | BOOLEAN | Sim | True<br>False |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False). Esta é uma configuração avançada. | BOOLEAN | Sim | True<br>False |

### Entradas do wan2.7-i2v

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt que descreve os elementos e as características visuais. Suporta inglês e chinês. | STRING | Sim | - |
| `negative_prompt` | Prompt negativo que descreve o que evitar. | STRING | Sim | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `duration` | A duração do vídeo gerado em segundos (padrão: 5). | INT | Sim | 2 a 15 |

**Nota:** A entrada `audio` tem uma restrição de duração. Se fornecida, o arquivo de áudio deve ter entre 2 e 30 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`

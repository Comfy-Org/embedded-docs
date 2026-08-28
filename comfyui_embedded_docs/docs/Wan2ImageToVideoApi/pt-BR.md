# Wan 2.7 Imagem para Vídeo

The Wan 2.7 Image to Video node generates a video starting from a first-frame image. You can optionally provide a last-frame image to create a transition between the two, or provide an audio file to guide the video's motion and timing. The node uses an AI model to animate the scene based on your text description.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de IA a ser usado para geração de vídeo. | DYNAMIC_COMBO | Sim | `"wan2.7-i2v"` |
| `first_frame` | Imagem do primeiro quadro. A proporção de aspecto da saída é derivada desta imagem. | IMAGE | Sim | - |
| `last_frame` | Imagem do último quadro. O modelo gera um vídeo com transição do primeiro para o último quadro. | IMAGE | Não | - |
| `audio` | Áudio para orientar a geração do vídeo (ex.: sincronização labial, movimento sincronizado com o ritmo). Duração: 2s a 30s. Se não for fornecido, o modelo gera automaticamente música de fundo ou efeitos sonoros correspondentes. | AUDIO | Não | - |
| `seed` | Semente a ser usada para geração (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA (padrão: True). Esta é uma configuração avançada. | BOOLEAN | Sim | True<br>False |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False). Esta é uma configuração avançada. | BOOLEAN | Sim | True<br>False |

### Entradas do wan2.7-i2v

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt descrevendo os elementos e características visuais. Suporta inglês e chinês. (padrão: vazio) | STRING | Sim | - |
| `negative_prompt` | Prompt negativo descrevendo o que evitar. (padrão: vazio) | STRING | Sim | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `duration` | A duração do vídeo gerado em segundos (padrão: 5). | INT | Sim | 2 a 15 |

**Nota:** A entrada `audio` tem uma restrição de duração. Se fornecida, o arquivo de áudio deve ter entre 2 e 30 segundos de duração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`

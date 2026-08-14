# Wan 2.7 Texto para Vídeo

Este nó gera um vídeo a partir de uma descrição de texto usando o modelo Wan 2.7. Ele envia sua solicitação para uma API externa, que processa o prompt e retorna um arquivo de vídeo. Opcionalmente, você pode fornecer um clipe de áudio para influenciar o movimento e a sincronização do vídeo.

## Entradas

As entradas incluem configurações comuns e configurações específicas do modelo que aparecem quando o modelo `wan2.7-t2v` está selecionado.

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `model` | O modelo específico a ser usado para geração de vídeo. | COMBO | Sim | `"wan2.7-t2v"` |
| `audio` | Áudio para orientar a geração de vídeo (ex.: sincronização labial, movimento sincronizado com batida). Duração: 1.5s-60s. Se não for fornecido, o modelo gera automaticamente música de fundo ou efeitos sonoros correspondentes. | AUDIO | Não | - |
| `seed` | Semente a ser usada para a geração (padrão: 0). | INT | Não | 0 a 2147483647 |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA (padrão: True). | BOOLEAN | Não True / False |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False). | BOOLEAN | Não True / False |

### Entradas do wan2.7-t2v

Essas configurações aparecem quando o modelo `wan2.7-t2v` está selecionado.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `prompt` | Prompt que descreve os elementos e as características visuais. Suporta inglês e chinês. | STRING | Sim | - |
| `negative_prompt` | Prompt negativo que descreve o que deve ser evitado. | STRING | Não | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `ratio` | A proporção do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | A duração do vídeo em segundos (padrão: 5). | INT | Sim | 2 a 15 |

**Nota:** A entrada `prompt` não pode ser vazia. A entrada `audio` é opcional; se for fornecida, sua duração deve estar entre 1,5 e 60 segundos. Se for omitida, o modelo gera automaticamente o áudio correspondente. Quando `negative_prompt` é deixado vazio, ele não é enviado à API. `prompt_extend` e `watermark` são opções avançadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`

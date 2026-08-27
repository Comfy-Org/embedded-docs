# Wan 2.7 Texto para Vídeo

Este nó gera um vídeo a partir de uma descrição em texto usando o modelo Wan 2.7. Ele envia seu prompt para a API de geração de vídeo do Wan, aguarda a conclusão da tarefa e retorna o vídeo resultante. Opcionalmente, você pode conectar um clipe de áudio para influenciar o movimento e o ritmo do vídeo; se nenhum áudio for fornecido, o modelo gera automaticamente um áudio correspondente.

## Entradas

### Entradas comuns

Estas entradas estão sempre disponíveis no nível superior do nó.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo específico a ser usado para geração de vídeo. | DYNAMIC_COMBO | Sim | `"wan2.7-t2v"` |
| `áudio` | Áudio para conduzir a geração de vídeo (ex.: sincronização labial, movimento em sincronia com a batida). Duração: 3s-30s. Se não for fornecido, o modelo gera automaticamente música de fundo ou efeitos sonoros correspondentes. | AUDIO | Não | - |
| `semente` | Semente a ser usada para geração (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `estender_prompt` | Se deve aprimorar o prompt com assistência de IA (padrão: True). | BOOLEAN | Sim | True<br>False |
| `marca_d'água` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False). | BOOLEAN | Sim | True<br>False |

### Entradas do wan2.7-t2v

Estas configurações aparecem quando o modelo `wan2.7-t2v` está selecionado.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt que descreve os elementos e as características visuais. Suporta inglês e chinês. | STRING | Sim | - |
| `negative_prompt` | Prompt negativo que descreve o que evitar. O padrão é uma string vazia. | STRING | Não | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | A duração do vídeo em segundos (padrão: 5). | INT | Sim | 2 a 15 |

**Nota:** A entrada `prompt` não deve estar vazia. A entrada `audio` é opcional; se for fornecida, o nó aceita áudio entre 1,5 e 60 segundos, embora a dica de ferramenta recomende 3s-30s. Se nenhum áudio for fornecido, o modelo gera automaticamente um áudio correspondente. Quando `negative_prompt` é deixado vazio, ele não é enviado à API. `prompt_extend` e `watermark` são opções avançadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`

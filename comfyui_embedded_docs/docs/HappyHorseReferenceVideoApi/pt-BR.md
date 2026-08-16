# HappyHorse Referência para Vídeo

Este nó gera um vídeo com uma pessoa ou objeto a partir de imagens de referência usando o modelo HappyHorse. Ele suporta performances de personagem único e interações com múltiplos personagens. As imagens de referência são enviadas e usadas para representar os personagens no vídeo gerado.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo HappyHorse de referência para vídeo a ser usado na geração. | DYNAMIC_COMBO | Sim | `"happyhorse-1.1-r2v"`<br>`"happyhorse-1.0-r2v"` |
| `seed` | Semente a ser usada para a geração (padrão: 0). Pode ser configurada para alterar automaticamente após cada geração. | INT | Sim | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False). | BOOLEAN | Sim | True ou False |

### Entradas do HappyHorse 1.1 (happyhorse-1.1-r2v)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt descrevendo o vídeo. Use identificadores como 'character1' e 'character2' para se referir aos personagens de referência. | STRING | Sim | N/A |
| `resolution` | A resolução do vídeo gerado. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `ratio` | A proporção do vídeo gerado. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"`<br>`"5:4"`<br>`"4:5"` |
| `duration` | A duração do vídeo gerado em segundos (padrão: 5). | INT | Sim | 3 a 15 |

### Entradas do HappyHorse 1.0 (happyhorse-1.0-r2v)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt descrevendo o vídeo. Use identificadores como 'character1' e 'character2' para se referir aos personagens de referência. | STRING | Sim | N/A |
| `resolution` | A resolução do vídeo gerado. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `ratio` | A proporção do vídeo gerado. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | A duração do vídeo gerado em segundos (padrão: 5). | INT | Sim | 3 a 15 |

### Entradas de Referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte de 1 a 9 imagens de referência da pessoa ou objeto que aparecerá no vídeo. Forneça pelo menos uma imagem de referência. | IMAGE | Sim | 1 a 9 (por modelo) |

Observação: Pelo menos uma imagem de referência deve ser fornecida; caso contrário, o nó apresentará um erro. Cada imagem de referência deve ter no mínimo 400 x 400 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1. O prompt não pode estar vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `252c918afc4cf38be9c7d09b7112075b9adb23490ec9fed1717a8548519d2554`

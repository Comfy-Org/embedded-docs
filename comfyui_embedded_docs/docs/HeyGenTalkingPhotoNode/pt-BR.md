# HeyGen Talking Photo

Anime uma imagem estática de uma pessoa em um vídeo falando com sincronização labial usando a tecnologia Avatar IV da HeyGen. Você pode conduzir a animação com um roteiro de texto que a HeyGen converte em fala, ou fornecer seu próprio áudio para o avatar fazer a sincronização labial.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `imagem` | Imagem de uma pessoa para animar. Redimensionada automaticamente se for maior que 2K. | IMAGE | Sim | - |
| `fala` | Conduza o avatar com um roteiro de texto (texto-para-fala da HeyGen) ou seu próprio áudio. | DYNAMIC_COMBO | Sim | `"script"`<br>`"audio"` |
| `resolução` | Resolução do vídeo de saída (padrão: `"1080p"`). | COMBO | Não | `"720p"`<br>`"1080p"` |
| `proporção` | Proporção de aspecto da saída. `"auto"` segue a imagem de entrada (padrão: `"auto"`). | COMBO | Não | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `expressividade` | O quanto o rosto e os gestos animados são expressivos (padrão: `"low"`). | COMBO | Não | `"low"`<br>`"medium"`<br>`"high"` |
| `semente` | Não é enviado para a HeyGen; altere-o para forçar uma nova execução (padrão: 42). | INT | Não | 0 a 2147483647 |

### Entradas de roteiro

Exibidas quando `speech` é `"script"`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `text` | Texto para o avatar falar (até 5000 caracteres). A fala gerada deve ter pelo menos 1 segundo de duração. (padrão: vazio) | STRING | Sim | 1 a 5000 caracteres |
| `voice` | Voz para o roteiro (as vozes mais populares da HeyGen). | COMBO | Sim | Várias opções disponíveis |
| `custom_voice_id` | ID de voz opcional da HeyGen. Quando definido, substitui a voz selecionada acima. Qualquer voz da biblioteca da HeyGen (2000+) pode ser usada. (padrão: vazio) | STRING | Não | - |
| `voice_speed` | Multiplicador de velocidade da fala (padrão: 1.0). | FLOAT | Não | 0.5 a 1.5 (passo 0.05) |

### Entradas de áudio

Exibidas quando `speech` é `"audio"`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `audio` | Áudio para o avatar sincronizar os lábios, até 10 minutos. | AUDIO | Sim | Até 10 minutos |

Nota: Quando `speech` é `"script"`, `text` deve ser especificado, e uma voz é obrigatória através do seletor `voice` (escolhendo qualquer opção que não seja a voz padrão do avatar) ou um `custom_voice_id`. Quando `speech` é `"audio"`, `audio` é obrigatório no lugar.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `video` | Vídeo gerado da foto animada falando, com fala sincronizada labial. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`

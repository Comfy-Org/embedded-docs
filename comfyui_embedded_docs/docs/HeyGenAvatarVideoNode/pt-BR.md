# HeyGenAvatarVideoNode

Gere um vídeo de apresentador falante a partir de um avatar HeyGen. Este nó cria um vídeo de um avatar de IA falando o texto fornecido ou sincronizando os lábios com seu próprio áudio, usando os mecanismos de renderização da HeyGen.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `engine` | Mecanismo de renderização; cada opção lista apenas os avatares que o suportam. 'auto' oferece todos os avatares e escolhe seu melhor mecanismo (Avatar IV preferido). Avatar V é o de maior fidelidade, Avatar III é o mais acessível. | COMBO | Sim | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | ID opcional de aparência do avatar HeyGen. Quando definido, substitui o avatar selecionado acima. Qualquer uma das mais de 3000 aparências públicas da HeyGen (ou seus avatares privados) pode ser usada. | STRING | Não |  |
| `speech` | Controla o avatar com um roteiro de texto (texto-para-fala da HeyGen) ou seu próprio áudio. | COMBO | Sim | `"script"`<br>`"audio"` |
| `resolution` | Resolução do vídeo de saída (padrão: "1080p"). | COMBO | Não | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Proporção de tela da saída. 'auto' segue a filmagem de origem do avatar (padrão: "auto"). | COMBO | Não | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `background_color` | Cor de fundo sólida opcional como código hexadecimal (ex: '#00ff00'). Deixe vazio para usar o fundo original do avatar. | STRING | Não |  |
| `seed` | Não é enviado para a HeyGen; altere-o para forçar uma nova execução (padrão: 42). | INT | Não | Mín: 0<br>Máx: 2147483647 |

Quando `speech` está definido como `"script"`, os seguintes subparâmetros estão disponíveis:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `text` | Texto para o avatar falar (até 5000 caracteres). A fala gerada deve ter pelo menos 1 segundo de duração. | STRING | Sim |  |
| `voice` | Voz para o roteiro. A opção padrão usa a voz que a HeyGen atribuiu ao avatar. | COMBO | Sim | Múltiplas opções disponíveis |
| `custom_voice_id` | ID opcional de voz HeyGen. Quando definido, substitui a voz selecionada acima. Qualquer voz da biblioteca da HeyGen (mais de 2000) pode ser usada. | STRING | Não |  |
| `voice_speed` | Multiplicador de velocidade da fala (padrão: 1.0). | FLOAT | Não | Mín: 0.5<br>Máx: 1.5<br>Passo: 0.05 |

Quando `speech` está definido como `"audio"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `audio` | Áudio para o avatar sincronizar os lábios, com até 10 minutos de duração. | AUDIO | Sim |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `VIDEO` | O vídeo do apresentador avatar gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `009bc72b841ca273af83fe6f80fb24d4b11c2efd96c011795b1ff1cf8e66ee61`

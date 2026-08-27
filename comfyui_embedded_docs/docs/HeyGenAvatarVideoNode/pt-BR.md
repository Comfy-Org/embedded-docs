# Vídeo de Avatar HeyGen

Gere um vídeo de apresentador com fala a partir de um avatar da HeyGen. Este nó cria um vídeo de um avatar de IA falando o texto fornecido ou sincronizando os lábios com seu próprio áudio, usando os mecanismos de renderização da HeyGen.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Valores |
|-----------|-------------|-----------|----------|-------|
| `engine` | Mecanismo de renderização; cada opção lista apenas os avatares que o suportam. `"auto"` oferece todos os avatares e escolhe o melhor mecanismo para cada um (o Avatar IV é o preferido). O Avatar V é o de maior fidelidade; o Avatar III é o mais acessível. | DYNAMIC_COMBO | Sim | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | ID opcional de visual de avatar da HeyGen. Quando definido, substitui o avatar selecionado acima. Qualquer um dos mais de 3000 visuais públicos da HeyGen (ou seus avatares privados) pode ser usado. Padrão: string vazia. | STRING | Não |  |
| `fala` | Controle o avatar por meio de um roteiro de texto (texto-para-fala da HeyGen) ou com seu próprio áudio. | DYNAMIC_COMBO | Sim | `"script"`<br>`"audio"` |
| `resolução` | Resolução do vídeo de saída. Padrão: `"1080p"`. | COMBO | Não | `"720p"`<br>`"1080p"` |
| `proporção` | Proporção de tela da saída. `"auto"` segue a filmagem de origem do avatar. Padrão: `"auto"`. | COMBO | Não | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `cor_de_fundo` | Cor de fundo sólida opcional como código hexadecimal (ex.: `"#00ff00"`). Deixe vazio para usar o fundo do próprio avatar. Se fornecida, o valor deve começar com `#`. Padrão: string vazia. | STRING | Não |  |
| `semente` | Não é enviado para a HeyGen; altere-o para forçar uma nova execução. Padrão: `42`. | INT | Não | Mín: 0<br>Máx: 2147483647 |

### Entradas de `auto`

Quando `engine` é `"auto"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Valores |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Visual de avatar para apresentar o vídeo (selecionado da biblioteca pública da HeyGen). O melhor mecanismo compatível com o visual é escolhido automaticamente. | COMBO | Sim | Múltiplas opções disponíveis |

### Entradas de `avatar_iv`

Quando `engine` é `"avatar_iv"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Valores |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Visuais de avatar compatíveis com o mecanismo Avatar IV. | COMBO | Sim | Múltiplas opções disponíveis |

### Entradas de `avatar_iii`

Quando `engine` é `"avatar_iii"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Valores |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Visuais de avatar compatíveis com o mecanismo Avatar III. | COMBO | Sim | Múltiplas opções disponíveis |

### Entradas de `avatar_v`

Quando `engine` é `"avatar_v"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Valores |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Visuais de avatar compatíveis com o mecanismo Avatar V. | COMBO | Sim | Múltiplas opções disponíveis |

### Entradas de `script`

Quando `speech` é `"script"`, os seguintes subparâmetros ficam disponíveis:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Valores |
|-----------|-------------|-----------|----------|-------|
| `text` | Texto para o avatar falar (até 5000 caracteres). A fala gerada deve ter pelo menos 1 segundo de duração. Padrão: string vazia. | STRING | Sim | Mín: 1 caractere<br>Máx: 5000 caracteres |
| `voice` | Voz para o roteiro. A opção padrão usa a voz que a HeyGen atribuiu ao avatar. | COMBO | Sim | `"(avatar's default voice)"`<br>Múltiplas opções gerais de voz disponíveis |
| `custom_voice_id` | ID opcional de voz da HeyGen. Quando definido, substitui a voz selecionada acima. Qualquer voz da biblioteca da HeyGen (mais de 2000) pode ser usada. Padrão: string vazia. | STRING | Não |  |
| `voice_speed` | Multiplicador de velocidade da fala. Padrão: `1.0`. | FLOAT | Não | Mín: 0.5<br>Máx: 1.5<br>Passo: 0.05 |

### Entradas de `audio`

Quando `speech` é `"audio"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Valores |
|-----------|-------------|-----------|----------|-------|
| `audio` | Áudio para o avatar sincronizar os lábios, com até 10 minutos. | AUDIO | Sim |  |

Nota: `speech` é um seletor de fonte com dois modos mutuamente exclusivos. No modo `"script"`, `text` é obrigatório (1 a 5000 caracteres); se `custom_voice_id` for fornecido, ele substitui `voice`. No modo `"audio"`, o avatar sincroniza os lábios com o clipe de áudio fornecido. `background_color` deve ser um código hexadecimal começando com `#` quando fornecido. Quando `custom_avatar_id` é definido, ele substitui a seleção de `avatar`, e o `engine` selecionado deve ser compatível com esse visual de avatar; caso contrário, um erro é gerado (a menos que `engine` seja `"auto"`).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo do apresentador com avatar gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `009bc72b841ca273af83fe6f80fb24d4b11c2efd96c011795b1ff1cf8e66ee61`

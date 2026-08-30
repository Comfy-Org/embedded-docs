# Vídeo de Avatar HeyGen

Gere um vídeo com um apresentador virtual falante a partir de um avatar da HeyGen. Este nó cria um vídeo de um avatar de IA falando o texto fornecido ou fazendo lip sync com o seu próprio áudio, usando os mecanismos de renderização da HeyGen.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `engine` | Mecanismo de renderização; cada opção lista apenas os avatares que o suportam. "auto" oferece todos os avatares e escolhe o melhor mecanismo para cada um (Avatar IV preferido). O Avatar V é o de maior fidelidade; o Avatar III é o mais acessível. | DYNAMIC_COMBO | Sim | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | ID opcional de aparência de avatar da HeyGen. Quando definido, substitui o avatar selecionado acima. Qualquer uma das mais de 3000 aparências públicas da HeyGen (ou seus avatares privados) pode ser usada. Padrão: `""`. | STRING | Não |  |
| `fala` | Controle o avatar por meio de um roteiro de texto (texto-para-fala da HeyGen) ou do seu próprio áudio. Nome de exibição: "speech source". | DYNAMIC_COMBO | Sim | `"script"`<br>`"audio"` |
| `resolução` | Resolução do vídeo de saída. Padrão: `"1080p"`. | COMBO | Não | `"720p"`<br>`"1080p"` |
| `proporção` | Proporção de tela da saída. "auto" segue a filmagem original do avatar. Padrão: `"auto"`. | COMBO | Não | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `cor_de_fundo` | Cor de fundo sólida opcional como código hexadecimal (ex.: `"#00ff00"`). Deixe vazio para usar o fundo original do avatar. Se for fornecida, o valor deve começar com `#`. Padrão: `""`. | STRING | Não |  |
| `semente` | Não é enviado para a HeyGen; altere-o para forçar uma nova execução. Padrão: `42`. | INT | Não | Mín.: 0<br>Máx.: 2147483647 |

### Entradas do `auto`

Quando `engine` é `"auto"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aparência do avatar para apresentar o vídeo (curada da biblioteca pública da HeyGen). O melhor mecanismo que essa aparência suporta é escolhido automaticamente. | COMBO | Sim | Várias opções disponíveis |

### Entradas do `avatar_iv`

Quando `engine` é `"avatar_iv"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aparências de avatar que suportam o mecanismo Avatar IV. | COMBO | Sim | Várias opções disponíveis |

### Entradas do `avatar_iii`

Quando `engine` é `"avatar_iii"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aparências de avatar que suportam o mecanismo Avatar III. | COMBO | Sim | Várias opções disponíveis |

### Entradas do `avatar_v`

Quando `engine` é `"avatar_v"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aparências de avatar que suportam o mecanismo Avatar V. | COMBO | Sim | Várias opções disponíveis |

### Entradas do `script`

Quando `speech` é `"script"`, os seguintes subparâmetros estão disponíveis:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `text` | Texto para o avatar falar (até 5000 caracteres). A fala gerada deve ter pelo menos 1 segundo de duração. Padrão: `""`. | STRING | Sim | Mín.: 1 caractere<br>Máx.: 5000 caracteres |
| `voice` | Voz para o roteiro. A opção padrão usa a voz que a HeyGen atribuiu ao avatar. Ignorada se `custom_voice_id` estiver definido. | COMBO | Sim | `"(avatar's default voice)"`<br>Várias opções gerais de voz disponíveis |
| `custom_voice_id` | ID opcional de voz da HeyGen. Quando definido, substitui a voz selecionada acima. Qualquer voz da biblioteca da HeyGen (mais de 2000) pode ser usada. Padrão: `""`. | STRING | Não |  |
| `voice_speed` | Multiplicador de velocidade da fala. Padrão: `1.0`. | FLOAT | Não | Mín.: 0.5<br>Máx.: 1.5<br>Incremento: 0.05 |

### Entradas do `audio`

Quando `speech` é `"audio"`, o seguinte subparâmetro está disponível:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `audio` | Áudio para o avatar fazer lip sync, com até 10 minutos. | AUDIO | Sim |  |

Nota: `engine` e `speech` são seletores que revelam subparâmetros diferentes dependendo do valor escolhido. O seletor `speech` tem dois modos mutuamente exclusivos: no modo `"script"`, `text` é obrigatório; se `custom_voice_id` for fornecido, ele substitui `voice`. No modo `"audio"`, o avatar faz lip sync com o clipe de áudio fornecido. `background_color` deve ser um código hexadecimal de cor começando com `#` quando fornecido. Quando `custom_avatar_id` está definido, ele substitui a seleção de `avatar`, e o `engine` selecionado deve ser suportado por essa aparência de avatar; caso contrário, um erro é gerado, a menos que `engine` seja `"auto"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com o avatar apresentador. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `86dc799d3a8cf2666449b0d422853b12feffb81ce002f84594f9b925d58b522a`

# Vídeo de Avatar HeyGen

Gere um vídeo de apresentador falante a partir de um avatar da HeyGen. Este nó cria um vídeo de um avatar de IA falando o texto fornecido ou fazendo lip-sync com seu próprio áudio, usando os motores de renderização da HeyGen.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `engine` | Motor de renderização; cada opção lista apenas os avatares que o suportam. "auto" oferece todos os avatares e escolhe o melhor motor para cada um (Avatar IV preferido). O Avatar V tem a maior fidelidade, o Avatar III é o mais acessível. | DYNAMIC_COMBO | Sim | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | ID de aparência de avatar da HeyGen opcional. Quando definido, substitui o avatar selecionado acima. Qualquer uma das mais de 3000 aparências públicas da HeyGen (ou seus avatares privados) pode ser usada. Padrão: `""`. | STRING | Não |  |
| `speech` | Conduza o avatar com um roteiro de texto (text-to-speech da HeyGen) ou com seu próprio áudio. Nome de exibição: "speech source". | DYNAMIC_COMBO | Sim | `"script"`<br>`"audio"` |
| `resolution` | Resolução do vídeo de saída. Padrão: `"1080p"`. | COMBO | Não | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Proporção de aspecto da saída. "auto" segue a filmagem de origem do avatar. Padrão: `"auto"`. | COMBO | Não | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `background_color` | Cor de fundo sólida opcional como código hexadecimal (por exemplo, `"#00ff00"`). Deixe vazio para usar o fundo do próprio avatar. Se fornecida, o valor deve começar com `#`. Padrão: `""`. | STRING | Não |  |
| `seed` | Não é enviado à HeyGen; altere-o para forçar uma nova execução. Padrão: `42`. | INT | Não | Mín: 0<br>Máx: 2147483647 |

### Entradas do `auto`

Quando `engine` é `"auto"`, o seguinte subparâmetro fica disponível:

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aparência de avatar para apresentar o vídeo (selecionada da biblioteca pública da HeyGen). O melhor motor compatível com a aparência é escolhido automaticamente. | COMBO | Sim | Várias opções disponíveis |

### Entradas do `avatar_iv`

Quando `engine` é `"avatar_iv"`, o seguinte subparâmetro fica disponível:

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aparências de avatar compatíveis com o motor Avatar IV. | COMBO | Sim | Várias opções disponíveis |

### Entradas do `avatar_iii`

Quando `engine` é `"avatar_iii"`, o seguinte subparâmetro fica disponível:

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aparências de avatar compatíveis com o motor Avatar III. | COMBO | Sim | Várias opções disponíveis |

### Entradas do `avatar_v`

Quando `engine` é `"avatar_v"`, o seguinte subparâmetro fica disponível:

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `avatar` | Aparências de avatar compatíveis com o motor Avatar V. | COMBO | Sim | Várias opções disponíveis |

### Entradas do `script`

Quando `speech` é `"script"`, os seguintes subparâmetros ficam disponíveis:

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `text` | Texto para o avatar falar (até 5000 caracteres). A fala gerada deve ter pelo menos 1 segundo de duração. Padrão: `""`. | STRING | Sim | Mín: 1 caractere<br>Máx: 5000 caracteres |
| `voice` | Voz para o roteiro. A opção padrão usa a voz que a HeyGen atribuiu ao avatar. Ignorada se `custom_voice_id` estiver definido. | COMBO | Sim | `"(avatar's default voice)"`<br>Várias opções de voz geral disponíveis |
| `custom_voice_id` | ID de voz da HeyGen opcional. Quando definido, substitui a voz selecionada acima. Qualquer voz da biblioteca da HeyGen (mais de 2000) pode ser usada. Padrão: `""`. | STRING | Não |  |
| `voice_speed` | Multiplicador de velocidade da fala. Padrão: `1.0`. | FLOAT | Não | Mín: 0.5<br>Máx: 1.5<br>Passo: 0.05 |

### Entradas do `audio`

Quando `speech` é `"audio"`, o seguinte subparâmetro fica disponível:

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `audio` | Áudio para o avatar fazer lip-sync, de até 10 minutos. | AUDIO | Sim |  |

Nota: `engine` e `speech` são seletores que revelam subparâmetros diferentes de acordo com o valor escolhido. O seletor `speech` tem dois modos mutuamente exclusivos: no modo `"script"`, `text` é obrigatório; se `custom_voice_id` for fornecido, ele substitui `voice`. No modo `"audio"`, o avatar faz lip-sync com o clipe de áudio fornecido. Quando fornecido, `background_color` deve ser um código de cor hexadecimal que começa com `#`. Quando `custom_avatar_id` está definido, ele substitui a seleção de `avatar`, e o `engine` selecionado deve ser compatível com essa aparência de avatar; caso contrário, um erro é gerado, a menos que `engine` seja `"auto"`.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo de apresentador com avatar gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `86dc799d3a8cf2666449b0d422853b12feffb81ce002f84594f9b925d58b522a`

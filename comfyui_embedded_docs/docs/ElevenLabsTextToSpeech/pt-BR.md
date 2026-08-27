# ElevenLabs Text to Speech

O nó ElevenLabs Text to Speech converte texto escrito em áudio falado usando a API ElevenLabs. Ele permite selecionar uma voz específica e ajustar diversas características da fala, como estabilidade, velocidade e estilo, para gerar uma saída de áudio personalizada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `modelo` | Modelo a ser usado para texto para fala. Selecionar um modelo revela seus parâmetros específicos. | DYNAMIC_COMBO | Não | `"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `voz` | Voz a ser usada para a síntese de fala. Conecte a partir do Voice Selector ou do Instant Voice Clone. | CUSTOM | Sim | N/A |
| `texto` | O texto a ser convertido em fala. Deve conter pelo menos um caractere. | STRING | Sim | N/A |
| `estabilidade` | Estabilidade da voz. Valores menores proporcionam uma gama emocional mais ampla, valores maiores produzem uma fala mais consistente, mas potencialmente monótona (padrão: 0.5). | FLOAT | Não | 0.0 - 1.0 |
| `aplicar normalização de texto` | Modo de normalização de texto. 'auto' permite que o sistema decida, 'on' sempre aplica a normalização, 'off' a ignora. | COMBO | Não | `"auto"`<br>`"on"`<br>`"off"` |
| `código do idioma` | Código de idioma ISO-639-1 ou ISO-639-3 (ex.: 'en', 'es', 'fra'). Deixe vazio para detecção automática (padrão: ""). | STRING | Não | N/A |
| `semente` | Semente para reprodutibilidade (determinismo não garantido) (padrão: 1). | INT | Não | 0 - 2147483647 |
| `formato de saída` | Formato de saída de áudio. | COMBO | Não | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entradas do eleven_multilingual_v2

Estes parâmetros ficam disponíveis quando `model` está definido como `"eleven_multilingual_v2"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `speed` | Velocidade da fala. 1.0 é normal, <1.0 mais lenta, >1.0 mais rápida (padrão: 1.0). | FLOAT | Não | 0.7 - 1.3 |
| `similarity_boost` | Aumento de similaridade. Valores mais altos tornam a voz mais semelhante à original (padrão: 0.75). | FLOAT | Não | 0.0 - 1.0 |
| `use_speaker_boost` | Aumentar a similaridade com a voz do locutor original (padrão: False). | BOOLEAN | Não | True / False |
| `style` | Exagero de estilo. Valores mais altos aumentam a expressividade estilística, mas podem reduzir a estabilidade (padrão: 0.0). | FLOAT | Não | 0.0 - 0.2 |

### Entradas do eleven_v3

Estes parâmetros ficam disponíveis quando `model` está definido como `"eleven_v3"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `speed` | Velocidade da fala. 1.0 é normal, <1.0 mais lenta, >1.0 mais rápida (padrão: 1.0). | FLOAT | Não | 0.7 - 1.3 |
| `similarity_boost` | Aumento de similaridade. Valores mais altos tornam a voz mais semelhante à original (padrão: 0.75). | FLOAT | Não | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `audio` | O áudio gerado a partir da conversão de texto para fala. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/pt-BR.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`

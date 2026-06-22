# ElevenLabs Text to Speech

O nó ElevenLabs Text to Speech converte texto escrito em áudio falado usando a API ElevenLabs. Ele permite selecionar uma voz específica e ajustar várias características da fala, como estabilidade, velocidade e estilo, para gerar uma saída de áudio personalizada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `voz` | Voz a ser usada na síntese de fala. Conecte a partir do Seletor de Voz ou Clone Instantâneo de Voz. | CUSTOM | Sim | N/A |
| `texto` | O texto a ser convertido em fala. | STRING | Sim | N/A |
| `estabilidade` | Estabilidade da voz. Valores mais baixos proporcionam uma faixa emocional mais ampla; valores mais altos produzem uma fala mais consistente, mas potencialmente monótona (padrão: 0.5). | FLOAT | Não | 0.0 - 1.0 |
| `aplicar normalização de texto` | Modo de normalização de texto. 'auto' permite que o sistema decida, 'on' sempre aplica a normalização, 'off' a ignora. | COMBO | Não | `"auto"`<br>`"on"`<br>`"off"` |
| `modelo` | Modelo a ser usado para conversão de texto em fala. Selecionar um modelo revela seus parâmetros específicos. | DYNAMICCOMBO | Não | `"eleven_multilingual_v2"`<br>`"eleven_v3"` |
| `código do idioma` | Código de idioma ISO-639-1 ou ISO-639-3 (ex.: 'en', 'es', 'fra'). Deixe vazio para detecção automática (padrão: ""). | STRING | Não | N/A |
| `semente` | Semente para reprodutibilidade (determinismo não garantido) (padrão: 1). | INT | Não | 0 - 2147483647 |
| `formato de saída` | Formato de saída de áudio. | COMBO | Não | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Parâmetros Específicos do Modelo:**
Quando o parâmetro `model` está definido como `"eleven_multilingual_v2"`, os seguintes parâmetros adicionais ficam disponíveis:

* `speed`: Velocidade da fala. 1.0 é normal, <1.0 mais lento, >1.0 mais rápido (padrão: 1.0, faixa: 0.7 - 1.3).
* `similarity_boost`: Reforço de similaridade. Valores mais altos tornam a voz mais semelhante à original (padrão: 0.75, faixa: 0.0 - 1.0).
* `use_speaker_boost`: Reforça a similaridade com a voz do locutor original (padrão: Falso).
* `style`: Exagero de estilo. Valores mais altos aumentam a expressão estilística, mas podem reduzir a estabilidade (padrão: 0.0, faixa: 0.0 - 0.2).

Quando o parâmetro `model` está definido como `"eleven_v3"`, os seguintes parâmetros adicionais ficam disponíveis:

* `speed`: Velocidade da fala. 1.0 é normal, <1.0 mais lento, >1.0 mais rápido (padrão: 1.0, faixa: 0.7 - 1.3).
* `similarity_boost`: Reforço de similaridade. Valores mais altos tornam a voz mais semelhante à original (padrão: 0.75, faixa: 0.0 - 1.0).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `audio` | O áudio gerado a partir da conversão de texto em fala. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d11d4ffa2d1f11dfd5ce378d9496cd9788d2197bf7f4135092ecefb287f3c2f7`

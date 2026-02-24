> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/pt-BR.md)

O nó **ElevenLabs Text to Speech** converte texto escrito em áudio falado usando a API da ElevenLabs. Ele permite que você selecione uma voz específica e ajuste várias características da fala, como estabilidade, velocidade e estilo, para gerar uma saída de áudio personalizada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | Sim | N/A | Voz a ser usada para a síntese de fala. Conecte a partir do seletor de voz ou do Instant Voice Clone. |
| `text` | STRING | Sim | N/A | O texto a ser convertido em fala. |
| `stability` | FLOAT | Não | 0.0 - 1.0 | Estabilidade da voz. Valores mais baixos proporcionam uma gama emocional mais ampla, valores mais altos produzem uma fala mais consistente, mas potencialmente monótona (padrão: 0.5). |
| `apply_text_normalization` | COMBO | Não | `"auto"`<br>`"on"`<br>`"off"` | Modo de normalização de texto. 'auto' deixa o sistema decidir, 'on' sempre aplica normalização, 'off' ignora. |
| `model` | DYNAMICCOMBO | Não | `"eleven_multilingual_v2"`<br>`"eleven_v3"` | Modelo a ser usado para a conversão de texto em fala. Selecionar um modelo revela seus parâmetros específicos. |
| `language_code` | STRING | Não | N/A | Código de idioma ISO-639-1 ou ISO-639-3 (ex.: 'en', 'es', 'fra'). Deixe vazio para detecção automática (padrão: ""). |
| `seed` | INT | Não | 0 - 2147483647 | Semente para reprodutibilidade (determinismo não garantido) (padrão: 1). |
| `output_format` | COMBO | Não | `"mp3_44100_192"`<br>`"opus_48000_192"` | Formato de saída de áudio. |

**Parâmetros Específicos do Modelo:**
Quando o parâmetro `model` é definido como `"eleven_multilingual_v2"`, os seguintes parâmetros adicionais ficam disponíveis:

* `speed`: Velocidade da fala. 1.0 é normal, <1.0 mais lento, >1.0 mais rápido (padrão: 1.0, intervalo: 0.7 - 1.3).
* `similarity_boost`: Aumento de similaridade. Valores mais altos tornam a voz mais semelhante à original (padrão: 0.75, intervalo: 0.0 - 1.0).
* `use_speaker_boost`: Aumenta a similaridade com a voz original do locutor (padrão: False).
* `style`: Exagero de estilo. Valores mais altos aumentam a expressão estilística, mas podem reduzir a estabilidade (padrão: 0.0, intervalo: 0.0 - 0.2).

Quando o parâmetro `model` é definido como `"eleven_v3"`, os seguintes parâmetros adicionais ficam disponíveis:

* `speed`: Velocidade da fala. 1.0 é normal, <1.0 mais lento, >1.0 mais rápido (padrão: 1.0, intervalo: 0.7 - 1.3).
* `similarity_boost`: Aumento de similaridade. Valores mais altos tornam a voz mais semelhante à original (padrão: 0.75, intervalo: 0.0 - 1.0).

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | O áudio gerado a partir da conversão de texto em fala. |

# ElevenLabs Fala para Fala

O nó ElevenLabs Speech to Speech transforma um arquivo de áudio de entrada de uma voz para outra. Ele usa a API ElevenLabs para converter fala, preservando o conteúdo original e o tom emocional do áudio.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a ser usado para a transformação de fala em fala. Cada opção de modelo fornece um conjunto correspondente de configurações de voz (similarity_boost, style, use_speaker_boost, speed). | DYNAMIC_COMBO | Não | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `voz` | Voz de destino para a transformação. Conecte a partir do Seletor de Voz ou Clone Instantâneo de Voz. | CUSTOM | Sim | - |
| `áudio` | Áudio de origem a ser transformado. | AUDIO | Sim | - |
| `estabilidade` | Estabilidade da voz. Valores mais baixos proporcionam uma gama emocional mais ampla; valores mais altos produzem fala mais consistente, mas potencialmente monótona (padrão: 0.5). | FLOAT | Não | 0.0 - 1.0 |
| `formato_de_saida` | Formato de saída do áudio (padrão: "mp3_44100_192"). | COMBO | Não | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `semente` | Semente para reprodutibilidade (padrão: 0). | INT | Não | 0 - 4294967295 |
| `remover_ruído_de_fundo` | Remover ruído de fundo do áudio de entrada usando isolamento de áudio (padrão: False). | BOOLEAN | Não | - |

### Configurações de Voz (Compartilhadas por `eleven_multilingual_sts_v2` e `eleven_english_sts_v2`)

Quando um modelo é selecionado, essas configurações de voz ficam disponíveis para a transformação.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `speed` | Velocidade da fala. 1.0 é normal, <1.0 mais lento, >1.0 mais rápido (padrão: 1.0). | FLOAT | Não | 0.7 - 1.3 |
| `similarity_boost` | Reforço de similaridade. Valores mais altos tornam a voz mais semelhante à original (padrão: 0.75). | FLOAT | Não | 0.0 - 1.0 |
| `use_speaker_boost` | Reforçar a similaridade com a voz do locutor original (padrão: False). | BOOLEAN | Não | - |
| `style` | Exagero de estilo. Valores mais altos aumentam a expressão estilística, mas podem reduzir a estabilidade (padrão: 0.0). | FLOAT | Não | 0.0 - 0.2 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `audio` | O arquivo de áudio transformado no formato de saída especificado. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`

# Breeze Text to Speech

Converte texto em fala com o Breeze TTS 2. Escolha uma voz Breeze, selecione o idioma do texto e, opcionalmente, direcione como a linha é executada. Inglês e Chinês podem usar qualquer um dos modelos Breeze TTS 2; todos os outros idiomas usam o Breeze TTS 2 Multilingual.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `voice` | Voz Breeze para falar, obtida do Breeze Voice Selector ou de um dos nós de criação de voz Breeze. | BREEZE_VOICE | Sim | - |
| `text` | Texto para falar, de 1 a 1000 caracteres. Tags de áudio como `(laughs)` ou `(sighs)` são executadas em vez de lidas. Padrão: vazio. | STRING | Sim | 1 a 1000 caracteres |
| `language` | Idioma do texto. Inglês e Chinês podem usar qualquer um dos modelos; outros idiomas usam o Breeze TTS 2 Multilingual. Uma voz soa melhor em seu próprio idioma, então para outro idioma use uma cópia feita com o Breeze Voice Localize. | DYNAMIC_COMBO | Sim | Múltiplas opções disponíveis |
| `delivery` | Como a linha é executada: `neutral` mantém a voz como está, `directed` segue instruções escritas. Padrão: `"neutral"`. | DYNAMIC_COMBO | Sim | `"neutral"`<br>`"directed"` |
| `speed` | Multiplicador de tempo que mantém o tom inalterado. Padrão: 1.0. | FLOAT | Não | 0.5 a 2.0 (passo 0.05) |
| `seed` | Controla se o nó é reexecutado; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Não | 0 a 2147483647 |

### Entradas para idioma "English" e "Chinese"

Estas aparecem apenas quando `language` é English ou Chinese.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` ou `Breeze TTS 2 Multilingual`. Padrão: `"Breeze TTS 2"`. | COMBO | Sim | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

### Entradas para entrega "neutral"

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `speaker_boost` | Mantém a voz mais próxima do som original. Padrão: false. | BOOLEAN | Não | True<br>False |

### Entradas para entrega "directed"

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `instructions` | Como executar o texto, escrito no mesmo idioma do texto. Padrão: vazio. | STRING | Não | Texto multilinha |
| `strength` | Quão fortemente a voz segue as instruções. Padrão: 4.0. | FLOAT | Não | 1.0 a 10.0 (passo 0.1) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `audio` | A fala gerada como áudio WAV. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeTextToSpeech/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e5e5201e8c951a878ef9e764db31e494285ddded6ec66d8e818ec132342bbe5c`

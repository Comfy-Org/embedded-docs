# Breeze Text to Speech

Converte il testo in parlato con Breeze TTS 2. Scegli una voce Breeze, seleziona la lingua del testo e, facoltativamente, indica come interpretare la battuta. L'inglese e il cinese possono usare uno qualsiasi dei due modelli Breeze TTS 2; tutte le altre lingue usano Breeze TTS 2 Multilingual.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `voice` | Voce Breeze con cui parlare, da Breeze Voice Selector o da uno dei nodi di creazione voce Breeze. | BREEZE_VOICE | Sì | - |
| `text` | Testo da pronunciare, da 1 a 1000 caratteri. I tag audio come `(laughs)` o `(sighs)` vengono interpretati anziché letti. Predefinito: vuoto. | STRING | Sì | 1 a 1000 caratteri |
| `language` | Lingua del testo. Inglese e cinese possono usare uno qualsiasi dei due modelli; le altre lingue usano Breeze TTS 2 Multilingual. Una voce suona al meglio nella propria lingua, quindi per un'altra lingua usa una copia creata con Breeze Voice Localize. | DYNAMIC_COMBO | Sì | Più opzioni disponibili |
| `delivery` | Come viene interpretata la battuta: `neutral` mantiene la voce così com'è, `directed` segue le istruzioni scritte. Predefinito: `"neutral"`. | DYNAMIC_COMBO | Sì | `"neutral"`<br>`"directed"` |
| `speed` | Moltiplicatore di tempo che lascia invariata l'intonazione. Predefinito: 1.0. | FLOAT | No | 0.5 a 2.0 (passo 0.05) |
| `seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici a prescindere dal seed. Predefinito: 42. | INT | No | 0 a 2147483647 |

### Input per la lingua "English" e "Chinese"

Questi campi compaiono solo quando `language` è English o Chinese.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` o `Breeze TTS 2 Multilingual`. Predefinito: `"Breeze TTS 2"`. | COMBO | Sì | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

### Input per Interpretazione "neutral"

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `speaker_boost` | Mantiene la voce più vicina al suo suono originale. Predefinito: false. | BOOLEAN | No | true<br>false |

### Input per Interpretazione "directed"

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `instructions` | Come interpretare il testo, scritto nella stessa lingua del testo. Predefinito: vuoto. | STRING | No | Testo multiriga |
| `strength` | Quanto fortemente la voce segue le istruzioni. Predefinito: 4.0. | FLOAT | No | 1.0 a 10.0 (passo 0.1) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `audio` | Il parlato generato come audio WAV. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeTextToSpeech/it.md)

---
**Source fingerprint (SHA-256):** `e5e5201e8c951a878ef9e764db31e494285ddded6ec66d8e818ec132342bbe5c`

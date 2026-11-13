# Breeze Voice Selector

Sceglie una voce Breeze in evidenza, o qualsiasi ID voce Breeze, e la passa a Breeze Text to Speech. Il nodo si limita a risolvere un ID e non effettua alcuna chiamata API.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `language` | Gruppo linguistico delle voci in evidenza, oppure `custom` per inserire un ID. Predefinito: `"English"`. | DYNAMIC_COMBO | Sì | `"English"`<br>`"Chinese"`<br>`"Japanese"`<br>`"custom"` |

### Input per la lingua "English", "Chinese" e "Japanese"

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `voice` | Voce in evidenza in quella lingua. | COMBO | Sì | Più opzioni disponibili |

### Input per la lingua "custom"

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `voice_id` | Qualsiasi ID voce Breeze, ad esempio una voce creata dagli altri nodi Breeze. Solo lettere, cifre, `_` e `-`. Predefinito: vuoto. | STRING | Sì | ID voce Breeze |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `voice` | La voce Breeze selezionata. | BREEZE_VOICE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceSelector/it.md)

---
**Source fingerprint (SHA-256):** `0bded8f1b6ec92abaec514ed843b3c138d804e3736758f5df3a2faf52e89a8b0`

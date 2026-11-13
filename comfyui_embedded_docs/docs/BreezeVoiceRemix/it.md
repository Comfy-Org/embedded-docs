# Breeze Voice Remix

Crea una copia modificata di una voce nella stessa lingua, a partire da una descrizione scritta della modifica oppure da un preset con nome. La copia viene salvata nel tuo account e restituita con un'anteprima audio.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `voice` | Voce Breeze da modificare. | BREEZE_VOICE | Sì | - |
| `change` | `custom` descrive la modifica a testo, `preset` seleziona una modifica con nome. Predefinito: `"custom"`. | DYNAMIC_COMBO | Sì | `"custom"`<br>`"preset"` |
| `strength` | Valori più alti modificano maggiormente la voce. Predefinito: 4.0. | FLOAT | No | 1.0 a 10.0 (passo: 0.1) |
| `seed` | Controlla se il nodo viene rieseguito; i risultati sono non deterministici indipendentemente dal seed. Predefinito: 42. | INT | No | 0 a 2147483647 |

### Input per la modifica "custom"

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Come deve cambiare la voce, ad esempio più anziana e rauca. Predefinito: vuoto. | STRING | Sì | Testo multiriga |

### Input per la modifica "preset"

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `preset` | Modifica con nome, raggruppata per età, genere, tonalità, ritmo, energia ed emozione. | COMBO | Sì | Più opzioni disponibili |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `voice` | La copia modificata della voce. | BREEZE_VOICE |
| `preview` | Anteprima audio della voce remixata. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceRemix/it.md)

---
**Source fingerprint (SHA-256):** `1bb135706fa760c6a6e8f4b9cb12a3f1506db375ee09cbd511b62d2bb24a9d2c`

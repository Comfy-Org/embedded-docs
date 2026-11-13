# Breeze Voice Localize

Crea una copia di una voce che parla nativamente un'altra lingua, invece di leggere una lingua straniera con il suo accento originale. La copia viene salvata nel tuo account e restituita con un'anteprima audio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `voice` | Voce Breeze da copiare. | BREEZE_VOICE | Sì | - |
| `language` | Lingua parlata dalla nuova voce. Predefinito: `"English"`. | COMBO | Sì | Più opzioni disponibili |
| `seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | No | 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `voice` | La copia localizzata della voce, denominata in base alla voce originale e alla lingua. | BREEZE_VOICE |
| `preview` | Anteprima audio della voce localizzata. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceLocalize/it.md)

---
**Source fingerprint (SHA-256):** `a997fbc3426669f6e5725c455f49f3e16d5e14806ea3fac26657459f63e99db1`

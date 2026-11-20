# Google Gemini Decision (Yes/No)

Poni una domanda con risposta sì/no sul testo, sulle immagini, sull'audio o sul video che colleghi e ottieni un valore booleano su cui basare l'instradamento. Collega `result` a un nodo If/Else Switch per instradare l'esecuzione su uno dei due percorsi e leggi `answer` e `probability` quando vuoi vedere perché il modello ha risposto in quel modo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare (predefinito: `"gemini-decision-1"`). | COMBO | Sì | `"gemini-decision-1"` |
| `question` | La domanda sì/no su ciò che è collegato, fino a 5000 caratteri. Formulala in modo che "sì" corrisponda al caso su cui agisci (predefinito: "Is there a person in the image?"). | STRING | Sì | Da 1 a 5000 caratteri |
| `threshold` | Probabilità di "sì" alla quale `result` diventa true. Le risposte chiaramente affermative ottengono un punteggio compreso tra circa 0.85 e 0.92, quindi 0.9 o più ne scarta molte (predefinito: 0.5). | FLOAT | Sì | 0.01 a 0.99 (passo: 0.01) |
| `images` | Immagini su cui porre la domanda, fino a 16 complessive negli slot espandibili (`image_1` ... `image_16`). Un'immagine in batch viene conteggiata una volta per ogni immagine. | IMAGE | No | Fino a 16 immagini |
| `audio` | Clip audio su cui porre la domanda. | AUDIO | No | - |
| `video` | Clip video su cui porre la domanda. | VIDEO | No | - |
| `text` | Testo a cui si riferisce la domanda, come un prompt o una risposta di un LLM, fino a 20000 caratteri. | STRING | No | Fino a 20000 caratteri |

Collega almeno uno tra `text`, `images`, `audio` o `video`; il nodo genera un errore quando non c'è nulla da esaminare. Con più immagini, denomininale `image_1`, `image_2` e così via all'interno della domanda.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `result` | La risposta come booleano: true per "sì", false per "no". | BOOLEAN |
| `answer` | La risposta come stringa `"yes"` o `"no"`. | STRING |
| `probability` | Probabilità di "sì" tra 0 e 1. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/it.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`

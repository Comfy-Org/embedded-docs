# Google Gemini Decision (Yes/No)

Poni una domanda sì/no riguardo al testo, alle immagini, all'audio o al video che colleghi e ottieni un booleano su cui instradare. Collega `result` a un nodo If/Else Switch per inviare l'esecuzione su uno dei due percorsi, e leggi `answer` e `probability` quando vuoi vedere perché il modello ha risposto in quel modo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `modello` | Modello da usare (predefinito: `"gemini-decision-1"`). | COMBO | Sì | `"gemini-decision-1"` |
| `domanda` | La domanda sì/no su ciò che è collegato, fino a 5000 caratteri. Formulala in modo che `"yes"` corrisponda al caso su cui agisci (predefinito: "Is there a person in the image?"). | STRING | Sì | 1 a 5000 caratteri |
| `soglia` | Probabilità di `"yes"` alla quale `result` diventa True. Le risposte chiaramente affermative ottengono un punteggio di circa 0.85-0.92, quindi 0.9 o più ne rifiuta molte (predefinito: 0.5). | FLOAT | Sì | 0.01 a 0.99 (passo 0.01) |
| `immagini` | Immagini su cui porre la domanda, fino a 16 complessive tramite gli slot espandibili (`image_1` ... `image_16`). Un'immagine in batch conta una volta per immagine. | IMAGE | No | Fino a 16 immagini |
| `audio` | Clip audio su cui porre la domanda. | AUDIO | No | - |
| `video` | Clip video su cui porre la domanda. | VIDEO | No | - |
| `testo` | Testo a cui si riferisce la domanda, come un prompt o una risposta di LLM, fino a 20000 caratteri. | STRING | No | Fino a 20000 caratteri |

Collega almeno uno tra `text`, `images`, `audio` o `video`; il nodo genera un errore quando non c'è nulla da esaminare. Con più immagini, assegnale i nomi `image_1`, `image_2` e così via all'interno della domanda: un batch viene espanso fotogramma per fotogramma, quindi i numeri contano i singoli fotogrammi attraverso gli slot nell'ordine di connessione.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `result` | True quando la probabilità di `"yes"` raggiunge `threshold`, altrimenti False. | BOOLEAN |
| `answer` | Il verdetto come stringa `"yes"` o `"no"`, seguendo lo stesso `threshold` di `result`. | STRING |
| `probability` | Probabilità di `"yes"` tra 0 e 1. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/it.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`

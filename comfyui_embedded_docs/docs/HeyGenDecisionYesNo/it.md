# HeyGen Decision (Yes/No)

Fai una domanda con risposta sì/no sul testo, sulle immagini, sull'audio o sul video che colleghi e ottieni un valore booleano su cui instradare. Collega `result` a un nodo If/Else Switch per scegliere tra due percorsi e leggi `answer` e `probability` per vedere quanto è stata chiara la risposta.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `modello` | Modello da usare. `heygen-decision-1-turbo` è più veloce e costa meno di `heygen-decision-1` (predefinito: `"heygen-decision-1"`). | COMBO | Sì | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `domanda` | La domanda sì/no su ciò che è collegato, fino a 5000 caratteri. Formulala in modo che il caso su cui agire corrisponda a "yes" (predefinito: "Is there a person in the image?"). | STRING | Sì | 1 a 5000 caratteri |
| `soglia` | Probabilità di "yes" alla quale `result` diventa true; le risposte chiare sono vicine a 0 o 1 (predefinito: 0.5). | FLOAT | Sì | 0.01 a 0.99 (passo 0.01) |
| `immagini` | Immagini su cui fare la domanda, fino a 4 in totale, contando ogni frame di un batch. Sono numerate da `image_1` a `image_4` in ordine tra i socket. | IMAGE | No | Fino a 4 immagini |
| `audio_1` | Audio su cui fare la domanda, fino a 30 minuti. | AUDIO | No | Fino a 30 minuti |
| `video_1` | Video su cui fare la domanda, fino a 60 secondi. | VIDEO | No | Fino a 60 secondi |
| `testo` | Testo su cui verte la domanda, ad esempio un prompt o una risposta di un LLM, fino a 20000 caratteri. | STRING | No | Fino a 20000 caratteri |

Collega almeno uno tra `text`, `images`, `audio_1` o `video_1` e fai riferimento a essi tramite il nome del socket all'interno della domanda, ad esempio "image_2 mostra la stessa persona di image_1?".

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `result` | True quando la probabilità di "yes" raggiunge `threshold`, false altrimenti. | BOOLEAN |
| `answer` | Il verdetto come stringa `"yes"` o `"no"`, seguendo lo stesso `threshold` di `result`. | STRING |
| `probability` | Probabilità di "yes" compresa tra 0 e 1. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionYesNo/it.md)

---
**Source fingerprint (SHA-256):** `5a6a606d5c6ef62eb3424bd54a0da3dc177da7d0acf4b5c235a62b78ad8d2df1`

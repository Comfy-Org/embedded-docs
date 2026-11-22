# HeyGen Decision (Score)

Valuta da 1 a 10 il testo, le immagini, l'audio o il video che colleghi e ottieni il punteggio insieme a un valore booleano che cambia stato in corrispondenza di una soglia impostata. Usalo per filtrare o ordinare gli output e collega `result` a un nodo If/Else Switch per agire in base al punteggio.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `modello` | Modello da utilizzare. `heygen-decision-1-turbo` è più veloce e costa meno di `heygen-decision-1` (predefinito: `"heygen-decision-1"`). | COMBO | Sì | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `domanda` | Cosa valutare, indicando cosa significano 1 e 10 (predefinito: "Rate the technical quality of the image from 1 (worst) to 10 (best)."). | STRING | Sì | 1 a 5000 caratteri |
| `soglia` | `result` è true quando il punteggio è almeno pari a questo valore. Le immagini pulite e nitide ottengono circa 7, quelle molto danneggiate circa da 3 a 5 (predefinito: 6.0). | FLOAT | Sì | 1.0 a 10.0 (passo 0.1) |
| `immagini` | Immagini da valutare, fino a 4 in totale, contando ogni fotogramma di un batch. Sono numerate da `image_1` a `image_4` in ordine attraverso i socket. | IMAGE | No | Fino a 4 immagini |
| `audio_1` | Audio da valutare, fino a 30 minuti. | AUDIO | No | Fino a 30 minuti |
| `video_1` | Video da valutare, fino a 60 secondi. | VIDEO | No | Fino a 60 secondi |
| `testo` | Testo a cui si riferisce la domanda, come un prompt o una risposta di un LLM, fino a 20000 caratteri. | STRING | No | Fino a 20000 caratteri |

Collega almeno un input da valutare e indica il relativo nome del socket all'interno della domanda, ad esempio "Quanto è nitida image_1?".

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `result` | True quando il punteggio è almeno pari a `threshold`, altrimenti false. | BOOLEAN |
| `score` | La valutazione da 1 a 10. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionScore/it.md)

---
**Source fingerprint (SHA-256):** `47f7aeab15292a2156b8da23c9911f4155c5b05c9ea9c0c502c30221aa522b58`

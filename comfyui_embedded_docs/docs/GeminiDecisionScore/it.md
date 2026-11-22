# Google Gemini Decision (Score)

Valuta da 1 a 10 il testo, le immagini, l'audio o il video che colleghi e ottieni il punteggio più un valore booleano che cambia stato in base a una soglia impostata. Usalo per filtrare o ordinare gli output, ad esempio per mantenere solo le immagini che ottengono almeno 7, e collega `result` a un nodo If/Else Switch per agire di conseguenza. Ogni esecuzione valuta nel suo insieme ciò che colleghi, quindi per filtrare singole immagini è necessario valutarle una alla volta.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da usare (predefinito: `"gemini-decision-1"`). | COMBO | Sì | `"gemini-decision-1"` |
| `question` | Cosa valutare, indicando cosa significano 1 e 10 (predefinito: "Rate the technical quality of the image from 1 (worst) to 10 (best)."). | STRING | Sì | 1 a 5000 caratteri |
| `threshold` | `result` è true quando il punteggio è almeno questo valore. Le immagini pulite e nitide ottengono circa da 7 a 8, quelle molto danneggiate circa da 3 a 5 (predefinito: 6.0). | FLOAT | Sì | 1.0 a 10.0 (passo 0.1) |
| `images` | Immagini da valutare, fino a 16 tramite gli slot espandibili (`image_1` ... `image_16`). Un'immagine inviata in batch conta una volta per ciascuna immagine. | IMAGE | No | Fino a 16 immagini |
| `audio` | Clip audio da valutare. | AUDIO | No | - |
| `video` | Clip video da valutare. | VIDEO | No | - |
| `text` | Testo a cui si riferisce la domanda, ad esempio un prompt o una risposta di un LLM, fino a 20000 caratteri. | STRING | No | Fino a 20000 caratteri |

Collega almeno uno tra `text`, `images`, `audio` o `video`; il nodo genera un errore quando non c'è nulla da valutare. Con più immagini, assegnale un nome come `image_1`, `image_2` e così via all'interno della domanda.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `result` | True quando il punteggio è almeno `threshold`, altrimenti false. | BOOLEAN |
| `score` | La valutazione da 1 a 10. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/it.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`

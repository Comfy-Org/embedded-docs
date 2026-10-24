# Ideogram Vector Generate SVG

Questo nodo genera un SVG modificabile da un prompt testuale con Ideogram Vector, con la possibilità di essere guidato da un massimo di 5 immagini di riferimento. Il risultato è markup vettoriale anziché un'immagine raster, quindi le forme restano modificabili in un editor vettoriale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare. Predefinito: `"ideogram-vector-1"`. | DYNAMIC_COMBO | Sì | `"ideogram-vector-1"` |
| `images` | Immagini di riferimento opzionali. L'immagine 1 è la fonte principale e le immagini da 2 a 5 sono riferimenti aggiuntivi; menzionale nel prompt come `@Image1`, `@Image2` e così via. Un input in batch conta una volta per immagine. | AUTOGROW | No | da 0 a 5 immagini |
| `prompt` | Descrizione dell'SVG. Supporta riferimenti in stile `@Image1` alle immagini di input. | STRING | Sì | da 1 a 9500 caratteri |
| `aspect_ratio` | `"auto"` segue l'immagine 1, oppure il prompt quando nessuna immagine è collegata. Predefinito: `"auto"`. | COMBO | Sì | `"auto"`<br>`"1:3"`<br>`"1:2"`<br>`"9:16"`<br>`"10:16"`<br>`"2:3"`<br>`"3:4"`<br>`"4:5"`<br>`"1:1"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:10"`<br>`"16:9"`<br>`"2:1"`<br>`"3:1"` |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo. Predefinito: `"medium"`. | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seme per la generazione. Lo stesso prompt, le stesse immagini, le stesse impostazioni e lo stesso seme producono lo stesso SVG. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

**Vincoli:**

* Il prompt deve contenere tra 1 e 9500 caratteri.
* `images` accetta al massimo 5 immagini, conteggiate per immagine quando l'input è in batch, e ogni immagine deve avere un rapporto d'aspetto compreso tra 1:6 e 6:1.
* Le immagini il cui lato più lungo supera 2048 pixel vengono ridimensionate prima del caricamento.
* Fare riferimento a un'immagine non collegata, ad esempio `@Image4` con solo due immagini fornite, genera un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `SVG` | L'SVG generato come markup vettoriale modificabile. | SVG |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorGenerateApi/it.md)

---
**Source fingerprint (SHA-256):** `5bd24ad48d6c26daf43f84544a9c22a18961dea645799104591f3785a851f819`

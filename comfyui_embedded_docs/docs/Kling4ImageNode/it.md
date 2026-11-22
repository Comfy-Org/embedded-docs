# Kling 4.0 Image

Genera o modifica immagini con Kling 4.0 da un prompt testuale e fino a 10 immagini di riferimento. Richiedi una singola immagine, oppure lascia che il nodo restituisca una serie di immagini correlate che mantengono gli stessi personaggi e stile.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `immagini di riferimento` | Slot espandibili per immagini di riferimento (`image_1` ... `image_10`). Fai riferimento ad esse nel prompt come `@Image1`, `@Image2` e così via. | AUTOGROW | No | 0 a 10 immagini |
| `prompt` | Descrizione dell'immagine. Fai riferimento alle immagini collegate come `@Image1`, `@Image2`, ... Predefinito: stringa vuota. | STRING | Sì | Testo multiriga |
| `risoluzione` | Risoluzione dell'immagine di output. Predefinito: `"2K"`. | COMBO | Sì | `"2K"`<br>`"4K"`<br>`"8K"` |
| `rapporto d'aspetto` | Proporzioni dell'immagine di output. `"auto"` segue le immagini di riferimento, altrimenti il prompt. Predefinito: `"auto"`. | COMBO | Sì | `"auto"`<br>`"9:16"`<br>`"2:3"`<br>`"3:4"`<br>`"1:1"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `numero di immagini nella serie` | Genera una serie di immagini correlate che mantengono gli stessi personaggi e stile. `"auto"` lascia che il modello scelga da 2 a 10 immagini. Predefinito: `"disabled"`. | COMBO | Sì | `"disabled"`<br>`"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

**Vincoli e comportamento:**

* È possibile collegare al massimo 10 immagini di riferimento.
* Ogni immagine deve essere di almeno 300x300 pixel con proporzioni comprese tra 2:5 e 5:2.
* Un prompt che menziona `@ImageN` genera un errore quando sono collegate meno di N immagini.
* Con `series_amount` impostato su `"disabled"` il nodo restituisce un'immagine; qualsiasi altro valore restituisce un batch di quel numero di immagini.
* Il prezzo di una chiamata varia in base alla risoluzione, al numero di immagini di riferimento e al numero di immagini nella serie.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `image` | L'immagine generata, o un batch di immagini quando `series_amount` è abilitato. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageNode/it.md)

---
**Source fingerprint (SHA-256):** `7840b108419e759942aed332456cab73e748d9f018462011da3b1293646a4ffe`

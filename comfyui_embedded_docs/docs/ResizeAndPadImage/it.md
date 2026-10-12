# ResizeAndPadImage

Il nodo ResizeAndPadImage ridimensiona un'immagine per adattarla alle dimensioni specificate mantenendo le proporzioni originali. Ridimensiona l'immagine proporzionalmente verso il basso per adattarla alla larghezza e all'altezza di destinazione, quindi aggiunge padding attorno ai bordi per riempire lo spazio rimanente. Il colore del padding e il metodo di interpolazione possono essere personalizzati per controllare l'aspetto delle aree di padding e la qualità del ridimensionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da ridimensionare e a cui aggiungere padding | IMAGE | Sì | - |
| `target_width` | La larghezza desiderata dell'immagine di output (predefinito: 512) | INT | Sì | da 1 a MAX_RESOLUTION |
| `target_height` | L'altezza desiderata dell'immagine di output (predefinito: 512) | INT | Sì | da 1 a MAX_RESOLUTION |
| `padding_color` | Il colore da usare per le aree di padding attorno all'immagine ridimensionata (predefinito: "white") | COMBO | Sì | "white"<br>"black" |
| `interpolation` | Il metodo di interpolazione usato per ridimensionare l'immagine (predefinito: "area") | COMBO | Sì | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine di output ridimensionata e con padding | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/it.md)

---
**Source fingerprint (SHA-256):** `cc516caee9f466d557e1c8e3c7fcef25acc1e33d181bc4b100302dc93530cb95`

# QuiverImageToSVGNodeV2

Vettorializza un'immagine raster in una grafica vettoriale scalabile (SVG) con Quiver AI. L'immagine viene inviata all'API di Quiver AI, che restituisce il risultato vettorializzato.

Selezionando un `model` vengono mostrati i parametri specifici del modello elencati di seguito.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `modello` | Modello da usare per la vettorializzazione SVG. | DYNAMIC_COMBO | Sì | `"arrow-2"`<br>`"arrow-2-telos"` |
| `image` | Immagine di input da vettorializzare. | IMAGE | Sì | N/A |
| `auto_crop` | Ritaglia automaticamente sul soggetto dominante. Parametro avanzato (predefinito: False). | BOOLEAN | Sì | `True`<br>`False` |
| `target_size` | Ridimensionamento quadrato applicato all'immagine di input prima della vettorializzazione, in pixel. 0 mantiene la dimensione sorgente, che produce una vettorializzazione più pulita rispetto a forzare un ridimensionamento; qualsiasi altro valore inferiore a 128 viene portato a 128. Questo non imposta il canvas di output; usa `width` e `height` per farlo. Parametro avanzato (predefinito: 0). | INT | Sì | 0 a 4096 |
| `width` | Larghezza del canvas SVG di output (viewBox), in unità utente. Imposta sia `width` sia `height` per controllare la dimensione e le proporzioni dell'output; lascia uno dei due a 0 per far scegliere al modello, che di solito produce un canvas quadrato. Parametro avanzato (predefinito: 0). | INT | Sì | 0 a 8192 |
| `height` | Altezza del canvas SVG di output (viewBox), in unità utente. Imposta sia `width` sia `height` per controllare la dimensione e le proporzioni dell'output; lascia uno dei due a 0 per far scegliere al modello, che di solito produce un canvas quadrato. Parametro avanzato (predefinito: 0). | INT | Sì | 0 a 8192 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal valore del seed. Questo parametro ha la funzionalità "control after generate" (predefinito: 42). | INT | Sì | 0 a 2147483647 |

### Input specifici del modello

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reasoning_effort` | Quanto ragionamento impiega il modello prima di disegnare. Livelli più alti migliorano il dettaglio e costano più token. Usato solo dai modelli `"arrow-2"` e `"arrow-2-telos"` (predefinito: `"high"`). | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | Controllo della casualità. Valori più alti aumentano la casualità. Non usato dal modello `"arrow-2-telos"`. Parametro avanzato (predefinito: 1.0). | FLOAT | Sì | 0.0 a 2.0 (passo 0.1) |
| `top_p` | Parametro di campionamento nucleus. Non usato dal modello `"arrow-2-telos"`. Parametro avanzato (predefinito: 1.0). | FLOAT | Sì | 0.05 a 1.0 (passo 0.05) |
| `presence_penalty` | Penalità di presenza dei token. Non usato dal modello `"arrow-2-telos"`. Parametro avanzato (predefinito: 0.0). | FLOAT | Sì | -2.0 a 2.0 (passo 0.1) |

**Nota:** `target_size` viene applicato prima della vettorializzazione e non modifica il canvas di output. Lascia `width` o `height` a 0 per far scegliere al modello la dimensione del canvas.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `SVG` | L'output SVG vettorializzato. | SVG |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `3531975fd46f5514e6d13b73bbbda413b7a08d8e36afeea73945ae7ea68d7216`

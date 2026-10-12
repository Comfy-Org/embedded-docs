# SAM3_Detect

## Panoramica

Il nodo SAM3 Detect esegue rilevamento e segmentazione a vocabolario aperto utilizzando descrizioni testuali, riquadri di delimitazione o prompt a punti. Può identificare e segmentare oggetti in un'immagine in base a ciò che descrivi nel testo, a dove disegni i riquadri o a dove fai clic con i punti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello SAM3 da usare per il rilevamento e la segmentazione | MODEL | Sì | - |
| `image` | L'immagine di input da elaborare | IMAGE | Sì | - |
| `conditioning` | Condizionamento testuale da CLIPTextEncode. Richiesto quando si usano prompt testuali per il rilevamento | CONDITIONING | No | - |
| `bboxes` | Riquadri di delimitazione entro cui segmentare. Può essere un singolo riquadro (applicato a tutti i frame), un elenco di riquadri (applicato a tutti i frame) o un elenco di elenchi (riquadri per frame). Se fornito senza condizionamento testuale, il nodo segmenta all'interno di ciascun riquadro | BOUNDING_BOX | No | - |
| `positive_coords` | Prompt a punti positivi in formato JSON `[{"x": int, "y": int}, ...]` usando coordinate in pixel. Sono punti che desideri includere nella segmentazione | STRING | No | - |
| `negative_coords` | Prompt a punti negativi in formato JSON `[{"x": int, "y": int}, ...]` usando coordinate in pixel. Sono punti che desideri escludere dalla segmentazione | STRING | No | - |
| `threshold` | Soglia di confidenza per i rilevamenti basati su testo. Vengono mantenuti solo i rilevamenti con punteggio superiore a questo valore (predefinito: 0.5) | FLOAT | No | 0.0 to 1.0 |
| `refine_iterations` | Numero di passaggi di rifinitura del decoder SAM. Valori più alti possono migliorare la qualità della maschera. Impostare a 0 per usare le maschere grezze del rilevatore senza rifinitura (predefinito: 2) | INT | No | 0 to 5 |
| `individual_masks` | Se abilitato, restituisce maschere separate per ciascun oggetto rilevato invece di combinarle in un'unica maschera (predefinito: False) | BOOLEAN | No | True/False |

### Vincoli e note sui parametri

- **Prompt testuali**: Per usare il rilevamento basato su testo, devi fornire l'input `conditioning`. Quando viene fornito il condizionamento testuale, il nodo esegue il rilevamento guidato dal testo sull'immagine.
- **Prompt a riquadri**: Quando vengono forniti `bboxes` senza condizionamento testuale, il nodo segmenta l'area all'interno di ciascun riquadro di delimitazione.
- **Prompt a punti**: Quando vengono forniti `positive_coords` o `negative_coords`, il nodo usa la segmentazione basata su punti. I punti vengono ridimensionati automaticamente alla risoluzione interna del modello.
- **Tipi di prompt multipli**: Puoi combinare diversi tipi di prompt. Ad esempio, puoi fornire sia il condizionamento testuale sia i riquadri di delimitazione per limitare il rilevamento testuale ad aree specifiche.
- **Elaborazione in batch**: Il nodo supporta immagini in batch. Quando si elaborano più frame, i riquadri di delimitazione possono essere forniti per frame usando un formato a elenco di elenchi.
- **Formato JSON per i punti**: Le coordinate dei punti devono essere fornite come stringhe JSON valide nel formato `[{"x": 100, "y": 200}, {"x": 150, "y": 250}]`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `masks` | Maschere di segmentazione. Quando `individual_masks` è False (predefinito), restituisce un'unica maschera combinata per frame. Quando è True, restituisce maschere individuali per ciascun oggetto rilevato | MASK |
| `bboxes` | Riquadri di delimitazione rilevati con coordinate e punteggi di confidenza. Ogni riquadro include i valori `x`, `y`, `width`, `height` e `score` | BOUNDING_BOX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_Detect/it.md)

---
**Source fingerprint (SHA-256):** `3f61343c284c249476f2010831863c6094260b11d0a348003b270a126c67d399`

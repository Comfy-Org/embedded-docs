# BerniniConditioning

Il nodo BerniniConditioning prepara i dati di condizionamento video e immagine per il modello Wan2.2-A14B. Codifica video sorgente, video di riferimento e immagini di riferimento usando il VAE fornito, quindi li collega ai dati di condizionamento come token in-context. Il task viene dedotto automaticamente da quali input sono collegati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `positive` | Dati di condizionamento positivi | CONDITIONING | Sì | - |
| `negative` | Dati di condizionamento negativi | CONDITIONING | Sì | - |
| `vae` | Modello VAE usato per codificare input video e immagine | VAE | Sì | - |
| `width` | Larghezza del latent di output (predefinito: 832) | INT | Sì | da 16 a 8192 (passo: 16) |
| `height` | Altezza del latent di output (predefinito: 480) | INT | Sì | da 16 a 8192 (passo: 16) |
| `length` | Numero di frame nel latent di output (predefinito: 81) | INT | Sì | da 1 a 8192 (passo: 4) |
| `batch_size` | Numero di video da generare in un singolo batch (predefinito: 1) | INT | Sì | da 1 a 4096 |
| `source_video` | Video sorgente da modificare o di cui riapplicare lo stile (v2v, rv2v). Ridimensionato a width/height e tagliato a length. | IMAGE | No | - |
| `reference_video` | Video da inserire nel video sorgente (ads2v). Tagliato a length e ridimensionato mantenendo le proporzioni (lato lungo limitato a ref_max_size). | IMAGE | No | - |
| `reference_images` | Immagini di riferimento iniettate come token in-context (r2v, rv2v). Ogni immagine viene codificata indipendentemente con il proprio rapporto d'aspetto nativo (lato lungo limitato a ref_max_size). È possibile fornire fino a 8 immagini. | IMAGE | No | da 0 a 8 immagini |
| `ref_max_size` | Dimensione massima per il lato lungo di reference_video e reference_images. Ridimensionato mantenendo le proporzioni e arrotondato a 16px (predefinito: 848). | INT | No | da 16 a 8192 (passo: 16) |

**Nota:** Il task viene dedotto da quali input sono collegati:
- Nessun input collegato → da testo a video (t2v)
- Solo `source_video` → da video a video (v2v)
- `source_video` + `reference_images` → editing video guidato da riferimenti (rv2v)
- Solo `reference_images` → da riferimento a video (r2v)
- `source_video` + `reference_video` → inserimento di immagine/video in video (ads2v)

I flussi di contesto vengono collegati in un ordine fisso: `source_video` (ID sorgente 1), poi `reference_video` (ID sorgente 2), poi ciascuna immagine di riferimento (ID sorgente 3, 4, ...). Un input di immagini di riferimento contenente più immagini contribuisce con un flusso per immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `positive` | Condizionamento positivo con latent di contesto allegati | CONDITIONING |
| `negative` | Condizionamento negativo con latent di contesto allegati | CONDITIONING |
| `latent` | Tensore latent vuoto con dimensioni corrispondenti a width, height, length e batch_size specificati | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BerniniConditioning/it.md)

---
**Source fingerprint (SHA-256):** `70b5026f9479249bc5d1fe4695583193216e34e1b092764ac30e0ec3b7eba670`

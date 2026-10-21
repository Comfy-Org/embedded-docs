# MOSS-Image Color/Depth Control

Aggiunge ai conditioning le mappe delle regioni colore e di profondità di un adattatore di controllo colore/profondità MOSS-Image. Collega i conditioning positivo e negativo, un VAE e una o entrambe le mappe: le mappe vengono codificate in latenti, unite in un segnale di controllo colore/profondità e associate al conditioning per la parte del campionamento scelta. Usalo insieme a un adattatore di controllo MOSS-Image caricato tramite un caricatore LoRA.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `positive` | Conditioning positivo a cui associare il segnale di controllo. | CONDITIONING | Sì | N/A |
| `negative` | Conditioning negativo a cui associare il segnale di controllo. | CONDITIONING | Sì | N/A |
| `vae` | VAE usato per codificare le mappe in latenti. | VAE | Sì | N/A |
| `color_map` | Un colore piatto per regione, alla dimensione dell'output. I colori sono solo ID di regione. | IMAGE | No | N/A |
| `depth_map` | Mappa di profondità alla dimensione dell'output; il primo piano è bianco. | IMAGE | No | N/A |
| `strength` | Ridimensiona il contributo delle mappe ai token dell'immagine. 0.0 equivale a nessuna mappa, 1.0 è l'intensità addestrata (predefinito: 1.0). | FLOAT | Sì | 0.0 a 10.0 (passo: 0.01) |
| `start_percent` | Percentuale di campionamento a cui inizia il controllo (predefinito: 0.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.001) |
| `end_percent` | Percentuale di campionamento a cui termina il controllo. Terminare prima mantiene il layout e la profondità, mentre i passaggi rimanenti rendono le forme meno rigide (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.001) |

**Nota:** Collega almeno una tra `color_map` e `depth_map`; senza nessuna delle due, il nodo restituisce i conditioning invariati. Una mappa mancante viene sostituita da zeri, quindi funzionano sia le configurazioni con solo colore sia quelle con sola profondità. Quando le due mappe hanno dimensioni diverse, quella più piccola viene ridimensionata alla dimensione dell'altra. Questo nodo è contrassegnato come sperimentale in ComfyUI.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `positive` | Il conditioning positivo con il segnale di controllo associato. | CONDITIONING |
| `negative` | Il conditioning negativo con il segnale di controllo associato. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageControl/it.md)

---
**Source fingerprint (SHA-256):** `c4a40c76f26237408e47cb9f683c13bccc3507bd775bec1b89919947a308c115`

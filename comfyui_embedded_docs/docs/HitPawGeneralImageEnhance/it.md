# HitPaw General Image Enhance

Questo nodo migliora le immagini a bassa risoluzione ingrandendole fino alla super-risoluzione, rimuovendo al contempo artefatti e rumore. Invia l'immagine a un'API esterna per l'elaborazione e può regolare automaticamente la dimensione di input per rimanere entro il limite di output consentito. La dimensione massima consentita dell'output è 32 megapixel.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello di miglioramento da utilizzare. Il modello `generative_portrait` è ottimizzato per i ritratti, mentre `generative` è un modello di uso generale. | COMBO | Sì | `"generative_portrait"`<br>`"generative"` |
| `image` | L'immagine di input da migliorare. | IMAGE | Sì | - |
| `upscale_factor` | Il fattore di ingrandimento delle dimensioni dell'immagine. Un fattore 1 significa nessun ingrandimento, 2 raddoppia le dimensioni, 4 le quadruplica. | COMBO | Sì | `1`<br>`2`<br>`4` |
| `auto_downscale` | Ridimensiona automaticamente verso il basso l'immagine di input se l'output supererebbe il limite. (predefinito: `False`) | BOOLEAN | No | - |

**Nota:** Il nodo genera un errore se la dimensione calcolata dell'output (larghezza input × upscale_factor × altezza input × upscale_factor) supera 32.000.000 pixel (32MP) e `auto_downscale` è disabilitato. Quando `auto_downscale` è abilitato, il nodo riduce automaticamente la dimensione dell'immagine di input o il fattore di ingrandimento (o entrambi) in modo che l'output rientri nel limite di 32MP. Il `model` selezionato e `upscale_factor` vengono combinati nel nome del modello inviato al servizio.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine di output migliorata e ingrandita. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/it.md)

---
**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`

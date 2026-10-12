# EmptyLatentHunyuan3Dv2

Questo nodo crea un batch di campioni latenti vuoti (tutti zero) formattati per i modelli di generazione 3D Hunyuan3Dv2. Produce il tensore latente con la forma corretta che funge da punto di partenza per i flussi di lavoro di generazione 3D, con il latente etichettato come tipo "hunyuan3dv2".

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `resolution` | La dimensione di risoluzione dello spazio latente da creare (predefinito: 3072) | INT | Sì | 1 - 8192 |
| `batch_size` | Il numero di immagini latenti nel batch (predefinito: 1) | INT | Sì | 1 - 4096 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `LATENT` | Un tensore latente vuoto di forma [batch_size, 64, resolution] contenente campioni riempiti di zeri, etichettato con il tipo "hunyuan3dv2" | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/it.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`

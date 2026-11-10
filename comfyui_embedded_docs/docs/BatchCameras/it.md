# Batch Cameras

Unisce camere e orbite delle camere in un unico elenco di camere, nell'ordine di input. Render Mesh e Render Splat eseguono il rendering di un'immagine per ciascuna camera nell'elenco, ed è così che viene costruito un rendering multi-vista.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `cameras` | Slot espandibile di camere, da Create Camera Info, Create Camera Orbit o da un visualizzatore. Un elenco di camere viene considerato come l'insieme di tutte le camere in esso contenute. | AUTOGROW | Sì | 1 a 50 camere |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `camera_info` | Un unico elenco di camere che contiene ogni camera di input, nell'ordine di input. | LOAD3D_CAMERA |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchCameras/it.md)

---
**Source fingerprint (SHA-256):** `a5ddae7f539a2d70efc1b156f7b4ec4b219d7cf78544b882f7b8f9538ae9a88d`

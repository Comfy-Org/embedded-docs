# RenderUVAtlas

Renderizza il layout UV di una mesh come immagine. Ogni regione UV connessa (chart) viene riempita con un colore distinto, e i bordi di confine del chart sono delineati in nero su uno sfondo grigio scuro.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | La mesh 3D di cui verrà renderizzato il layout UV. La mesh deve avere coordinate UV; altrimenti il nodo genera l'errore "mesh has no UVs to render. Run UnwrapMesh first." | MESH | Sì | - |
| `resolution` | La larghezza e l'altezza, in pixel, dell'immagine quadrata renderizzata (predefinito: 1024). | INT | Sì | 64 to 4096 (step 64) |

Nota: Se la mesh contiene una dimensione batch (array UV o array di facce 3D), viene renderizzato solo il primo elemento del batch.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine dell'atlante UV renderizzata, restituita come batch di una singola immagine. Ogni chart UV è colorato, e i bordi di confine del chart sono delineati in nero. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/it.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`

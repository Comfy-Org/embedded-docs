# MoGeRender

Questo nodo riceve un pacchetto MOGE_GEOMETRY (prodotto da un nodo di stima depth/normal MoGe) e lo renderizza in un formato immagine standard. È possibile scegliere di produrre in output una mappa di profondità, una mappa di profondità colorata, una mappa delle normali o una maschera.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Il pacchetto di dati geometrici proveniente da un nodo di stima MoGe. | MOGE_GEOMETRY | Sì | N/D |
| `output` | Il tipo di immagine da renderizzare dai dati geometrici. `depth` produce una mappa di profondità in scala di grigi, `depth_colored` produce una mappa di profondità colorata, `normal_opengl` e `normal_directx` producono mappe delle normali, e `mask` produce una maschera. DirectX rispetto a OpenGL controlla la convenzione del canale verde delle mappe delle normali. DirectX: verde = -Y verso il basso (Unreal). OpenGL: verde = +Y verso l'alto (Blender, Substance, Unity, glTF). (predefinito: "depth") | COMBO | Sì | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**Nota:** Il pacchetto geometrico deve contenere dati corrispondenti alla modalità `output` scelta. Le modalità `depth` e `depth_colored` richiedono dati di profondità nel pacchetto. Le modalità `normal_opengl` e `normal_directx` richiedono dati delle normali, oppure dati di punti dai quali vengono derivate le normali. La modalità `mask` richiede dati di maschera. Se i dati richiesti mancano, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `IMAGE` | L'immagine renderizzata come batch di tensori RGB. Il contenuto dipende dalla modalità `output`: una mappa di profondità in scala di grigi, una mappa di profondità colorata, una mappa delle normali, oppure una maschera convertita in RGB. La dimensione del batch di output corrisponde alla dimensione del batch della geometria in input. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/it.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`

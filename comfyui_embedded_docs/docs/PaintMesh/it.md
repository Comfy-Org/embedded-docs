# Dipingi mesh

PaintMesh prende una mesh 3D e un campo di colori voxel. Assegna a ciascun vertice il colore del voxel più vicino nel campo e restituisce la mesh con quei colori dei vertici applicati. Se il campo voxel è vuoto, la mesh viene colorata con colori dei vertici predefiniti a zero (nero).

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | La mesh da colorare. | MESH | Sì | N/A |
| `voxel_colors` | Campo voxel contenente i dati di colore usati per la colorazione. Dal campo vengono utilizzati solo i canali RGB del colore di base. | VOXEL | Sì | N/A |

Nota: quando le coordinate del campo voxel includono un canale indice di batch e la mesh di input contiene più elementi mesh, il nodo applica i colori separatamente a ciascun elemento mesh nel batch. Se un dato elemento mesh non ha voxel corrispondenti, riceve colori dei vertici predefiniti a zero (nero). I colori campionati vengono convertiti da sRGB a RGB lineare per la mesh di output, poiché il campo voxel può contenere dati PBR completi ma solo l'RGB del colore di base viene utilizzato per i colori dei vertici.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `mesh` | La mesh colorata con i colori dei vertici applicati. | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PaintMesh/it.md)

---
**Source fingerprint (SHA-256):** `55683bef55b18487ba660fe619d6ec176f786de346be12724751b71901c14116`

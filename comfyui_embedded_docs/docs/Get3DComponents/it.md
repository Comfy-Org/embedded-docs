# Ottieni componenti 3D

Get3DComponents analizza un file di modello 3D (GLB, GLTF, OBJ o STL) e lo converte in una mesh modificabile che può essere utilizzata da nodi di elaborazione mesh come decimate, remesh, UV unwrap e bake. Tutti i nodi e le primitive della scena vengono uniti in un'unica mesh con le rispettive trasformazioni applicate, mentre texture e impostazioni del materiale provengono dal primo materiale. È la controparte del nodo MeshToFile3D.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_3d` | File di modello 3D da Load 3D o da un altro nodo 3D. FBX/USDZ non sono supportati: convertire prima in GLB. | File3DGLB<br>File3DGLTF<br>File3DOBJ<br>File3DSTL<br>File3DAny | Sì | GLB<br>GLTF<br>OBJ<br>STL |

Nota: i file FBX e USDZ non sono supportati e causano un errore; convertirli prima in GLB o GLTF. Se il formato del file non può essere riconosciuto come GLB, GLTF, OBJ o STL, il nodo genera un errore che elenca i formati supportati. Se la scena glTF non contiene geometria triangolare, oppure se il file contiene indici di facce che puntano al di fuori dell'elenco dei vertici (segno di un file danneggiato), il nodo genera un errore. Se il file 3D contiene più materiali, vengono mantenute solo le texture e i fattori del primo materiale (viene registrato un avviso). Tutte le primitive della scena vengono unite in un'unica mesh con le rispettive trasformazioni applicate. Questo nodo è sperimentale.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `mesh` | Mesh modificabile contenente vertici, facce, UV, colori dei vertici, normali e tangenti, oltre alle informazioni sul materiale prelevate dal file (texture, metallic-roughness, normal map, colore emissivo, flag unlit, flag occlusion-in-metallic-roughness e dati del materiale). | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Get3DComponents/it.md)

---
**Source fingerprint (SHA-256):** `f2cdc9767a50503988484f09d2b3d110caf086b8cd84f65034a4a1e17a94405e`

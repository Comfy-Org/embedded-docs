# BakeTextureFromVoxel

Questo nodo esegue il baking di texture PBR su una mesh 3D usando il layout UV esistente della mesh. Rasterizza la mesh nello spazio UV e campiona colore e attributi materiale da un volume voxel sparso su ciascun texel, restituendo un'immagine di colore base più le mappe metallic e roughness. Non esegue l'unwrap della mesh, quindi un nodo di unwrap UV deve essere collegato a monte; le immagini risultanti sono pensate per essere abbinate alla stessa mesh in ApplyTextureToMesh per il salvataggio come GLB.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | La mesh 3D su cui eseguire il baking delle texture. Deve avere già un layout UV; un nodo di unwrap UV deve essere collegato a monte. | MESH | Sì | |
| `voxel_colors` | Volume voxel sparso contenente colori per-voxel e attributi PBR opzionali (canali metallic e roughness). | VOXEL | Sì | |
| `texture_size` | Risoluzione dell'atlante UV quadrato (nome visualizzato: «resolution», predefinito: 2048). | INT | Sì | da 64 a 8192 |
| `reference_mesh` | Mesh densa opzionale precedente alla decimazione; riproietta ogni texel sulla sua superficie reale prima del campionamento, eliminando il baking sfaccettato sulle mesh grossolane. | MESH | No | |

Note:

- La mesh di input deve avere UV. Se non sono presenti UV, il nodo genera un errore. Le UV devono essere 1:1 con i vertici (una UV per vertice).
- Quando la mesh e le coordinate voxel contengono una dimensione batch, ogni elemento del batch viene cotto separatamente. Se un elemento del batch non ha voxel o non ha facce, viene saltato e per esso viene emessa una texture nera.
- Quando `reference_mesh` viene fornito per un batch, viene associato per indice di batch, a meno che non contenga una sola mesh; in tal caso quella mesh viene usata per tutti gli elementi.
- I texel non coperti da alcun triangolo UV vengono riempiti dal texel coperto più vicino, in modo che le cuciture delle texture non incorporino nero.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `base_color` | Mappa di texture di colore base RGB. I valori sono float nell'intervallo 0–1. | IMAGE |
| `metallic` | Mappa metallic in scala di grigi (float, 0–1). Nera quando i colori dei voxel non contengono alcun canale metallic. | IMAGE |
| `roughness` | Mappa roughness in scala di grigi (float, 0–1). Nera quando i colori dei voxel non contengono alcun canale roughness. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/it.md)

---
**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`

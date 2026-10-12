# Texture mesh in immagine

Questo nodo estrae le texture precalcolate (baked) di una mesh e le restituisce come immagini separate: colore di base, metallico, rugosità, occlusione e normal map. I canali delle texture che non sono stati precalcolati vengono restituiti con valori predefiniti neutri: bianco per l'occlusione e un blu uniforme per la normal map.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | La mesh di cui estrarre le texture precalcolate. La mesh deve avere una texture di colore di base; le mesh che hanno solo colori per vertice (ad esempio dopo un nodo PaintMesh) non contengono una texture e causano un errore. | MESH | Sì | — |

Nota: La mesh deve avere una texture di colore di base precalcolata. In caso contrario, il nodo solleva un errore e consiglia di eseguire prima BakeTextureFromVoxel. Quando la texture metallic-roughness è assente, gli output `metallic` e `roughness` sono neri (0). L'output `occlusion` è bianco a meno che la mesh contenga occlusione ambientale precalcolata (il flag occlusion-in-metallic-roughness della mesh è impostato). L'output `normal_map` è un blu neutro uniforme quando non è stata precalcolata alcuna normal map.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `base_color` | La texture di colore di base della mesh come immagine. | IMAGE |
| `metallic` | Il canale metallico della texture occlusion-roughness-metallic della mesh, come immagine in scala di grigi. Nero (0) significa non metallico, bianco (1) significa completamente metallico. Nero quando la texture è assente. | IMAGE |
| `roughness` | Il canale di rugosità della texture occlusion-roughness-metallic della mesh, come immagine in scala di grigi. Nero quando la texture è assente. | IMAGE |
| `occlusion` | Il canale di occlusione ambientale della texture occlusion-roughness-metallic della mesh, come immagine in scala di grigi. Bianco (nessuna occlusione) quando l'occlusione ambientale non è stata precalcolata. | IMAGE |
| `normal_map` | La texture normal map della mesh. Una normal map neutra uniforme (0.5, 0.5, 1.0, che appare blu uniforme) quando non è stata precalcolata alcuna normal map. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/it.md)

---
**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`

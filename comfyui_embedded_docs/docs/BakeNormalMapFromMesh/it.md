# BakeNormalMapFromMesh

Questo nodo esegue il baking di una normal map in spazio tangente da una mesh high-poly sul layout UV di una mesh low-poly, catturando il dettaglio di superficie perso durante la decimazione. Collega la mesh low-poly con UV unwrap e la mesh high-poly da cui deriva, e il nodo restituisce in output un'immagine pronta per l'input `normal_map` di Apply Texture To Mesh.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `low_poly` | La mesh low-poly con UV unwrap che riceve il dettaglio sottoposto a baking. Deve avere UV esistenti; il nodo non esegue mai l'unwrap. | MESH | Sì | — |
| `high_poly` | La mesh high-poly il cui dettaglio di superficie viene trasferito tramite baking nel layout UV della low-poly. | MESH | Sì | — |
| `resolution` | Lunghezza del lato in pixel della normal map quadrata di output (predefinito: 1024). | INT | Sì | 64 a 8192 (passo 64) |
| `cage_distance` | Banda di ricerca sulla superficie, come frazione della diagonale del bounding box. Aumentala per patch errate/mancanti in caso di decimazione intensa; riducila se cattura attraverso gli spazi vuoti. Predefinito: 0.05. | FLOAT | Sì | 0.001 a 0.5 (passo 0.001) |
| `ignore_backfaces` | Salta le superfici high-poly rivolte dalla parte opposta rispetto al texel, così fessure/spazi chiusi non catturano la parete opposta. Disabilita solo se l'ordine di avvolgimento (winding) della high-poly è incoerente. Predefinito: true. | BOOLEAN | Sì | true / false |

Nota: `low_poly` deve avere coordinate UV. Se non ne ha, il nodo genera un errore perché esegue il baking sul layout UV esistente e non esegue l'unwrap della mesh. Quando `low_poly` è un batch, ogni elemento viene sottoposto a baking in ordine; se `high_poly` contiene un solo elemento, tale elemento viene riutilizzato per ogni elemento del batch. Le mesh vuote nel batch vengono saltate con un avviso e producono una normal map piatta di grigio medio (0.5). Se gli UV della low-poly fuoriescono dall'intervallo [0,1], vengono adattati uniformemente in [0,1] (con un avviso quando il layout sembra tiled/UDIM), così il baking e Apply Texture To Mesh usano gli stessi UV.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `normal_map` | La normal map in spazio tangente sottoposta a baking (convenzione glTF/OpenGL +Y) come immagine RGB quadrata resolution × resolution con valori in [0,1]. Collegala all'input `normal_map` di Apply Texture To Mesh. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/it.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`

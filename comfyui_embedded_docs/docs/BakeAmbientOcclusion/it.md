# BakeAmbientOcclusion

Genera una mappa di occlusione ambientale da una mesh high-poly nel layout UV di una mesh low-poly. L'output è un'immagine in scala di grigi in cui i texel bianchi indicano aree esposte e i texel scuri indicano cavità; è pensata per l'input occlusion del nodo Apply Texture To Mesh. Collegare la mesh low-poly con UV srotolate e la mesh high-poly da cui è stata decimata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `low_poly` | La mesh low-poly con UV srotolate in cui eseguire il bake. Deve avere UV; il nodo genera un errore se mancano. | MESH | Sì | - |
| `high_poly` | La mesh high-poly da cui è stata decimata la low-poly, usata come geometria sorgente per l'occlusione. | MESH | Sì | - |
| `resolution` | Risoluzione della texture in pixel; ogni texel riceve un valore di occlusione. Predefinito: 1024. | INT | Sì | da 64 a 8192 (passo 64) |
| `samples` | Raggi per texel. Più alto = più uniforme, più lento. Aumentare se risulta granuloso. Predefinito: 64. | INT | Sì | da 4 a 1024 (passo 4) |
| `max_distance` | Lunghezza del raggio, come frazione della diagonale del bounding box. Valori più piccoli = occlusione più stretta e più locale. Predefinito: 0.5. | FLOAT | Sì | da 0.01 a 2.0 (passo 0.01) |
| `strength` | Scala l'occlusione. >1 scurisce, <1 schiarisce. Predefinito: 1.0. | FLOAT | Sì | da 0.0 a 2.0 (passo 0.05) |
| `bias` | Sollevamento dell'origine del raggio dalla superficie, come frazione della diagonale del bounding box. Aumentare se anche le superfici piane mostrano macchie scure/buchi. Predefinito: 0.01. | FLOAT | Sì | da 0.0001 a 0.2 (passo 0.0005) |

Nota: `low_poly` deve avere coordinate UV — questo nodo non srotola mai la mesh. Se `high_poly` contiene un solo elemento del batch, viene riutilizzato per ogni elemento del batch di `low_poly`; gli elementi del batch di `low_poly` senza facce vengono saltati e sostituiti con un'immagine completamente bianca, registrando un avviso. Se le UV di `low_poly` fuoriescono dall'intervallo 0-1, vengono ricondotte uniformemente al suo interno e viene registrato un avviso quando viene rilevato un layout di tipo tiled/UDIM.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `occlusion` | Immagine di occlusione ambientale in scala di grigi con valori in [0,1] (bianco = aree esposte, scuro = cavità), un'immagine per ogni elemento del batch di `low_poly`. Destinata all'input occlusion del nodo Apply Texture To Mesh (inserita nella mappa ORM / occlusionTexture). | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/it.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`

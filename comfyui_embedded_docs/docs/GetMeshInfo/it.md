# Ottieni informazioni sulla mesh

Get Mesh Info riporta il numero di vertici e facce in una mesh, insieme agli attributi che contiene (come UV, colori dei vertici, normali e texture). Il report viene visualizzato sul nodo e restituito come output testuale, mentre la mesh stessa passa attraverso il nodo senza modifiche.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | La mesh da ispezionare. Il nodo conta i suoi vertici e facce, rileva quali attributi sono presenti e passa la mesh attraverso il nodo senza modifiche. | MESH | Sì | — |

Nota: quando l'input contiene più mesh (un batch), il report mostra i conteggi totali di vertici e facce per l'intero batch, più una suddivisione per mesh. Per i batch con padding a zeri, vengono usati i conteggi per elemento memorizzati nei dati della mesh.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `mesh` | La mesh originale, passata attraverso il nodo senza alcuna modifica. | MESH |
| `info` | Un report testuale multilinea con il conteggio dei vertici, il conteggio delle facce e gli attributi rilevati (uvs, vertex_colors, normals, tangents, texture, metallic_roughness, normal_map). Gli attributi di tipo texture sono mostrati con le loro dimensioni altezza × larghezza. I conteggi elevati sono formattati con virgole, ad esempio "1,234,567 (1.23M)" o "12,345 (12.3K)". Lo stesso testo viene visualizzato sul nodo. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetMeshInfo/it.md)

---
**Source fingerprint (SHA-256):** `cd168a5e69131a4a37f1f47014af2bc2ac2c8aa69e146cf33c2072480b35ebb2`

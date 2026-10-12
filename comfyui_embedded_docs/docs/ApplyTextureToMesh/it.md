# Applica texture alla mesh

Questo nodo collega le immagini delle texture precalcolate al layout UV di una mesh, in modo che possano essere esportate insieme alla mesh dal nodo SaveGLB. Fornisci la stessa mesh con UV srotolate da cui hai precalcolato le texture, insieme alle mappe immagine precalcolate. Le mappe opzionali metallic, roughness e occlusion vengono impacchettate in un'unica texture ORM; fornendo anche una normal map, vengono memorizzate le normali per vertice smooth e la base tangente necessarie per un'ombreggiatura corretta.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | La mesh con UV srotolate a cui verranno collegate le texture precalcolate. Deve essere la stessa mesh usata durante il bake; viene generato un errore se la mesh non ha UV. | MESH | Sì | — |
| `base_color` | L'immagine precalcolata del colore di base. Memorizzata come texture della mesh e limitata all'intervallo 0-1. | IMAGE | Sì | — |
| `metallic` | La mappa metallic precalcolata. Usata come canale blu della texture ORM combinata; il valore predefinito è 0 quando non fornita. | IMAGE | No | — |
| `roughness` | La mappa roughness precalcolata. Usata come canale verde della texture ORM combinata; il valore predefinito è 1 quando non fornita. | IMAGE | No | — |
| `occlusion` | La mappa di occlusione ambientale precalcolata. Usata come canale rosso della texture ORM combinata; il valore predefinito è 1 quando non fornita. Quando fornita, la texture ORM viene anche contrassegnata come texture di occlusione per SaveGLB. | IMAGE | No | — |
| `normal_map` | La normal map precalcolata in spazio tangente. Quando fornita, il nodo ricalcola le tangenti per vertice ed esporta normali per vertice smooth, affinché la normal map venga ombreggiata correttamente. | IMAGE | No | — |

Nota: L'input `mesh` deve avere coordinate UV; in caso contrario, il nodo genera un errore che chiede di collegare la stessa mesh con UV srotolate usata per il bake.

Nota: Quando uno tra `metallic`, `roughness` o `occlusion` è collegato, tutti e tre vengono impacchettati in un'unica texture ORM glTF con canali R = occlusion, G = roughness, B = metallic. Le mappe mancanti vengono riempite con valori predefiniti (occlusion 1, roughness 1, metallic 0), e le mappe con risoluzioni diverse vengono ridimensionate alla larghezza e all'altezza maggiori tra le mappe fornite.

Nota: Quando `normal_map` è collegato, le normali memorizzate della mesh vengono sostituite con normali per vertice smooth calcolate e viene aggiunta una base tangente per vertice. Le coordinate UV che cadono al di fuori dell'intervallo [0,1] vengono scalate uniformemente in [0,1] preservando le proporzioni; viene registrato un avviso se l'intervallo UV sembra un layout tiled/UDIM. Per le mesh in batch, la normalizzazione UV viene applicata separatamente a ciascun elemento del batch usando la stessa logica della fase di bake, così entrambe rimangono allineate.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `mesh` | La mesh di input con le immagini delle texture collegate al suo layout UV, pronta per essere salvata da SaveGLB. | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/it.md)

---
**Source fingerprint (SHA-256):** `7492922c9c7c0117366cb8b9017fc192eb8dd6b6594fd429044d60408693210e`

# MeshToFile3D

Questo nodo serializza una mesh in un oggetto file GLB che può essere passato ai nodi Save 3D o Preview 3D. Trasporta con sé tutti i dati della mesh, incluse UV, colori, normali, texture, mappe normali/di occlusione/emissive e impostazioni del materiale. Viene utilizzato solo il primo elemento di un batch con più elementi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | La mesh da convertire in un file GLB, incluse UV, colori, normali, texture, mappe normali/di occlusione/emissive e materiale. È supportato un solo elemento per batch; se un batch contiene più elementi, viene utilizzato il primo. | MESH | Sì | Mesh singola |

Nota: il nodo supporta un solo elemento per batch. Se la mesh di input contiene più di un elemento nel suo batch, viene registrato un avviso e viene utilizzato il primo elemento. La mesh deve contenere almeno un vertice e una faccia; una mesh vuota genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `model_3d` | Un oggetto file GLB (glTF Binary) contenente la mesh serializzata, pronto per essere salvato o visualizzato in anteprima da altri nodi 3D. | FILE3D |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshToFile3D/it.md)

---
**Source fingerprint (SHA-256):** `f004c2907c0df2e0127e49b4767d1624bf89c72665fc7028347a0b8a63a5772e`

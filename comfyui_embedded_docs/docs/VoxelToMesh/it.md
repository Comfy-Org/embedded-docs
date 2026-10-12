# VoxelToMesh

Il nodo VoxelToMesh converte dati voxel 3D in una geometria mesh estraendo una superficie a un valore di soglia specificato. Offre due algoritmi per l'estrazione della superficie: un metodo base che crea facce semplici simili a cubi, e un metodo surface net che produce mesh più levigate e dettagliate. Il nodo elabora ciascuna griglia voxel nell'input e genera vertici e facce che formano una rappresentazione mesh 3D.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `voxel` | I dati voxel di input da convertire in geometria mesh | VOXEL | Sì | - |
| `algorithm` | L'algoritmo usato per l'estrazione della superficie. "surface net" produce mesh più levigate, mentre "basic" crea facce semplici simili a cubi (predefinito: "surface net") | COMBO | Sì | `"surface net"`<br>`"basic"` |
| `threshold` | Il valore di soglia per l'estrazione della superficie. I voxel con valori superiori a questa soglia sono considerati solidi (predefinito: 0.6) | FLOAT | Sì | da -1.0 a 1.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MESH` | La mesh 3D generata contenente vertici e facce da tutte le griglie voxel di input. Se tutte le griglie voxel producono mesh con forme identiche, l'output è un tensore impilato; altrimenti, viene restituito un batch a lunghezza variabile | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/it.md)

---
**Source fingerprint (SHA-256):** `b600be13f1a484d8c0cc1f9c3918630d00c15d35008bcac0f677b21ef64b5d98`

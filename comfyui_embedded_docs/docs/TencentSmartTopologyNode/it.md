# TencentSmartTopologyNode

Questo nodo esegue una retopologia intelligente su un modello 3D, creando automaticamente una mesh nuova e più pulita con un numero di poligoni ottimizzato. Si connette a un'API Tencent Hunyuan 3D per elaborare il modello, supportando i formati di file GLB e OBJ fino a 200 MB. Il nodo restituisce il modello elaborato come file OBJ.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_3d` | Modello 3D di input (GLB o OBJ). Il file deve essere in formato GLB o OBJ e non può superare 200 MB. | FILE3D | Sì | - |
| `polygon_type` | Tipo di composizione della superficie. | STRING | Sì | `"triangle"`<br>`"quadrilateral"` |
| `face_level` | Livello di riduzione dei poligoni. | STRING | Sì | `"medium"`<br>`"high"`<br>`"low"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | No | da 0 a 2147483647 |

**Nota:** Il parametro `seed` viene utilizzato per attivare una nuova esecuzione del nodo, ma non è garantito che l'output finale sia identico per lo stesso valore di seed.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `OBJ` | Il modello 3D elaborato con topologia ottimizzata, restituito in formato OBJ. | FILE3D |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/it.md)

---
**Source fingerprint (SHA-256):** `effbccb4d239ffb6b575fc547dd54cbb61aa4508502345cb5bef1d66b320926b`

# Tencent3DPartNode

Questo nodo utilizza l'API Tencent Hunyuan3D per identificare e generare automaticamente i componenti di un modello 3D in base alla sua struttura. Accetta un modello FBX, lo elabora e restituisce un nuovo file FBX.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_3d` | Modello 3D in formato FBX. Il modello deve avere meno di 30000 facce. | FILE3D | Sì | FBX, Any |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | Sì | 0 to 2147483647 |

**Nota:** L'input `model_3d` supporta solo file in formato FBX. Se viene fornito un formato di file 3D diverso, il nodo genererà un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `FBX` | Il modello 3D elaborato, restituito come file FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/it.md)

---
**Source fingerprint (SHA-256):** `827b42559f4b2c341f08c58f53778d27c1c6afce607c36c8d1eae7c208c6a738`

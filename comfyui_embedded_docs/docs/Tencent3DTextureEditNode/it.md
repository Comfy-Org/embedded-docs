# Tencent3DTextureEditNode

Questo nodo utilizza l'API Tencent Hunyuan3D per modificare le texture di un modello 3D. Fornisci un modello 3D e una descrizione testuale delle modifiche desiderate; il nodo restituisce una nuova versione del modello con le texture ridisegnate in base al prompt fornito.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Modello 3D in formato FBX. Il modello deve avere meno di 100000 facce. | FILE3D | Sì | FBX, Any |
| `prompt` | Descrive la modifica delle texture. Supporta fino a 1024 caratteri UTF-8. | STRING | Sì |  |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | No | 0 a 2147483647 |

**Nota:** L'input `model_3d` deve essere un file in formato FBX. Gli altri formati di file 3D non sono supportati da questo nodo. Il parametro `prompt` è obbligatorio e deve avere una lunghezza compresa tra 1 e 1024 caratteri.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `GLB` | Il modello 3D elaborato in formato GLB. | FILE3D |
| `OBJ` | Il modello 3D elaborato in formato OBJ. | FILE3D |
| `texture_image` | L'immagine della texture appena generata per il modello 3D. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/it.md)

---
**Source fingerprint (SHA-256):** `eedddc8bd47a4af6e45a516f2817e7c1dded575d9e28ea9b66a1d7a39b93526c`

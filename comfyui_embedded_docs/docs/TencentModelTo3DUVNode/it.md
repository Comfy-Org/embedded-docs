# Hunyuan3D: Modello a UV

Questo nodo utilizza l'API Tencent Hunyuan3D per eseguire lo svolgimento UV su un modello 3D. Prende in input un file di modello 3D, lo invia all'API per l'elaborazione e restituisce il modello elaborato nei formati OBJ e FBX insieme a un'immagine di texture UV generata. Il modello di input deve avere meno di 30.000 facce.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Modello 3D di input (GLB, OBJ o FBX). Il modello deve avere meno di 30000 facce. | FILE3D | Sì | GLB<br>OBJ<br>FBX |
| `seed` | Il parametro `seed` controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 1) | INT | No | 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `OBJ` | Il file del modello 3D elaborato in formato OBJ. | FILE3D |
| `FBX` | Il file del modello 3D elaborato in formato FBX. | FILE3D |
| `uv_image` | L'immagine di texture UV generata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/it.md)

---
**Source fingerprint (SHA-256):** `b69519df055043555ab7f4d75cfb3b77b9011d5a8e93d0b3ba30c7a8674bd2cb`

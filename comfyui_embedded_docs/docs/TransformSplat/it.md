# TransformSplat

Il nodo Transform Splat applica trasformazioni di traslazione, rotazione e scala a uno splat gaussiano. Sposta, ruota e ridimensiona l'intero splat come un singolo oggetto e, quando viene applicata una scala non uniforme, rimodella anche ogni singolo splat gaussiano per ottenere risultati accurati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `splat` | Lo splat gaussiano da trasformare | SPLAT | Sì | - |
| `translate_x` | Traslazione lungo l'asse X (predefinito: 0.0) | FLOAT | Sì | -100.0 a 100.0 |
| `translate_y` | Traslazione lungo l'asse Y (predefinito: 0.0) | FLOAT | Sì | -100.0 a 100.0 |
| `translate_z` | Traslazione lungo l'asse Z (predefinito: 0.0) | FLOAT | Sì | -100.0 a 100.0 |
| `rotate_x` | Rotazione attorno all'asse X in gradi (predefinito: 0.0) | FLOAT | Sì | -360.0 a 360.0 |
| `rotate_y` | Rotazione attorno all'asse Y in gradi (predefinito: 0.0) | FLOAT | Sì | -360.0 a 360.0 |
| `rotate_z` | Rotazione attorno all'asse Z in gradi (predefinito: 0.0) | FLOAT | Sì | -360.0 a 360.0 |
| `scale_x` | Fattore di scala lungo l'asse X (predefinito: 1.0) | FLOAT | Sì | 0.01 a 100.0 |
| `scale_y` | Fattore di scala lungo l'asse Y (predefinito: 1.0) | FLOAT | Sì | 0.01 a 100.0 |
| `scale_z` | Fattore di scala lungo l'asse Z (predefinito: 1.0) | FLOAT | Sì | 0.01 a 100.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `splat` | Lo splat gaussiano trasformato con posizioni, scale e rotazioni aggiornate | SPLAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TransformSplat/it.md)

---
**Source fingerprint (SHA-256):** `19e6a7da7b4f0d8c9674ead2d35d742df460576b01c4ab4108dd59a2d08dfcb0`

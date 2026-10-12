# RecraftColorRGB

Crea un colore Recraft specificando singoli valori di rosso, verde e blu. Questo nodo accetta valori interi RGB (0-255) e li converte in un formato colore Recraft utilizzabile in altre operazioni Recraft. Puoi anche fornire opzionalmente una catena di colori Recraft esistente per estenderla con il nuovo colore.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `r` | Valore rosso del colore (predefinito: 0) | INT | Sì | 0-255 |
| `g` | Valore verde del colore (predefinito: 0) | INT | Sì | 0-255 |
| `b` | Valore blu del colore (predefinito: 0) | INT | Sì | 0-255 |
| `recraft_color` | Catena di colori Recraft esistente opzionale da estendere con il nuovo colore RGB | COLOR | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `recraft_color` | L'oggetto colore Recraft creato contenente i valori RGB specificati, oppure la catena di colori estesa se ne è stata fornita una esistente | COLOR |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/it.md)

---
**Source fingerprint (SHA-256):** `2246d266bc36d1aa7f115402b049f895f2b15d0085b84d1b0a813cdfb1b6e2fc`

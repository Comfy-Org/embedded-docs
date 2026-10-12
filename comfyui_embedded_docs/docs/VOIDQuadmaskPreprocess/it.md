# Preprocessore Quadmask VOID

## Panoramica

Il nodo VOIDQuadmaskPreprocess prepara una maschera per l'inpainting VOID convertendola in uno speciale "quadmask" a quattro livelli. Riceve una maschera di input, dilata opzionalmente la regione primaria, quindi quantizza i valori della maschera in quattro livelli distinti che rappresentano diverse regioni semantiche (oggetto primario, sovrapposizione, area interessata e sfondo). Infine, inverte e normalizza la maschera in modo che i valori di output siano nell'intervallo [0, 1], dove 1.0 indica l'area da rimuovere e 0.0 indica l'area da mantenere.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `mask` | La maschera di input da preprocessare. | MASK | Sì | N/A |
| `dilate_width` | Raggio di dilatazione per la regione primaria della maschera. Un valore di 0 significa che non viene applicata alcuna dilatazione. (predefinito: 0) | INT | No | Da 0 a 50 (passo: 1) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `quadmask` | La quadmask preprocessata con valori in [0, 1], che rappresenta quattro livelli discreti: 1.0 (oggetto primario da rimuovere), ~0.75 (sovrapposizione tra primario e area interessata), ~0.50 (regione interessata) e 0.0 (sfondo da mantenere). | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/it.md)

---
**Source fingerprint (SHA-256):** `a972ff74686baaa3a3659a74517d3b6f7335e8f62d09be9329d0e71d1fad137a`

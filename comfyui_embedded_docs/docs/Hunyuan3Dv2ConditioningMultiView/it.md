# Hunyuan3Dv2ConditioningMultiView

Il nodo Hunyuan3Dv2ConditioningMultiView combina gli output CLIP vision da un massimo di quattro viste (frontale, sinistra, posteriore e destra) in un unico condizionamento multi-vista. A ciascuna vista fornita viene aggiunta una codifica posizionale al proprio embedding CLIP vision, e gli embedding risultanti vengono concatenati. Il nodo restituisce un condizionamento positivo basato sugli embedding combinati e un condizionamento negativo riempito con zeri della stessa forma.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `front` | Output CLIP vision per la vista frontale. Input di vista opzionale. | CLIP_VISION_OUTPUT | No | - |
| `left` | Output CLIP vision per la vista sinistra. Input di vista opzionale. | CLIP_VISION_OUTPUT | No | - |
| `back` | Output CLIP vision per la vista posteriore. Input di vista opzionale. | CLIP_VISION_OUTPUT | No | - |
| `right` | Output CLIP vision per la vista destra. Input di vista opzionale. | CLIP_VISION_OUTPUT | No | - |

**Nota:** È necessario fornire almeno un input di vista affinché il nodo funzioni. Il nodo elabora solo le viste che contengono dati validi di output CLIP vision e salta le viste non connesse. Ciascuna vista riceve una codifica posizionale fissa in base al proprio slot (front, left, back, right), e gli embedding elaborati da tutte le viste fornite vengono uniti lungo la dimensione della sequenza.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Condizionamento positivo contenente gli embedding multi-vista combinati con codifica posizionale. | CONDITIONING |
| `negative` | Condizionamento negativo con valori zero corrispondenti alla forma del condizionamento positivo. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/it.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`

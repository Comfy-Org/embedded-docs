# Recraft Vettorizza Immagine

Genera grafica vettoriale SVG da un'immagine di input. Questo nodo converte immagini raster in formato vettoriale scalabile inviando ciascuna immagine all'API Recraft e restituendo i risultati in un singolo output SVG. Tale output contiene un documento SVG separato per ogni immagine elaborata; i documenti non vengono uniti in uno solo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `immagine` | L'immagine di input da convertire in formato SVG. Supporta l'elaborazione in batch di più immagini. | IMAGE | Sì | - |
| `versione` | La versione del vettorizzatore: `v1` è la versione standard, mentre `v1_pro` (Vectorizer Pro) produce SVG più puliti con curve morbide, linee rette e angoli netti, ideale per scritte e forme intricate (predefinito: "v1"). | COMBO | No | "v1"<br>"v1_pro" |
| `shape_stacking` | Come vengono impilate le forme nell'SVG: `hierarchical` dispone le forme a strati una sopra l'altra; `cut_out` crea forme che non si sovrappongono mai, per plotter, taglierine per vinile e serigrafia (predefinito: "hierarchical"). | COMBO | No | "hierarchical"<br>"cut_out" |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `SVG` | La grafica vettoriale generata. Il singolo output SVG contiene un documento SVG separato per ogni immagine elaborata. | SVG |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/it.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`

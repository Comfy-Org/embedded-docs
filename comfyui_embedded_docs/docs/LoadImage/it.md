# Carica Immagine

Il nodo LoadImage è progettato per caricare e preelaborare immagini da un percorso specificato. Gestisce formati immagine con più frame, applica le trasformazioni necessarie, come la rotazione basata sui dati EXIF, normalizza i valori dei pixel e genera facoltativamente una maschera per immagini con canale alfa. Questo nodo è essenziale per preparare le immagini a ulteriori elaborazioni o analisi all'interno di una pipeline.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | Il parametro 'image' specifica l'identificatore dell'immagine da caricare ed elaborare. È cruciale per determinare il percorso del file immagine e successivamente caricare l'immagine per la trasformazione e la normalizzazione. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine elaborata, con i valori dei pixel normalizzati e le trasformazioni applicate secondo necessità. È pronta per ulteriori elaborazioni o analisi. | `IMAGE` |
| `mask` | Un output opzionale che fornisce una maschera per l'immagine, utile in scenari in cui l'immagine include un canale alfa per la trasparenza. | `MASK` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImage/it.md)

# SAM3_TrackPreview

## Panoramica

Questo nodo crea un'anteprima video degli oggetti tracciati, disegnando ciascun oggetto tracciato con una distinta sovrapposizione colorata e un'etichetta numerica. Non restituisce tensori immagine o video — invece salva il video di anteprima risultante direttamente in un file temporaneo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `track_data` | I dati di tracciamento contenenti maschere impacchettate e informazioni sugli oggetti da un nodo di tracciamento SAM3. | TRACK_DATA | Sì | - |
| `images` | Immagini di input opzionali da usare come sfondo per l'anteprima. Se non fornite, viene usato uno sfondo nero. | IMAGE | No | - |
| `opacity` | L'opacità della sovrapposizione colorata applicata agli oggetti tracciati (predefinito: 0.5). | FLOAT | No | 0.0 to 1.0 (step: 0.05) |
| `fps` | La frequenza di fotogrammi del video di output (predefinito: 24.0). | FLOAT | No | 1.0 to 120.0 (step: 1.0) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `ui` | Un elemento UI che visualizza il video di anteprima generato. Non viene restituito alcun dato tensoriale. | PREVIEW_VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackPreview/it.md)

---
**Source fingerprint (SHA-256):** `76389f354c8acdf249137d966765069d530034a0f8eeb39d769bde3c0f7a1bd0`

# WanDancerPadKeyframesList

## Panoramica

Questo nodo riceve in input una sequenza di immagini e una traccia audio opzionale e le suddivide in un numero specificato di segmenti con padding. È progettato per preparare sequenze di keyframe per la generazione video, in cui ogni segmento viene portato a una lunghezza uniforme tramite padding e viene creata una maschera corrispondente per indicare quali frame sono validi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | La sequenza di immagini di input da suddividere in segmenti. | IMAGE | Sì | N/A |
| `segment_length` | Lunghezza di ciascun segmento in frame (predefinito: 149). | INT | Sì | 1 a 10000 |
| `num_segments` | Quanti segmenti con padding emettere come liste (predefinito: 1). | INT | Sì | 1 a 100 |
| `audio` | Audio da suddividere per ciascun segmento emesso. | AUDIO | No | N/A |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `keyframes_sequence` | Un elenco di sequenze di keyframe con padding, una per ciascun segmento. | IMAGE |
| `keyframes_mask` | Un elenco di maschere che indicano i frame validi per ciascun segmento. | MASK |
| `audio_segment` | Un elenco di segmenti audio, uno per ciascun segmento video. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/it.md)

---
**Source fingerprint (SHA-256):** `f9918166a75f688f1de6a09008780bc629bbdfb3b8d547de9ba8661ef07fc97e`

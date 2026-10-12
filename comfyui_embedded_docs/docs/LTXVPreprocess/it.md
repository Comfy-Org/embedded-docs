# LTXV Preprocess

Il nodo LTXVPreprocess applica una preelaborazione di compressione video alle immagini. Simula la perdita di qualità della compressione video codificando un'immagine come video MP4 a fotogramma singolo e decodificandola di nuovo, consentendo di controllare il livello di compressione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da elaborare | IMAGE | Sì | - |
| `img_compression` | Quantità di compressione da applicare all'immagine. Un valore di 0 disabilita completamente la compressione (predefinito: 35) | INT | No | 0-100 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output_image` | L'immagine di output elaborata con artefatti di compressione applicati | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/it.md)

---
**Source fingerprint (SHA-256):** `4381837f2778948e6d8b710cf1857ce9e579b3cc630223d97266162b9799342b`

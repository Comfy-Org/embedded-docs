# Vidu2ImageToVideoNode

Il nodo Vidu2 Image-to-Video Generation crea una sequenza video a partire da una singola immagine di input. Utilizza un modello Vidu2 specificato per animare la scena in base a un prompt testuale opzionale, controllando la durata, la risoluzione e l'intensità del movimento del video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello Vidu2 da utilizzare per la generazione video. Modelli diversi offrono diversi compromessi tra velocità e qualità. | COMBO | Sì | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` |
| `image` | Un'immagine da utilizzare come frame iniziale del video generato. È consentita una sola immagine. | IMAGE | Sì | - |
| `prompt` | Un prompt testuale opzionale per la generazione video (max 2000 caratteri). Il valore predefinito è una stringa vuota. | STRING | No | - |
| `duration` | La durata del video generato in secondi. Il valore predefinito è 5. | INT | Sì | da 1 a 10 |
| `seed` | Un valore di seed per la generazione di numeri casuali per garantire risultati riproducibili. Il valore predefinito è 1. | INT | No | da 0 a 2147483647 |
| `resolution` | La risoluzione di output del video generato. Questo parametro è avanzato. | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `movement_amplitude` | L'ampiezza del movimento degli oggetti nell'inquadratura. Questo parametro è avanzato. | COMBO | Sì | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Vincoli:**

- L'input `image` deve contenere esattamente un'immagine.
- Il rapporto d'aspetto dell'immagine di input deve essere compreso tra 1:4 e 4:1.
- Il testo del `prompt` è limitato a un massimo di 2000 caratteri.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `4cf56654286561f3d211ce50d0dce141880fe0e0a63aa45ab41ae0ff5ab6ccc3`

# Ideogram Vector Image to SVG

Questo nodo converte un'immagine in un SVG modificabile con Ideogram Vector. Il risultato è markup vettoriale anziché un'immagine raster, quindi le forme tracciate restano modificabili in un editor vettoriale. Le aree trasparenti di un'immagine con alpha restano trasparenti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare. Predefinito: `"ideogram-vector-1"`. | DYNAMIC_COMBO | Sì | `"ideogram-vector-1"` |
| `image` | L'immagine da convertire. Un input in batch viene convertito immagine per immagine e gli SVG risultanti vengono restituiti insieme. | IMAGE | Sì | - |
| `mode` | `"simple"` traccia meno forme, di dimensioni maggiori; `"default"` mantiene dettagli più fini. Predefinito: `"default"`. | COMBO | Sì | `"simple"`<br>`"default"` |

**Vincoli:**

* Le immagini il cui lato più lungo supera 2048 pixel vengono ridimensionate a una risoluzione inferiore prima del caricamento.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `SVG` | L'immagine convertita come markup vettoriale modificabile. | SVG |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorImageToSVGApi/it.md)

---
**Source fingerprint (SHA-256):** `6553291e9d887b31485b9cbf8f6ced4186470eb47e8621ebb0f4e5df6542123e`

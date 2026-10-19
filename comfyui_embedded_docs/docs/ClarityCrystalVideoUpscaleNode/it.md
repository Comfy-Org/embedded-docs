# Clarity AI Crystal Video Upscale

Esegui l'upscale di un video con Crystal Video Upscaler di Clarity AI, un upscaler ad alta fedeltà che rimane fedele alla sorgente. La clip viene caricata, ne viene aumentata la risoluzione in base al fattore impostato e viene restituita come video. L'output è limitato a 9 megapixel per fotogramma (ad esempio 4000x2250) e a 360 megapixel-secondo per clip, quindi clip grandi o lunghe vengono restituite a una risoluzione inferiore rispetto a quella richiesta dal fattore.

Selezionando un `model` vengono mostrati i parametri specifici di quel modello.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare. Selezionando un modello vengono mostrati i parametri specifici: `video` e `scale_factor`. | DYNAMIC_COMBO | Sì | `"crystal-video-upscaler"` |
| `video` | Il video da upscalare. | VIDEO | Sì | N/A |
| `scale_factor` | Fattore per moltiplicare larghezza e altezza del video. L'output è limitato a 9 megapixel per fotogramma e a 360 megapixel-secondo per clip, quindi i video grandi o lunghi vengono upscalati di meno; il fattore viene inoltre ridotto quando porterebbe un lato oltre 5120 pixel (predefinito: 2.0). | FLOAT | Sì | da 1.0 a 200.0 (passo 0.1) |

**Nota:** La clip può avere al massimo 5120 pixel per lato e al massimo 9 megapixel per fotogramma. La durata massima dipende dalle dimensioni del fotogramma e dalla frequenza fotogrammi: si ottiene dividendo 360 megapixel-secondo per i pixel del fotogramma e per la frequenza fotogrammi arrotondata per eccesso a un multiplo di 30 fps; quindi una clip 1080p a 30 fps può durare fino a circa 173 secondi. Le clip sopra 30 fps costano 2 volte tanto, sopra 60 fps 3 volte tanto, e così via.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video upscalato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalVideoUpscaleNode/it.md)

---
**Source fingerprint (SHA-256):** `ca44ed6591474421edaf7e4e99e6da62e0c2e4e66964b7dac51d45758150aaa8`

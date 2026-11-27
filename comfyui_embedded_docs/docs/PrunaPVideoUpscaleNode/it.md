# Pruna P-Video Upscale

Pruna P-Video Upscale ingrandisce un video a 720p, 1080p, 2K o 4K mantenendone le proporzioni e la traccia audio. La clip viene inviata a Pruna, la previsione viene interrogata periodicamente e il video ingrandito viene restituito. Una sorgente già pari o superiore alla dimensione di destinazione mantiene le proprie dimensioni e viene solo migliorata.

## Ingressi

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Video da ingrandire, fino a 512 MiB. I video più grandi di 10 megapixel possono essere inviati solo alla destinazione 2K o 4K. | VIDEO | Sì | Fino a 512 MiB |
| `target` | Area in pixel dell'output: 720p corrisponde a circa 0,9 megapixel, 1080p a 2,1, 2K a 3,7 e 4K a 8,3. La lunghezza massima della clip è limitata dalla destinazione: 2400, 1200, 600 o 300 fotogrammi, circa 100, 50, 25 o 12,5 secondi a 24 fps (predefinito: "1080p"). | COMBO | Sì | "720p"<br>"1080p"<br>"2K"<br>"4K" |
| `fps` | Frequenza fotogrammi dell'output (predefinito: "source"). "source" mantiene la frequenza del video, fino a 60; una frequenza superiore viene interpolata. Un output superiore a 30 fps costa il doppio, tranne con `turbo`. | COMBO | Sì | "source"<br>"16"<br>"24"<br>"25"<br>"30"<br>"48"<br>"50"<br>"60" |
| `turbo` | Ingrandimento più rapido con dettaglio più morbido, a un prezzo inferiore (predefinito: false). | BOOLEAN | No | true<br>false |

### Vincoli sui parametri

- La clip deve essere pari o inferiore a 512 MiB, misurati dopo la ricodifica in H.264 MP4.
- Il limite di fotogrammi è calcolato a un massimo di 30 fps: 2400 fotogrammi per 720p, 1200 per 1080p, 600 per 2K e 300 per 4K. Una clip più lunga richiede una destinazione inferiore, un `fps` inferiore o un taglio più breve.

## Uscite

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il video ingrandito con il suo audio originale. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaPVideoUpscaleNode/it.md)

---
**Source fingerprint (SHA-256):** `0c475fe2afc5804811ddacc6caf8565cf414e27cbbbc2d57175f39b28f927ab6`

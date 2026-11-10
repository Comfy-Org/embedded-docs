# LTX Video Upscale

Esegue l'upscaling di un video a 1080p, 4K o 8K, mantenendo proporzioni, frequenza dei fotogrammi e audio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Video da sottoporre a upscaling, con il lato corto di almeno 480 pixel e con risoluzione massima di 7680x4320 in entrambi gli orientamenti. Fino a 2401 fotogrammi per 1080p, 601 fotogrammi per 4K e 241 fotogrammi per 8K. | VIDEO | Sì | - |
| `resolution` | Dimensione di output, la massima che rientra in 1920x1080, 3840x2160 o 7680x4320, ruotata per i video verticali. Predefinito: `"4k"`. | COMBO | Sì | `"1080p"`<br>`"4k"`<br>`"8k"` |
| `seed` | Controlla se il nodo viene eseguito nuovamente; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | No | 0 a 4294967295 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il video sottoposto a upscaling, con l'audio mantenuto. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoUpscale/it.md)

---
**Source fingerprint (SHA-256):** `e9b3b760365568ab2f6572c5f4f28758d67c4f5795fc39716ed4f648aafef80e`

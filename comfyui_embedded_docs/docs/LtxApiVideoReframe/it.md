# LTX Video Reframe

Riquadra un video a una nuova risoluzione e proporzioni. L'area esterna al video originale viene generata per adattarsi al suo contenuto, così una clip verticale può diventare orizzontale o viceversa.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Video da riquadrare, fino a 60 secondi e 1800 fotogrammi, con ciascun lato compreso tra 64 e 4096 pixel. | VIDEO | Sì | - |
| `resolution` | Dimensione e proporzioni dell'output, a 720p o 1080p. Predefinito: `"(1080p) 1080x1920 (9:16)"`. | COMBO | Sì | `"(720p) 720x720 (1:1)"`<br>`"(720p) 720x900 (4:5)"`<br>`"(720p) 900x720 (5:4)"`<br>`"(720p) 720x1280 (9:16)"`<br>`"(720p) 1280x720 (16:9)"`<br>`"(1080p) 1080x1080 (1:1)"`<br>`"(1080p) 1080x1350 (4:5)"`<br>`"(1080p) 1350x1080 (5:4)"`<br>`"(1080p) 1080x1920 (9:16)"`<br>`"(1080p) 1920x1080 (16:9)"` |
| `placement` | Dove si trova il video originale nella nuova inquadratura. Il video riempie sempre un lato dell'inquadratura, quindi un'ancora lo sposta solo lungo l'altro lato. Predefinito: `"center"`. | DYNAMIC_COMBO | Sì | `"center"`<br>`"top"`<br>`"bottom"`<br>`"left"`<br>`"right"`<br>`"custom"` |
| `seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | No | 0 a 4294967295 |

### Input di Placement "custom"

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `x` | Bordo sinistro del video come frazione della larghezza dell'output. Predefinito: 0.25. | FLOAT | No | 0.0 a 0.99 (passo 0.01) |
| `y` | Bordo superiore del video come frazione dell'altezza dell'output. Predefinito: 0.25. | FLOAT | No | 0.0 a 0.99 (passo 0.01) |
| `width` | Larghezza del video come frazione della larghezza dell'output; l'altezza segue le proporzioni del video. Il video deve rimanere all'interno dell'inquadratura e può essere ingrandito al massimo di 2x. Predefinito: 0.5. | FLOAT | No | 0.01 a 1.0 (passo 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il video riquadrato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoReframe/it.md)

---
**Source fingerprint (SHA-256):** `85fcce4a8054fa8faf0085a55510ee09bce89afd1cf9f19d6ea45105549f2656`

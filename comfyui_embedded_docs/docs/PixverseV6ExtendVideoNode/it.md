# PixverseV6ExtendVideoNode

Questo nodo continua un video esistente usando il modello PixVerse V6, generando facoltativamente una traccia audio nativa insieme alla continuazione. Il video di origine deve essere più corto di 40 secondi e non più grande di 1920 pixel su ciascun lato. L'output mantiene la risoluzione del video di origine, quindi l'impostazione quality controlla la qualità con cui viene renderizzata la continuazione, non la dimensione del fotogramma.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video` | Video da continuare. | VIDEO | Sì | Più corto di 40 secondi; al massimo 1920 pixel di larghezza e altezza |
| `model` | Modello e impostazioni di generazione. | DYNAMIC_COMBO | Sì | "PixVerse V6" |

### Input di PixVerse V6

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt che descrive come il video deve continuare. (predefinito: vuoto) | STRING | Sì | 1–5000 caratteri |
| `quality` | Qualità di rendering della continuazione generata: 1080p è visibilmente migliore di 540p o 360p. Non ridimensiona mai: l'output mantiene la risoluzione del video di origine. (predefinito: "720p") | COMBO | Sì | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Durata del video generato in secondi. (predefinito: 5) | INT | Sì | 1–15 |
| `generate_audio` | Genera una traccia audio nativa insieme al video. (predefinito: true) | BOOLEAN | Sì | true / false |
| `seed` | Seme per la generazione del video. PixVerse lo registra ma non riproduce un'esecuzione a partire da esso. (predefinito: 42) | INT | Sì | 0–2147483647 |
| `negative_prompt` | Descrizione testuale facoltativa degli elementi indesiderati nel video. (predefinito: vuoto) | STRING | No | Fino a 2048 caratteri |
| `style` | Stile visivo facoltativo applicato all'intero video. (predefinito: "none") | COMBO | No | Molteplici opzioni disponibili; "none" è l'impostazione predefinita |

**Nota:** Il `video` di origine deve essere più corto di 40 secondi e al massimo 1920 pixel sia in larghezza che in altezza; i video più lunghi o più grandi vengono rifiutati. L'output generato mantiene la risoluzione del video di origine, quindi `quality` cambia la fedeltà di rendering, non la dimensione del fotogramma di output. Il `prompt` è obbligatorio e deve contenere tra 1 e 5000 caratteri dopo aver rimosso gli spazi bianchi. Il `negative_prompt`, quando fornito, è limitato a 2048 caratteri. Il `seed` viene registrato da PixVerse ma non può essere usato per riprodurre la stessa esecuzione.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `video` | Il video di continuazione generato, alla stessa risoluzione del video di origine. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ExtendVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `8bd2a04a5da95b39fb963922e2e54a7aa4efb670260fa38313d21db3af295029`

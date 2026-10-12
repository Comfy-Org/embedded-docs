# PixverseV6ImageToVideoNode

Questo nodo anima un'immagine di input con il modello PixVerse V6 e restituisce un video, facoltativamente con una traccia audio nativa. Il video di output mantiene le proporzioni dell'immagine di input.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da animare. | IMAGE | Sì | Immagine singola |
| `model` | Modello e impostazioni di generazione. | DYNAMIC_COMBO | Sì | "PixVerse V6" |

### Input di PixVerse V6

Queste impostazioni compaiono quando è selezionato il modello "PixVerse V6".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione del video (predefinito: vuoto). | STRING | Sì | Da 1 a 5000 caratteri |
| `quality` | Risoluzione di output. Imposta il lato lungo: 360p corrisponde a 640px, 540p a 1024px, 720p a 1280px, 1080p a 1920px (predefinito: "720p"). | COMBO | Sì | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Durata del video generato in secondi (predefinito: 5). | INT | Sì | Da 1 a 15 |
| `generate_audio` | Genera una traccia audio nativa insieme al video (predefinito: true). | BOOLEAN | Sì | true o false |
| `multi_clip` | Consente al modello di suddividere il video in diverse inquadrature invece di una ripresa continua (predefinito: false). | BOOLEAN | Sì | true o false |
| `seed` | Seed per la generazione del video. PixVerse lo registra ma non riproduce un'esecuzione a partire da esso (predefinito: 42, controllo dopo generate abilitato). | INT | Sì | Da 0 a 2147483647 |
| `negative_prompt` | Descrizione testuale facoltativa degli elementi indesiderati nel video (predefinito: vuoto). | STRING | No | Fino a 2048 caratteri |
| `style` | Stile visivo facoltativo applicato all'intero video (predefinito: nessuno). | COMBO | No | Più opzioni disponibili (preset di stile PixVerse V6) |

Nota: il prompt deve contenere almeno un carattere diverso da spazi e al massimo 5000 caratteri; il prompt negativo, se fornito, deve contenere al massimo 2048 caratteri. Il video di output corrisponde sempre alle proporzioni dell'immagine di input, quindi non è necessaria alcuna impostazione delle proporzioni. È accettata una sola immagine di input. PixVerse può rifiutare una richiesta quando la moderazione dei contenuti non ha esito positivo, quando l'account del provider ha esaurito i crediti o quando è già in corso il numero massimo di generazioni simultanee.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video generato, inclusa la traccia audio nativa quando `generate_audio` è abilitato. Le proporzioni corrispondono a quelle dell'immagine di input. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `6ecf958e510e7afc43f5f0e4e5dfd2b789aea02bec882d928326732501cee7b3`

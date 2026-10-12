# PixVerse V6 da testo a video

PixVerse V6 Text to Video genera un video da un prompt testuale utilizzando il modello V6 di PixVerse. Il nodo invia il prompt insieme al rapporto d'aspetto, alla risoluzione, alla durata e alle altre impostazioni scelte a PixVerse, attende il completamento della generazione e restituisce il video risultante — inclusa una traccia audio nativa quando la generazione audio è abilitata.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Impostazioni del modello e di generazione. Seleziona il modello e configura le sue opzioni di generazione. | DYNAMIC_COMBO | Sì | "PixVerse V6" |

### Input di PixVerse V6

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione del video. (predefinito: "") | STRING | Sì | 1–5000 caratteri |
| `aspect_ratio` | Rapporto d'aspetto di output. Seleziona uno dei rapporti d'aspetto supportati da PixVerse V6. | COMBO | Sì | Più opzioni disponibili |
| `quality` | Risoluzione di output. Imposta il lato lungo: 360p è 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (predefinito: "720p") | COMBO | Sì | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Durata del video generato in secondi. (predefinito: 5) | INT | Sì | 1–15 |
| `generate_audio` | Genera una traccia audio nativa insieme al video. (predefinito: True) | BOOLEAN | Sì | True<br>False |
| `multi_clip` | Consente al modello di tagliare il video in diverse inquadrature invece di una singola ripresa continua. (predefinito: False) | BOOLEAN | Sì | True<br>False |
| `seed` | Seme per la generazione del video. PixVerse lo registra ma non riproduce un'esecuzione a partire da esso. Supporta la randomizzazione dopo la generazione. (predefinito: 42) | INT | Sì | 0–2147483647 |
| `negative_prompt` | Descrizione testuale opzionale degli elementi indesiderati nel video. (predefinito: "") | STRING | No | 0–2048 caratteri |
| `style` | Stile visivo opzionale applicato all'intero video. (predefinito: "none") | COMBO | No | Più opzioni disponibili |

**Nota:** Il `prompt` è obbligatorio e, dopo aver rimosso gli spazi bianchi, non deve essere vuoto; la sua lunghezza massima è di 5000 caratteri. Il `negative_prompt` è limitato a 2048 caratteri. Impostare `style` su "none" (il valore predefinito) significa che non viene applicato alcuno stile visivo. Il `seed` viene registrato da PixVerse ma non può essere usato per riprodurre la stessa esecuzione. Il nodo attende che PixVerse finisca di generare il video e poi lo scarica; se la richiesta fallisce — ad esempio perché PixVerse ha già raggiunto il numero massimo di generazioni simultanee, l'account del provider ha esaurito i crediti oppure la moderazione dei contenuti rifiuta il prompt — il nodo restituisce un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `VIDEO` | Il video generato. Se `generate_audio` è abilitato, il video include la traccia audio nativa. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `4c268be9720a4606e77a9347570ac26b489625fc6b9528b9d3cceb4497d8683b`

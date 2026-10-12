# PixverseV6FirstLastFrameNode

PixVerse V6 First-Last-Frame to Video genera un video che effettua una transizione dal primo all'ultimo fotogramma tramite PixVerse, opzionalmente con audio nativo. Le due immagini fornite vengono inviate all'API PixVerse, che produce il video di transizione e lo restituisce come file video. L'output mantiene il rapporto d'aspetto del primo fotogramma.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `first_frame` | L'immagine iniziale del video. | IMAGE | Sì | — |
| `last_frame` | L'immagine finale del video. | IMAGE | Sì | — |
| `model` | Modello e impostazioni di generazione. Seleziona il modello PixVerse e mostra i relativi parametri di generazione. | DYNAMIC_COMBO | Sì | "PixVerse V6" |

### Input di PixVerse V6

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt che descrive la transizione. | STRING | Sì | Fino a 5000 caratteri |
| `quality` | Risoluzione di output. Imposta il lato lungo: 360p corrisponde a 640px, 540p a 1024px, 720p a 1280px, 1080p a 1920px. (predefinito: 720p) | COMBO | Sì | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Durata del video generato in secondi. (predefinito: 5) | INT | Sì | da 1 a 15 |
| `generate_audio` | Genera una traccia audio nativa insieme al video. (predefinito: true) | BOOLEAN | Sì | true<br>false |
| `seed` | Seed per la generazione del video. PixVerse lo registra ma non riproduce un'esecuzione a partire da esso. (predefinito: 42) | INT | Sì | da 0 a 2147483647 |
| `negative_prompt` | Descrizione testuale opzionale degli elementi indesiderati nel video. | STRING | No | Fino a 2048 caratteri |
| `style` | Stile visivo opzionale applicato all'intero video. (predefinito: none) | COMBO | No | Più opzioni disponibili (predefinito: "none") |

Nota: il prompt non deve essere vuoto dopo la rimozione degli spazi bianchi ed è limitato a 5000 caratteri. Il prompt negativo, quando fornito, è limitato a 2048 caratteri. La durata deve essere compresa tra 1 e 15 secondi. Il video di output mantiene il rapporto d'aspetto del primo fotogramma.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video generato che effettua la transizione dal primo all'ultimo fotogramma, includendo una traccia audio quando `generate_audio` è abilitato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FirstLastFrameNode/it.md)

---
**Source fingerprint (SHA-256):** `cdb5e45e9de2b429b9d43bbff90b6529af246911ecae8c2809c8abd539101aaa`

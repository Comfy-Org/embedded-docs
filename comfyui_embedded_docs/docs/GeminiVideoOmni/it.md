# Google Gemini Omni (Video)

Genera un video con audio da un prompt testuale usando il modello Gemini Omni Flash di Google. Facoltativamente, fornisci immagini e/o video di riferimento per guidare o modificare il risultato. Descrivi la lunghezza desiderata (3-10 s) e le proporzioni (16:9 o 9:16) direttamente nel prompt.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello video Gemini utilizzato per generare il video. | DYNAMIC_COMBO | Sì | "Omni Flash" |
| `seed` | Il parametro `seed` controlla se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed (predefinito: 42). | INT | Sì | da 0 a 2147483647 |

### Input di Omni Flash

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrivi il video da generare. Specifica la lunghezza e le proporzioni direttamente nel prompt, ad es. "una clip di 6 secondi in 16:9". La lunghezza può essere 3-10 secondi; le proporzioni devono essere 16:9 (orizzontale) o 9:16 (verticale). L'output è 720p, 24 FPS, con audio. | STRING | Sì | Minimo 1 carattere dopo aver rimosso gli spazi bianchi |
| `temperature` | Controlla la casualità. Un valore più basso è più focalizzato/deterministico, uno più alto è più vario (predefinito: 1.0). | FLOAT | No | da 0.0 a 2.0 |
| `top_p` | Campionamento nucleus: campiona dal più piccolo insieme di token la cui probabilità cumulativa raggiunge top_p (predefinito: 0.95). | FLOAT | No | da 0.0 a 1.0 |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot espandibile: collega una o più immagini di riferimento (`image_1`...`image_14`) per guidare o animare il video. Fino a 14 immagini in totale. | IMAGE | No | da 0 a 14 immagini |
| `videos` | Slot espandibile: collega uno o più video di riferimento (`video_1`...`video_3`) per guidare o modificare. Fino a 3 video, ciascuno lungo fino a 10 secondi. | VIDEO | No | da 0 a 3 video, ciascuno max 10 secondi |

Note:
- Se un input immagine contiene più fotogrammi, ogni fotogramma contribuisce al massimo di 14 immagini.
- Quando vengono fornite immagini o video di riferimento, la dimensione totale dei media codificati deve rimanere sotto circa 90 MB; in caso contrario il nodo genera un errore.
- Quando non vengono fornite immagini o video di riferimento, il nodo genera il video solo dal prompt testuale.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `VIDEO` | Il video generato con audio dal modello Gemini. | VIDEO |
| `STRING` | Qualsiasi risposta testuale del modello, come ragionamenti o spiegazioni. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/it.md)

---
**Source fingerprint (SHA-256):** `648844868affb68298d2eac8ac20095bfe378d32e721396781de330ef6a6d69f`

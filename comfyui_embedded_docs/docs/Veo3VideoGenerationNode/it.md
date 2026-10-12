# Google Veo 3 Generazione Video

Genera video da prompt testuali usando l'API Veo 3 di Google. Questo nodo supporta più modelli Veo 3, incluse le varianti fast e lite, e consente di specificare risoluzione video, durata e generazione audio.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione testuale del video (predefinito: "") | STRING | Sì | - |
| `aspect_ratio` | Rapporto d'aspetto del video di output (predefinito: "16:9") | COMBO | Sì | "16:9"<br>"9:16" |
| `resolution` | Risoluzione del video di output. 4K non è disponibile per il modello veo-3.1-lite. (predefinito: "720p") | COMBO | No | "720p"<br>"1080p"<br>"4k" |
| `negative_prompt` | Prompt testuale negativo per indicare cosa evitare nel video (predefinito: "") | STRING | No | - |
| `duration_seconds` | Durata del video di output in secondi (predefinito: 8) | INT | No | 4 - 8 (passo 2) |
| `enhance_prompt` | Questo parametro è deprecato e ignorato. (predefinito: True) | BOOLEAN | No | - |
| `person_generation` | Indica se consentire la generazione di persone nel video (predefinito: "ALLOW") | COMBO | No | "ALLOW"<br>"BLOCK" |
| `seed` | Seed per la generazione del video (0 per casuale) (predefinito: 0) | INT | No | 0 - 4294967295 |
| `image` | Immagine di riferimento opzionale per guidare la generazione del video | IMAGE | No | - |
| `model` | Modello Veo 3 da usare per la generazione del video (predefinito: "veo-3.1-generate") | COMBO | No | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite" |
| `generate_audio` | Genera l'audio per il video. Supportato da tutti i modelli Veo 3. (predefinito: False) | BOOLEAN | No | - |

**Nota:** Il parametro `enhance_prompt` è deprecato e il suo valore viene ignorato. Il nodo migliora sempre il prompt internamente. Se si seleziona la risoluzione "4k" con il modello veo-3.1-lite, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/it.md)

---
**Source fingerprint (SHA-256):** `5320736448ad854e2f93e08ccaa870e977e06497666cb305f314bc76ff917740`

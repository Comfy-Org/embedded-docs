# VEED Remove Video Background

Ritaglia il soggetto da un video con VEED e restituisce i fotogrammi insieme a una maschera alpha. Usa i due output per il compositing oppure inviali a Join Image with Alpha e Save WEBM per scrivere un video trasparente. Scegli `"standard"` per i bordi migliori su qualsiasi sfondo, `"fast"` quando la velocità è importante, o `"green screen"` per filmati girati su uno sfondo verde.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello di segmentazione da usare: `"standard"` per qualsiasi sfondo con i bordi migliori e output fino a 3840x2160, `"fast"` per un risultato più rapido fino a 1920x1080, o `"green screen"` per rimuovere uno sfondo verde fino a 3840x2160. I video più grandi vengono ridimensionati. Selezionando un'opzione vengono mostrati i relativi parametri. | DYNAMIC_COMBO | Sì | `"standard"`<br>`"fast"`<br>`"green screen"` |
| `video` | Il video da cui ritagliare il soggetto. Fino a 60 secondi. | VIDEO | Sì | Fino a 60 secondi |
| `refine_foreground_edges` | Bordi più puliti su capelli, pelo e dettagli fini. Disattivarlo riduce il prezzo. Disponibile per `"standard"` e `"fast"` (predefinito: True). | BOOLEAN | Sì | false<br>true |
| `subject_is_person` | Disattiva quando il soggetto è un oggetto o un animale. Disponibile per `"standard"` e `"fast"` (predefinito: True). | BOOLEAN | Sì | false<br>true |
| `spill_suppression_strength` | Quanto intensamente viene rimossa la dominante verde dal soggetto. Aumentalo quando rimangono macchie verdi; riducilo quando i colori del soggetto cambiano. Disponibile per `"green screen"` (predefinito: 0.8). | FLOAT | Sì | da 0.0 a 1.0 (passo 0.01) |

La clip è limitata a 60 secondi; i video più lunghi vengono rifiutati con un errore. La maschera è 1 dove lo sfondo è stato rimosso, quindi usa Invert Mask prima di Image Composite Masked quando invece vuoi mantenere il soggetto.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `images` | I fotogrammi del video con lo sfondo rimosso. | IMAGE |
| `mask` | 1 dove lo sfondo è stato rimosso, per ogni fotogramma. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedRemoveVideoBackgroundNode/it.md)

---
**Source fingerprint (SHA-256):** `1bf52a380ab09437a5a57f70215856d4ea0055f78ce8b42fe2a2b87d686e8d26`

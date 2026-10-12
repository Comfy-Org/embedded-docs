# EmptyCosmosLatentVideo

EmptyCosmosLatentVideo crea un tensore video latente vuoto con le dimensioni specificate. Genera una rappresentazione latente riempita di zeri che può essere utilizzata come punto di partenza per flussi di lavoro di generazione video, con parametri configurabili `width`, `height`, `length` e `batch_size`.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `width` | La larghezza del video latente in pixel (predefinito: 1280, incrementi di 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `height` | L'altezza del video latente in pixel (predefinito: 704, incrementi di 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `length` | Il numero di frame nel video latente (predefinito: 121, incrementi di 8) | INT | Sì | da 1 a MAX_RESOLUTION |
| `batch_size` | Il numero di video latenti da generare in un batch (predefinito: 1) | INT | No | da 1 a 4096 |

Nota: il tensore latente viene sottocampionato spazialmente di un fattore 8 sia in altezza sia in larghezza e contiene 16 canali. Il numero di frame temporali latenti è calcolato come `((length - 1) // 8) + 1`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `samples` | Il tensore video latente vuoto generato con valori zero | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/it.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`

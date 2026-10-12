# EmptyARVideoLatent

Il nodo EmptyARVideoLatent crea una rappresentazione latente vuota per la generazione video. Costruisce un tensore di zeri usando la larghezza, l'altezza, il numero di frame e la dimensione del batch richiesti, che può poi essere utilizzato per inizializzare un processo di generazione video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza dei frame video in pixel (predefinito: 832) | INT | Sì | 16 a 8192 (passo: 16) |
| `height` | L'altezza dei frame video in pixel (predefinito: 480) | INT | Sì | 16 a 8192 (passo: 16) |
| `length` | Il numero di frame nel video (predefinito: 81) | INT | Sì | 1 a 1024 (passo: 4) |
| `batch_size` | Il numero di video da generare in un singolo batch (predefinito: 1) | INT | Sì | 1 a 64 |

Nota: La dimensione latente interna viene derivata da questi input. `width` e `height` sono divisi per 8, e il numero di passi temporali latenti viene calcolato come `((length - 1) // 4) + 1`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `LATENT` | Un tensore latente riempito di zeri, che rappresenta uno spazio latente video vuoto con le dimensioni, la lunghezza e la dimensione del batch specificati. La forma del tensore è [batch_size, 16, lat_t, height/8, width/8], dove lat_t = ((length - 1) // 4) + 1 è il numero di passi temporali latenti derivati dalla lunghezza richiesta. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/it.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`

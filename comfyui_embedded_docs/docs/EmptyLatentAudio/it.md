# EmptyLatentAudio

Empty Latent Audio crea un tensore latente vuoto per l'elaborazione audio. Genera una rappresentazione latente audio vuota con una durata e una dimensione batch specificate, che può essere utilizzata come punto di partenza per flussi di lavoro di generazione o elaborazione audio. Il nodo calcola automaticamente le dimensioni latenti appropriate in base alla durata dell'audio e alla frequenza di campionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `seconds` | La durata dell'audio in secondi (predefinito: 47.6) | FLOAT | Sì | 1.0 - 1000.0 |
| `batch_size` | Il numero di immagini latenti nel batch (predefinito: 1) | INT | Sì | 1 - 4096 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `LATENT` | Restituisce un tensore latente vuoto per l'elaborazione audio con la durata e la dimensione batch specificate. Il tensore ha una forma [batch_size, 64, length], dove length viene calcolato dalla durata dell'audio e dalla frequenza di campionamento. L'output include anche metadati che indicano che il tipo è "audio" e un rapporto di riduzione temporale pari a 2048. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/it.md)

---
**Source fingerprint (SHA-256):** `6ca63d26febe2d87ff751a57044eb81b553b19756f4b3f9478ecb5a733ec0041`

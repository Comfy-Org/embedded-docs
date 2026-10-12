# EmptyLTXVLatentVideo

Il nodo EmptyLTXVLatentVideo crea un tensore latente video vuoto (riempito di zeri) usando larghezza, altezza, lunghezza e dimensione batch specificate. Fornisce un punto di partenza vuoto per i flussi di lavoro di generazione video LTXV, con le dimensioni latenti compresse automaticamente rispetto alla dimensione video richiesta.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza del tensore latente video (predefinito: 768, passo: 32) | INT | Sì | da 64 a MAX_RESOLUTION |
| `height` | L'altezza del tensore latente video (predefinito: 512, passo: 32) | INT | Sì | da 64 a MAX_RESOLUTION |
| `length` | Il numero di fotogrammi nel video latente (predefinito: 97, passo: 8) | INT | Sì | da 1 a MAX_RESOLUTION |
| `batch_size` | Il numero di video latenti da generare in un batch (predefinito: 1) | INT | Sì | da 1 a 4096 |

Nota: il video latente è compresso rispetto alle dimensioni richieste: le dimensioni spaziali (larghezza e altezza) sono divise per 32, mentre il numero di fotogrammi (lunghezza) è diviso per 8 e arrotondato per eccesso al numero intero più vicino. I valori di passo per larghezza, altezza e lunghezza aiutano a mantenere queste divisioni senza resto.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | Il tensore latente vuoto generato con valori zero nelle dimensioni specificate, insieme a un rapporto di riduzione spaziale di 32 | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/it.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`

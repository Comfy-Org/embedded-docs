# EmptyMochiLatentVideo

EmptyMochiLatentVideo crea un tensore latente video vuoto con le dimensioni specificate. Genera una rappresentazione latente riempita di zeri che può essere usata come punto di partenza per i flussi di lavoro di generazione video. Il nodo consente di definire larghezza, altezza, lunghezza e dimensione del batch del tensore latente video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `width` | La larghezza del video latente in pixel (predefinito: 848, i valori aumentano con incrementi di 16) | INT | Sì | Da 16 a MAX_RESOLUTION |
| `height` | L'altezza del video latente in pixel (predefinito: 480, i valori aumentano con incrementi di 16) | INT | Sì | Da 16 a MAX_RESOLUTION |
| `length` | Il numero di fotogrammi nel video latente (predefinito: 25, i valori aumentano con incrementi di 6, a partire da 7) | INT | Sì | Da 7 a MAX_RESOLUTION |
| `batch_size` | Il numero di video latenti da generare in un batch (predefinito: 1) | INT | No | Da 1 a 4096 |

**Nota:** Le dimensioni effettive del latente sono calcolate come width/8 e height/8, la dimensione temporale è calcolata come `((length - 1) // 6) + 1`, e il tensore ha 12 canali. Poiché `length` avanza con incrementi di 6 a partire da 7, i valori validi sono 7, 13, 19, 25 e così via.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `samples` | Un tensore latente video vuoto con le dimensioni specificate, contenente tutti zeri | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/it.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`

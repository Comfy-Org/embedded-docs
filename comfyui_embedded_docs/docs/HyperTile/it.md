# HyperTile

HyperTile applica una tecnica di tiling al meccanismo di attenzione all'interno dei modelli di diffusione per ridurre l'utilizzo di memoria durante la generazione di immagini. Suddivide lo spazio latente in tile più piccoli, elabora l'attenzione per ciascun tile separatamente e poi riassembla i risultati. Ciò consente di lavorare con dimensioni di immagine maggiori senza esaurire la memoria.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui applicare l'ottimizzazione HyperTile | MODEL | Sì | - |
| `tile_size` | La dimensione target dei tile per l'elaborazione (predefinito: 256). Internamente, il valore viene limitato a un minimo di 32 e poi diviso per 8 per ottenere la dimensione effettiva dei tile. | INT | Sì | 1 - 2048 |
| `swap_size` | Controlla come i tile vengono riorganizzati durante l'elaborazione per migliorare l'efficienza. Valori più grandi consentono una maggiore variazione nelle dimensioni dei tile (predefinito: 2) | INT | Sì | 1 - 128 |
| `max_depth` | Il livello massimo di profondità (scala di risoluzione) a cui applicare il tiling. Un valore di 0 applica il tiling solo alla risoluzione più alta (predefinito: 0) | INT | Sì | 0 - 10 |
| `scale_depth` | Quando è abilitato, la dimensione dei tile viene scalata proporzionalmente ai livelli di profondità maggiori. Questo può aiutare a mantenere la qualità a risoluzioni inferiori (predefinito: False) | BOOLEAN | Sì | True / False |

Nota: `tile_size`, `swap_size`, `max_depth` e `scale_depth` sono contrassegnati come input avanzati, quindi vengono mostrati solo quando le opzioni avanzate sono abilitate nell'interfaccia.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con l'ottimizzazione HyperTile applicata | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/it.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`

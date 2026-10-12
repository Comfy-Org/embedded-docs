# Regola Luminosità

Il nodo Adjust Brightness modifica l'aspetto della luminosità di un'immagine. Moltiplica i valori di colore dell'immagine per un `factor` e mantiene i risultati all'interno dell'intervallo valido da 0.0 a 1.0. Un fattore di 1.0 lascia l'immagine invariata, i valori inferiori a 1.0 la rendono più scura e i valori superiori a 1.0 la rendono più luminosa.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da regolare. Accetta una singola immagine o un batch di immagini. | IMAGE | Sì | - |
| `factor` | Fattore di luminosità. 1.0 = nessuna modifica, valori inferiori a 1.0 = più scura, valori superiori a 1.0 = più luminosa. (predefinito: 1.0) | FLOAT | No | 0.0 - 2.0 |

Nota: se l'immagine di input ha un canale alpha (RGBA), vengono regolati solo i canali di colore. Il canale alpha viene copiato dall'input senza modifiche perché memorizza la trasparenza, non il colore.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine di output con luminosità regolata. Se l'input ha un canale alpha, i valori alpha rimangono invariati. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/it.md)

---
**Source fingerprint (SHA-256):** `64c1499d16deb5922fa63538182cd227e8f2ba9ded5962064ce9f228a0f4a163`

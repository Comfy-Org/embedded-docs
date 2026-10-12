# NormalizeImages

Questo nodo normalizza i colori di un'immagine di input regolando i valori dei pixel in base a una media e a una deviazione standard specificate. A ogni pixel viene sottratta la media e il risultato viene poi diviso per la deviazione standard; si tratta di un passaggio comune per standardizzare i dati delle immagini prima di altre elaborazioni.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da normalizzare. | IMAGE | Sì | - |
| `mean` | Valore medio per la normalizzazione (predefinito: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `std` | Deviazione standard per la normalizzazione (predefinito: 0.5). | FLOAT | No | 0.001 - 1.0 |

I parametri `mean` e `std` controllano la normalizzazione applicata all'immagine di input. Il valore predefinito per entrambi i parametri è 0.5.

Nota: se l'immagine di input ha un canale alpha (trasparenza), tale canale non viene normalizzato. Viene copiato invariato nell'output perché alpha memorizza la trasparenza anziché il colore.

Nota: il nodo funziona con qualsiasi dimensione del batch, quindi è possibile elaborare più immagini contemporaneamente.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine risultante dopo l'applicazione del processo di normalizzazione. I valori dei pixel vengono regolati utilizzando la media e la deviazione standard specificate, e il canale alpha (se presente) viene preservato. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/it.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`

# Ritaglia Immagine (Casuale)

Il nodo Random Crop Images seleziona casualmente una sezione rettangolare da ogni immagine di input e la ritaglia a una larghezza e un'altezza specificate. Questo è comunemente utilizzato per il data augmentation per creare varianti delle immagini di addestramento. La posizione casuale del ritaglio è determinata da un valore di seed, garantendo che lo stesso ritaglio possa essere riprodotto.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine da ritagliare. | IMAGE | Sì | - |
| `width` | La larghezza dell'area di ritaglio (predefinito: 512). | INT | No | 1 - 8192 |
| `height` | L'altezza dell'area di ritaglio (predefinito: 512). | INT | No | 1 - 8192 |
| `seed` | Un numero utilizzato per controllare la posizione casuale del ritaglio (predefinito: 0). | INT | No | 0 - 18446744073709551615 |

**Nota:** I parametri `width` e `height` devono essere minori o uguali alle dimensioni dell'immagine di input. Se una dimensione specificata è maggiore dell'immagine, il ritaglio sarà limitato al bordo dell'immagine.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine risultante dopo l'applicazione del ritaglio casuale. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/it.md)

---
**Source fingerprint (SHA-256):** `8452a07a1cf66a520fb482f5239df3f33cfe3a77a28e289894ccd1d2544ecf40`

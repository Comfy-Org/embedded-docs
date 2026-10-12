# LTXVImgToVideoInplace

LTXVImgToVideoInplace codifica un'immagine di input nello spazio latente e colloca quei fotogrammi codificati all'inizio di un video latente esistente. Il valore `strength` controlla quanto fortemente l'immagine codificata condiziona quei fotogrammi iniziali e, quando `bypass` è abilitato, il latente di input viene restituito invariato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `vae` | Il modello VAE utilizzato per codificare l'immagine di input nello spazio latente. | VAE | Sì | - |
| `image` | L'immagine di input da codificare e utilizzare per condizionare il latente video. | IMAGE | Sì | - |
| `latent` | La rappresentazione latente video di destinazione da modificare. | LATENT | Sì | - |
| `strength` | Controlla quanto fortemente l'immagine codificata condiziona i fotogrammi iniziali del latente. Un valore di 1.0 condiziona completamente i fotogrammi iniziali con l'immagine codificata, mentre valori inferiori li condizionano in misura minore. La maschera di rumore per i fotogrammi iniziali è impostata su `1.0 - strength`. (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `bypass` | Ignora il condizionamento. Quando è abilitato, il nodo restituisce il latente di input invariato. (predefinito: False) | BOOLEAN | Sì | True or False |

**Nota:** L'`image` verrà ridimensionata automaticamente per corrispondere alle dimensioni spaziali richieste dal `vae` per la codifica, in base alla larghezza e all'altezza del `latent` di input. Per la codifica vengono utilizzati solo i canali RGB dell'`image`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | La rappresentazione latente video risultante. Quando il bypass è disabilitato, contiene i `samples` aggiornati e una `noise_mask` che applica la forza di condizionamento ai fotogrammi iniziali. Quando il bypass è abilitato, è il latente di input restituito invariato. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/it.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`

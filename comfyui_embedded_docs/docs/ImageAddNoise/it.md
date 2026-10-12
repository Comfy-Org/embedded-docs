# ImageAddNoise

Il nodo ImageAddNoise aggiunge rumore casuale a un'immagine di input. Utilizza un seed casuale specificato per generare pattern di rumore coerenti e consente di controllare l'intensità dell'effetto rumore. L'immagine risultante mantiene le stesse dimensioni dell'input, ma con una texture visiva aggiunta.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input a cui verrà aggiunto il rumore | IMAGE | Sì | - |
| `seed` | Il seed casuale utilizzato per creare il rumore (predefinito: 0). Questo parametro supporta la funzionalità "controllo dopo generazione". | INT | Sì | 0 a 18446744073709551615 |
| `strength` | Controlla l'intensità dell'effetto rumore (predefinito: 0.5, passo: 0.01) | FLOAT | Sì | 0.0 a 1.0 |

**Nota:** I valori di rumore vengono aggiunti all'immagine e il risultato viene limitato all'intervallo 0.0–1.0. Se l'immagine di input ha un canale alpha (4 canali), il canale alpha originale viene preservato inalterato — il rumore viene applicato solo ai canali di colore.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine di output con il rumore aggiunto | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/it.md)

---
**Source fingerprint (SHA-256):** `e6b9815e7c075c7ee97c924c22a92dfef6d9c65b97b6e65b0f9e1c96628f39f2`

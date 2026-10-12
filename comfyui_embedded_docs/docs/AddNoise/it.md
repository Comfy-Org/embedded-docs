# AddNoise

Questo nodo aggiunge rumore controllato a un'immagine latente utilizzando un generatore di rumore specificato e valori sigma. Elabora l'input attraverso il sistema di campionamento del modello per applicare una scalatura del rumore appropriata all'intervallo sigma specificato, restituendo una nuova rappresentazione latente con il rumore applicato. Questo nodo è attualmente contrassegnato come sperimentale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello contenente i parametri di campionamento e le funzioni di elaborazione | MODEL | Sì | - |
| `noise` | Il generatore di rumore che produce il pattern di rumore di base | NOISE | Sì | - |
| `sigmas` | Valori sigma che controllano l'intensità della scalatura del rumore. Se vuoto, il nodo restituisce l'immagine latente originale invariata. Quando vengono forniti più sigma, la scala del rumore viene calcolata come differenza assoluta tra il primo e l'ultimo valore sigma. Quando viene fornito un solo sigma, quel valore viene usato direttamente come scala. | SIGMAS | Sì | - |
| `latent_image` | La rappresentazione latente di input a cui verrà aggiunto il rumore. Le immagini latenti vuote (contenenti solo zeri) non vengono modificate durante l'elaborazione. | LATENT | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `LATENT` | La rappresentazione latente modificata con il rumore aggiunto. Eventuali valori NaN o infiniti nell'output vengono convertiti in zeri per stabilità. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/it.md)

---
**Source fingerprint (SHA-256):** `6b11db10af9a2b8ea24dbf3b40c08d7e37de39df746e3966e5bfc94b84dee068`

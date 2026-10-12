# Crea Dataset di Addestramento

Questo nodo prepara i dati per l'addestramento codificando immagini e testo. Riceve un elenco di immagini e un elenco corrispondente di didascalie testuali, quindi utilizza un modello VAE per convertire le immagini in rappresentazioni latenti e un modello CLIP per convertire il testo in dati di condizionamento. I latenti e il condizionamento accoppiati risultanti vengono restituiti come liste, pronti per l'uso nei flussi di lavoro di addestramento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Elenco di immagini da codificare. | IMAGE | Sì | N/A |
| `vae` | Modello VAE per codificare le immagini in latenti. | VAE | Sì | N/A |
| `clip` | Modello CLIP per codificare il testo in condizionamento. | CLIP | Sì | N/A |
| `texts` | Elenco di didascalie testuali. Può avere lunghezza n (corrispondente alle immagini), 1 (ripetuta per tutte) o essere omesso (usa una stringa vuota). | STRING | No | 0, 1 o n elementi (n = numero di immagini) |

**Vincoli sui parametri:**

* Questo nodo utilizza input di tipo lista: `images` e `texts` vengono elaborati come liste, mentre `vae` e `clip` accettano un solo modello ciascuno (viene utilizzato il primo elemento della lista fornita).
* Il numero di elementi nella lista `texts` deve essere 0, 1 o corrispondere esattamente al numero di elementi nella lista `images`. Se è 0 o omesso, per tutte le immagini viene utilizzata una stringa vuota. Se è 1, quel singolo testo viene ripetuto per tutte le immagini. Qualsiasi altra lunghezza genera un errore.
* Le liste di output `latents` e `conditioning` contengono sempre lo stesso numero di elementi della lista `images`, quindi ogni latente è accoppiato al condizionamento della didascalia corrispondente.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latents` | Elenco di dizionari latenti. | LATENT |
| `conditioning` | Elenco di liste di condizionamento. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/it.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`

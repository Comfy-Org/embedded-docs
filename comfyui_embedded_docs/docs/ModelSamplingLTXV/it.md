# ModelSamplingLTXV

Il nodo ModelSamplingLTXV applica parametri di campionamento avanzati a un modello in base al numero di token. Calcola un valore di shift interpolando linearmente tra `base_shift` e `max_shift` su un intervallo di token, quindi applica una patch al modello di input con una configurazione di campionamento specializzata. Se viene fornito un `latent`, le sue dimensioni determinano il numero di token; altrimenti vengono usati 4096 token.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di input a cui applicare i parametri di campionamento. | MODEL | Sì | - |
| `max_shift` | Il valore massimo di shift utilizzato nel calcolo di interpolazione lineare (predefinito: 2.05). | FLOAT | Sì | da 0.0 a 100.0 (passo: 0.01) |
| `base_shift` | Il valore di shift di base utilizzato nel calcolo di interpolazione lineare (predefinito: 0.95). | FLOAT | Sì | da 0.0 a 100.0 (passo: 0.01) |
| `latent` | Input latent opzionale usato per determinare il numero di token per il calcolo dello shift. Se non fornito, viene usato un numero di token predefinito di 4096. | LATENT | No | - |

Il valore di shift viene calcolato interpolando tra `base_shift` a 1024 token e `max_shift` a 4096 token. Quando viene fornito `latent`, il numero di token è il prodotto di tutte le dimensioni dopo le prime due nei campioni `latent` (le dimensioni spaziali/temporali). Se non viene fornito alcun `latent`, il numero di token predefinito è 4096.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con i parametri di campionamento applicati. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/it.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`

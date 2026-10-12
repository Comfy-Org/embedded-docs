# Imposta Audio di Riferimento

Questo nodo imposta l'audio di riferimento per il processo "ace step 1.5". Riceve un input di condizionamento e, facoltativamente, una rappresentazione latente dell'audio, quindi associa quei dati latenti ai dati di condizionamento in modo che i nodi successivi possano usarli come latenti del timbro dell'audio di riferimento. Questo nodo è contrassegnato come sperimentale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `conditioning` | I dati di condizionamento a cui verranno associate le informazioni dell'audio di riferimento. | CONDITIONING | Sì |  |
| `latent` | Una rappresentazione latente opzionale dell'audio di riferimento (predefinito: None). Se fornita, i suoi campioni vengono aggiunti ai dati di condizionamento come latenti del timbro dell'audio di riferimento. | LATENT | No |  |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `conditioning` | I dati di condizionamento modificati, che ora contengono i latenti del timbro dell'audio di riferimento se è stato fornito l'input opzionale `latent`. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/it.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`

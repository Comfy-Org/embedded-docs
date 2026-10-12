# ReferenceLatent

Questo nodo imposta il latent guida per un modello di modifica. Riceve dati di condizionamento e un input latent opzionale, quindi modifica il conditioning per includere le informazioni del latent di riferimento. Se il modello lo supporta, è possibile concatenare più nodi Set Reference Latent per impostare più immagini di riferimento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `conditioning` | I dati di condizionamento da modificare con le informazioni del latent di riferimento | CONDITIONING | Sì | - |
| `latent` | Dati latenti opzionali da usare come riferimento per il modello di modifica. Se non forniti, il conditioning viene restituito invariato | LATENT | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | I dati di condizionamento modificati contenenti le informazioni del latent di riferimento | CONDITIONING |

## Note

- Il latent di riferimento viene memorizzato come una lista di tensori campione, quindi collegare in sequenza diversi nodi Set Reference Latent aggiunge ulteriori riferimenti invece di sostituire quello precedente.
- Quando non è collegato alcun `latent`, il nodo lascia passare il `conditioning` in ingresso senza modifiche.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/it.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`

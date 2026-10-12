# FluxProDepthNode

Questo nodo genera immagini utilizzando un'immagine di controllo della profondità come guida. Riceve un'immagine di controllo e un prompt testuale, quindi crea una nuova immagine che segue sia le informazioni sulla profondità dell'immagine di controllo sia la descrizione nel prompt. Il nodo si connette a un'API esterna per eseguire il processo di generazione dell'immagine.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `control_image` | L'immagine di controllo della profondità utilizzata per guidare la generazione dell'immagine | IMAGE | Sì | - |
| `prompt` | Prompt per la generazione dell'immagine (predefinito: stringa vuota) | STRING | No | - |
| `prompt_upsampling` | Indica se eseguire l'upsampling sul prompt. Se attivo, modifica automaticamente il prompt per una generazione più creativa, ma i risultati sono non deterministici (lo stesso seed non produrrà esattamente lo stesso risultato). (predefinito: False) | BOOLEAN | No | - |
| `skip_preprocessing` | Indica se saltare la preelaborazione; impostare su True se `control_image` è già convertita in profondità, False se è un'immagine grezza. (predefinito: False) | BOOLEAN | No | - |
| `guidance` | Forza di guida per il processo di generazione dell'immagine (predefinito: 15) | FLOAT | No | 1-100 |
| `steps` | Numero di passaggi per il processo di generazione dell'immagine (predefinito: 50) | INT | No | 15-50 |
| `seed` | Il seed casuale utilizzato per creare il rumore. (predefinito: 0) | INT | No | 0-18446744073709551615 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output_image` | L'immagine generata in base all'immagine di controllo della profondità e al prompt | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/it.md)

---
**Source fingerprint (SHA-256):** `34b80d7d63158b7dc4ad02da6b3a573b713d77efd0955d3477409f776f964462`

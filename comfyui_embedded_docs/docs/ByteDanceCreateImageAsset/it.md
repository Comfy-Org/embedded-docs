# ByteDance Crea Asset Immagine

Questo nodo crea un asset immagine personale per il servizio Seedance 2.0 di ByteDance. Carica un'immagine di input e la registra all'interno di un gruppo di asset specificato. Se non viene fornito alcun ID gruppo, avvierà nel browser un processo di autenticazione della persona reale per creare un nuovo gruppo prima di aggiungere l'asset.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine da registrare come asset personale. | IMAGE | Sì |  |
| `group_id` | Riutilizza un ID gruppo asset Seedance esistente per evitare verifiche umane ripetute per la stessa persona. Lascia vuoto per eseguire nel browser l'autenticazione della persona reale e creare un nuovo gruppo (predefinito: vuoto). | STRING | No |  |

**Vincoli sull'immagine:**
- La larghezza dell'immagine deve essere compresa tra 300 e 6000 pixel.
- L'altezza dell'immagine deve essere compresa tra 300 e 6000 pixel.
- Le proporzioni dell'immagine devono essere comprese tra 0,4:1 e 2,5:1.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `asset_id` | L'identificatore univoco per l'asset immagine appena creato. | STRING |
| `group_id` | L'identificatore per il gruppo di asset. Sarà il `group_id` fornito o uno appena creato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/it.md)

---
**Source fingerprint (SHA-256):** `44d2bc880cbd8780ce1deb27eee5e41dc43973653751b0022a2631df725b155d`

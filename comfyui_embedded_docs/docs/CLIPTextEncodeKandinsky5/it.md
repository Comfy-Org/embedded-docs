# CLIPTextEncodeKandinsky5

Il nodo CLIP Text Encode (Kandinsky 5) prepara i prompt testuali per l'uso con il modello Kandinsky 5. Prende due input testuali separati, li tokenizza con un modello CLIP fornito e li combina in un unico output di condizionamento che guida il processo di generazione dell'immagine.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP utilizzato per tokenizzare e codificare i prompt testuali. | CLIP | Sì |  |
| `clip_l` | Il prompt testuale primario. Questo input supporta testo multilinea e prompt dinamici. | STRING | Sì |  |
| `qwen25_7b` | Il prompt testuale secondario. Questo input supporta testo multilinea e prompt dinamici. | STRING | Sì |  |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento combinati generati da entrambi i prompt testuali, pronti per essere inseriti in un modello Kandinsky 5 per la generazione di immagini. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/it.md)

---
**Source fingerprint (SHA-256):** `d988c47ab9a5f01549a3ae01b365d39e9fa2464bb69ea018ec20151939dcfc56`

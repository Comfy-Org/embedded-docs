# TextEncodeQwenImageEdit

Il nodo TextEncodeQwenImageEdit converte prompt testuali e immagini opzionali in dati di condizionamento per la generazione o la modifica di immagini. Utilizza un modello CLIP per tokenizzare l'input e può codificare opzionalmente immagini di riferimento con un VAE per creare latent di riferimento. Quando viene fornita un'immagine, questa viene ridimensionata automaticamente per mantenere una scala di elaborazione coerente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP utilizzato per la tokenizzazione di testo e immagini | CLIP | Sì | - |
| `prompt` | Prompt testuale per la generazione del condizionamento, supporta input multilinea e prompt dinamici | STRING | Sì | - |
| `vae` | Modello VAE opzionale per codificare immagini di riferimento in latent | VAE | No | - |
| `image` | Immagine di input opzionale per scopi di riferimento o modifica | IMAGE | No | - |

**Nota:** Quando viene fornita un'immagine, questa viene ridimensionata in modo che il numero totale di pixel rimanga vicino a 1.048.576 (1024 × 1024), e vengono usati solo i suoi canali RGB. L'immagine ridimensionata viene passata al tokenizer CLIP insieme al prompt. Quando vengono forniti sia `image` che `vae`, il nodo codifica anche l'immagine in latent di riferimento e li allega all'output di condizionamento.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | Dati di condizionamento contenenti token testuali e latent di riferimento opzionali per la generazione di immagini | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/it.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`

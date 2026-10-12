# ByteDanceImageEditNode

Il nodo ByteDance Image Edit consente di modificare le immagini utilizzando i modelli AI di ByteDance tramite un'API. Si fornisce un'immagine di input e un prompt testuale che descrive le modifiche desiderate, quindi il nodo elabora l'immagine in base alle istruzioni. Il nodo gestisce automaticamente la comunicazione con l'API e restituisce l'immagine modificata.

## Input

| Parametro | Descrizione | Tipo di dato | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `model` | Nome del modello | MODEL | COMBO | seededit_3 | opzioni Image2ImageModelName |
| `image` | L'immagine di base da modificare | IMAGE | IMAGE | - | - |
| `prompt` | Istruzione per modificare l'immagine | STRING | STRING | "" | - |
| `seed` | Seed da utilizzare per la generazione | INT | INT | 0 | 0-2147483647 |
| `guidance_scale` | Un valore più alto fa sì che l'immagine segua più fedelmente il prompt | FLOAT | FLOAT | 5.5 | 1.0-10.0 |
| `watermark` | Indica se aggiungere una filigrana "AI generated" all'immagine | BOOLEAN | BOOLEAN | True | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `IMAGE` | L'immagine modificata restituita dall'API di ByteDance | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/it.md)

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`

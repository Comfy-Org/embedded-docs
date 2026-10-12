# KlingVirtualTryOnNode

Nodo Kling Virtual Try On. Inserisci un'immagine di una persona e un'immagine di un capo di abbigliamento per provare il capo sulla persona. Puoi unire più immagini di capi di abbigliamento in un'unica immagine con sfondo bianco.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `human_image` | L'immagine della persona su cui provare i vestiti | IMAGE | Sì | - |
| `cloth_image` | L'immagine del capo di abbigliamento da provare sulla persona | IMAGE | Sì | - |
| `model_name` | Il modello di prova virtuale da utilizzare (predefinito: "kolors-virtual-try-on-v1") | STRING | Sì | `"kolors-virtual-try-on-v1"` |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | L'immagine risultante che mostra la persona con il capo di abbigliamento provato | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/it.md)

---
**Source fingerprint (SHA-256):** `bf256d8732f4c6acf65838812fc322e48ef886257bbb48c02b0cc6ab5d78dce5`

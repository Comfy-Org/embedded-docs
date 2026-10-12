# Ribalta immagine

Il nodo ImageFlip ribalta le immagini lungo assi diversi. Può ribaltare le immagini verticalmente lungo l'asse x oppure orizzontalmente lungo l'asse y. Il nodo utilizza operazioni torch.flip per eseguire il ribaltamento in base al metodo selezionato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da ribaltare | IMAGE | Sì | - |
| `flip_method` | La direzione di ribaltamento da applicare (predefinito: "x-axis: vertically") | STRING | Sì | "x-axis: vertically"<br>"y-axis: horizontally" |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine di output ribaltata | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/it.md)

---
**Source fingerprint (SHA-256):** `481cd167d57746f242fcc4b5f2e3bb0bff0184b5870626d5f24a34422464ddd6`

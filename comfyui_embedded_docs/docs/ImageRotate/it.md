# ImageRotate

Il nodo ImageRotate ruota un'immagine di input di angoli specificati. Supporta quattro opzioni di rotazione: nessuna rotazione, 90 gradi in senso orario, 180 gradi e 270 gradi in senso orario. La rotazione viene eseguita utilizzando efficienti operazioni sui tensori che preservano l'integrità dei dati dell'immagine.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da ruotare | IMAGE | Sì | - |
| `rotation` | L'angolo di rotazione da applicare all'immagine (predefinito: "none") | STRING | Sì | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine di output ruotata | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/it.md)

---
**Source fingerprint (SHA-256):** `1de36d9e42e64fe80cc13dd7da96bd946f02ba78d81317f073cf54c4e5bd12f7`

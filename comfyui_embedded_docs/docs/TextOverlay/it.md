# TextOverlay

Questo nodo disegna testo sopra un'immagine o un batch di immagini. Crea una sovrapposizione di testo utilizzando dimensione del carattere, colore, posizione verticale, allineamento orizzontale e contorno nero opzionale configurabili, quindi combina la sovrapposizione con i pixel dell'immagine originale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `images` | L'immagine o il batch di immagini di input su cui disegnare il testo | IMAGE | Sì | |
| `text` | Il testo da sovrapporre all'immagine (predefinito: ""). Supporta più righe: le sequenze di escape `\n` e `\t` vengono convertite in nuove righe e tabulazioni, e le righe lunghe vengono automaticamente mandate a capo per rientrare nella larghezza dell'immagine. | STRING | Sì | |
| `font_size` | Dimensione del carattere come percentuale dell'altezza dell'immagine (predefinito: 5.0) | FLOAT | Sì | 0.5 a 50.0 (passo 0.5) |
| `color` | Colore del testo (predefinito: "#ffffff") | COLOR | Sì | |
| `position` | Posizione verticale del testo sull'immagine (predefinito: "top") | COMBO | Sì | "top"<br>"bottom" |
| `align` | Allineamento orizzontale del testo (predefinito: "left") | COMBO | Sì | "left"<br>"center"<br>"right" |
| `outline` | Disegna un contorno nero attorno al testo (predefinito: True) | BOOLEAN | Sì | |

Nota: se `text` è vuoto o contiene solo spazi bianchi, il nodo restituisce le immagini di input invariate. La sovrapposizione di testo viene renderizzata una volta e applicata a ogni immagine del batch. Se il blocco di testo renderizzato è più alto dell'area disponibile dell'immagine, la dimensione del carattere viene ridotta automaticamente finché non rientra o raggiunge una dimensione minima.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `images` | Le immagini di input con la sovrapposizione di testo applicata sopra | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/it.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`

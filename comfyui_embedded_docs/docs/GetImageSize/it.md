# Ottieni Dimensione Immagine

GetImageSize legge un'immagine di input e restituisce la sua larghezza, altezza e dimensione del batch. Il nodo visualizza inoltre questi valori misurati direttamente sull'interfaccia del nodo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da cui vengono estratte larghezza, altezza e dimensione del batch | IMAGE | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `width` | La larghezza dell'immagine di input in pixel | INT |
| `height` | L'altezza dell'immagine di input in pixel | INT |
| `batch_size` | Il numero di immagini contenute nel batch di input | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/it.md)

---
**Source fingerprint (SHA-256):** `dc29add37a3362384e63cb1e57f03758a82f77811c78797fdffd486462cb19b8`

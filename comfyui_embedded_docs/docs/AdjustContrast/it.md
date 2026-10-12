# Regola Contrasto

Il nodo Adjust Contrast regola il contrasto di un'immagine di input scalando la differenza tra le aree chiare e scure attorno al punto medio dell'intervallo di colore. Un fattore pari a 1.0 lascia l'immagine invariata, i valori inferiori a 1.0 riducono il contrasto, mentre i valori superiori a 1.0 aumentano il contrasto.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input di cui regolare il contrasto. | IMAGE | Sì | - |
| `factor` | Fattore di contrasto. 1.0 = nessuna modifica, <1.0 = meno contrasto, >1.0 = più contrasto. (predefinito: 1.0) | FLOAT | No | 0.0 - 2.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine risultante con il contrasto regolato. I valori dei pixel vengono limitati all'intervallo 0.0–1.0. Se l'immagine di input ha un canale alpha, tale canale viene preservato invariato. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/it.md)

---
**Source fingerprint (SHA-256):** `489f840cc3d98339a5cf7b55e9179c60878c58b2f992740796c7d49642e05932`

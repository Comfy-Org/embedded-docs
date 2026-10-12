# BatchImagesNode

Il nodo Batch Images combina più immagini singole in un singolo batch. Riceve un numero variabile di input immagine e li restituisce come un unico tensore di immagini in batch, consentendo di elaborarli insieme nei nodi successivi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Un elenco dinamico di input immagine. Puoi aggiungere da 2 a 50 immagini da combinare in un batch. L'interfaccia del nodo consente di aggiungere altri slot di input immagine secondo necessità. | IMAGE | Sì | da 2 a 50 input |

**Nota:** Devi collegare almeno due immagini affinché il nodo funzioni. Il primo slot di input è sempre obbligatorio e puoi aggiungerne altri usando il pulsante "+" che appare nell'interfaccia del nodo.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Un singolo tensore di immagini in batch contenente tutte le immagini di input impilate insieme. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/it.md)

---
**Source fingerprint (SHA-256):** `f756fb15760cd2518da9c3f88281d3ab3361b4c2b4820fe2be152e4db1cf102c`

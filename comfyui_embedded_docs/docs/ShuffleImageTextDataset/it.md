# Mescola Coppie Immagine-Testo

Questo nodo mescola insieme una lista di immagini e una lista di testi, mantenendone intatti gli abbinamenti. Utilizza un seed casuale per determinare l'ordine di mescolamento, garantendo che le stesse liste di input vengano mescolate allo stesso modo ogni volta che il seed viene riutilizzato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Lista di immagini da mescolare. | IMAGE | Sì | - |
| `texts` | Lista di testi da mescolare. | STRING | Sì | - |
| `seed` | Seed casuale. L'ordine di mescolamento è determinato da questo valore (predefinito: 0). | INT | No | 0 a 18446744073709551615 |

**Nota:** Gli input `images` e `texts` devono essere liste della stessa lunghezza. Il nodo abbinerà la prima immagine con il primo testo, la seconda immagine con il secondo testo, e così via, prima di mescolare insieme queste coppie.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `images` | La lista mescolata di immagini. | IMAGE |
| `texts` | La lista mescolata di testi, mantenendo gli abbinamenti originali con le immagini. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/it.md)

---
**Source fingerprint (SHA-256):** `77050e9f7255e64b07bd394908b679acef399d78ec9be7c1346d6f297c109968`

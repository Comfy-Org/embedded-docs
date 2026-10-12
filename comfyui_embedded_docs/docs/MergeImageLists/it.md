# MergeImageLists

Il nodo Merge Image Lists combina più liste separate di immagini in un'unica lista continua. Funziona prendendo tutte le immagini da ciascun input collegato e concatenandole nell'ordine in cui vengono ricevute. È utile per organizzare o raggruppare in batch immagini provenienti da fonti diverse per ulteriori elaborazioni.

**Nota:** Questo nodo è deprecato ed è stato sostituito dal nodo Create List.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Una lista di immagini da unire. Questo input può accettare più connessioni e ogni lista collegata verrà concatenata nell'output finale. | IMAGE | Sì | - |

**Nota:** Questo nodo è progettato per ricevere più input. È possibile collegare diverse liste di immagini all'unico socket di input `images`. Il nodo concatenarà automaticamente tutte le immagini da tutte le liste collegate in un'unica lista di output.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `images` | La lista unica e unificata contenente tutte le immagini da ogni lista di input collegata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeImageLists/it.md)

---
**Source fingerprint (SHA-256):** `0c9e302b02694a6a23fc7776c872856b1a629df3efe914a3e591a89d5a28914a`

# Confronta Immagini

## Panoramica

Il nodo Image Compare fornisce un'interfaccia visiva per confrontare due immagini affiancate tramite un cursore trascinabile. È progettato come nodo di output, il che significa che non trasmette dati ad altri nodi, ma mostra le immagini direttamente nell'interfaccia utente per l'ispezione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image_a` | La prima immagine da confrontare. | IMAGE | No | - |
| `image_b` | La seconda immagine da confrontare. | IMAGE | No | - |
| `compare_view` | Il controllo che abilita la vista di confronto con cursore nell'interfaccia utente. | IMAGECOMPARE | Sì | - |

**Nota:** Questo nodo è un nodo di output. Sebbene `image_a` e `image_b` siano opzionali, è necessario fornire almeno un'immagine affinché il nodo abbia un effetto visibile. Il nodo mostrerà un'area vuota per qualsiasi input immagine non connesso. Ogni batch di immagini fornito viene salvato nell'archivio temporaneo rispettivamente con i prefissi `comfy.compare.a` e `comfy.compare.b`, quindi visualizzato nella vista con cursore.

## Output

Questo nodo è un nodo di output e non produce alcun dato di output utilizzabile in altri nodi. La sua funzione è visualizzare le immagini fornite nell'interfaccia di ComfyUI.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/it.md)

---
**Source fingerprint (SHA-256):** `bc065572c5631ed80c0590aabae775c51d0f607895a87cb2cca78037ab9a6638`

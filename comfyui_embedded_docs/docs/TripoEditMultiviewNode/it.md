# TripoEditMultiviewNode

Modifica le viste di un risultato Tripo: Image to Multiview utilizzando un'istruzione testuale separata per ciascuna vista. Le viste senza un'istruzione rimangono invariate. Le immagini modificate sono pensate per essere collegate a Tripo: Multiview to Model per creare un modello 3D; un set multiview modificato non può essere modificato di nuovo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `multiview_task_id` | Task ID del risultato Tripo: Image to Multiview le cui viste verranno modificate. Deve provenire dal nodo Tripo: Image to Multiview. | MULTIVIEW_TASK_ID | Sì | Task ID |
| `front_prompt` | Istruzione testuale che descrive la modifica da applicare alla vista frontale. Se vuota, la vista frontale rimane invariata. Predefinito: stringa vuota. | STRING | No | Testo multilinea |
| `left_prompt` | Istruzione testuale che descrive la modifica da applicare alla vista sinistra. Se vuota, la vista sinistra rimane invariata. Predefinito: stringa vuota. | STRING | No | Testo multilinea |
| `back_prompt` | Istruzione testuale che descrive la modifica da applicare alla vista posteriore. Se vuota, la vista posteriore rimane invariata. Predefinito: stringa vuota. | STRING | No | Testo multilinea |
| `right_prompt` | Istruzione testuale che descrive la modifica da applicare alla vista destra. Se vuota, la vista destra rimane invariata. Predefinito: stringa vuota. | STRING | No | Testo multilinea |

Nota: almeno uno dei quattro prompt (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) deve contenere testo non vuoto; il testo composto solo da spazi viene considerato vuoto e, se tutti i prompt sono vuoti, il nodo genera un errore.

Nota: il costo è di circa 0,05 USD per ogni vista che ha un'istruzione di modifica.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `front` | Immagine della vista frontale modificata. | IMAGE |
| `left` | Immagine della vista sinistra modificata. | IMAGE |
| `back` | Immagine della vista posteriore modificata. | IMAGE |
| `right` | Immagine della vista destra modificata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/it.md)

---
**Source fingerprint (SHA-256):** `db8b0a3ffe4332fcbcaac4da0d7b07217d01d2f05526750540f6036293e013ab`

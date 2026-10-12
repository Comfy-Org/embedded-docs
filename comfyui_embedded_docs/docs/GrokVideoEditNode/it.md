# GrokVideoEditNode

Questo nodo utilizza l'API Grok per modificare un video esistente in base a un prompt testuale. Carica il tuo video, invia una richiesta al modello AI per modificarlo in base alla tua descrizione e restituisce il video appena generato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `model` | Il modello AI da utilizzare per la modifica video (predefinito: "grok-imagine-video"). | COMBO | Sì | "grok-imagine-video" |
| `prompt` | Descrizione testuale del video desiderato. | STRING | Sì | N/A |
| `video` | Il video di input da modificare. La durata massima supportata è di 8,7 secondi e la dimensione massima del file è di 50MB. | VIDEO | Sì | N/A |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi non sono deterministici, indipendentemente dal seed (predefinito: 0). | INT | No | 0 a 2147483647 |

**Vincoli:**

* Il `prompt` non deve essere vuoto.
* Il `video` di input deve avere una durata compresa tra 1 e 8,7 secondi.
* La dimensione del file `video` di input non deve superare 50MB.

**Nota:** Questo nodo è un nodo API e richiede un account Comfy.org e una chiave API per funzionare. L'utilizzo viene fatturato a circa $0,06 per secondo di video.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video modificato generato dal modello AI. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/it.md)

---
**Source fingerprint (SHA-256):** `7ceedff2f858bc0849b5e0d92d10ed51e7fdccd1391c6a6966561cb05999b4b1`

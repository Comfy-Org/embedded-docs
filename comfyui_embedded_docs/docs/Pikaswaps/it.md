# Pikaswaps

Il nodo Pika Swaps sostituisce oggetti o regioni nel video con una nuova immagine. Si definiscono le aree da sostituire utilizzando una maschera e il nodo sostituisce in modo fluido il contenuto specificato per tutta la sequenza video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Il video in cui sostituire un oggetto. | VIDEO | Sì | - |
| `image` | L'immagine utilizzata per sostituire l'oggetto mascherato nel video. | IMAGE | Sì | - |
| `mask` | Utilizza la maschera per definire le aree del video da sostituire. | MASK | Sì | - |
| `prompt_text` | Prompt testuale che descrive la sostituzione desiderata. | STRING | Sì | - |
| `negative_prompt` | Prompt testuale che descrive ciò che si desidera evitare nella sostituzione. | STRING | Sì | - |
| `seed` | Valore di seed casuale per risultati coerenti. | INT | Sì | da 0 a 4294967295 |

**Nota:** Questo nodo richiede che vengano forniti tutti i parametri di input. `video`, `image` e `mask` collaborano per definire l'operazione di sostituzione, in cui la maschera specifica quali aree del video verranno sostituite con l'immagine fornita.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il video elaborato in cui l'oggetto o la regione specificati sono stati sostituiti. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/it.md)

---
**Source fingerprint (SHA-256):** `007b7bc429fdada2fb8910392b056ae3a98d482cce9e280bdcd162ede497eb03`

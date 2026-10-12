# Salva Immagine (in Cartella) (DEPRECATO)

Questo nodo salva un elenco di immagini in una cartella specificata all'interno della directory di output di ComfyUI. Scrive ogni immagine su disco come file PNG utilizzando un prefisso del nome file configurabile. Questo nodo è deprecato e sostituito dai nodi Save Image esistenti, dove la cartella di destinazione può essere specificata nel prefisso del nome file.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `images` | Elenco di immagini da salvare. | IMAGE | Sì | N/A |
| `folder_name` | Nome della cartella in cui salvare le immagini (all'interno della directory di output). Predefinito: "dataset". | STRING | No | N/A |
| `filename_prefix` | Prefisso per i nomi file delle immagini salvate. Predefinito: "image". Parametro avanzato. | STRING | No | N/A |
| `mode` | Indica se sovrascrivere i file esistenti o incrementare i nomi file per evitare la sovrascrittura. Predefinito: "overwrite". | COMBO | No | "overwrite"<br>"increment" |

**Note:**

- L'input `images` è un elenco, quindi più immagini possono essere salvate in una singola esecuzione.
- I parametri `folder_name`, `filename_prefix` e `mode` sono valori scalari; se viene collegato un elenco, viene utilizzato solo il primo valore di tale elenco.
- Il `folder_name` deve risolversi in una posizione all'interno della directory di output di ComfyUI. I valori che escono dalla directory di output (ad esempio, percorsi contenenti `..` o percorsi assoluti, lettere di unità o escape di collegamenti simbolici) vengono rifiutati con un errore.
- Nella modalità "overwrite", i file vengono salvati come `{prefix}_00000.png`, `{prefix}_00001.png` e così via, sostituendo eventuali file esistenti. Nella modalità "increment", viene inserito un contatore nel nome file in modo che i file esistenti non vengano sovrascritti.
- È supportato solo l'output PNG.

## Output

Questo nodo non ha output. È un nodo di output che esegue un'operazione di salvataggio sul filesystem.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/it.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`

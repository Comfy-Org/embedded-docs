# LoadImageSetFromFolderNode

LoadImageSetFromFolderNode carica più immagini da una cartella specificata per scopi di addestramento. Rileva automaticamente i formati immagine comuni e può facoltativamente ridimensionare le immagini utilizzando metodi diversi prima di restituirle come batch.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `folder` | La cartella da cui caricare le immagini. | STRING | Sì | Sono disponibili più opzioni |
| `resize_method` | Il metodo da utilizzare per ridimensionare le immagini (predefinito: "None"). | STRING | No | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `IMAGE` | Il batch di immagini caricate come un singolo tensore. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/it.md)

---
**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`

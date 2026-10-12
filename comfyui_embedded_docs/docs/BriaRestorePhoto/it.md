# Bria Ripristina foto

Questo nodo ripara fotografie vecchie o danneggiate tramite l'API Bria. Rimuove grana, graffi e sfocatura, neutralizza le dominanti di colore legate all'invecchiamento, può ritagliare via supporti in cartoncino e bordi da studio, e ridisegna i volti. Il risultato viene renderizzato nuovamente a circa 1 megapixel, quindi non è allineato al pixel con l'input.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | La fotografia da riparare. Il canale alpha viene eliminato prima del caricamento. | IMAGE | Sì | - |
| `moderation` | Impostazioni di moderazione per la richiesta. Selezionando `"true"` vengono mostrati due ulteriori interruttori booleani; selezionando `"false"` non viene inviato alcun flag di moderazione. Predefinito: `"false"`. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |

### Input di moderazione

Questi input compaiono solo quando `moderation` è impostato su `"true"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `visual_input_moderation` | Abilita la moderazione dei contenuti visivi sull'immagine di input. Predefinito: false. | BOOLEAN | No | true<br>false |
| `visual_output_moderation` | Abilita la moderazione dei contenuti visivi sull'immagine di output. Predefinito: false. | BOOLEAN | No | true<br>false |

**Nota:** Il nodo renderizza nuovamente l'intera inquadratura a circa 1 megapixel, quindi il risultato non è allineato al pixel con l'input. Usa il nodo Bria Increase Resolution per ingrandire l'immagine invece di questo nodo.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | La fotografia riparata restituita da Bria. | IMAGE |
| `structured_prompt` | Descrizione strutturata dell'immagine modificata, per una modifica successiva con Bria FIBO Image Edit. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRestorePhoto/it.md)

---
**Source fingerprint (SHA-256):** `387ec3e049464f185e27f79d160ade2a4170ab238853064c008892d84523fa68`

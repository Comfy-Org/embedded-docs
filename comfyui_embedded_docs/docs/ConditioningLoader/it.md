# ConditioningLoader

Questo nodo carica dalla cartella embeddings un conditioning salvato in precedenza con il nodo Save Conditioning, oppure qualsiasi file safetensors che contenga un tensore `conditioning`. Ripristina inoltre eventuali opzioni extra e valori di liste numerate memorizzati insieme al conditioning.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `conditioning_name` | Il file da caricare dalla cartella embeddings. L'elenco delle scelte viene costruito dai file attualmente disponibili in tale cartella. | COMBO | Sì | Tutti i file nella cartella embeddings |

**Nota:** Il file selezionato deve contenere un tensore `conditioning`. Qualsiasi chiave aggiuntiva memorizzata nel file viene ripristinata: le chiavi numerate (ad esempio `key.0`, `key.1`) vengono raggruppate di nuovo in liste ordinate, mentre le altre chiavi vengono ripristinate come opzioni semplici. Le opzioni extra vengono lette dai metadati `conditioning_options` del file, quando presenti.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `CONDITIONING` | Il conditioning caricato dal file, insieme alle opzioni ripristinate. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningLoader/it.md)

---
**Source fingerprint (SHA-256):** `08fc58bcaa2309fcf03d4e4cc634b930aaf6ccf8097181fd3d45924abda144eb`

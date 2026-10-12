# SaveText

Il nodo Save Text scrive contenuto testuale in un file nella directory di output. Supporta il salvataggio nei formati .txt, .csv, .md o .json e gestisce automaticamente la formattazione leggibile del JSON quando viene fornito JSON valido.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `text` | Il contenuto testuale da salvare in un file. Questo input deve essere collegato da un altro nodo. | STRING | Sì | - |
| `filename_prefix` | Prefisso per il nome del file di output. Un contatore di 5 cifre viene aggiunto per evitare di sovrascrivere file esistenti (predefinito: "ComfyUI"). | STRING | No | - |
| `format` | Formato del file in cui salvare il testo (predefinito: "txt"). Quando è selezionato "json", il testo JSON valido viene formattato con indentazione di 2 spazi; in caso contrario, il testo viene salvato così com'è. | COMBO | No | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

### Note

- `text` è un input forzato e deve essere collegato a un altro nodo; non può essere digitato direttamente.
- Il file salvato è denominato `<filename_prefix>_<5-digit counter>.<extension>` e viene scritto nella directory di output di ComfyUI (in una sottocartella derivata dal prefisso).
- Selezionando il formato `"json"` si tenta di analizzare il testo come JSON. Se l'analisi riesce, il contenuto viene scritto formattato con indentazione di 2 spazi; se l'analisi fallisce, il testo grezzo viene scritto invariato.
- Il nodo segnala il file salvato all'interfaccia, in modo che compaia insieme agli altri file di output generati.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `text` | Il contenuto testuale originale che è stato salvato nel file | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/it.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`

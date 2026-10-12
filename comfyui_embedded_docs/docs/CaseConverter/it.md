# Converti Maiuscole/Minuscole

Il nodo Case Converter trasforma le stringhe di testo in diversi formati di maiuscole/minuscole. Riceve una stringa di input e la converte in base alla modalità selezionata, producendo una stringa di output con la formattazione di maiuscole/minuscole specificata applicata. Il nodo supporta quattro diverse opzioni di conversione delle maiuscole/minuscole per modificare la capitalizzazione del testo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `string` | La stringa di testo da convertire in un diverso formato di maiuscole/minuscole | STRING | Sì | - |
| `mode` | La modalità di conversione delle maiuscole/minuscole da applicare (predefinita: `"UPPERCASE"`) | STRING | Sì | `"UPPERCASE"`<br>`"lowercase"`<br>`"Capitalize"`<br>`"Title Case"` |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | La stringa di input convertita nel formato di maiuscole/minuscole specificato | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/it.md)

---
**Source fingerprint (SHA-256):** `6cc933ec8a245ff454195b699ab7d72d2a014ec9a6e920a8c875acf7eb77e01a`

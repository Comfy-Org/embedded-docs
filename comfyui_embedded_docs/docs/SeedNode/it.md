# SeedNode

Il nodo Seed fornisce un valore intero che può essere usato come seed per controllare la riproducibilità delle operazioni casuali in altri nodi. Fornendo un valore iniziale coerente, aiuta a mantenere i risultati generati ripetibili quando necessario.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `seed` | Il valore seed da usare. L'opzione control after generate determina se il valore rimane fisso o cambia dopo ogni generazione; in questo nodo è impostata su fixed. | INT | Sì | da 0 a 9223372036854775807 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `seed` | Il valore seed generato. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/it.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`

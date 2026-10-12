# OpenAIInputFiles

Carica e formatta i file di input per l'API OpenAI. Questo nodo prepara file di testo (.txt) e PDF (.pdf) da includere come input di contesto per il nodo OpenAI Chat. I file verranno letti dal modello OpenAI durante la generazione di una risposta. Più nodi OpenAI Input Files possono essere concatenati per includere diversi file in un singolo messaggio.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `file` | File di input da includere come contesto per il modello. Per ora accetta solo file di testo (.txt) e PDF (.pdf). I file devono essere più piccoli di 32MB. | COMBO | Sì | Sono disponibili più opzioni (tutti i file .txt e .pdf nella directory di input di dimensione inferiore a 32MB) |
| `OPENAI_INPUT_FILES` | Uno o più file aggiuntivi opzionali da raggruppare insieme al file caricato da questo nodo. Consente di concatenare i file di input in modo che un singolo messaggio possa includere più file di input. | OPENAI_INPUT_FILES | No | N/A |

**Vincoli sui file:**

- Sono supportati solo file .txt e .pdf
- Dimensione massima del file: 32MB
- I file vengono caricati dalla directory di input di ComfyUI

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `OPENAI_INPUT_FILES` | File di input formattati, pronti per essere usati come contesto per le chiamate all'API OpenAI. | OPENAI_INPUT_FILES |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/it.md)

---
**Source fingerprint (SHA-256):** `6554e685184ced830ee27aa96efefc8bb9616bd0504685bdb643c715ebc6dd98`

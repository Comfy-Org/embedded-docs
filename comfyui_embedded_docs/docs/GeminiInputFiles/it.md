# GeminiInputFiles

Carica e formatta i file di input per l'uso con l'API Gemini. Questo nodo consente agli utenti di includere file di testo (.txt) e PDF (.pdf) come contesto di input per il modello Gemini. I file vengono convertiti nel formato appropriato richiesto dall'API e possono essere concatenati per includere più file in un'unica richiesta.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `file` | File di input da includere come contesto per il modello. Per ora accetta solo file di testo (.txt) e PDF (.pdf). I file devono essere più piccoli del limite massimo di dimensione del file di input (20 MB). | COMBO | Sì | Più opzioni disponibili (solo file .txt e .pdf inferiori a 20 MB) |
| `GEMINI_INPUT_FILES` | File aggiuntivi opzionali da raggruppare insieme al file caricato da questo nodo. Consente il concatenamento dei file di input in modo che un singolo messaggio possa includere più file di input. | GEMINI_INPUT_FILES | No | N/A |

**Nota:** Il parametro `file` mostra solo file di testo (.txt) e PDF (.pdf) inferiori a 20 MB. I file vengono automaticamente filtrati e ordinati per nome.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `GEMINI_INPUT_FILES` | Dati dei file formattati e pronti per l'uso con i nodi Gemini LLM, contenenti il contenuto del file caricato nel formato API appropriato. | GEMINI_INPUT_FILES |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/it.md)

---
**Source fingerprint (SHA-256):** `1c80a87746c7ac73379f5c1e2d5c4d22f0fc44d3241fafb0297e087e436df7d6`

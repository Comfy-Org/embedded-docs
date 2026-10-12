# Salva Conditioning

Questo nodo salva un singolo conditioning nella cartella di output come file safetensors. Il file salvato può essere spostato nella cartella models/embeddings e caricato successivamente con Load Conditioning, ad esempio per saltare il codificatore di testo. Il nodo lascia passare il conditioning invariato, così può ancora essere utilizzato successivamente nel workflow.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | Il conditioning da salvare. È supportata una sola voce di conditioning. | CONDITIONING | Sì | - |
| `filename_prefix` | Prefisso usato per costruire il nome del file di output. Il file viene scritto nella cartella di output con un contatore numerico aggiunto. Predefinito: `conditioning/ComfyUI` | STRING | Sì | - |

**Note:**

- Se l'input `conditioning` contiene più di una voce (ad esempio dopo aver combinato conditioning), il nodo genera un errore: "Save Conditioning supports a single conditioning entry, save it before combining."
- Le opzioni del conditioning che sono tensori, liste/tuple di tensori, booleani, interi, float o stringhe vengono salvate insieme al conditioning. Le opzioni che sono `None` vengono saltate. Qualsiasi altro tipo di opzione genera un errore indicando che l'opzione non può essere salvata.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `conditioning` | Lo stesso conditioning passato in ingresso, invariato. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveConditioning/it.md)

---
**Source fingerprint (SHA-256):** `07b7d2be5262c4782f237138d034b130322507e62ae8775b9c94634df8e7a3fa`

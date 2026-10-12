# Salva Audio (MP3) (DEPRECATO)

Il nodo SaveAudioMP3 salva i dati audio come file MP3. Riceve un input audio e lo esporta nella directory di output con un nome file e un'impostazione di qualità personalizzabili, gestendo automaticamente la denominazione dei file e la conversione nel formato MP3. **Questo nodo è deprecato e potrebbe essere rimosso nelle versioni future.**

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `audio` | I dati audio da salvare come file MP3 | AUDIO | Sì | - |
| `filename_prefix` | Il prefisso per il nome del file di output (predefinito: "audio/ComfyUI") | STRING | No | - |
| `quality` | L'impostazione della qualità audio per il file MP3 (predefinito: "V0") | COMBO | No | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Dati del prompt interni, forniti automaticamente dal sistema | PROMPT | No | - |
| `extra_pnginfo` | Informazioni PNG aggiuntive, fornite automaticamente dal sistema | EXTRA_PNGINFO | No | - |

**Nota:** Se l'input `audio` è None (ad esempio, quando il video di origine non ha una traccia audio), il nodo solleva un ValueError.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `audio` | I dati audio che sono stati salvati in un file MP3 | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/it.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`

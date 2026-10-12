# PixverseTextToVideoNode

Genera video da un prompt testuale utilizzando l'API di PixVerse. Il nodo consente di controllare forma, qualità, durata e stile di movimento del video e può facoltativamente applicare un modello di stile salvato. Invia la richiesta, attende il completamento della generazione e restituisce il video finito.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt per la generazione del video (predefinito: "") | STRING | Sì | Deve contenere almeno 1 carattere |
| `aspect_ratio` | Proporzioni per il video generato | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `quality` | Impostazione della qualità video (predefinito: "540p") | COMBO | Sì | `"540p"`<br>`"1080p"` |
| `duration_seconds` | Durata del video generato in secondi | COMBO | Sì | `"5"`<br>`"10"` |
| `motion_mode` | Stile di movimento per la generazione del video | COMBO | Sì | `"normal"`<br>`"fast"` |
| `seed` | Seed per la generazione del video (predefinito: 0) | INT | Sì | da 0 a 2147483647 |
| `negative_prompt` | Una descrizione testuale opzionale degli elementi indesiderati in un'immagine (predefinito: "") | STRING | No | - |
| `pixverse_template` | Un modello opzionale per influenzare lo stile della generazione, creato dal nodo PixVerse Template | CUSTOM | No | - |

**Nota:** Il `prompt` deve contenere almeno 1 carattere. Quando è selezionata la qualità 1080p, la modalità di movimento viene impostata automaticamente su `normal` e la durata è limitata a 5 secondi. Per qualsiasi durata diversa da 5 secondi, anche la modalità di movimento viene impostata automaticamente su `normal`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `output` | Il file video generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`

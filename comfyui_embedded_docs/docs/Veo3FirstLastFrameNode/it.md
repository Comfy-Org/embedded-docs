# Google Veo 3 Da Primo-Ultimo Frame a Video

Il nodo Veo3FirstLastFrameNode utilizza il modello Veo 3 di Google per generare un video basato su un prompt testuale, con un primo e un ultimo frame forniti che definiscono l'inizio e la fine della sequenza video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione testuale del video (predefinito: stringa vuota). | STRING | Sì | N/A |
| `negative_prompt` | Prompt di testo negativo per guidare ciò che si deve evitare nel video (predefinito: stringa vuota). | STRING | No | N/A |
| `resolution` | La risoluzione del video di output. | COMBO | Sì | `"720p"`<br>`"1080p"`<br>`"4k"` |
| `aspect_ratio` | Rapporto d'aspetto del video di output (predefinito: "16:9"). | COMBO | No | `"16:9"`<br>`"9:16"` |
| `duration` | Durata del video di output in secondi (predefinito: 8, passo: 2). | INT | No | 4 to 8 |
| `seed` | Seme per la generazione del video (predefinito: 0). | INT | No | 0 to 4294967295 |
| `first_frame` | Il frame iniziale del video. | IMAGE | Sì | N/A |
| `last_frame` | Il frame finale del video. | IMAGE | Sì | N/A |
| `model` | Il modello Veo specifico da usare per la generazione (predefinito: "veo-3.1-generate"). | COMBO | No | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"`<br>`"veo-3.1-lite"` |
| `generate_audio` | Genera l'audio per il video (predefinito: True). | BOOLEAN | No | N/A |

**Nota:** Il modello `veo-3.1-lite` non supporta la risoluzione 4K. Se selezioni `veo-3.1-lite` e la risoluzione `4k`, si verificherà un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/it.md)

---
**Source fingerprint (SHA-256):** `2fe55d2a1d018e58fd290c901c596708898acda835d2358adf36ed80103aeb6e`

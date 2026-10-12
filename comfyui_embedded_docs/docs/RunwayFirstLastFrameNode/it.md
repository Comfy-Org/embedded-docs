# Runway First-Last-Frame to Video

Il nodo Runway First-Last-Frame to Video genera un video utilizzando un frame iniziale, un frame finale e un prompt testuale. Crea una transizione fluida tra i due keyframe forniti utilizzando il modello gen3a_turbo di Runway. È particolarmente utile per transizioni complesse in cui il frame finale è completamente diverso dal frame iniziale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione (predefinito: stringa vuota) | STRING | Sì | N/D |
| `start_frame` | Frame iniziale da utilizzare per il video | IMAGE | Sì | N/D |
| `end_frame` | Frame finale da utilizzare per il video. Supportato solo per gen3a_turbo. | IMAGE | Sì | N/D |
| `duration` | Durata del video generato in secondi. La durata maggiore di 10 s dà alla generazione più tempo per transitare in modo fluido tra il frame iniziale e quello finale (predefinito: "5"). | COMBO | Sì | `"5"`<br>`"10"` |
| `ratio` | Rapporto d'aspetto per il video generato (predefinito: "768:1280") | COMBO | Sì | `"768:1280"`<br>`"1280:768"` |
| `seed` | Seme casuale per la generazione (predefinito: 0) | INT | Sì | da 0 a 4294967295 |

**Vincoli dei parametri:**

- Il `prompt` deve contenere almeno 1 carattere
- Sia `start_frame` che `end_frame` devono avere dimensioni massime di 7999x7999 pixel
- Sia `start_frame` che `end_frame` devono avere un rapporto d'aspetto compreso tra 0.5 e 2.0
- Il parametro `end_frame` è supportato solo quando si utilizza il modello gen3a_turbo

**Note:**

- Il costo di generazione si basa sulla durata selezionata: 0,0715 USD al secondo (0,3575 USD per 5 secondi, 0,715 USD per 10 secondi)
- Questo nodo è contrassegnato come deprecato

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il video generato che transita tra il frame iniziale e quello finale | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/it.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`

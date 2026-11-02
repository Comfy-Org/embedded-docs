# MiniMax H3 Max Reframe Video

Questo nodo adatta un video a un nuovo rapporto d'aspetto inserendolo in una nuova tela e generando le aree circostanti. La temporizzazione e l'audio del video di origine vengono mantenuti. Usalo per trasformare una clip orizzontale in una verticale, o viceversa, senza tagliare il soggetto fuori dall'inquadratura.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare per la generazione video. | DYNAMIC_COMBO | Sì | "MiniMax H3 Max" |

### Input di MiniMax H3 Max

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Video di origine da riinquadrare, della durata da 0,5 a 300 secondi. | VIDEO | Sì | 0.5 a 300 secondi |
| `aspect_ratio` | Rapporto d'aspetto della tela di output (predefinito: "9:16"). | COMBO | Sì | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21" |
| `resolution` | Risoluzione del video di output (predefinito: "768P"). | COMBO | Sì | "480P"<br>"768P"<br>"1080P" |
| `prompt` | Indicazioni facoltative per le aree circostanti generate. | STRING | Sì | 0 a 50000 caratteri |
| `seed` | Seme casuale. La stessa richiesta con lo stesso seme produce risultati simili, ma non garantiti identici (predefinito: 42). | INT | Sì | 0 a 4294967295 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il video riinquadrato con il rapporto d'aspetto selezionato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxReframeVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `83d780c2fe8c42475d4ad25ad5b318f2a4c135edef9c0ca1ff0d1fd07d90c1c6`

# YuE2 Genera ABC

Questo nodo genera una notazione ABC per un brano basandosi su una descrizione di stile e sulle parole, utilizzando un modello YuE2 per testo e testi. L'output `abc` risultante può essere collegato al nodo YuE2 Generate Music per produrre audio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Il modello YuE2 utilizzato per tokenizzare lo stile e le parole e generare la notazione ABC. | CLIP | Sì | - |
| `style` | Testo che descrive lo stile musicale del brano. Supporta input multilinea e prompt dinamici. | STRING | Sì | - |
| `lyrics` | Testo contenente le parole del brano. Supporta input multilinea e prompt dinamici. | STRING | Sì | - |
| `seed` | Seme casuale utilizzato per la generazione. Modificarlo produce risultati diversi. Predefinito: 0. | INT | Sì | 0 a 18446744073709551615 |
| `mode` | full: genera melodia e accordi; melody: genera solo la melodia, consigliato per le cover. | COMBO | Sì | "full"<br>"melody" |
| `max_abc_tokens` | Numero massimo di token generati per la notazione ABC. Predefinito: 8192. Impostazione avanzata. | INT | Sì | 1 a 20000 |
| `temperature` | Controlla la casualità dei token generati. Valori più alti producono un output più vario. Predefinito: 0.7. Impostazione avanzata. | FLOAT | Sì | 0.0 a 5.0 |
| `top_p` | Soglia di campionamento nucleus; vengono considerati solo i token entro questa probabilità cumulativa. Predefinito: 0.9. Impostazione avanzata. | FLOAT | Sì | 0.01 a 1.0 |
| `top_k` | Limita la selezione dei token ai K token più probabili. Predefinito: 30. Impostazione avanzata. | INT | Sì | 1 a 32768 |
| `repetition_penalty` | Penalità applicata ai token ripetuti durante la generazione. Predefinito: 1.005. Impostazione avanzata. | FLOAT | Sì | 0.01 a 10.0 |
| `penalty_window` | Numero di token ABC recenti utilizzati per penalizzare la ripetizione. Predefinito: 100. Impostazione avanzata. | INT | Sì | 1 a 20000 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `abc` | La notazione ABC generata per il brano, che può essere collegata al nodo YuE2 Generate Music. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/it.md)

---
**Source fingerprint (SHA-256):** `2c1bf0841a044724ff0477f920972d70bbd97de49b56fbe6213a9ac134797130`

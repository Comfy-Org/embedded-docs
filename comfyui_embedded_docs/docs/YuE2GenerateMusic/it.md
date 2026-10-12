# YuE2 Genera musica

Genera token musicali e condizionamento acustico a partire da uno stile, da un testo e da una notazione ABC. Restituisce il condizionamento e la durata generata in secondi; quest'ultima deve essere fornita al nodo Empty YuE2 Latent Audio. Se l'input ABC viene lasciato vuoto, la modalità selezionata viene ignorata e viene usata automaticamente la modalità off.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip` | Il modello CLIP usato per tokenizzare e codificare gli input musicali. | CLIP | Sì | - |
| `style` | Testo che descrive lo stile musicale. Supporta input multiriga e prompt dinamici. | STRING | Sì | Testo multiriga |
| `lyrics` | Testo per la musica generata. Supporta input multiriga e prompt dinamici. | STRING | Sì | Testo multiriga |
| `abc` | Collega il generatore ABC oppure fornisci uno spartito modificato. Lascia vuoto per usare automaticamente la modalità off. predefinito: "" | STRING | Sì | Testo multiriga |
| `seed` | Seme casuale per la generazione. predefinito: 0 | INT | Sì | da 0 a 18446744073709551615 |
| `mode` | full: genera melodia e accordi; melody: genera solo melodia, consigliato per le cover. predefinito: "full" | COMBO | Sì | "full"<br>"melody" |
| `max_duration` | Durata massima in secondi. Ridotta automaticamente per prompt lunghi; la generazione può interrompersi prima. predefinito: 360.0 | FLOAT | Sì | da 0.04 a 900.0 |
| `temperature` | Temperatura di campionamento per la generazione. predefinito: 1.0 (avanzato) | FLOAT | Sì | da 0.0 a 5.0 |
| `top_p` | Soglia di probabilità per il campionamento nucleus. predefinito: 0.95 (avanzato) | FLOAT | Sì | da 0.01 a 1.0 |
| `top_k` | Limite di campionamento top-k. predefinito: 100 (avanzato) | INT | Sì | da 1 a 32768 |
| `repetition_penalty` | Penalità applicata ai token ripetuti. predefinito: 1.2 (avanzato) | FLOAT | Sì | da 0.01 a 10.0 |
| `cfg_scale` | Guidance autoregressiva per stile e testo. 1.0 disabilita CFG, in linea con il workflow ABC. Usa 1.01 per corrispondere alla guidance originale della modalità off. predefinito: 1.0 (avanzato, opzionale) | FLOAT | No | da 0.0 a 100.0 |

Nota: se `abc` è vuoto o contiene solo spazi bianchi, la selezione di `mode` viene ignorata e viene usata automaticamente la modalità off.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `CONDITIONING` | Condizionamento acustico generato dai token musicali. | CONDITIONING |
| `seconds` | La durata audio generata in secondi. Fornisci questo valore al nodo Empty YuE2 Latent Audio. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/it.md)

---
**Source fingerprint (SHA-256):** `5a88e185d2998c51acff7f0c76c8c35ca30b80b88cb541d97f9ab91566b5a3ed`

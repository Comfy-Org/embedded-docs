# ConditioningSetAreaPercentageVideo

Il nodo ConditioningSetAreaPercentageVideo modifica i dati di conditioning definendo un'area specifica e una regione temporale per la generazione video. Utilizza valori percentuali relativi alle dimensioni complessive per impostare la posizione, le dimensioni e la durata dell'area in cui viene applicato il conditioning. Questo è utile per concentrare la generazione su parti specifiche di una sequenza video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | I dati di conditioning da modificare | CONDITIONING | Sì | - |
| `width` | La larghezza dell'area come percentuale della larghezza totale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step 0.01) |
| `height` | L'altezza dell'area come percentuale dell'altezza totale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step 0.01) |
| `temporal` | La durata temporale dell'area come percentuale della lunghezza totale del video (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step 0.01) |
| `x` | La posizione iniziale orizzontale dell'area come percentuale (predefinito: 0.0) | FLOAT | Sì | 0.0 - 1.0 (step 0.01) |
| `y` | La posizione iniziale verticale dell'area come percentuale (predefinito: 0.0) | FLOAT | Sì | 0.0 - 1.0 (step 0.01) |
| `z` | La posizione iniziale temporale dell'area come percentuale della linea temporale del video (predefinito: 0.0) | FLOAT | Sì | 0.0 - 1.0 (step 0.01) |
| `strength` | Il moltiplicatore di forza applicato al conditioning all'interno dell'area definita (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 (step 0.01) |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `conditioning` | I dati di conditioning modificati con le impostazioni di area e forza specificate applicate | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/it.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`

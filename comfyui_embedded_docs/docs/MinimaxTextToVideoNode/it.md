# MiniMax Da Testo a Video

Genera video in modo sincrono basandosi su un prompt testuale e parametri opzionali utilizzando l'API di MiniMax. Questo nodo crea contenuti video a partire da descrizioni testuali connettendosi al servizio text-to-video di MiniMax.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt_text` | Prompt testuale per guidare la generazione del video | STRING | Sì | - |
| `model` | Modello da utilizzare per la generazione del video (predefinito: "T2V-01") | COMBO | No | "T2V-01"<br>"T2V-01-Director" |
| `seed` | Il seme casuale utilizzato per creare il rumore (predefinito: 0) | INT | No | 0 to 18446744073709551615 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `output` | Il video generato in base al prompt di input | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `1d389bdcc48f903e04dad043a8609250f34466b9084b1319c411e155a8040422`

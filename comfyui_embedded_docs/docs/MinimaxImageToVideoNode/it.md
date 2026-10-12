# MinimaxImageToVideoNode

Genera video in modo sincrono a partire da un'immagine e un prompt, e da parametri opzionali, utilizzando l'API di MiniMax. Questo nodo riceve un'immagine di input e una descrizione testuale per creare una sequenza video, con varie opzioni di modello e impostazioni di configurazione disponibili.

## Input
| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Immagine da usare come primo fotogramma della generazione video | IMAGE | Sì | - |
| `prompt_text` | Prompt testuale per guidare la generazione video (predefinito: stringa vuota) | STRING | Sì | - |
| `model` | Modello da usare per la generazione video (predefinito: "I2V-01") | COMBO | Sì | "I2V-01-Director"<br>"I2V-01"<br>"I2V-01-live" |
| `seed` | Il seed casuale usato per creare il rumore (predefinito: 0) | INT | No | 0 to 18446744073709551615 |

## Output
| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | L'output video generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `90eef1d58fa0ae4897ab19d702ecad707948eb79181ac4927dba650056e954c8`

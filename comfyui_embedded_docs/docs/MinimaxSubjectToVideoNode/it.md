# MinimaxSubjectToVideoNode

Genera un video in modo sincrono basandosi su un'immagine del soggetto e un prompt testuale utilizzando l'API di MiniMax. Questo nodo prende in input un'immagine di un soggetto e una descrizione per creare un video che anima o ha come protagonista quel soggetto in base al prompt.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `subject` | Immagine del soggetto da usare come riferimento per la generazione del video | IMAGE | Sì | - |
| `prompt_text` | Prompt testuale per guidare la generazione del video (predefinito: stringa vuota) | STRING | Sì | - |
| `model` | Modello da utilizzare per la generazione del video (predefinito: "S2V-01") | COMBO | No | `"S2V-01"` |
| `seed` | Il seed casuale utilizzato per creare il rumore (predefinito: 0) | INT | No | 0 to 18446744073709551615 |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `output` | Il video generato in base all'immagine del soggetto e al prompt di input | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `e7d496d8e24a776bbea4afe102858e7d31c4f2e273889703eb02cc61e8389055`

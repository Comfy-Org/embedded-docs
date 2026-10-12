# ViduImageToVideoNode

Il nodo Vidu Image To Video Generation crea un breve video a partire da un'immagine iniziale e da una descrizione testuale opzionale. Utilizza un modello AI per generare contenuto video che continua dal frame immagine fornito e restituisce il video risultante.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | Nome del modello (predefinito: viduq1) | COMBO | Sì | `viduq1` |
| `image` | Un'immagine da usare come frame iniziale del video generato | IMAGE | Sì | - |
| `prompt` | Una descrizione testuale per la generazione del video (predefinito: vuoto) | STRING | No | - |
| `duration` | Durata del video di output in secondi (predefinito: 5, fissato a 5 secondi) | INT | No | 5-5 |
| `seed` | Seed per la generazione del video (0 per casuale) (predefinito: 0) | INT | No | 0-2147483647 |
| `resolution` | I valori supportati possono variare in base al modello e alla durata (predefinito: 1080p) | COMBO | No | `1080p` |
| `movement_amplitude` | L'ampiezza di movimento degli oggetti nel frame (predefinito: auto) | COMBO | No | `auto`<br>`small`<br>`medium`<br>`large` |

**Vincoli:**

- È consentita una sola immagine di input (non è possibile elaborare più immagini).
- L'immagine di input deve avere un rapporto d'aspetto compreso tra 1:4 e 4:1.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `output` | L'output video generato | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `9e3b1ba325c44fcd03207f93030eba1a66507f9613d93135546ab7b6f37f7699`

# OpenAI GPT Image 2

Genera immagini in modo sincrono tramite l'endpoint GPT Image di OpenAI. Può creare nuove immagini da un prompt testuale o modificare immagini esistenti quando vengono fornite un'immagine di input e una maschera opzionale. Il nodo supporta i modelli `gpt-image-1`, `gpt-image-1.5` e `gpt-image-2` ed è contrassegnato come deprecato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale per GPT Image (predefinito: "") | STRING | Sì | - |
| `seed` | Seme casuale per la generazione; non ancora implementato nel backend (predefinito: 0) | INT | No | 0 a 2147483647 |
| `quality` | Qualità dell'immagine, influisce sul costo e sul tempo di generazione (predefinito: "low") | COMBO | No | "low"<br>"medium"<br>"high" |
| `background` | Restituisce l'immagine con o senza sfondo (predefinito: "auto") | COMBO | No | "auto"<br>"opaque"<br>"transparent" |
| `size` | Dimensione dell'immagine. Seleziona "Custom" per usare larghezza e altezza personalizzate (solo GPT Image 2) (predefinito: "auto") | COMBO | No | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Quante immagini generare (predefinito: 1) | INT | No | 1 a 8 |
| `image` | Immagine di riferimento opzionale per la modifica delle immagini | IMAGE | No | - |
| `mask` | Maschera opzionale per l'inpainting (le aree bianche verranno sostituite) | MASK | No | - |
| `model` | Modello GPT Image da usare (predefinito: "gpt-image-2") | COMBO | No | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | Usato solo quando `size` è "Custom". Deve essere un multiplo di 16 (solo GPT Image 2) (predefinito: 1024) | INT | No | 1024 a 3840, passo 16 |
| `custom_height` | Usato solo quando `size` è "Custom". Deve essere un multiplo di 16 (solo GPT Image 2) (predefinito: 1024) | INT | No | 1024 a 3840, passo 16 |

**Vincoli dei parametri:**

- Quando viene fornito `image`, il nodo utilizza l'endpoint di modifica delle immagini.
- `mask` può essere utilizzato solo quando viene fornito `image`.
- Quando si utilizza `mask`, sono supportate solo immagini singole (la dimensione del batch deve essere 1).
- `mask` e `image` devono avere le stesse dimensioni.
- La risoluzione personalizzata (`size` = "Custom") è supportata solo dal modello `gpt-image-2`.
- La larghezza e l'altezza personalizzate devono essere multipli di 16.
- Il lato più lungo di una risoluzione personalizzata deve essere 3840 o inferiore.
- Le proporzioni di una risoluzione personalizzata non devono superare 3:1.
- Il numero totale di pixel di una risoluzione personalizzata deve essere compreso tra 655.360 e 8.294.400.
- I modelli `gpt-image-1` e `gpt-image-1.5` supportano solo le dimensioni `auto`, `1024x1024`, `1024x1536` e `1536x1024`. Le altre dimensioni sono supportate solo dal modello `gpt-image-2`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `IMAGE` | Immagine o immagini generate o modificate. Più immagini vengono restituite come batch; se le immagini restituite hanno dimensioni diverse, vengono ridimensionate per corrispondere alla prima immagine. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/it.md)

---
**Source fingerprint (SHA-256):** `f0f0db7fd2cdf8efd2155522b289aa8f3f939fa79a6e9060b0ffbb2dd20efa1e`

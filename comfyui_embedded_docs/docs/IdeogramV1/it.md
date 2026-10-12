# IdeogramV1

Il nodo IdeogramV1 genera immagini usando il modello Ideogram V1 tramite un'API. Accetta prompt testuali e varie impostazioni di generazione per creare una o più immagini in base all'input. Il nodo supporta diversi rapporti d'aspetto e modalità di generazione per personalizzare l'output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione dell'immagine (predefinito: vuoto) | STRING | Sì | - |
| `turbo` | Indica se usare la modalità turbo (generazione più rapida, potenzialmente qualità inferiore) (predefinito: False) | BOOLEAN | Sì | - |
| `aspect_ratio` | Il rapporto d'aspetto per la generazione dell'immagine (predefinito: "1:1") | COMBO | No | "1:1"<br>"4:3"<br>"3:4"<br>"16:9"<br>"9:16"<br>"2:1"<br>"1:2"<br>"3:2"<br>"2:3"<br>"4:5"<br>"5:4" |
| `magic_prompt_option` | Determina se MagicPrompt deve essere usato durante la generazione (predefinito: "AUTO") | COMBO | No | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Valore di seed casuale per la generazione (predefinito: 0) | INT | No | 0-2147483647 |
| `negative_prompt` | Descrizione di ciò che deve essere escluso dall'immagine (predefinito: vuoto) | STRING | No | - |
| `num_images` | Numero di immagini da generare (predefinito: 1) | INT | No | 1-8 |

**Nota:** Il parametro `num_images` ha un limite massimo di 8 immagini per richiesta di generazione.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | L'immagine o le immagini generate dal modello Ideogram V1 | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/it.md)

---
**Source fingerprint (SHA-256):** `c9b336054cf5d66228aeccab615985d2e9c9bdf7dce5d607212fed8a35c2c793`

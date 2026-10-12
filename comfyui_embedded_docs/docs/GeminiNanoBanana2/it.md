# Nano Banana 2

Il nodo Nano Banana 2 genera o modifica immagini in modo sincrono tramite l'API Google Vertex utilizzando il modello Gemini 3.1 Flash Image. Invia un prompt testuale, insieme a immagini o file di riferimento opzionali, e restituisce l'immagine generata, eventuale testo di accompagnamento e, opzionalmente, un'immagine dal processo di pensiero del modello. Questo nodo è contrassegnato come deprecato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `prompt` | Prompt testuale che descrive l'immagine da generare o le modifiche da applicare. Includere eventuali vincoli, stili o dettagli che il modello deve seguire. Non può essere vuoto o contenere solo spazi bianchi. (predefinito: vuoto) | STRING | Sì | N/A |
| `model` | Il modello Gemini da utilizzare per la generazione di immagini. | COMBO | Sì | "Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | Quando il seed è fissato a un valore specifico, il modello fa del suo meglio per fornire la stessa risposta a richieste ripetute. L'output deterministico non è garantito. Inoltre, modificare il modello o le impostazioni dei parametri, come la temperature, può causare variazioni nella risposta anche quando si utilizza lo stesso valore di seed. Per impostazione predefinita, viene utilizzato un valore di seed casuale. (predefinito: 42) | INT | Sì | 0 a 18446744073709551615 |
| `aspect_ratio` | Se impostato su 'auto', corrisponde alle proporzioni dell'immagine di input; se non viene fornita alcuna immagine, viene solitamente generato un formato 16:9. (predefinito: "auto") | COMBO | Sì | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | Risoluzione di output desiderata. Per 2K/4K viene utilizzato l'upscaler nativo di Gemini. | COMBO | Sì | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | Determina il tipo di contenuto restituito dal modello: "IMAGE" restituisce solo un'immagine, "IMAGE+TEXT" restituisce anche del testo. (avanzato) | COMBO | Sì | "IMAGE"<br>"IMAGE+TEXT" |
| `thinking_level` | Controlla la profondità del processo di ragionamento del modello. | COMBO | Sì | "MINIMAL"<br>"HIGH" |
| `images` | Immagine(i) di riferimento opzionale(i). Per includere più immagini, utilizzare il nodo Batch Images (fino a 14). | IMAGE | No | 1 a 14 immagini |
| `files` | File opzionale(i) da utilizzare come contesto per il modello. Accetta input dal nodo Gemini Generate Content Input Files. | CUSTOM | No | N/A |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento di un'IA. (predefinito: un prompt preimpostato che istruisce il modello a produrre sempre un'immagine) (avanzato) | STRING | No | N/A |

**Nota:** L'input `images` supporta un massimo di 14 immagini. Se ne vengono fornite di più, il nodo genera un errore. L'input `prompt` non deve essere vuoto o contenere solo spazi bianchi.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine principale generata o modificata dal modello. | IMAGE |
| `string` | Qualsiasi contenuto testuale restituito dal modello. | STRING |
| `thought_image` | Prima immagine dal processo di pensiero del modello. Disponibile solo con `thinking_level` impostato su HIGH e la modalità IMAGE+TEXT. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/it.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`

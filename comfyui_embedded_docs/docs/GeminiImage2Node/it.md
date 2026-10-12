# GeminiImage2Node

Genera o modifica immagini in modo sincrono tramite l'API Google Vertex AI Gemini. Fornisci un prompt testuale e puoi facoltativamente allegare immagini di riferimento o file di input Gemini. Il nodo restituisce l'immagine generata e, in base alla modalità di risposta selezionata, una risposta testuale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale che descrive l'immagine da generare o le modifiche da applicare. Includi eventuali vincoli, stili o dettagli che il modello deve seguire. Il prompt deve contenere almeno un carattere dopo la rimozione degli spazi bianchi. | STRING | Sì | N/D |
| `model` | Il modello Gemini da usare per la generazione. L'opzione "Nano Banana 2 (Gemini 3.1 Flash Image)" viene inviata come `gemini-3.1-flash-image`; "gemini-3-pro-image-preview" viene inviata come `gemini-3-pro-image`. | COMBO | Sì | "gemini-3-pro-image-preview"<br>"Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | Quando il seed è fissato a un valore specifico, il modello fa del suo meglio per fornire la stessa risposta a richieste ripetute. L'output deterministico non è garantito. Inoltre, modificare il modello o le impostazioni dei parametri, come la temperatura, può causare variazioni nella risposta anche quando usi lo stesso valore di seed. Per impostazione predefinita, viene usato un valore di seed casuale. Predefinito: 42. | INT | Sì | 0 a 18446744073709551615 |
| `aspect_ratio` | Se impostato su 'auto', corrisponde alle proporzioni dell'immagine di input; se non viene fornita alcuna immagine, viene solitamente generato un formato 16:9. Predefinito: "auto". | COMBO | Sì | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | Risoluzione di output desiderata. Per 2K/4K viene usato l'upscaler nativo di Gemini. | COMBO | Sì | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | Scegli 'IMAGE' per un output solo immagine, oppure 'IMAGE+TEXT' per restituire sia l'immagine generata sia una risposta testuale. Impostazione avanzata. | COMBO | Sì | "IMAGE+TEXT"<br>"IMAGE" |
| `images` | Immagini di riferimento opzionali. Per includere più immagini, usa il nodo Batch Images (fino a 14). | IMAGE | No | N/D |
| `files` | File opzionali da usare come contesto per il modello. Accetta input dal nodo Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | No | N/D |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento di un'IA. Predefinito: un prompt di sistema predefinito per la generazione di immagini. Impostazione avanzata. | STRING | No | N/D |

**Vincoli:**

* L'input `images` supporta un massimo di 14 immagini. Se ne vengono fornite di più, viene generato un errore.
* Quando vengono fornite più di 10 immagini, le prime 10 vengono caricate come riferimenti URL e le immagini rimanenti vengono inviate direttamente nella richiesta.
* L'input `files` deve essere collegato a un nodo che restituisce il tipo di dati `GEMINI_INPUT_FILES`.
* Quando `response_modalities` è impostato su `"IMAGE"`, viene restituita solo l'immagine e l'output testuale è vuoto.
* L'input `prompt` viene validato e deve contenere almeno un carattere dopo la rimozione degli spazi bianchi.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine generata o modificata dal modello Gemini. | IMAGE |
| `string` | La risposta testuale del modello. Questo output è vuoto se `response_modalities` è impostato su `"IMAGE"`. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/it.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`

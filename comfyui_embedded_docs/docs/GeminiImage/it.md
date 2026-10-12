# GeminiImage

Il nodo GeminiImage genera risposte di testo e immagini dai modelli AI Gemini di Google. Consente di fornire input multimodali, tra cui prompt testuali, immagini e file, per creare output coerenti di testo e immagini. Il nodo gestisce tutta la comunicazione API e l'analisi delle risposte con i modelli Gemini più recenti.

## Input

| Parametro | Descrizione | Tipo di dati | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `prompt` | Prompt testuale per la generazione | STRING | obbligatorio | "" | - |
| `model` | Il modello Gemini da usare per generare risposte. | COMBO | obbligatorio | gemini_2_5_flash_image_preview | `gemini_2_5_flash_image_preview`<br>`gemini_2_5_pro_exp_03_25`<br>`gemini_2_0_flash_exp_image_generation` |
| `seed` | Quando il seed è fissato a un valore specifico, il modello si impegna al massimo per fornire la stessa risposta a richieste ripetute. Non è garantito un output deterministico. Inoltre, modificare il modello o le impostazioni dei parametri, come la temperatura, può causare variazioni nella risposta anche quando si usa lo stesso valore di seed. Per impostazione predefinita, viene usato un valore di seed casuale. | INT | obbligatorio | 42 | da 0 a 18446744073709551615 |
| `images` | Immagini opzionali da usare come contesto per il modello. Per includere più immagini, puoi usare il nodo Batch Images. | IMAGE | opzionale | Nessuno | - |
| `files` | File opzionali da usare come contesto per il modello. Accetta input dal nodo Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | opzionale | Nessuno | - |

**Nota:** Il nodo include parametri nascosti (`auth_token`, `comfy_api_key`, `unique_id`) gestiti automaticamente dal sistema, che non richiedono input da parte dell'utente.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `IMAGE` | La risposta immagine generata dal modello Gemini | IMAGE |
| `STRING` | La risposta testuale generata dal modello Gemini | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/it.md)

---
**Source fingerprint (SHA-256):** `bf55ec4f5a869a6bc5a15366f55f86ad25f9498c14056acc80951d3637bf08f2`

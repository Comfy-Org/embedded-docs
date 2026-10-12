# GeminiImageNode

Il nodo GeminiImage genera risposte di testo e immagini dai modelli Gemini AI di Google. Consente di fornire input multimodali, inclusi prompt testuali, immagini e file, per creare output coerenti di testo e immagini. Il nodo gestisce tutta la comunicazione API e l'analisi delle risposte con i modelli Gemini più recenti.

## Input

| Parametro | Descrizione | Tipo di dati | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `prompt` | Prompt testuale per la generazione | STRING | obbligatorio | "" | - |
| `model` | Il modello Gemini da utilizzare per generare le risposte | COMBO | obbligatorio | gemini_2_5_flash_image_preview | Modelli Gemini disponibili<br>Opzioni estratte dall'enum GeminiImageModel |
| `seed` | Quando `seed` viene fissato a un valore specifico, il modello compie il massimo sforzo per fornire la stessa risposta a richieste ripetute. L'output deterministico non è garantito. Inoltre, cambiare il modello o le impostazioni dei parametri, come la temperatura, può causare variazioni nella risposta anche quando si utilizza lo stesso valore di seed. Per impostazione predefinita, viene utilizzato un valore di seed casuale | INT | obbligatorio | 42 | Da 0 a 18446744073709551615 |
| `images` | Immagini opzionali da usare come contesto per il modello. Per includere più immagini, puoi utilizzare il nodo Batch Images | IMAGE | opzionale | None | - |
| `files` | File opzionali da usare come contesto per il modello. Accetta input dal nodo Gemini Generate Content Input Files | GEMINI_INPUT_FILES | opzionale | None | - |

*Nota: il nodo include parametri nascosti (`auth_token`, `comfy_api_key`, `unique_id`) gestiti automaticamente dal sistema e che non richiedono l'intervento dell'utente.*

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `IMAGE` | La risposta immagine generata dal modello Gemini | IMAGE |
| `STRING` | La risposta testuale generata dal modello Gemini | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImageNode/it.md)

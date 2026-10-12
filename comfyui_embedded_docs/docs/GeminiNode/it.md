# Google Gemini

This node allows users to interact with Google's Gemini AI models to generate text responses. You can provide multiple types of inputs including text, images, audio, video, and files as context for the model to generate more relevant and meaningful responses. The node handles all API communication and response parsing automatically.

**Note:** This node is marked as deprecated in the source code.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Input testuali per il modello, usati per generare una risposta. Puoi includere istruzioni dettagliate, domande o contesto per il modello. Predefinito: stringa vuota. | STRING | Sì | - |
| `model` | Il modello Gemini da usare per generare le risposte. Predefinito: gemini-3-1-pro. | COMBO | Sì | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `seed` | Quando il seed è fissato a un valore specifico, il modello fa del suo meglio per fornire la stessa risposta a richieste ripetute. L'output deterministico non è garantito. Inoltre, cambiare il modello o le impostazioni dei parametri, come la temperatura, può causare variazioni nella risposta anche quando usi lo stesso valore di seed. Per impostazione predefinita, viene usato un valore di seed casuale. Predefinito: 42. | INT | Sì | da 0 a 18446744073709551615 |
| `images` | Immagine/i opzionale/i da usare come contesto per il modello. Per includere più immagini, puoi usare il nodo Batch Images. Predefinito: Nessuno. | IMAGE | No | - |
| `audio` | Audio opzionale da usare come contesto per il modello. Predefinito: Nessuno. | AUDIO | No | - |
| `video` | Video opzionale da usare come contesto per il modello. Predefinito: Nessuno. | VIDEO | No | - |
| `files` | File opzionale/i da usare come contesto per il modello. Accetta input dal nodo Gemini Generate Content Input Files. Predefinito: Nessuno. | GEMINI_INPUT_FILES | No | - |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento di un'IA. Predefinito: stringa vuota. Questo è un parametro avanzato. | STRING | No | - |

Tutte le immagini collegate vengono usate come contesto. Quando vengono fornite più di 10 immagini, le prime 10 vengono caricate come riferimenti a file e le immagini rimanenti vengono inviate inline all'API.

Il nodo usa il nome del modello selezionato così come indicato nell'elenco; alcune voci vengono mappate internamente ai loro identificatori correnti del modello API prima che la richiesta venga inviata.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `STRING` | La risposta testuale generata dal modello Gemini. Se il modello non produce testo, il nodo restituisce "Empty response from Gemini model...". | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/it.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`

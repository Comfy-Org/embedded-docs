# Bria Aggiungi oggetto

Questo nodo inserisce in un'immagine un oggetto descritto in testo semplice usando Bria. Bria esegue nuovamente il rendering dell'intero frame a circa 1 megapixel, quindi il risultato non è allineato a livello di pixel con l'input.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine a cui viene aggiunto l'oggetto descritto. Il canale alpha viene rimosso prima del caricamento dell'immagine. | IMAGE | Sì | - |
| `instruction` | Cosa aggiungere e dove, ad esempio 'Posiziona un vaso rosso con fiori sul tavolo'. Non deve essere vuoto. Predefinito: "" (stringa vuota). | STRING | Sì | - |
| `seed` | Bria non accetta un seed qui e rigenera la modifica a ogni chiamata, quindi esecuzioni ripetute possono differire. Il valore non viene mai inviato: modifica solo la chiave di cache di questo nodo, così che un grafo per il resto identico esegua di nuovo la modifica invece di restituire il risultato memorizzato nella cache. Predefinito: 42. | INT | Sì | 0 to 2147483647 |
| `moderation` | Impostazioni di moderazione. Scegli "true" per mostrare i flag di moderazione riportati di seguito. | DYNAMIC_COMBO | Sì | "false"<br>"true" |

### Input con moderazione abilitata

Disponibili quando `moderation` è impostato su "true".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `visual_input_moderation` | Abilita la moderazione dei contenuti sull'immagine di input. Predefinito: False. | BOOLEAN | No | True / False |
| `visual_output_moderation` | Abilita la moderazione dei contenuti sull'immagine di output generata. Predefinito: False. | BOOLEAN | No | True / False |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine modificata con l'oggetto descritto aggiunto. | IMAGE |
| `structured_prompt` | Descrizione strutturata dell'immagine modificata, per una modifica successiva con Bria FIBO Image Edit. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaAddObject/it.md)

---
**Source fingerprint (SHA-256):** `41c9a3e511763372d8dc8be9da4f70158e53d5156a88eb3c66f81149efdbd566`

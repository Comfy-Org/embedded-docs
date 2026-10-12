# BriaEraseByText

Questo nodo rimuove da un'immagine un oggetto descritto in testo semplice utilizzando Bria. Bria esegue nuovamente il rendering dell'intero fotogramma a circa 1 megapixel, pertanto il risultato non è allineato a livello di pixel con l'input.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine da cui rimuovere l'oggetto indicato. | IMAGE | Sì | - |
| `object_name` | Nome dell'oggetto da rimuovere, ad esempio 'the lamp'. È possibile indicare più oggetti contemporaneamente, ad esempio 'the phone and the pencils'. Indicare qualcosa che non è presente nell'immagine restituisce comunque un'immagine ri-renderizzata e la richiesta viene comunque addebitata. Deve contenere almeno 1 carattere (predefinito: vuoto). | STRING | Sì | - |
| `moderation` | Impostazioni di moderazione. Seleziona se mostrare i controlli opzionali di moderazione. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |

### Input di moderazione

Questi parametri vengono visualizzati quando `moderation` è impostato su `"true"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `visual_input_moderation` | Abilita la moderazione dei contenuti sull'immagine di input (predefinito: false). | BOOLEAN | No | true<br>false |
| `visual_output_moderation` | Abilita la moderazione dei contenuti sull'immagine di output generata (predefinito: false). | BOOLEAN | No | true<br>false |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine ri-renderizzata con l'oggetto indicato rimosso. | IMAGE |
| `structured_prompt` | Descrizione strutturata dell'immagine modificata, per una modifica successiva con Bria FIBO Image Edit. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseByText/it.md)

---
**Source fingerprint (SHA-256):** `51ac362bea731251c99905172c41cdebb5165e7564c508f13aa43cf9072964ef`

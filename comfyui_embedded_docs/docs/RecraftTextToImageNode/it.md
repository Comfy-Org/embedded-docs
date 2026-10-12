# RecraftTextToImageNode

Genera immagini in modo sincrono in base al prompt e alla risoluzione. Questo nodo si connette all'API Recraft per creare immagini da descrizioni testuali con dimensioni specificate e parametri opzionali di stile e controllo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione dell'immagine. (predefinito: "") | STRING | Sì | 1-1000 caratteri |
| `size` | La dimensione dell'immagine generata. (predefinito: "1024x1024") | COMBO | Sì | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `n` | Il numero di immagini da generare. (predefinito: 1) | INT | Sì | 1-6 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | Sì | 0-18446744073709551615 |
| `recraft_style` | Selezione opzionale dello stile per la generazione dell'immagine. Se non fornito, il valore predefinito è lo stile "realistic_image". | RECRAFT_STYLE | No | Più opzioni disponibili |
| `negative_prompt` | Descrizione testuale opzionale degli elementi indesiderati in un'immagine. (predefinito: "") | STRING | No | - |
| `recraft_controls` | Controlli aggiuntivi opzionali sulla generazione tramite il nodo Recraft Controls. | RECRAFT_CONTROLS | No | Più opzioni disponibili |

**Nota:** Il parametro `seed` controlla solo quando il nodo viene rieseguito, ma non rende deterministica la generazione dell'immagine. Le immagini di output effettive varieranno anche con lo stesso valore di seed.

**Nota:** Il parametro `prompt` deve avere una lunghezza compresa tra 1 e 1000 caratteri.

**Nota:** Se usi uno `style_id` dalla Infinite Style Library, assicurati che non sia uno stile Vector art, poiché restituirebbe dati SVG invece di un'immagine e causerebbe un errore.

**Nota:** Questo è un nodo API a pagamento. Il costo è di $0,0572 per immagine generata, in base al valore di `n`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine o le immagini generate come output tensore in batch. Quando vengono generate più immagini (n > 1), queste vengono concatenate lungo la dimensione batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/it.md)

---
**Source fingerprint (SHA-256):** `d0955cb57c93c752b19379b4c4f9c85dc72cdf6309bc433024f115fa7b996f4d`

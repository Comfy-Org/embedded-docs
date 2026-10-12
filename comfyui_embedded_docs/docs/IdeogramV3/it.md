# Ideogram V3

Il nodo Ideogram V3 genera immagini utilizzando il modello Ideogram V3. Supporta sia la generazione standard di immagini da prompt testuali sia la modifica di immagini quando vengono fornite sia un'immagine sia una maschera. Il nodo offre vari controlli per rapporto d'aspetto, risoluzione, velocità di generazione e immagini di riferimento opzionali per personaggi.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione o la modifica dell'immagine (predefinito: vuoto) | STRING | Sì | - |
| `image` | Immagine di riferimento opzionale per la modifica dell'immagine | IMAGE | No | - |
| `mask` | Maschera opzionale per l'inpainting (le aree bianche verranno sostituite) | MASK | No | - |
| `aspect_ratio` | Il rapporto d'aspetto per la generazione dell'immagine. Ignorato se resolution non è impostato su Auto (predefinito: "1:1") | COMBO | No | "1:1"<br>"1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4" |
| `resolution` | La risoluzione per la generazione dell'immagine. Se non impostata su Auto, sovrascrive l'impostazione aspect_ratio (predefinito: "Auto") | COMBO | No | "Auto"<br>"512x1536"<br>"576x1408"<br>"576x1472"<br>"576x1536"<br>"640x1344"<br>"640x1408"<br>"640x1472"<br>"640x1536"<br>"704x1152"<br>"704x1216"<br>"704x1280"<br>"704x1344"<br>"704x1408"<br>"704x1472"<br>"736x1312"<br>"768x1088"<br>"768x1216"<br>"768x1280"<br>"768x1344"<br>"800x1280"<br>"832x960"<br>"832x1024"<br>"832x1088"<br>"832x1152"<br>"832x1216"<br>"832x1248"<br>"864x1152"<br>"896x960"<br>"896x1024"<br>"896x1088"<br>"896x1120"<br>"896x1152"<br>"960x832"<br>"960x896"<br>"960x1024"<br>"960x1088"<br>"1024x832"<br>"1024x896"<br>"1024x960"<br>"1024x1024"<br>"1088x768"<br>"1088x832"<br>"1088x896"<br>"1088x960"<br>"1120x896"<br>"1152x704"<br>"1152x832"<br>"1152x864"<br>"1152x896"<br>"1216x704"<br>"1216x768"<br>"1216x832"<br>"1248x832"<br>"1280x704"<br>"1280x768"<br>"1280x800"<br>"1312x736"<br>"1344x640"<br>"1344x704"<br>"1344x768"<br>"1408x576"<br>"1408x640"<br>"1408x704"<br>"1472x576"<br>"1472x640"<br>"1472x704"<br>"1536x512"<br>"1536x576"<br>"1536x640" |
| `magic_prompt_option` | Determina se MagicPrompt deve essere utilizzato durante la generazione (predefinito: "AUTO") | COMBO | No | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Seme casuale per la generazione (predefinito: 0) | INT | No | 0-2147483647 |
| `num_images` | Numero di immagini da generare (predefinito: 1) | INT | No | 1-8 |
| `rendering_speed` | Controlla il compromesso tra velocità di generazione e qualità (predefinito: "DEFAULT") | COMBO | No | "DEFAULT"<br>"TURBO"<br>"QUALITY" |
| `character_image` | Immagine da utilizzare come riferimento per il personaggio | IMAGE | No | - |
| `character_mask` | Maschera opzionale per l'immagine di riferimento del personaggio | MASK | No | - |

**Vincoli dei parametri:**

- Quando vengono forniti sia `image` che `mask`, il nodo passa alla modalità di modifica
- Se viene fornito solo uno tra `image` o `mask`, si verificherà un errore
- `character_mask` richiede la presenza di `character_image`
- Il parametro `aspect_ratio` viene ignorato quando `resolution` non è impostato su "Auto"
- Le aree bianche nella maschera verranno sostituite durante l'inpainting
- La maschera del personaggio e l'immagine del personaggio devono avere le stesse dimensioni

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | L'immagine o le immagini generate o modificate | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/it.md)

---
**Source fingerprint (SHA-256):** `d5005a9cdbdad79762dfd24eaa73e6c293d28b72813e96883ecdfccb8339ca75`

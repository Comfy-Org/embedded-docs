# IdeogramV2

Il nodo Ideogram V2 genera immagini utilizzando il modello AI Ideogram V2. Accetta prompt testuali e diverse impostazioni di generazione per creare immagini tramite un servizio API. Il nodo supporta vari rapporti d'aspetto, risoluzioni e opzioni di stile per personalizzare le immagini di output.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione dell'immagine (predefinito: stringa vuota) | STRING | Sì | - |
| `turbo` | Indica se usare la modalità turbo (generazione più veloce, potenzialmente qualità inferiore) (predefinito: False) | BOOLEAN | No | - |
| `aspect_ratio` | Il rapporto d'aspetto per la generazione dell'immagine. Ignorato se `resolution` non è impostato su AUTO. (predefinito: "1:1") | COMBO | No | "1:1"<br>"4:3"<br>"3:4"<br>"16:9"<br>"9:16"<br>"2:1"<br>"1:2"<br>"3:2"<br>"2:3"<br>"4:5"<br>"5:4" |
| `resolution` | La risoluzione per la generazione dell'immagine. Se non impostata su AUTO, sovrascrive l'impostazione `aspect_ratio`. (predefinito: "Auto") | COMBO | No | "Auto"<br>"512 x 1536"<br>"576 x 1408"<br>"576 x 1472"<br>"576 x 1536"<br>"640 x 1024"<br>"640 x 1344"<br>"640 x 1408"<br>"640 x 1472"<br>"640 x 1536"<br>"704 x 1152"<br>"704 x 1216"<br>"704 x 1280"<br>"704 x 1344"<br>"704 x 1408"<br>"704 x 1472"<br>"720 x 1280"<br>"736 x 1312"<br>"768 x 1024"<br>"768 x 1088"<br>"768 x 1152"<br>"768 x 1216"<br>"768 x 1232"<br>"768 x 1280"<br>"768 x 1344"<br>"832 x 960"<br>"832 x 1024"<br>"832 x 1088"<br>"832 x 1152"<br>"832 x 1216"<br>"832 x 1248"<br>"864 x 1152"<br>"896 x 960"<br>"896 x 1024"<br>"896 x 1088"<br>"896 x 1120"<br>"896 x 1152"<br>"960 x 832"<br>"960 x 896"<br>"960 x 1024"<br>"960 x 1088"<br>"1024 x 640"<br>"1024 x 768"<br>"1024 x 832"<br>"1024 x 896"<br>"1024 x 960"<br>"1024 x 1024"<br>"1088 x 768"<br>"1088 x 832"<br>"1088 x 896"<br>"1088 x 960"<br>"1120 x 896"<br>"1152 x 704"<br>"1152 x 768"<br>"1152 x 832"<br>"1152 x 864"<br>"1152 x 896"<br>"1216 x 704"<br>"1216 x 768"<br>"1216 x 832"<br>"1232 x 768"<br>"1248 x 832"<br>"1280 x 704"<br>"1280 x 720"<br>"1280 x 768"<br>"1280 x 800"<br>"1312 x 736"<br>"1344 x 640"<br>"1344 x 704"<br>"1344 x 768"<br>"1408 x 576"<br>"1408 x 640"<br>"1408 x 704"<br>"1472 x 576"<br>"1472 x 640"<br>"1472 x 704"<br>"1536 x 512"<br>"1536 x 576"<br>"1536 x 640" |
| `magic_prompt_option` | Determina se MagicPrompt deve essere usato nella generazione (predefinito: "AUTO") | COMBO | No | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Seme casuale per la generazione (predefinito: 0) | INT | No | 0-2147483647 |
| `style_type` | Tipo di stile per la generazione (solo V2) (predefinito: "NONE") | COMBO | No | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" |
| `negative_prompt` | Descrizione di ciò che deve essere escluso dall'immagine (predefinito: stringa vuota) | STRING | No | - |
| `num_images` | Numero di immagini da generare (predefinito: 1) | INT | No | 1-8 |

**Nota:** Quando `resolution` non è impostato su "Auto", sovrascrive l'impostazione `aspect_ratio`. Il parametro `num_images` ha un limite massimo di 8 immagini per generazione.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | L'immagine o le immagini generate dal modello Ideogram V2 | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/it.md)

---
**Source fingerprint (SHA-256):** `a034a57996ac0b3902cab36096ac6b8401bb544faa00b8ed213bf752fdd423e2`

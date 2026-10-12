# WanTextToVideoApi

Il nodo Wan Text to Video genera contenuti video basati su descrizioni testuali. Utilizza modelli di IA per creare video a partire da prompt e supporta varie dimensioni video, durate e input audio opzionali. Il nodo può generare automaticamente l'audio quando necessario e fornisce opzioni per il miglioramento del prompt e l'aggiunta di filigrana.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare (predefinito: "wan2.6-t2v") | COMBO | Sì | "wan2.5-t2v-preview"<br>"wan2.6-t2v" |
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta l'inglese e il cinese (predefinito: "") | STRING | Sì | - |
| `negative_prompt` | Prompt negativo che descrive ciò che si desidera evitare (predefinito: "") | STRING | No | - |
| `size` | Risoluzione e proporzioni del video (predefinito: "720p: 1:1 (960x960)") | COMBO | No | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" |
| `duration` | Durata del video in secondi. Una durata di 15 secondi è disponibile solo per il modello Wan 2.6 (predefinito: 5) | INT | No | 5-15 (con incrementi di 5) |
| `audio` | L'audio deve contenere una voce chiara e forte, senza rumori estranei o musica di sottofondo | AUDIO | No | - |
| `seed` | Seme da utilizzare per la generazione (predefinito: 0) | INT | No | 0-2147483647 |
| `generate_audio` | Se non viene fornito alcun input audio, genera automaticamente l'audio (predefinito: False) | BOOLEAN | No | - |
| `prompt_extend` | Indica se migliorare il prompt con l'assistenza dell'IA (predefinito: True) | BOOLEAN | No | - |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato (predefinito: False) | BOOLEAN | No | - |
| `shot_type` | Specifica il tipo di inquadratura per il video generato, ovvero se il video è un'unica ripresa continua o più inquadrature con tagli. Questo parametro ha effetto solo quando `prompt_extend` è True (predefinito: "single") | COMBO | No | "single"<br>"multi" |

**Nota:** Il modello Wan 2.6 non supporta le risoluzioni 480p. Una durata di 15 secondi è supportata solo dal modello Wan 2.6. Quando si fornisce un input audio, questo deve avere una durata compresa tra 3,0 e 29,0 secondi e contenere una voce chiara, senza rumore di fondo o musica.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | Il video generato in base ai parametri di input | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `105ff4b575dc6cd319448b0f4c0e9cfab360df025480190ae6bccc324d351525`

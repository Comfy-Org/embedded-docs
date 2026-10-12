# MoonvalleyTxt2VideoNode

Il nodo Moonvalley Marey Text to Video genera contenuti video a partire da descrizioni testuali utilizzando l'API Moonvalley. Prende un prompt testuale e lo converte in un video con impostazioni personalizzabili per risoluzione, qualità e stile. Il nodo gestisce l'intero processo, dall'invio della richiesta di generazione al download del video finale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Descrizione testuale del contenuto video da generare | STRING | Sì | - |
| `negative_prompt` | Testo del prompt negativo (predefinito: elenco esteso di elementi esclusi come sintetico, taglio di scena, artefatti, rumore, ecc.) | STRING | No | - |
| `resolution` | Risoluzione del video di output (predefinito: "16:9 (1920 x 1080)") | STRING | No | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)"<br>"21:9 (2560 x 1080)" |
| `prompt_adherence` | Scala di guidance per il controllo della generazione (predefinito: 4.0) | FLOAT | No | 1.0-20.0 |
| `seed` | Valore del seed casuale (predefinito: 9) | INT | No | 0-4294967295 |
| `steps` | Passaggi di inferenza (predefinito: 33) | INT | No | 1-100 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il video di output generato in base al prompt testuale | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/it.md)

---
**Source fingerprint (SHA-256):** `3654043567d7aca3af741d706ee07a8d2e28dbeb4b5b8755514b790aa7c1bd41`

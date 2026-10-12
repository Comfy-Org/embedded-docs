# MoonvalleyImg2VideoNode

Il nodo Moonvalley Marey Image to Video trasforma un'immagine di riferimento in un video utilizzando l'API Moonvalley. Prende un'immagine di input e un prompt testuale per generare un video con risoluzione specificata, impostazioni di qualità e controlli creativi. Il nodo gestisce l'intero processo, dal caricamento dell'immagine alla generazione e al download del video.

## Input
| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di riferimento utilizzata per generare il video | IMAGE | Sì | - |
| `prompt` | Descrizione testuale per la generazione del video (input multilinea) | STRING | Sì | - |
| `negative_prompt` | Testo del prompt negativo per escludere elementi indesiderati (predefinito: ampio elenco di prompt negativi) | STRING | No | - |
| `resolution` | Risoluzione del video in output (predefinito: "16:9 (1920 x 1080)") | COMBO | No | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)" |
| `prompt_adherence` | Scala di guidance per il controllo della generazione (predefinito: 4.5, passo: 1.0) | FLOAT | No | 1.0 - 20.0 |
| `seed` | Valore del seed casuale (predefinito: 9, controllo dopo la generazione abilitato) | INT | No | 0 - 4294967295 |
| `steps` | Numero di passaggi di denoising (predefinito: 33, passo: 1) | INT | No | 1 - 100 |

**Vincoli:**

- L'immagine di input deve avere dimensioni comprese tra 300x300 pixel e l'altezza/larghezza massima consentita
- La lunghezza del testo del prompt e del prompt negativo è limitata alla lunghezza massima del prompt di Moonvalley Marey

## Output
| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Il video generato in output | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/it.md)

---
**Source fingerprint (SHA-256):** `674e69a7f106f6f961f10c179008b7bb1147bf0e569c72d207a105f3fab2aaf5`

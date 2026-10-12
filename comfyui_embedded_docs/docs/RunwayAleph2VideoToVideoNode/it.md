# Runway Aleph2 Video to Video

## Panoramica

Questo nodo modifica un video usando un prompt testuale con il modello Aleph2 di Runway. Trasforma il filmato applicando un nuovo stile, modificando l'illuminazione, aggiungendo o rimuovendo elementi oppure cambiando il punto di vista, preservando il movimento e la temporizzazione originali. La risoluzione di output corrisponde al video di input.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrive ciò che dovrebbe apparire nell'output (1-1000 caratteri). | STRING | Sì | 1-1000 caratteri |
| `video` | Video di input da modificare. Deve durare tra 2 e 30 secondi a 30 fps o meno. | VIDEO | Sì | Durata 2-30 secondi, 30 fps max |
| `seed` | Seme casuale per la generazione (predefinito: 0). | INT | Sì | Da 0 a 4294967295 |
| `public_figure_threshold` | Moderazione dei contenuti per personaggi pubblici riconoscibili (predefinito: `"low"`). | COMBO | Sì | `"auto"`<br>`"low"` |
| `keyframes` | Immagini di guida ancorate al video di input, dai nodi Aleph2 Keyframe (fino a 5). Usa i keyframe o le immagini prompt, non entrambi. | KEYFRAME | No | Fino a 5 elementi |
| `prompt_images` | Immagini di guida ancorate al video di output, dai nodi Aleph2 Prompt Image (fino a 5). Usa i keyframe o le immagini prompt, non entrambi. | PROMPT_IMAGE | No | Fino a 5 elementi |

**Vincoli importanti:**
- Il video di input deve durare tra 2 e 30 secondi e avere una frequenza di fotogrammi pari o inferiore a 30 fps.
- Puoi usare `keyframes` o `prompt_images` per la guida, ma non entrambi contemporaneamente.
- Ogni input di guida (keyframe o immagini prompt) supporta un massimo di 5 elementi.
- I timestamp dei keyframe e i timestamp delle immagini prompt non devono superare la durata del video di input.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `video` | Il video modificato generato dal modello Aleph2. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2VideoToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `bda4d0f49843c1a8f311ddbce5911a2a157cae798a26f7a183b31fe41686d0b7`

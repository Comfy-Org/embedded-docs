# Luma Ray 3.2 Riquadratura Video

Questo nodo modifica il rapporto d'aspetto di un video esistente utilizzando Luma Ray 3.2, che riempie le nuove aree esposte della tela con contenuti generati. Il video di origine può durare fino a 30 secondi e la fatturazione è al secondo di output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Video di origine da riformattare. Fino a 30 secondi. | VIDEO | Sì | - |
| `prompt` | Descrive come devono essere riempite le nuove aree esposte della tela. | STRING | Sì | Lunghezza minima: 1 carattere<br>Lunghezza massima: 6000 caratteri |
| `aspect_ratio` | Il rapporto d'aspetto di destinazione per il video riformattato (predefinito: "16:9"). | STRING | Sì | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9" |
| `resolution` | La risoluzione di output del video riformattato (predefinito: "720p"). | STRING | Sì | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `seed` | Seed per una generazione riproducibile. | INT | Sì | - |

**Nota:** La risoluzione `1080p` non è disponibile per i rapporti d'aspetto verticali (`9:16` e `3:4`) durante la modifica del rapporto d'aspetto.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video riformattato con il nuovo rapporto d'aspetto e le aree della tela riempite. | VIDEO |
| `generation_id` | L'identificatore univoco per la richiesta di generazione. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoReframeNode/it.md)

---
**Source fingerprint (SHA-256):** `d35ff5b63a850e4e44a40857188918ab5cde00b9159e3720a189a81807cfa7cb`

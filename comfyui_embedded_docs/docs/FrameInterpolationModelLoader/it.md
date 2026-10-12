# FrameInterpolationModelLoader

Questo nodo carica un file di modello per l'interpolazione dei frame e lo prepara per l'uso nel workflow. Rileva automaticamente se il file è un modello FILM o RIFE e configura il modello per l'hardware disponibile.

## Input
| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model_name` | Seleziona un modello di interpolazione dei frame da caricare. I modelli devono essere inseriti nella cartella 'frame_interpolation'. | COMBO | Sì | Elenco dei file di modello nella cartella `frame_interpolation` |

Nota: il nodo supporta i formati di modello FILM e RIFE. Se il file selezionato non è in un formato riconosciuto, viene generato un errore.

## Output
| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | Il modello di interpolazione dei frame caricato e configurato, pronto per l'uso in altri nodi. | INTERP_MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/it.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`

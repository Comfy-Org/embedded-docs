# USOStyleReference

Il nodo USOStyleReference applica un riferimento di stile a un modello combinando le feature di visione CLIP con una patch del modello e restituisce una copia patchata del modello di input. Le informazioni di stile visivo vengono combinate con il condizionamento testuale del modello in modo che possano influenzare la generazione. Questo nodo è destinato ai modelli Flux ed è contrassegnato come sperimentale.

## Input
| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di base a cui viene applicata la patch di riferimento di stile. | MODEL | Sì | - |
| `model_patch` | La patch del modello contenente il modello di proiezione utilizzato per codificare le caratteristiche dell'immagine di riferimento. | MODEL_PATCH | Sì | - |
| `clip_vision_output` | Le caratteristiche visive codificate estratte dall'elaborazione di visione CLIP dell'immagine di riferimento. | CLIP_VISION_OUTPUT | Sì | - |

Nota: il `clip_vision_output` deve provenire da un modello di visione CLIP che fornisca gli stati nascosti completi e il penultimo stato nascosto. Il nodo combina il ventesimo dall'ultimo, l'undicesimo dall'ultimo e il penultimo stato nascosto nell'embedding di stile. Il `model_patch` deve esporre un modello di proiezione tramite il suo attributo `model` che converte queste caratteristiche dell'immagine nell'embedding di stile. Durante il campionamento, l'embedding di stile viene anteposto al condizionamento testuale in modo che possa influenzare la generazione, e gli ID di testo corrispondenti in posizione zero vengono anteposti agli ID di testo in modo che la sequenza di identificatori rimanga allineata con il condizionamento esteso.

## Output
| Nome uscita | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato con la patch di riferimento di stile applicata. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/it.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`

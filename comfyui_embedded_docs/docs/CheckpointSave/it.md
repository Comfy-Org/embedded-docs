# Salva Checkpoint

Il nodo `Save Checkpoint` è progettato per salvare un modello Stable Diffusion completo (inclusi i componenti UNet, CLIP e VAE) come file checkpoint in formato **.safetensors**.

Il nodo Save Checkpoint viene utilizzato principalmente nei workflow di fusione dei modelli. Dopo aver creato un nuovo modello fuso tramite nodi come `ModelMergeSimple`, `ModelMergeBlocks`, ecc., puoi usare questo nodo per salvare il risultato come file checkpoint riutilizzabile.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il parametro `model` rappresenta il modello principale di cui deve essere salvato lo stato. È essenziale per catturare lo stato corrente del modello per un futuro ripristino o analisi. | MODEL |
| `clip` | Il parametro `clip` è destinato al modello CLIP associato al modello principale, consentendo di salvarne lo stato insieme al modello principale. | CLIP |
| `vae` | Il parametro `vae` è relativo al modello Variational Autoencoder (VAE), consentendo di salvarne lo stato per usi o analisi future insieme al modello principale e a CLIP. | VAE |
| `filename_prefix` | Questo parametro specifica il prefisso del nome file con cui verrà salvato il checkpoint. | STRING |

Inoltre, il nodo presenta due input nascosti per i metadati:

**prompt (PROMPT)**: informazioni sul prompt del workflow
**extra_pnginfo (EXTRA_PNGINFO)**: informazioni PNG aggiuntive

## Output

Questo nodo produrrà in output un file checkpoint; il percorso del file di output corrispondente è la directory `output/checkpoints/`

## Compatibilità delle architetture

- Attualmente pienamente supportate: SDXL, SD3, SVD e altre architetture mainstream; vedi il [codice sorgente](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- Supporto di base: altre architetture possono essere salvate, ma senza informazioni standardizzate sui metadati

## Link correlati

Codice sorgente correlato: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/it.md)

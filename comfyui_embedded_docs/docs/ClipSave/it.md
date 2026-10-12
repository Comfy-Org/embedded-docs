# ClipSave

Il nodo `CLIPSave` salva su disco un modello text encoder CLIP in formato SafeTensors. È progettato per flussi di lavoro avanzati di fusione dei modelli e separa automaticamente il modello CLIP nelle sue parti componenti (come CLIP-L, CLIP-G o T5XXL) in base alla struttura interna del modello, salvando ciascun componente come file separato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP da salvare. | CLIP | Sì | - |
| `filename_prefix` | Il percorso di prefisso e il nome file per i file salvati. Il nodo aggiungerà un suffisso di componente (ad es. `_clip_l`, `_clip_g`) e un contatore per creare nomi file univoci (predefinito: `clip/ComfyUI`). | STRING | Sì | - |
| `prompt` | Le informazioni del prompt del workflow, salvate come metadati nel file di output. Questo parametro è nascosto nell'interfaccia utente. | PROMPT | No | - |
| `extra_pnginfo` | Metadati aggiuntivi, salvati come coppie chiave-valore nel file di output. Questo parametro è nascosto nell'interfaccia utente. | EXTRA_PNGINFO | No | - |

## Output

Questo nodo non ha connessioni di output. Salva i file elaborati direttamente nella directory `ComfyUI/output/`. I file salvati includono metadati (il formato è impostato su "pt", più il prompt del workflow e qualsiasi informazione PNG extra) a meno che ComfyUI non venga avviato con l'argomento `--disable-metadata`.

### Dettagli dei file salvati

Il nodo analizza il dizionario di stato del modello CLIP e salva file SafeTensors separati per ciascun componente rilevato. Il componente è identificato dal prefisso delle chiavi dei suoi parametri. Vengono controllati i seguenti prefissi:

- `clip_l.` (text encoder CLIP-L)
- `clip_g.` (text encoder CLIP-G)
- `clip_h.` (text encoder CLIP-H)
- `t5xxl.` (text encoder T5-XXL)
- `pile_t5xl.` (text encoder Pile-T5-XL)
- `mt5xl.` (text encoder mT5-XL)
- `umt5xxl.` (text encoder UMT5-XXL)
- `t5base.` (text encoder T5-Base)
- `gemma2_2b.` (text encoder Gemma 2 2B)
- `llama.` (text encoder LLaMA)
- `hydit_clip.` (text encoder CLIP Hydit)
- Prefisso vuoto (altri componenti CLIP)

Per ciascun componente rilevato, il nodo crea un file con il nome `{filename_prefix}_{counter:05}_.safetensors`, dove il prefisso del componente viene aggiunto al prefisso del nome file (ad es. `clip/ComfyUI_clip_l_00001_.safetensors`). Il prefisso `transformer.` viene rimosso dalle chiavi dei parametri durante il salvataggio.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipSave/it.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`

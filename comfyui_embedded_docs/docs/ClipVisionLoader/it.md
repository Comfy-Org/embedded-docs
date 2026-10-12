# ClipVisionLoader

Questo nodo rileva automaticamente i modelli situati nella cartella `ComfyUI/models/clip_vision`, così come eventuali percorsi aggiuntivi dei modelli configurati nel file `extra_model_paths.yaml`. Se aggiungi modelli dopo aver avviato ComfyUI, **aggiorna l'interfaccia di ComfyUI** per assicurarti che gli ultimi file dei modelli siano elencati.

## Input

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `clip_name` | Elenca tutti i file modello supportati nella cartella `ComfyUI/models/clip_vision`. | COMBO[STRING] |

## Output

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `clip_vision` | Modello CLIP Vision caricato, pronto per codificare immagini o altre attività legate alla visione. | CLIP_VISION |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipVisionLoader/it.md)

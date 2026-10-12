# DiffusersLoader

Il nodo DiffusersLoader carica modelli pre-addestrati salvati nel formato diffusers. Cerca nelle cartelle `diffusers` configurate le directory che contengono un file `model_index.json`, consente di selezionarne una e la carica come componenti MODEL, CLIP e VAE utilizzati nella pipeline. Questo nodo è deprecato, ma rimane disponibile per la compatibilità con i modelli diffusers di Hugging Face.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model_path` | Il percorso della directory del modello diffusers da caricare. Il nodo analizza automaticamente le cartelle `diffusers` configurate (incluse le sottocartelle collegate) per individuare le directory che contengono un file `model_index.json` e mostra le opzioni disponibili. Il percorso selezionato viene convalidato prima del caricamento; un modello non valido o mancante genera un errore. | COMBO | Sì | Elenco compilato automaticamente delle cartelle che contengono `model_index.json`<br>(percorsi relativi all'interno delle cartelle `diffusers` configurate) |

## Output

| Nome output | Descrizione | Tipo di dato |
|-----------|-------------|-----------|
| `MODEL` | Il componente modello caricato dal formato diffusers. | MODEL |
| `CLIP` | Il componente del modello CLIP caricato dal formato diffusers. | CLIP |
| `VAE` | Il componente VAE (Autoencoder variazionale) caricato dal formato diffusers. | VAE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/it.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`

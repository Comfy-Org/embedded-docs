# TripleCLIPLoader

TripleCLIPLoader carica contemporaneamente tre modelli text encoder e li combina in un unico modello CLIP. È utilizzato per workflow che richiedono più text encoder che lavorano insieme, come SD3, che utilizza i modelli clip-l, clip-g e t5.

Una combinazione comune per SD3 è: clip-l, clip-g, t5.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip_name1` | Il primo modello text encoder da caricare tra i text encoder disponibili | COMBO | Sì | Opzioni multiple disponibili (tutti i file nella cartella text_encoders) |
| `clip_name2` | Il secondo modello text encoder da caricare tra i text encoder disponibili | COMBO | Sì | Opzioni multiple disponibili (tutti i file nella cartella text_encoders) |
| `clip_name3` | Il terzo modello text encoder da caricare tra i text encoder disponibili | COMBO | Sì | Opzioni multiple disponibili (tutti i file nella cartella text_encoders) |

**Nota:** Tutti e tre i parametri sono obbligatori. Le opzioni disponibili sono i file text encoder nella cartella text_encoders. Se un file selezionato non viene trovato, il nodo genera un errore. Il nodo carica tutti e tre i modelli selezionati e li combina in un unico modello CLIP.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `CLIP` | Un modello CLIP combinato contenente tutti e tre i text encoder caricati | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/it.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`

# CLIP Text Encode (Controlnet)

Il nodo CLIP Text Encode (Controlnet) codifica un prompt testuale con un modello CLIP e aggiunge la codifica testuale risultante ai dati di condizionamento esistenti. Memorizza gli embedding testuali come parametri cross-attention di controlnet all'interno di ogni voce di condizionamento, così il condizionamento restituito porta con sé queste informazioni controlnet aggiuntive.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP usato per la tokenizzazione e la codifica del testo | CLIP | Sì | - |
| `conditioning` | Dati di condizionamento esistenti da combinare con la codifica testuale CLIP | CONDITIONING | Sì | - |
| `text` | Il prompt testuale da elaborare con il modello CLIP. Supporta testo multiriga e prompt dinamici | STRING | Sì | - |

**Nota:** Tutti e tre gli input (`clip`, `conditioning` e `text`) sono obbligatori affinché questo nodo funzioni. L'input `text` supporta testo multiriga e prompt dinamici per un'elaborazione flessibile del testo. Questo nodo è contrassegnato come sperimentale nel codice sorgente.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | Dati di condizionamento migliorati con l'aggiunta dei parametri cross-attention di controlnet (`cross_attn_controlnet` e `pooled_output_controlnet`) derivati dalla codifica testuale CLIP | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/it.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`

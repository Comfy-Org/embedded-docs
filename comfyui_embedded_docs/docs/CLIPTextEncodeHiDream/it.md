# CLIPTextEncodeHiDream

Il nodo CLIPTextEncodeHiDream elabora quattro input di testo separati utilizzando modelli linguistici diversi (CLIP-L, CLIP-G, T5-XXL e LLaMA) e li combina in un unico output di conditioning. Tokenizza ogni input di testo con il modello corrispondente e li codifica insieme utilizzando un approccio di codifica pianificata, consentendo un condizionamento testuale più sofisticato sfruttando simultaneamente più modelli linguistici.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP utilizzato per la tokenizzazione e la codifica | CLIP | Sì | - |
| `clip_l` | Input di testo per l'elaborazione con il modello CLIP-L. Supporta testo multilinea e prompt dinamici. | STRING | Sì | - |
| `clip_g` | Input di testo per l'elaborazione con il modello CLIP-G. Supporta testo multilinea e prompt dinamici. | STRING | Sì | - |
| `t5xxl` | Input di testo per l'elaborazione con il modello T5-XXL. Supporta testo multilinea e prompt dinamici. | STRING | Sì | - |
| `llama` | Input di testo per l'elaborazione con il modello LLaMA. Supporta testo multilinea e prompt dinamici. | STRING | Sì | - |

**Nota:** Tutti e quattro gli input di testo (`clip_l`, `clip_g`, `t5xxl` e `llama`) sono obbligatori per un corretto funzionamento, poiché ciascuno contribuisce all'output di conditioning finale attraverso il processo di codifica pianificata.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | L'output di conditioning combinato da tutti gli input di testo elaborati, codificato utilizzando il metodo di codifica pianificata | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/it.md)

---
**Source fingerprint (SHA-256):** `c5e269c17bd2dd7d7171c02598a87983a988d953dd7df285978fc25a9c896e46`

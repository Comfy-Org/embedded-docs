# CLIP Text Encode (SD3)

CLIPTextEncodeSD3 elabora input di testo per i modelli Stable Diffusion 3 codificando più prompt di testo utilizzando modelli CLIP diversi. Gestisce tre input di testo separati (`clip_g`, `clip_l` e `t5xxl`) e fornisce opzioni per la gestione del padding del testo vuoto. Il nodo garantisce un corretto allineamento dei token tra i diversi input di testo e restituisce dati di condizionamento adatti alle pipeline di generazione SD3.

## Input
| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP utilizzato per la codifica del testo | CLIP | Sì | - |
| `clip_l` | Input di testo per il modello CLIP locale. Supporta testo multilinea e prompt dinamici. | STRING | Sì | - |
| `clip_g` | Input di testo per il modello CLIP globale. Supporta testo multilinea e prompt dinamici. | STRING | Sì | - |
| `t5xxl` | Input di testo per il modello T5-XXL. Supporta testo multilinea e prompt dinamici. | STRING | Sì | - |
| `empty_padding` | Controlla come vengono gestiti gli input di testo vuoti. Quando è impostato su "none", gli input di testo vuoti per `clip_g`, `clip_l` o `t5xxl` producono liste di token vuote invece del padding. Quando è impostato su "empty_prompt", gli input vuoti vengono tokenizzati come prompt vuoti (comportamento standard di padding). Questo è un parametro avanzato (predefinito: "none"). | COMBO | Sì | `"none"`<br>`"empty_prompt"` |

**Vincoli dei parametri:**

- Quando `empty_padding` è impostato su "none", gli input di testo vuoti per `clip_g`, `clip_l` o `t5xxl` producono liste di token vuote invece del padding
- Il nodo bilancia automaticamente le lunghezze dei token tra gli input `clip_l` e `clip_g`, applicando padding a quello più corto con token vuoti quando le lunghezze differiscono
- Tutti gli input di testo supportano prompt dinamici e inserimento di testo multilinea

## Output
| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento del testo codificati, pronti per l'uso nelle pipeline di generazione SD3 | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/it.md)

---
**Source fingerprint (SHA-256):** `874869bac024e6b5ac6b4bf4f79c31bb750e54f7096f6638647aac6b95bb202f`

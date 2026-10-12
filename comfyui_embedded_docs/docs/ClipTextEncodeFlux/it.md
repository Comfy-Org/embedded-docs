# ClipTextEncodeFlux

`CLIPTextEncodeFlux` è un nodo di codifica testuale progettato per l'architettura Flux. Elabora due input testuali separati attraverso encoder diversi—CLIP-L e T5XXL—e li combina con una scala di guida per produrre un output di condizionamento unificato per la generazione di immagini.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Un modello CLIP che supporta l'architettura Flux, inclusi entrambi gli encoder CLIP-L e T5XXL. | CLIP | Sì | - |
| `clip_l` | Input testuale elaborato dall'encoder CLIP-L. Adatto a descrizioni concise per parole chiave, come stile o tema. Supporta input multilinea e prompt dinamici. | STRING | Sì | - |
| `t5xxl` | Input testuale elaborato dall'encoder T5XXL. Adatto a descrizioni dettagliate in linguaggio naturale, per esprimere scene e dettagli complessi. Supporta input multilinea e prompt dinamici. | STRING | Sì | - |
| `guidance` | Controlla l'influenza delle condizioni testuali sul processo di generazione. Valori più alti indicano un'aderenza più stretta al testo. Predefinito: 3.5. Regolabile con incrementi di 0.1. | FLOAT | Sì | 0.0 - 100.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | Contiene gli embedding fusi di entrambi gli encoder e il parametro di guida, usati per la generazione condizionata di immagini. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncodeFlux/it.md)

---
**Source fingerprint (SHA-256):** `022928fa6917102f5dc599364df9541b2451b42eb36a11813931b5fd71990b74`

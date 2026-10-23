# ClipTextEncodeHunyuanDit

Il nodo `CLIPTextEncodeHunyuanDiT` converte le descrizioni testuali in un formato che il modello HunyuanDiT può comprendere. È un nodo di condizionamento avanzato progettato per l'architettura a doppio encoder testuale di HunyuanDiT, che elabora due input testuali separati tramite tokenizer diversi e combina i risultati in un unico output di condizionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Istanza del modello CLIP usata per la tokenizzazione e la codifica del testo, fondamentale per generare i condizionamenti. | CLIP | Sì | - |
| `bert` | Input testuale da codificare tramite il tokenizer BERT. Preferisce frasi e parole chiave. Supporta prompt multilinea e dinamici. | STRING | Sì | - |
| `mt5xl` | Input testuale da codificare tramite il tokenizer mT5-XL. Supporta prompt multilinea e dinamici (multilingua). Può usare frasi complete e descrizioni complesse. | STRING | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | L'output di condizionamento codificato, che combina il testo tokenizzato BERT e mT5-XL, utilizzato per ulteriori elaborazioni nelle attività di generazione. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/it.md)

---
**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`

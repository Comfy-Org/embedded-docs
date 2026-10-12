# StableCascade_StageB_Conditioning

Il nodo StableCascade_StageB_Conditioning prepara i dati di condizionamento per la generazione di Stable Cascade Stage B combinando le informazioni di condizionamento esistenti con la rappresentazione latente a priori prodotta dallo Stage C. Copia ogni voce di condizionamento e vi memorizza i campioni latenti dello Stage C, così i passaggi di generazione successivi possono usare queste informazioni a priori per ottenere risultati più coerenti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `conditioning` | I dati di condizionamento da modificare con le informazioni a priori dello Stage C. Ogni voce della lista viene copiata e riceve i campioni dello Stage C. | CONDITIONING | Sì | - |
| `stage_c` | La rappresentazione latente dallo Stage C. Il suo valore `samples` viene usato come informazione a priori aggiunta al condizionamento. | LATENT | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento modificati con le informazioni a priori dello Stage C integrate. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/it.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`

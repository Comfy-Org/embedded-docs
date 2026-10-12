# TextEncodeAceStepAudio

Il nodo TextEncodeAceStepAudio elabora input testuali per il condizionamento audio combinando tag e testi delle canzoni in token, quindi li codifica con una forza dei testi regolabile. Riceve un modello CLIP insieme a descrizioni testuali e testi delle canzoni, li tokenizza insieme e genera dati di condizionamento adatti ad attività di generazione audio. Il nodo consente di regolare con precisione l'influenza dei testi tramite un parametro di forza che ne controlla l'impatto sull'output finale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP utilizzato per la tokenizzazione e la codifica | CLIP | Sì | - |
| `tags` | Tag testuali o descrizioni per il condizionamento audio (supporta input multilinea e prompt dinamici) | STRING | Sì | - |
| `lyrics` | Testo delle canzoni per il condizionamento audio (supporta input multilinea e prompt dinamici) | STRING | Sì | - |
| `lyrics_strength` | Controlla la forza dell'influenza dei testi sull'output di condizionamento (predefinito: 1.0, passo: 0.01) | FLOAT | Sì | 0.0 - 10.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `conditioning` | I dati di condizionamento codificati contenenti token di testo elaborati con la forza dei testi applicata | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/it.md)

---
**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`

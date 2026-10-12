# Guida con Bias Positivo

Il nodo Mahiro modifica la funzione di guidance per concentrarsi maggiormente sulla direzione del prompt positivo anziché sulla differenza tra prompt positivi e negativi. Crea un modello patchato che applica un approccio personalizzato di scalatura della guidance usando la similarità coseno tra output denoizzati condizionati e non condizionati normalizzati. Questo nodo sperimentale aiuta a orientare la generazione con maggiore forza verso la direzione prevista dal prompt positivo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello da patchare con la funzione di guidance modificata | MODEL | Sì |  |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `patched_model` | Il modello modificato con la funzione di guidance Mahiro applicata | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/it.md)

---
**Source fingerprint (SHA-256):** `56f13cd14ffde21ab980850b62e07bdd4db6733a545f9329bf908c6030147981`

# Guida Attenzione Normalizzata

Il nodo NAGuidance applica la Normalized Attention Guidance a un modello. Questa tecnica consente di usare prompt negativi con modelli distillati o schnell modificando il meccanismo di attenzione del modello durante il processo di campionamento, per indirizzare la generazione lontano da concetti indesiderati.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare la Normalized Attention Guidance. | MODEL | Sì | - |
| `nag_scale` | Il fattore di scala della guidance. Valori più alti spingono la generazione più lontano dal prompt negativo. (predefinito: 5.0) | FLOAT | Sì | 0.0 - 50.0 |
| `nag_alpha` | Il fattore di miscelazione per l'attenzione normalizzata. Un valore di 1.0 sostituisce completamente l'attenzione originale, mentre 0.0 non ha alcun effetto. (predefinito: 0.5) | FLOAT | Sì | 0.0 - 1.0 |
| `nag_tau` | Un fattore di scala usato per limitare il rapporto di normalizzazione. (predefinito: 1.5) | FLOAT | Sì | 1.0 - 10.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con la Normalized Attention Guidance abilitata. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/it.md)

---
**Source fingerprint (SHA-256):** `42b4d601312dcbb1c934c6a79bbb5e9fd6598fa5f32b18f5c0affcb596672cba`

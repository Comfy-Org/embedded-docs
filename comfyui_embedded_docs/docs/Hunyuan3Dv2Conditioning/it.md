# Hunyuan3Dv2Conditioning

Il nodo Hunyuan3Dv2Conditioning elabora l'output della visione CLIP per generare dati di condizionamento per modelli 3D. Estrae gli embedding dello stato nascosto finale dall'output di visione e crea sia la coppia di condizionamento positiva sia quella negativa. Il condizionamento positivo utilizza gli embedding effettivi, mentre quello negativo utilizza embedding con valore zero della stessa forma.

## Input

| Parametro | Descrizione | Tipo di dati | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `clip_vision_output` | L'output di un modello di visione CLIP contenente embedding visivi | CLIP_VISION_OUTPUT | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `positive` | Dati di condizionamento positivi contenenti gli embedding della visione CLIP | CONDITIONING |
| `negative` | Dati di condizionamento negativi contenenti embedding con valore zero corrispondenti alla forma degli embedding positivi | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/it.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`

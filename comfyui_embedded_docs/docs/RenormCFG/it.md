# RenormCFG

Il nodo RenormCFG modifica il processo di classifier-free guidance (CFG) nei modelli di diffusione applicando scalatura condizionale e normalizzazione. Regola il processo di denoising in base a una soglia di timestep specificata e a un fattore di rinormalizzazione, controllando l'influenza delle previsioni condizionate rispetto a quelle non condizionate durante la generazione dell'immagine. Il modello risultante viene restituito con questo comportamento CFG patchato.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui applicare il CFG rinormalizzato | MODEL | Sì | - |
| `cfg_trunc` | Soglia di timestep per applicare la scalatura CFG. Quando il timestep corrente è inferiore a questo valore, vengono applicate la scalatura CFG e la rinormalizzazione; altrimenti, viene utilizzata solo la previsione condizionata (predefinito: 100.0) | FLOAT | No | 0.0 - 100.0 (step 0.01) |
| `renorm_cfg` | Fattore di rinormalizzazione che limita la norma massima della previsione scalata con CFG rispetto alla previsione condizionata originale. Un valore di 0.0 disabilita la rinormalizzazione (predefinito: 1.0) | FLOAT | No | 0.0 - 100.0 (step 0.01) |

Nota: `cfg_trunc` e `renorm_cfg` sono parametri avanzati. La rinormalizzazione ha effetto solo quando `renorm_cfg` è maggiore di 0.0 e il timestep corrente è inferiore a `cfg_trunc`; se la norma della nuova previsione è già inferiore al massimo calcolato, non viene eseguito alcun riscalamento.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con la funzione CFG rinormalizzata applicata | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/it.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`

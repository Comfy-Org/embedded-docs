# CFGNorm

CFGNorm regola il modo in cui il classifier-free guidance (CFG) viene applicato nei modelli di diffusione confrontando la dimensione (norma) della previsione condizionata con la previsione guidata e riscalando il risultato. Un valore `strength` controlla quanta parte dell'aggiustamento viene applicata. Per impostazione predefinita, la scalatura attenua solo l'output del guidance, mentre abilitando `pre_cfg` si riscala il rumore combinato prima della combinazione CFG del sampler, senza clamping, il che può amplificare il risultato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui applicare la normalizzazione CFG | MODEL | Sì | - |
| `strength` | Controlla l'intensità dell'effetto di normalizzazione applicato alla scalatura CFG (predefinito: 1.0) | FLOAT | Sì | 0.0 a 100.0 (passo 0.01) |
| `pre_cfg` | Se true, riscala il rumore combinato PRIMA della combinazione CFG del sampler, senza clamping (può amplificare). Corrisponde al CFG con scala normalizzata usato da modelli come Lens. Il valore predefinito false mantiene il comportamento originale di sola attenuazione nello spazio x0 post-CFG. (predefinito: False) | BOOLEAN | No | true / false |

Nota: questo nodo è contrassegnato come sperimentale.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `patched_model` | Restituisce il modello modificato con la normalizzazione CFG applicata al suo processo di campionamento | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/it.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`

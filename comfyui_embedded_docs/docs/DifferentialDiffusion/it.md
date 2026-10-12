# DifferentialDiffusion

Il nodo Differential Diffusion modifica il processo di denoising applicando una maschera binaria basata su soglie di timestep. Crea una maschera che fonde la maschera di denoising originale con una maschera binaria basata su soglia, consentendo una regolazione controllata dell'intensità del processo di diffusione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione da modificare | MODEL | Sì | - |
| `strength` | Controlla l'intensità di fusione tra la maschera di denoising originale e la maschera binaria a soglia (predefinito: 1.0) | FLOAT | No | 0.0 - 1.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello di diffusione modificato con la funzione della maschera di denoising aggiornata | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/it.md)

---
**Source fingerprint (SHA-256):** `26387c3e6c7ead5415b36cfc9b9eef73448527e70646ab253984ff9627f69a25`

# PerturbedAttentionGuidance

Il nodo PerturbedAttentionGuidance applica la perturbed attention guidance a un modello di diffusione per migliorare la qualità di generazione. Durante il campionamento effettua una previsione aggiuntiva in cui l'auto-attenzione del blocco intermedio viene sostituita da una versione semplificata che passa direttamente le proiezioni dei valori, poi aggiunge al risultato denoised la differenza scalata tra la previsione condizionale normale e questa previsione perturbata. Impostare `scale` a 0 disabilita completamente l'effetto.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello di diffusione a cui applicare la perturbed attention guidance | MODEL | Sì | - |
| `scale` | La forza dell'effetto perturbed attention guidance (predefinito: 3.0). Se impostato a 0, il nodo non ha alcun effetto e restituisce il risultato denoised originale invariato. | FLOAT | Sì | 0.0 - 100.0 (step: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `model` | Il modello modificato con la patch di perturbed attention guidance allegata al suo processo di campionamento | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/it.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`

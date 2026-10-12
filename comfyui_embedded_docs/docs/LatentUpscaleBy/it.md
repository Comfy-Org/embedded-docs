# Ingrandisci Latent di

Il nodo LatentUpscaleBy è progettato per l'upscaling delle rappresentazioni latenti delle immagini. Consente di regolare il fattore di scala e il metodo di upscaling, offrendo flessibilità nel miglioramento della risoluzione dei campioni latenti.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `samples` | La rappresentazione latente delle immagini da sottoporre a upscaling. Questo parametro è cruciale per determinare i dati di input che verranno elaborati nel processo di upscaling. | `LATENT` |
| `upscale_method` | Specifica il metodo utilizzato per l'upscaling dei campioni latenti. La scelta del metodo può influire significativamente sulla qualità e sulle caratteristiche dell'output sottoposto a upscaling. | COMBO[STRING] |
| `scale_by` | Determina il fattore di scala applicato ai campioni latenti. Questo parametro influenza direttamente la risoluzione dell'output, consentendo un controllo preciso sul processo di upscaling. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `latent` | La rappresentazione latente sottoposta a upscaling, pronta per ulteriori attività di elaborazione o generazione. Questo output è essenziale per migliorare la risoluzione delle immagini generate o per successive operazioni del modello. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleBy/it.md)

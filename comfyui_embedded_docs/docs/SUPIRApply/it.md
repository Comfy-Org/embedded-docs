# SUPIRApply

Il nodo SUPIRApply applica una patch del modello SUPIR a un modello di diffusione. Utilizza la patch per modificarne il comportamento, consentendogli di incorporare la guida fornita da un'immagine di input durante il processo di campionamento. Il nodo fornisce inoltre controlli per regolare la forza di questa guida nel tempo e include una funzionalità opzionale per aiutare a mantenere la fedeltà all'input originale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione di base a cui verrà applicata la patch SUPIR. | MODEL | Sì | - |
| `model_patch` | La patch del modello SUPIR contenente i pesi e la configurazione per modificare il modello. | MODEL_PATCH | Sì | - |
| `vae` | Il VAE (autoencoder variazionale) utilizzato per codificare l'immagine di input in una rappresentazione latente. | VAE | Sì | - |
| `image` | L'immagine di input utilizzata per guidare il processo di generazione. Vengono utilizzati solo i primi tre canali di colore (RGB). | IMAGE | Sì | - |
| `strength_start` | Forza di controllo all'inizio del campionamento (sigma alto). L'influenza della guida dell'immagine inizia da questo valore. (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 |
| `strength_end` | Forza di controllo alla fine del campionamento (sigma basso). Interpolata linearmente dall'inizio. L'influenza della guida dell'immagine termina a questo valore. (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 |
| `restore_cfg` | Attira l'output denoised verso il latente di input. Valori più alti = maggiore fedeltà all'input. 0 per disabilitare. (predefinito: 4.0, impostazione avanzata) | FLOAT | Sì | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | Soglia sigma al di sotto della quale `restore_cfg` viene disabilitato. (predefinito: 0.05, impostazione avanzata) | FLOAT | Sì | 0.0 - 1.0 |

*Nota:* L'input `image` viene elaborato per estrarre solo i canali RGB. Se viene fornita un'immagine con canale alfa, il canale alfa viene ignorato.

*Nota:* Se la patch del modello SUPIR fornisce pesi dell'encoder denoise, l'immagine di input viene codificata con quei pesi invece che con l'encoder VAE standard.

*Nota:* `restore_cfg` ha effetto solo se impostato a un valore maggiore di 0. Impostandolo a 0 si disabilita completamente la post-elaborazione restore. Quando è attivo, la correzione viene applicata solo mentre il valore sigma corrente è superiore a `restore_cfg_s_tmin`.

*Nota:* Questo nodo è contrassegnato come sperimentale in ComfyUI.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Una copia clonata del modello di input con la patch SUPIR applicata e eventuali funzioni post-CFG aggiuntive configurate. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/it.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`

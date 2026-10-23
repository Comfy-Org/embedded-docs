# VaeLoader

Questo nodo rileva i modelli presenti nella cartella `ComfyUI/models/vae` e legge anche i modelli da percorsi aggiuntivi configurati nel file `extra_model_paths.yaml`. A volte potrebbe essere necessario **aggiornare l'interfaccia di ComfyUI** per consentirle di leggere i file dei modelli dalla cartella corrispondente.

Il nodo VAELoader è progettato per caricare modelli di Autoencoder Variazionale (VAE), con gestione specifica sia dei VAE standard sia di quelli approssimati. Supporta il caricamento dei VAE per nome, incluso il supporto specializzato per i modelli 'taesd' e 'taesdxl', e si adatta dinamicamente in base alla configurazione specifica del VAE.

## Input

| Campo | Descrizione | Comfy dtype |
| --- | --- | --- |
| `vae_name` | Specifica il nome del VAE da caricare, determinando quale modello VAE viene recuperato e caricato, con supporto per una serie di nomi VAE predefiniti tra cui 'taesd' e 'taesdxl'. | `COMBO[STRING]` |

## Output

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `vae` | Restituisce il modello VAE caricato, pronto per ulteriori operazioni quali codifica o decodifica. L'output è un oggetto modello che incapsula lo stato del modello caricato. | `VAE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAELoader/it.md)

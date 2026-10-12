# SamplerLCMUpscale

Questo nodo fornisce un metodo di campionamento specializzato che combina il campionamento con Latent Consistency Model (LCM) e l'upscaling progressivo dell'immagine. Durante il campionamento, l'immagine viene sottoposta a upscaling passo dopo passo verso un rapporto di scala obiettivo utilizzando un metodo di interpolazione scelto, consentendo risultati a risoluzione più alta in un singolo passaggio di campionamento. Il nodo restituisce un oggetto sampler configurato che può essere collegato a un nodo di campionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `scale_ratio` | Il fattore di scala totale da applicare durante l'upscaling. Un valore di 1.0 mantiene la risoluzione originale (predefinito: 1.0) | FLOAT | Sì | 0.1 - 20.0 |
| `scale_steps` | Il numero di passaggi da utilizzare per il processo di upscaling. Usare -1 per il calcolo automatico in base alla pianificazione del campionamento (predefinito: -1) | INT | Sì | -1 - 1000 |
| `upscale_method` | Il metodo di interpolazione utilizzato per l'upscaling dell'immagine a ogni passaggio di upscaling (predefinito: "bislerp") | COMBO | Sì | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` e `scale_steps` sono parametri avanzati. L'immagine viene sottoposta a upscaling gradualmente dalla sua dimensione originale fino al `scale_ratio` obiettivo nel corso dei passaggi di upscaling. Quando `scale_steps` è -1, il numero di passaggi di upscaling viene calcolato automaticamente come circa la metà del numero di passaggi di campionamento, con un minimo di 2; quando viene fornito un valore positivo, il nodo lo regola internamente e lo limita in base al numero totale di passaggi di campionamento.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sampler` | Un oggetto sampler configurato che esegue il campionamento LCM con upscaling progressivo, pronto per essere utilizzato nella pipeline di campionamento | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/it.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`

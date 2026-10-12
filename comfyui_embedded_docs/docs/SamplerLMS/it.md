# SamplerLMS

Il nodo SamplerLMS crea un sampler Least Mean Squares (LMS) da utilizzare nei modelli di diffusione. Genera un oggetto sampler che può essere usato nel processo di campionamento, permettendoti di controllare l'ordine dell'algoritmo LMS per stabilità e accuratezza numerica.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `order` | Il parametro `order` per l'algoritmo del sampler LMS, che controlla l'accuratezza e la stabilità del metodo numerico (predefinito: 4). Questo parametro è mostrato nella sezione avanzata dell'interfaccia del nodo. | INT | Sì | da 1 a 100 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sampler` | Un oggetto sampler LMS configurato che può essere utilizzato nella pipeline di campionamento | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/it.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`

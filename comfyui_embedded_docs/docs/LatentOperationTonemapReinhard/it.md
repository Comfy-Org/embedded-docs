# LatentOperationTonemapReinhard

Questo nodo crea un'operazione latente che applica il tonemapping di Reinhard ai vettori latenti. Normalizza ciascun vettore latente, misura la distribuzione complessiva della magnitudine (media e deviazione standard) e poi comprime le magnitudini estreme usando la curva di Reinhard, con l'intensità complessiva controllata da un moltiplicatore. Il nodo è contrassegnato come sperimentale (ricercabile anche come "hdr latent").

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `multiplier` | Controlla l'intensità dell'effetto di tonemapping (predefinito: 1.0) | FLOAT | Sì | 0.0 a 100.0 (passo 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `operation` | Restituisce un'operazione di tonemapping che può essere applicata ai vettori latenti | LATENT_OPERATION |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/it.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`

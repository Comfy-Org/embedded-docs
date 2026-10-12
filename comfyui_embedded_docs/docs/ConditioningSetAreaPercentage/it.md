# ConditioningSetAreaPercentage

Il nodo ConditioningSetAreaPercentage è specializzato nella regolazione dell'area di influenza per gli elementi di conditioning in base a valori percentuali. Consente di specificare le dimensioni e la posizione dell'area come percentuali della dimensione totale dell'immagine, insieme a un parametro `strength` per modulare l'intensità dell'effetto di conditioning.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | Rappresenta gli elementi di conditioning da modificare, fungendo da base per l'applicazione delle regolazioni di area e strength. | CONDITIONING |
| `width` | Specifica la larghezza dell'area come percentuale della larghezza totale dell'immagine, influenzando l'estensione orizzontale dell'influenza del conditioning. | `FLOAT` |
| `height` | Determina l'altezza dell'area come percentuale dell'altezza totale dell'immagine, influenzando l'estensione verticale dell'influenza del conditioning. | `FLOAT` |
| `x` | Indica il punto di partenza orizzontale dell'area come percentuale della larghezza totale dell'immagine, posizionando l'effetto di conditioning. | `FLOAT` |
| `y` | Specifica il punto di partenza verticale dell'area come percentuale dell'altezza totale dell'immagine, posizionando l'effetto di conditioning. | `FLOAT` |
| `strength` | Controlla l'intensità dell'effetto di conditioning all'interno dell'area specificata, consentendo di regolarne con precisione l'impatto. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | Restituisce gli elementi di conditioning modificati con i parametri area e strength aggiornati, pronti per ulteriori elaborazioni o applicazioni. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/it.md)

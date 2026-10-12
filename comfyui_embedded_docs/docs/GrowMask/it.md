# Grow Mask

Il nodo `GrowMask` è progettato per modificare le dimensioni di una maschera data, espandendola o contraendola, con la possibilità di applicare un effetto affusolato agli angoli. Questa funzionalità è cruciale per regolare dinamicamente i confini delle maschere nelle attività di elaborazione delle immagini, consentendo un controllo più flessibile e preciso sull'area di interesse.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `mask` | La maschera di input da modificare. Questo parametro è centrale per il funzionamento del nodo, poiché funge da base sulla quale la maschera viene espansa o contratta. | MASK |
| `expand` | Determina l'ampiezza e la direzione della modifica della maschera. I valori positivi causano l'espansione della maschera, mentre i valori negativi ne causano la contrazione. Questo parametro influenza direttamente le dimensioni finali della maschera. | INT |
| `tapered_corners` | Un flag booleano che, quando impostato su True, applica un effetto affusolato agli angoli della maschera durante la modifica. Questa opzione consente transizioni più uniformi e risultati visivamente gradevoli. | BOOLEAN |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `mask` | La maschera modificata dopo aver applicato l'espansione/contrazione specificata e l'eventuale effetto affusolato agli angoli. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrowMask/it.md)

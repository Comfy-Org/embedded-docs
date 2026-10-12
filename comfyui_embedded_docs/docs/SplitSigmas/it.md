# SplitSigmas

Il nodo SplitSigmas è progettato per suddividere una sequenza di valori sigma in due parti in base a un passo specificato. Questa funzionalità è fondamentale per le operazioni che richiedono una gestione o un'elaborazione diversa della parte iniziale e di quella successiva della sequenza sigma, consentendo una manipolazione più flessibile e mirata di questi valori.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | Il parametro `sigmas` rappresenta la sequenza di valori sigma da suddividere. È essenziale per determinare il punto di suddivisione e le due sequenze risultanti di valori sigma, influenzando l'esecuzione e i risultati del nodo. | `SIGMAS` |
| `step` | Il parametro `step` specifica l'indice in corrispondenza del quale la sequenza sigma deve essere suddivisa. Svolge un ruolo critico nel definire il confine tra le due sequenze sigma risultanti, influenzando la funzionalità del nodo e le caratteristiche dell'output. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | Il nodo restituisce due sequenze di valori sigma, ciascuna delle quali rappresenta una parte della sequenza originale suddivisa in corrispondenza del parametro `step` specificato. Questi output sono cruciali per le operazioni successive che richiedono una gestione differenziata dei valori sigma. | `SIGMAS` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmas/it.md)

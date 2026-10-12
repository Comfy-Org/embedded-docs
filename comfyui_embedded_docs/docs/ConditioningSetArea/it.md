# Conditioning (Imposta Area)

Questo nodo è progettato per modificare le informazioni di condizionamento impostando aree specifiche all'interno del contesto di condizionamento. Consente la manipolazione spaziale precisa degli elementi di condizionamento, abilitando regolazioni e miglioramenti mirati in base alle dimensioni e alla forza specificate.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento da modificare. Fungono da base per applicare le regolazioni spaziali. | CONDITIONING |
| `width` | Specifica la larghezza dell'area da impostare all'interno del contesto di condizionamento, influenzando l'estensione orizzontale della regolazione. | `INT` |
| `height` | Determina l'altezza dell'area da impostare, influenzando l'estensione verticale della modifica del condizionamento. | `INT` |
| `x` | Il punto di partenza orizzontale dell'area da impostare, posizionando la regolazione all'interno del contesto di condizionamento. | `INT` |
| `y` | Il punto di partenza verticale per la regolazione dell'area, stabilendone la posizione all'interno del contesto di condizionamento. | `INT` |
| `strength` | Definisce l'intensità della modifica del condizionamento all'interno dell'area specificata, consentendo un controllo preciso sull'impatto della regolazione. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento modificati, che riflettono le impostazioni dell'area e le regolazioni specificate. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetArea/it.md)

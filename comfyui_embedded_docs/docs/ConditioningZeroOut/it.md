# Condizionamento Azzerato

Questo nodo azzera elementi specifici all'interno della struttura dati di condizionamento, neutralizzandone di fatto l'influenza nei successivi passaggi di elaborazione. È progettato per operazioni di condizionamento avanzate in cui è richiesta la manipolazione diretta della rappresentazione interna del condizionamento.

## Input

| Parametro | Descrizione | Comfy dtype |
| --- | --- | --- |
| `CONDITIONING` | La struttura dati di condizionamento da modificare. Questo nodo azzera gli elementi 'pooled_output' all'interno di ogni voce di condizionamento, se presenti. | CONDITIONING |

## Output

| Parametro | Descrizione | Comfy dtype |
| --- | --- | --- |
| `CONDITIONING` | La struttura dati di condizionamento modificata, con gli elementi 'pooled_output' impostati a zero dove applicabile. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/it.md)

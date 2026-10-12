# ControlnetApplyAdvanced

Questo nodo applica trasformazioni avanzate del ControlNet ai dati di condizionamento basandosi su un'immagine e su un modello ControlNet. Consente regolazioni finemente calibrate dell'influenza del ControlNet sul contenuto generato, permettendo modifiche più precise e variegate al condizionamento.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | I dati di condizionamento positivo a cui verranno applicate le trasformazioni del ControlNet. Rappresentano gli attributi o le caratteristiche desiderate da potenziare o mantenere nel contenuto generato. | `CONDITIONING` |
| `negative` | I dati di condizionamento negativo, che rappresentano attributi o caratteristiche da ridurre o rimuovere dal contenuto generato. Anche a questi dati vengono applicate le trasformazioni del ControlNet, consentendo una regolazione bilanciata delle caratteristiche del contenuto. | `CONDITIONING` |
| `control_net` | Il modello ControlNet è cruciale per definire le regolazioni e i potenziamenti specifici dei dati di condizionamento. Interpreta l'immagine di riferimento e i parametri di intensità per applicare trasformazioni, influenzando in modo significativo il risultato finale modificando gli attributi sia nei dati di condizionamento positivo sia in quelli negativi. | `CONTROL_NET` |
| `image` | L'immagine che funge da riferimento per le trasformazioni del ControlNet. Influenza le regolazioni apportate dal ControlNet ai dati di condizionamento, guidando il potenziamento o la soppressione di caratteristiche specifiche. | `IMAGE` |
| `strength` | Un valore scalare che determina l'intensità dell'influenza del ControlNet sui dati di condizionamento. Valori più alti producono regolazioni più pronunciate. | `FLOAT` |
| `start_percent` | La percentuale iniziale dell'effetto del ControlNet, che consente l'applicazione graduale delle trasformazioni su un intervallo specificato. | `FLOAT` |
| `end_percent` | La percentuale finale dell'effetto del ControlNet, che definisce l'intervallo in cui vengono applicate le trasformazioni. Ciò consente un controllo più sfumato sul processo di regolazione. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | I dati di condizionamento positivo modificati dopo l'applicazione delle trasformazioni del ControlNet, che riflettono i potenziamenti effettuati in base ai parametri di input. | `CONDITIONING` |
| `negative` | I dati di condizionamento negativo modificati dopo l'applicazione delle trasformazioni del ControlNet, che riflettono la soppressione o la rimozione di caratteristiche specifiche in base ai parametri di input. | `CONDITIONING` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlnetApplyAdvanced/it.md)

# ConditioningSettimestepRange

Questo nodo è progettato per regolare l'aspetto temporale del condizionamento impostando un intervallo specifico di timestep. Consente un controllo preciso sui punti di inizio e fine del processo di condizionamento, abilitando una generazione più mirata ed efficiente.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | L'input `CONDITIONING` rappresenta lo stato attuale del processo di generazione, che questo nodo modifica impostando un intervallo specifico di timestep. | CONDITIONING |
| `start` | Il parametro `start` specifica l'inizio dell'intervallo di timestep come percentuale del processo di generazione totale, consentendo un controllo preciso su quando iniziano gli effetti del condizionamento. | `FLOAT` |
| `end` | Il parametro `end` definisce il punto finale dell'intervallo di timestep come percentuale, consentendo un controllo preciso sulla durata e sulla conclusione degli effetti del condizionamento. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | L'output è il condizionamento modificato a cui è stato applicato l'intervallo di timestep specificato, pronto per ulteriori elaborazioni o generazione. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSettimestepRange/it.md)

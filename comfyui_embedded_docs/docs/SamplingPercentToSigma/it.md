# SamplingPercentToSigma

Converte una percentuale di campionamento nel valore sigma corrispondente utilizzando le impostazioni di campionamento del modello selezionato. Mappa una percentuale compresa tra 0.0 e 1.0 sulla schedulazione del rumore del modello e può facoltativamente restituire il valore sigma massimo o minimo reale del modello nei due punti estremi.

## Input

| Parametro | Descrizione | Tipo di dati | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello contenente i parametri di campionamento usati per la conversione | MODEL | Sì | - |
| `sampling_percent` | La percentuale di campionamento da convertire in un valore sigma (predefinito: 0.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.0001) |
| `return_actual_sigma` | Restituisce il valore sigma effettivo invece del valore usato per i controlli degli intervalli. Questo influisce solo sui risultati a 0.0 e 1.0. (predefinito: False) | BOOLEAN | Sì | - |

Quando `return_actual_sigma` è abilitato, un `sampling_percent` di 0.0 restituisce il valore sigma massimo del modello (sigma_max), e un `sampling_percent` di 1.0 restituisce il valore sigma minimo (sigma_min). Per tutte le altre percentuali, il risultato è lo stesso indipendentemente dal fatto che questa opzione sia abilitata o meno.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sigma_value` | Il valore sigma corrispondente alla percentuale di campionamento in input | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/it.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`

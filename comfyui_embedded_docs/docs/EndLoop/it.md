# EndLoop

End Loop contrassegna la fine di un blocco loop. Raccoglie il valore prodotto dall'ultimo nodo nel corpo del ciclo e restituisce solo l'iterazione finale oppure ogni iterazione, a seconda dell'impostazione `accumulate`, passando inoltre un valore a Start Loop in modo che possa iniziare l'iterazione successiva.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `output_value` | Valore restituito da End Loop. Restituisce l'iterazione finale o tutte le iterazioni in base a `accumulate`. | ANY | No | Qualsiasi tipo di valore |
| `next_iteration_value` | Valore inviato da End Loop a Start Loop per l'iterazione successiva. | ANY | No | Qualsiasi tipo di valore |
| `accumulate` | Se abilitato, restituisce `output_value` da ogni iterazione; altrimenti restituisce solo l'iterazione finale. | BOOLEAN | No | `true`<br>`false` (predefinito: `false`) |
| `terminations` | Collega output che devono essere eseguiti a ogni iterazione. I loro valori non vengono restituiti. Slot espandibili denominati `termination_1`, `termination_2` e così via. | ANY | No | Da 0 a 50 slot |

Nota: `terminations` è un elenco espandibile di slot con un minimo di 0 e un massimo di 50 connessioni. I valori collegati qui forzano l'esecuzione a ogni iterazione ma non fanno parte del risultato restituito.

Nota: Questo nodo è un nodo di elenco di input, quindi i suoi input ricevono i valori raccolti da ogni iterazione del ciclo.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `outputs` | L'`output_value` dell'iterazione finale, oppure i valori accumulati tra le iterazioni quando `accumulate` è abilitato. | ANY (list) |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EndLoop/it.md)

---
**Source fingerprint (SHA-256):** `142840dca7f238eb00c72074d265478c548ad5c047e05744d0c3715e452f795a`

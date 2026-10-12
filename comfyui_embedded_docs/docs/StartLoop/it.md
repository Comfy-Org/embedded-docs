# StartLoop

Il nodo Start Loop avvia una struttura di ciclo all'interno di un workflow. Esegue il corpo del ciclo collegato una volta per iterazione e può contare le iterazioni in tre modi: un numero fisso di ripetizioni (simple), un intervallo di indici numerici (For) oppure un passaggio per ogni elemento di una lista (List). Ogni passaggio espone l'indice corrente, i flag first/last e un valore trasportato opzionale che può essere passato da un'iterazione alla successiva.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `mode` | La modalità di iterazione del ciclo (predefinita: `"simple"`). La modalità selezionata determina quali parametri aggiuntivi vengono mostrati. | DYNAMIC_COMBO | Sì | `"simple"`<br>`"For"`<br>`"List"` |
| `cache_iterations` | Riutilizza i risultati invariati delle iterazioni dalle esecuzioni precedenti. Disabilita per eseguire di nuovo ogni iterazione. Predefinito: false. | BOOLEAN | Sì | true<br>false |
| `parent_iteration` | Collega iteration_index da un Start Loop esterno per annidare questo ciclo. Questo input è solo force-input (è richiesto un collegamento). | INT | No | Qualsiasi numero intero |
| `initial_iteration_value` | Valore esposto come current_iteration_value durante la prima iterazione. | ANY (type-matched) | No | Qualsiasi valore |

### Input della modalità Simple

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `num_iterations` | Numero di volte in cui eseguire il corpo del ciclo. Predefinito: 4. | INT | Sì | Minimo 0 |

### Input della modalità For

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `start_iteration_index` | Indice della prima iterazione quando si usa la modalità For. Predefinito: 0. | INT | Sì | Qualsiasi numero intero |
| `max_iteration` | Il valore di arresto esclusivo per iteration_index nella modalità For. Predefinito: 4. | INT | Sì | Massimo 0xffffffffffffffff |
| `step` | La dimensione del passo dell'indice tra un'iterazione e l'altra quando si usa la modalità For. Predefinito: 1. | INT | Sì | Minimo 1 |

### Input della modalità List

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `list` | Lista di elementi su cui itera il ciclo. Il corpo del ciclo viene eseguito una volta per elemento. | ANY (type-matched list item) | Sì | Qualsiasi lista |

Note:

- Vengono mostrati e usati solo i parametri appartenenti alla `mode` attualmente selezionata.
- Nella modalità Simple, gli indici di iterazione vanno da 0 fino a `num_iterations` meno 1. Nella modalità For, gli indici vanno da `start_iteration_index` fino a (ma non incluso) `max_iteration`, aumentando di `step`. Nella modalità List, viene eseguita un'iterazione per ogni elemento in `list`.
- `step` non deve essere 0; un valore di 0 genera un errore. Valori inferiori a 1 non sono consentiti.
- Se il numero calcolato di iterazioni è zero, l'output `is_last` viene riportato come true e il corpo del ciclo non viene eseguito.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `iteration_index` | Indice dell'iterazione corrente del ciclo. | INT |
| `is_first` | Vero durante la prima iterazione del ciclo. | BOOLEAN |
| `is_last` | Vero durante l'ultima iterazione del ciclo. | BOOLEAN |
| `list_item` | Elemento corrente della lista quando si usa la modalità List. Nessuno nelle modalità Simple e For. | ANY (type-matched) |
| `current_iteration_value` | Valore trasportato dal ciclo per l'iterazione corrente: initial_iteration_value durante la prima iterazione, poi next_iteration_value da End Loop in ogni iterazione successiva. | ANY (type-matched) |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StartLoop/it.md)

---
**Source fingerprint (SHA-256):** `be34fedd4db9d4f4cc795855c87f6489f294e029da316b5dc66e5af7dff004a9`

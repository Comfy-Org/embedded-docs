# DCTestNode

DCTestNode è un nodo logico che restituisce diversi tipi di dati in base alla selezione effettuata dall'utente da una casella combinata dinamica. Funziona come un router condizionale, in cui l'opzione scelta determina quale campo di input è attivo e quale tipo di valore il nodo restituirà. Il nodo è contrassegnato come nodo di output in ComfyUI.

## Input

Il nodo utilizza un selettore combinato dinamico: il parametro `combo` è sempre visibile, mentre gli altri campi di input vengono visualizzati solo quando viene selezionata l'opzione corrispondente.

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `combo` | La selezione principale che determina quale campo di input è attivo e cosa restituirà il nodo. | DYNAMIC_COMBO | Sì | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### Input di option1

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `string` | Un campo di input testuale. Questo campo è attivo e obbligatorio solo quando `combo` è impostato su `"option1"`. | STRING | Sì | - |

### Input di option2

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `integer` | Un campo di input per un numero intero. Questo campo è attivo e obbligatorio solo quando `combo` è impostato su `"option2"`. | INT | Sì | - |

### Input di option3

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `image` | Un campo di input per un'immagine. Questo campo è attivo e obbligatorio solo quando `combo` è impostato su `"option3"`. | IMAGE | Sì | - |

### Input di option4

Quando `combo` è impostato su `"option4"`, il nodo mostra un secondo selettore combinato dinamico (`subcombo`) che controlla un insieme annidato di campi di input.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `subcombo` | Una selezione combinata dinamica secondaria che appare quando `combo` è impostato su `"option4"`. Determina quali campi di input annidati sono attivi. | DYNAMIC_COMBO | Sì | `"opt1"`<br>`"opt2"` |
| `float_x` | Un input per un numero decimale. Questo campo è attivo e obbligatorio solo quando `combo` è impostato su `"option4"` e `subcombo` è impostato su `"opt1"`. | FLOAT | Sì | - |
| `float_y` | Un input per un numero decimale. Questo campo è attivo e obbligatorio solo quando `combo` è impostato su `"option4"` e `subcombo` è impostato su `"opt1"`. | FLOAT | Sì | - |
| `mask1` | Un campo di input per una maschera. Questo campo è attivo solo quando `combo` è impostato su `"option4"` e `subcombo` è impostato su `"opt2"`. È opzionale. | MASK | No | - |

**Vincoli dei parametri:**

* Il parametro `combo` controlla la visibilità e l'obbligatorietà di tutti gli altri campi di input. Verranno mostrati e saranno obbligatori solo gli input associati all'opzione `combo` selezionata (tranne `mask1`, che è opzionale).
* Quando `combo` è impostato su `"option4"`, il parametro `subcombo` diventa obbligatorio e controlla un secondo insieme di input annidati (`float_x`/`float_y` o `mask1`).
* Se `combo` riceve un valore che non è una delle quattro opzioni elencate, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | L'output dipende dall'opzione `combo` selezionata. Può essere una STRING (`"option1"`), un INT (`"option2"`), un'IMAGE (`"option3"`) o una rappresentazione stringa del valore `subcombo` (`"option4"`). | ANYTYPE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/it.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`

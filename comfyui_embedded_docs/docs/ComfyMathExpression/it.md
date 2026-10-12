# ComfyMathExpression

Il nodo ComfyMathExpression valuta una formula matematica scritta come testo. La formula può fare riferimento ai valori di input del nodo usando nomi di lettera come `a`, `b`, `c`, e puoi aggiungere tutti i valori di input necessari tramite il gruppo espandibile `values`. Il risultato del calcolo viene restituito contemporaneamente come numero in virgola mobile, numero intero e valore booleano.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `expression` | La formula matematica da valutare, scritta come testo (ad esempio `a + b`), usando i nomi di lettera dei valori di input come variabili. Input multilinea. (predefinito: "a + b") | STRING | Sì | N/A |
| `values` | Gruppo espandibile di valori di input che fornisce le variabili per l'espressione. Ogni valore aggiunto al gruppo riceve automaticamente il successivo nome di lettera minuscola a partire da `a` (`a`, `b`, `c`, ...), e quel nome può quindi essere usato all'interno di `expression`. Ogni elemento accetta un numero (INT o FLOAT) o un booleano (TRUE/FALSE). | FLOAT, INT, BOOLEAN | Sì | Da 1 a 26 valori, denominati da `a` a `z` |

### Note e vincoli

- Il parametro `expression` non può essere vuoto o contenere solo spazi bianchi.
- L'espressione deve restituire un risultato numerico (INT o FLOAT) o un risultato booleano (TRUE/FALSE). I risultati booleani vengono trattati come 1 per TRUE e 0 per FALSE. Se il risultato è di un tipo diverso, ad esempio testo, il nodo genera un errore.
- Il risultato numerico deve essere finito e convertibile in un float. Risultati troppo grandi o non finiti causano un errore.
- L'intero insieme dei valori di input è disponibile anche all'interno dell'espressione con il nome di variabile `values` (come lista), quindi sono possibili espressioni come `sum(values)`.
- All'interno dell'espressione sono disponibili le seguenti funzioni matematiche: `sum`, `min`, `max`, `abs`, `round`, `pow`, `sqrt`, `ceil`, `floor`, `log`, `log2`, `log10`, `sin`, `cos`, `tan`, `int`, `float`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `FLOAT` | Il risultato dell'espressione come numero in virgola mobile. | FLOAT |
| `INT` | Il risultato dell'espressione convertito in un numero intero, con la parte decimale troncata. | INT |
| `BOOL` | Il risultato convertito in un valore booleano: TRUE quando il risultato numerico non è zero, FALSE quando è zero. | BOOLEAN |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/it.md)

---
**Source fingerprint (SHA-256):** `4c77e9834fe7341143352f95ed8808dc81def3361b197c67e33a531bb3696d71`

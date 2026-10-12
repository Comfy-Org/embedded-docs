# ComfyNumberConvert

Il nodo Number Convert trasforma vari tipi di dati di input in valori numerici. Accetta un singolo input di tipo intero, float, stringa o booleano e produce due output: un numero in virgola mobile e un intero. Questo è utile per convertire testo o valori logici in un formato utilizzabile da altri nodi matematici o di elaborazione nel flusso di lavoro.

## Input
| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `value` | Il valore da convertire in output numerici. Accetta un intero, un numero in virgola mobile, una stringa di testo o un booleano true/false. | INT, FLOAT, STRING, BOOLEAN | Sì | N/A |

**Nota:** Quando l'input è una stringa, non deve essere vuota e deve contenere una rappresentazione valida di un numero (ad es. `"123"`, `"3.14"`). Il nodo genererà un errore per stringhe vuote, testo che non può essere interpretato come numero o valori che non sono finiti (come `"inf"` o `"nan"`). Per input booleani, `true` viene convertito in 1.0 (FLOAT) e 1 (INT), mentre `false` viene convertito in 0.0 (FLOAT) e 0 (INT). Per input di tipo float e per stringhe che contengono un numero decimale, l'output intero si ottiene troncando la parte decimale.

## Output
| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `FLOAT` | Il valore di input convertito in un numero in virgola mobile. | FLOAT |
| `INT` | Il valore di input convertito in un intero. Per input di tipo float e stringhe decimali, esegue un troncamento. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/it.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`

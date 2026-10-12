# AutogrowPrefixTestNode

AutogrowPrefixTestNode è un nodo logico che verifica la funzionalità di input autogrow. Accetta un numero dinamico di input di tipo float, converte ogni valore in testo, li combina in una stringa separata da virgole e restituisce come output tale stringa.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `autogrow` | Un gruppo di input dinamico che accetta da 1 a 10 valori float. Ogni valore è un numero in virgola mobile e gli input generati sono denominati con il prefisso `float`. | AUTOGROW | Sì | da 1 a 10 input |

**Nota:** L'input `autogrow` è un input dinamico speciale. Puoi aggiungere più input float a questo gruppo, da un minimo di 1 fino a un massimo di 10. Il nodo elabora tutti i valori forniti e include ogni input collegato nella stringa di output.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Una singola stringa contenente tutti i valori float di input, separati da virgole. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/it.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`

# Epsilon Scaling

Questo nodo implementa il metodo Epsilon Scaling descritto nell'articolo di ricerca "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/2308.15321v6). Funziona scalando il rumore previsto durante il processo di campionamento per contribuire a ridurre il bias di esposizione, il che può portare a una qualità migliore nelle immagini generate. Questa implementazione utilizza la "schedulazione uniforme" consigliata dall'articolo per la sua praticità ed efficacia.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare la patch di epsilon scaling. | MODEL | Sì | - |
| `scaling_factor` | Il fattore con cui viene scalato il rumore previsto. Un valore maggiore di 1.0 riduce il rumore, mentre un valore minore di 1.0 lo aumenta (predefinito: 1.005). Questo è un parametro avanzato. | FLOAT | No | 0.5 - 1.5 (passo: 0.001) |

Nota: se `scaling_factor` è impostato su 0, il nodo lo sostituisce automaticamente con un valore molto piccolo (1e-9) per evitare la divisione per zero. Il valore minimo dell'interfaccia utente di 0.5 di norma impedisce che ciò accada.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Una versione con patch del modello di input con la funzione di epsilon scaling applicata al suo processo di campionamento. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/it.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`

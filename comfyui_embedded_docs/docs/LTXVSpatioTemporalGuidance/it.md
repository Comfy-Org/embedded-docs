# LTXVSpatioTemporalGuidance

Questo nodo migliora il dettaglio spaziale e la coerenza del movimento della generazione video LTXV eseguendo un passaggio aggiuntivo a ogni passo di campionamento. Durante questo passaggio, l'auto-attenzione dei blocchi transformer selezionati viene degradata a un pass-through del valore, e la generazione viene guidata ad allontanarsi da quel risultato degradato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello di base a cui applicare la guida spazio-temporale. Il modello viene clonato e una funzione di guida post-CFG viene associata al clone. | MODEL | Sì | — |
| `scale` | La forza della guida applicata al risultato denoizzato. Quando è impostata a 0, la guida non ha effetto. (predefinito: 1.0) | FLOAT | Sì | 0.0 a 100.0 (passo 0.01) |
| `blocks` | Indici dei blocchi transformer da perturbare, separati da virgole. Vengono usati solo valori numerici; qualsiasi altro carattere viene ignorato. (predefinito: "29") | STRING | Sì | — |
| `start_percent` | La frazione del processo di campionamento in cui inizia la guida. Questo è un parametro avanzato. (predefinito: 0.0) | FLOAT | Sì | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | La frazione del processo di campionamento in cui termina la guida. Questo è un parametro avanzato. (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo 0.001) |

Nota: la guida viene applicata solo durante l'intervallo di campionamento compreso tra `start_percent` e `end_percent`. Al di fuori di tale intervallo, il risultato denoizzato originale viene restituito invariato. Se `scale` è 0 o `blocks` non contiene valori numerici, il passaggio guidato non ha alcun effetto sul processo di campionamento.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `MODEL` | Il modello clonato con la funzione di guida spazio-temporale associata. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/it.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`

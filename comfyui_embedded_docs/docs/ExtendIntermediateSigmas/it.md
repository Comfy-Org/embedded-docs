# Estendi Sigmas Intermedi

Il nodo ExtendIntermediateSigmas prende una sequenza esistente di valori sigma e inserisce ulteriori valori sigma intermedi tra di essi. Consente di specificare quanti passaggi aggiuntivi aggiungere, il metodo di spaziatura per l'interpolazione e i limiti opzionali di sigma iniziale e finale per controllare dove avviene l'estensione all'interno della sequenza sigma.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `sigmas` | La sequenza sigma di input da estendere con valori intermedi | SIGMAS | Sì | - |
| `steps` | Controlla il numero di valori sigma intermedi inseriti tra ogni coppia di sigma esistenti. L'intervallo tra due sigma è diviso in `steps` parti, producendo `steps - 1` nuovi valori per coppia (predefinito: 2, che inserisce un valore per coppia) | INT | Sì | 1 to 100 |
| `start_at_sigma` | Limite superiore di sigma per l'estensione. Solo gli intervalli sigma il cui sigma iniziale è minore o uguale a questo valore vengono estesi. Quando impostato a -1.0, viene trattato come infinito, il che significa che non viene applicato alcun limite superiore. Predefinito: -1.0 | FLOAT | Sì | -1.0 to 20000.0 |
| `end_at_sigma` | Limite inferiore di sigma per l'estensione. Solo gli intervalli sigma il cui sigma iniziale è maggiore o uguale a questo valore vengono estesi. Predefinito: 12.0 | FLOAT | Sì | 0.0 to 20000.0 |
| `spacing` | Il metodo di interpolazione per la spaziatura dei valori sigma intermedi (predefinito: "linear") | COMBO | Sì | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Nota:** Il nodo inserisce valori sigma intermedi solo per gli intervalli sigma in cui il sigma iniziale è minore o uguale a `start_at_sigma` e maggiore o uguale a `end_at_sigma`. Quando `start_at_sigma` è impostato a -1.0, viene trattato come infinito, quindi si applica solo il limite inferiore `end_at_sigma`.

## Output

| Nome dell'output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | La sequenza sigma estesa con ulteriori valori intermedi inseriti | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/it.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`

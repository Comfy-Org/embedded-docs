# ModelSamplingFlux

Il nodo ModelSamplingFlux applica il campionamento del modello Flux a un modello specificato calcolando un parametro shift basato sulle dimensioni dell'immagine. Crea una configurazione di campionamento specializzata che adatta il comportamento del modello in base ai parametri width, height e shift specificati, quindi restituisce il modello modificato con le nuove impostazioni di campionamento applicate.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare il campionamento Flux | MODEL | Sì | - |
| `max_shift` | Valore massimo di shift per il calcolo del campionamento (predefinito: 1.15) | FLOAT | Sì | 0.0 - 100.0 (step 0.01) |
| `base_shift` | Valore base di shift per il calcolo del campionamento (predefinito: 0.5) | FLOAT | Sì | 0.0 - 100.0 (step 0.01) |
| `width` | Larghezza dell'immagine di destinazione in pixel (predefinito: 1024) | INT | Sì | 16 - MAX_RESOLUTION (step 8) |
| `height` | Altezza dell'immagine di destinazione in pixel (predefinito: 1024) | INT | Sì | 16 - MAX_RESOLUTION (step 8) |

`max_shift` e `base_shift` sono parametri avanzati. Lo shift applicato alla configurazione di campionamento viene calcolato dalle dimensioni dell'immagine: la risoluzione latente viene calcolata come `width × height / 256`, e il valore di shift viene interpolato tra `base_shift` a una risoluzione latente di 256 e `max_shift` a una risoluzione latente di 4096.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato con la configurazione di campionamento Flux applicata | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/it.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`

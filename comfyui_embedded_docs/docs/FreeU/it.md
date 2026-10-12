# FreeU

Il nodo FreeU applica modifiche nel dominio della frequenza ai blocchi di output di un modello per migliorare la qualità della generazione di immagini. Funziona scalando diversi gruppi di canali e applicando un filtraggio di Fourier a specifiche mappe di caratteristiche, consentendo un controllo ottimizzato del comportamento del modello durante il processo di generazione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello su cui applicare le modifiche FreeU | MODEL | Sì | - |
| `b1` | Fattore di scalatura della backbone applicato alle mappe di caratteristiche con model_channels × 4 canali (predefinito: 1.1). Contrassegnato come impostazione avanzata. | FLOAT | Sì | 0.0 - 10.0 |
| `b2` | Fattore di scalatura della backbone applicato alle mappe di caratteristiche con model_channels × 2 canali (predefinito: 1.2). Contrassegnato come impostazione avanzata. | FLOAT | Sì | 0.0 - 10.0 |
| `s1` | Fattore di scalatura della skip connection applicato alle mappe di caratteristiche con model_channels × 4 canali (predefinito: 0.9). Contrassegnato come impostazione avanzata. | FLOAT | Sì | 0.0 - 10.0 |
| `s2` | Fattore di scalatura della skip connection applicato alle mappe di caratteristiche con model_channels × 2 canali (predefinito: 0.2). Contrassegnato come impostazione avanzata. | FLOAT | Sì | 0.0 - 10.0 |

Nota: le regolazioni FreeU vengono applicate solo alle mappe di caratteristiche il cui numero di canali è uguale a model_channels × 4 (usando `b1` e `s1`) oppure model_channels × 2 (usando `b2` e `s2`). Il filtro di Fourier scala solo la regione centrale a bassa frequenza (soglia di 1) delle mappe di caratteristiche della skip connection; tutte le altre componenti in frequenza rimangono invariate. Tutti e quattro i parametri di scalatura accettano valori compresi tra 0.0 e 10.0 con incrementi di 0.01.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato con le patch FreeU applicate | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/it.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`

# SplitSigmasDenoise

Il nodo SplitSigmasDenoise divide una sequenza di valori sigma in due parti in base a un parametro di forza di denoising. Suddivide i sigma di input in sequenze di sigma alte e basse, dove il punto di divisione è determinato moltiplicando il numero totale di passaggi (uno in meno rispetto al numero di valori sigma) per il fattore denoise. Ciò consente di separare lo schedule del rumore in diversi intervalli di intensità per un'elaborazione specializzata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `sigmas` | La sequenza di valori sigma di input che rappresenta lo schedule del rumore | SIGMAS | Sì | - |
| `denoise` | Il fattore di forza di denoising che determina dove dividere la sequenza sigma (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `high_sigmas` | La prima porzione della sequenza sigma, contenente i valori sigma più alti fino al punto di divisione | SIGMAS |
| `low_sigmas` | La seconda porzione della sequenza sigma, contenente i valori sigma più bassi dal punto di divisione in poi | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/it.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`

# ModelSamplingSD3

Questo nodo applica impostazioni di campionamento in stile Stable Diffusion 3 a un modello. Crea una copia del modello e sostituisce il suo metodo di campionamento con una configurazione di campionamento basata su flusso che utilizza il valore `shift` fornito, il quale controlla la forma della distribuzione di campionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di input a cui applicare i parametri di campionamento SD3 | MODEL | Sì | - |
| `shift` | Controlla il parametro di shift del campionamento (predefinito: 3.0) | FLOAT | Sì | 0.0 - 100.0 (step: 0.01) |

Nota: Il valore `shift` viene applicato insieme a un moltiplicatore interno fisso di 1000. Se il modello originale ha un'impostazione della scala di rumore, tale valore viene trasferito al modello modificato. Il modello originale non viene modificato; viene restituita una copia clonata e patchata.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato con i parametri di campionamento SD3 applicati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/it.md)

---
**Source fingerprint (SHA-256):** `a77e38c2cebf6f21f841a953ec5c59096eaf60ffc205c24f34f635e54c5718cb`

# APG

Il nodo APG (Adaptive Projected Guidance) modifica il processo di campionamento regolando il modo in cui la guida viene applicata durante la diffusione. Separa il vettore di guida in componenti parallele e ortogonali rispetto all'output condizionale, consentendo una generazione di immagini più controllata. Il nodo fornisce parametri per scalare la guida, normalizzarne l'ampiezza e applicare il momentum per transizioni più fluide tra i passaggi di diffusione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui applicare la guida proiettata adattiva | MODEL | Sì | - |
| `eta` | Controlla la scala del vettore di guida parallelo. Comportamento CFG predefinito con un'impostazione di 1 (predefinito: 1.0). | FLOAT | No | -10.0 to 10.0 |
| `norm_threshold` | Normalizza il vettore di guida a questo valore; normalizzazione disabilitata con un'impostazione di 0 (predefinito: 5.0). | FLOAT | No | 0.0 to 50.0 |
| `momentum` | Controlla una media mobile della guida durante la diffusione; disabilitata con un'impostazione di 0 (predefinito: 0.0). | FLOAT | No | -5.0 to 1.0 |

Nota: Quando il livello di rumore (`sigma`) aumenta durante il campionamento, la media mobile del momentum viene ripristinata a zero. Se il modello fornisce un solo output di condizionamento (nessun condizionamento incondizionato separato), la regolazione della guida viene saltata e il condizionamento viene lasciato invariato.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Restituisce il modello modificato con la guida proiettata adattiva applicata al relativo processo di campionamento | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/it.md)

---
**Source fingerprint (SHA-256):** `df0c76aee28479d49c4e471e54d1d32082adc6921a6a50b506675144a79e018a`

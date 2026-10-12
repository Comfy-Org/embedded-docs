# LTXVModalityGuidance

Questo nodo applica una guida cross-modale (audio-video) a un modello LTXV-AV. Durante il campionamento, esegue un passaggio forward extra per ogni step con le connessioni cross-attention da audio a video e da video ad audio disabilitate, quindi spinge il risultato verso la previsione accoppiata per rafforzare la sincronizzazione audio-visiva, come il lip-sync. Il valore predefinito di riferimento per `modality_scale` è 3.0; impostandolo a 1.0 si disabilita il passaggio extra, e si combina con il guider dual-CFG e STG.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello di base a cui applicare la guida di modalità. Viene clonato internamente, lasciando invariato il modello originale. | MODEL | Sì | - |
| `modality_scale` | Forza della guida all'accoppiamento audio-video. Il valore predefinito è 3.0. Impostare a 1.0 per disabilitare il passaggio forward extra. | FLOAT | Sì | 1.0 a 100.0 (predefinito: 3.0) |
| `start_percent` | Il punto nel processo di campionamento, come percentuale da 0.0 a 1.0, in cui inizia la guida di modalità. Questo è un parametro avanzato. Il valore predefinito è 0.0. | FLOAT | Sì | 0.0 a 1.0 (predefinito: 0.0) |
| `end_percent` | Il punto nel processo di campionamento, come percentuale da 0.0 a 1.0, in cui termina la guida di modalità. Questo è un parametro avanzato. Il valore predefinito è 1.0. | FLOAT | Sì | 0.0 a 1.0 (predefinito: 1.0) |

La guida viene applicata solo per gli step di campionamento i cui valori sigma rientrano nell'intervallo definito da `start_percent` e `end_percent`. Al di fuori di questo intervallo, il nodo restituisce il risultato denoised invariato. Anche un valore di `modality_scale` pari a 1.0 disabilita completamente il passaggio forward extra.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `model` | Il modello clonato con una funzione di guida post-CFG collegata. Questo modello modificato applica la guida di modalità durante il campionamento. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/it.md)

---
**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`

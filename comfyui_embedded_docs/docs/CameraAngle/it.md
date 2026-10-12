# CameraAngle

Questo nodo seleziona un angolo di camera attorno a un soggetto e trasforma questa scelta in due elementi: una struttura `camera_info` che i nodi 3D possono renderizzare e una descrizione dell'inquadratura in inglese semplice che puoi incollare in un prompt. Il soggetto si trova nell'origine della scena, dove i nodi 3D a valle centrano i loro modelli, quindi l'angolo scelto qui corrisponde all'anteprima.

Usalo per inquadrare un render prima della generazione, oppure per descrivere un punto di vista come `front view eye-level shot medium shot` per un modello di immagini o video. L'anteprima 3D nel nodo mostra la posizione risultante della camera.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `horizontal_angle` | Azimut attorno al soggetto in gradi: 0 è la parte anteriore, 90 il lato destro e 180 il retro. (predefinito: 0) | INT | Sì | 0 a 360 |
| `vertical_angle` | Elevazione in gradi. I valori negativi inquadrano dal basso verso l'alto, quelli positivi dall'alto verso il basso. (predefinito: 0) | INT | Sì | -30 a 60 |
| `zoom` | Zoom dell'obiettivo sul soggetto: 0 è un campo largo, 10 un primo piano. Il valore viene riportato anche in `camera_info.zoom`. (predefinito: 5.0) | FLOAT | Sì | 0.0 a 10.0 (passo 0.1) |
| `image` | Immagine di riferimento opzionale, mostrata sulla faccia anteriore del cubo del soggetto nell'anteprima 3D. | IMAGE | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `camera_info` | Informazioni sulla camera per i nodi 3D: posizione, target di puntamento, fattore di zoom, tipo di camera e campo visivo. La camera mantiene un campo visivo fisso di 35 gradi ed è posizionata a 6 unità dal target. | LOAD3DCAMERA |
| `prompt` | Breve descrizione dell'inquadratura costruita dall'angolo, dall'elevazione e dalla distanza, ad esempio `front view eye-level shot medium shot`. | STRING |

## Termini della descrizione dell'inquadratura

L'output `prompt` combina un termine da ciascun gruppo riportato di seguito. I valori vengono prima limitati agli intervalli dei widget.

- L'angolo orizzontale è suddiviso in otto settori di 45 gradi: `front view`, `front-right quarter view`, `right side view`, `back-right quarter view`, `back view`, `back-left quarter view`, `left side view`, `front-left quarter view`.
- L'angolo verticale diventa `low-angle shot` sotto -15 gradi, `eye-level shot` sotto 15, `elevated shot` sotto 45 e `high-angle shot` da 45 gradi in su.
- Lo zoom diventa `wide shot` sotto 2, `medium shot` sotto 6 e `close-up` da 6 in su.

Il fattore `camera_info.zoom` riscala il valore del widget su un intervallo da 1.0 a 1.875, quindi uno zoom pari a 0 restituisce 1.0 e uno zoom pari a 10 restituisce 1.875.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CameraAngle/it.md)

---
**Source fingerprint (SHA-256):** `8ed2cd186bc6ca02dbc8da006b2e9156245ef691a2257f286f6e32ffa480fd5d`

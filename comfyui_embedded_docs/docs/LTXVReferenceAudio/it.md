# LTXVReferenceAudio

LTXV Reference Audio trasferisce l'identità vocale di un parlante da una clip audio di riferimento all'audio generato. Codifica l'audio di riferimento nel condizionamento e, facoltativamente, applica una patch al modello con la guida dell'identità, che esegue un passaggio forward aggiuntivo senza il riferimento a ogni step per amplificare l'effetto dell'identità del parlante.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare la patch con la guida dell'identità. | MODEL | Sì | - |
| `positive` | L'input di condizionamento positivo. | CONDITIONING | Sì | - |
| `negative` | L'input di condizionamento negativo. | CONDITIONING | Sì | - |
| `reference_audio` | Clip audio di riferimento di cui trasferire l'identità del parlante. Consigliati ~5 secondi (durata di addestramento). Clip più corte o più lunghe possono degradare il trasferimento dell'identità vocale. | AUDIO | Sì | - |
| `audio_vae` | VAE audio LTXV per la codifica. | VAE | Sì | - |
| `identity_guidance_scale` | Forza della guida dell'identità. Esegue un passaggio forward aggiuntivo senza il riferimento a ogni step per amplificare l'identità del parlante. Impostare a 0 per disabilitare (nessun passaggio aggiuntivo). (predefinito: 3.0) | FLOAT | Sì | 0.0 - 100.0 |
| `start_percent` | Inizio dell'intervallo sigma in cui la guida dell'identità è attiva. (predefinito: 0.0) | FLOAT | Sì | 0.0 - 1.0 |
| `end_percent` | Fine dell'intervallo sigma in cui la guida dell'identità è attiva. (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

Nota: la guida dell'identità viene applicata solo quando `identity_guidance_scale` è maggiore di 0 e lo step di campionamento corrente rientra nell'intervallo definito da `start_percent` e `end_percent`. L'audio di riferimento viene ricampionato alla frequenza di campionamento del VAE audio se i due valori differiscono.

Nota: `start_percent` e `end_percent` sono parametri avanzati, mostrati solo quando le opzioni avanzate sono abilitate nell'interfaccia.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello con patch alla funzione di guida dell'identità. | MODEL |
| `positive` | Il condizionamento positivo, ora contenente i dati dell'audio di riferimento codificati. | CONDITIONING |
| `negative` | Il condizionamento negativo, ora contenente i dati dell'audio di riferimento codificati. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/it.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`

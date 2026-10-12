# Fish Audio Testo in voce

Questo nodo converte il testo scritto in audio parlato utilizzando i modelli text-to-speech di Fish Audio. Supporta indicazioni emotive incorporate nel testo ([happy], [whispering] su s2.1-pro; (happy) su s1) e dialoghi multi-voce tramite i tag @Voice1/@Voice2 quando sono collegate più voci. Sono disponibili due modelli: s2.1-pro, che supporta fino a cinque voci e dialoghi multi-voce, e s1, che utilizza un'unica voce opzionale.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `text` | Il testo da convertire in parlato. Con due o più voci collegate, contrassegna i cambi di parlante con @Voice1, @Voice2, ecc. (predefinito: vuoto) | STRING | Sì | Qualsiasi testo non vuoto |
| `model` | Modello da utilizzare per il text-to-speech. | DYNAMIC_COMBO | Sì | "s2.1-pro"<br>"s1" |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 42) | INT | Sì | da 0 a 2147483647 |

### Input di s2.1-pro

Questi input vengono visualizzati quando è selezionato il modello s2.1-pro.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `voices` | Slot espandibile: collega da 0 a 5 elementi voce (`voice_1`, `voice_2`, ...). Voci per la sintesi. Lascia vuoto per la voce predefinita. Con due o più voci, contrassegna i cambi di parlante nel testo con @Voice1, @Voice2, ecc. | FISHAUDIO_VOICE | No | da 0 a 5 voci |
| `temperature` | Espressività. Valori più alti sono più vari, valori più bassi più coerenti. (predefinito: 0.7) | FLOAT | Sì | da 0.0 a 1.0 |
| `top_p` | Diversità tramite campionamento nucleus. (predefinito: 0.7) | FLOAT | Sì | da 0.01 a 1.0 |
| `speed` | Velocità di parlato. 1.0 è normale, <1.0 più lento, >1.0 più veloce. (predefinito: 1.0) | FLOAT | Sì | da 0.5 a 2.0 |
| `volume` | Regolazione del volume in decibel. 0 indica nessuna modifica. (predefinito: 0.0) | FLOAT | Sì | da -10.0 a 10.0 |
| `normalize` | Normalizza numeri e testo per inglese e cinese, migliorando la stabilità per numeri e date. (predefinito: true) | BOOLEAN | Sì | true / false |

### Input di s1

Questi input vengono visualizzati quando è selezionato il modello s1.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `voice` | Voce per la sintesi. Lascia non collegato per la voce predefinita. | FISHAUDIO_VOICE | No | Voce singola opzionale |
| `temperature` | Espressività. Valori più alti sono più vari, valori più bassi più coerenti. (predefinito: 0.7) | FLOAT | Sì | da 0.0 a 1.0 |
| `top_p` | Diversità tramite campionamento nucleus. (predefinito: 0.7) | FLOAT | Sì | da 0.01 a 1.0 |
| `speed` | Velocità di parlato. 1.0 è normale, <1.0 più lento, >1.0 più veloce. (predefinito: 1.0) | FLOAT | Sì | da 0.5 a 2.0 |
| `volume` | Regolazione del volume in decibel. 0 indica nessuna modifica. (predefinito: 0.0) | FLOAT | Sì | da -10.0 a 10.0 |
| `normalize` | Normalizza numeri e testo per inglese e cinese, migliorando la stabilità per numeri e date. (predefinito: true) | BOOLEAN | Sì | true / false |

**Nota:** L'input `text` non deve essere vuoto. I tag del parlante (@Voice1, @Voice2, ecc.) non distinguono maiuscole e minuscole e devono riferirsi a una voce collegata; contrassegnare una voce non collegata genera un errore. Quando sono collegate due o più voci, il testo deve fare riferimento a ogni voce collegata almeno una volta, altrimenti il nodo segnala i tag mancanti. Su s2.1-pro, collegare 0 voci usa la voce predefinita, 1 voce usa quella voce da sola e 2 o più voci abilitano il dialogo multi-voce. Su s1, viene usata un'unica voce opzionale e, se non collegata, viene usata la voce predefinita. Le indicazioni emotive possono essere inserite nel testo: [happy] e [whispering] su s2.1-pro, e (happy) su s1.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `audio` | Il parlato generato come file audio. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/it.md)

---
**Source fingerprint (SHA-256):** `6cc005ae76fc7b60d9399b1b0a3c5de40a6eff47cd6f0f0b73b4212c0270ae29`

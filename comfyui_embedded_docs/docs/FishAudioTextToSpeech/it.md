# Fish Audio Testo in voce

Questo nodo converte il testo scritto in audio parlato utilizzando i modelli text-to-speech di Fish Audio. Supporta indicatori incorporati nel testo: [happy] e [whispering] su s2.1-pro, (happy) su s1, e [directions] in linguaggio naturale più tag di parola `<whisper>...</whisper>` su drama-3. Il dialogo multi-speaker utilizza i tag @Voice1/@Voice2 quando sono collegate più voci. Sono disponibili tre modelli: drama-3 e s2.1-pro, che supportano entrambi fino a cinque voci e il dialogo multi-speaker, e s1, che utilizza una singola voce opzionale.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `testo` | Il testo da convertire in parlato. Con due o più voci collegate, contrassegna i cambi di speaker con @Voice1, @Voice2, ecc. (predefinito: vuoto) | STRING | Sì | Qualsiasi testo non vuoto |
| `modello` | Modello da utilizzare per la sintesi vocale. | DYNAMIC_COMBO | Sì | "drama-3"<br>"s2.1-pro"<br>"s1" |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed. (predefinito: 42) | INT | Sì | 0 a 2147483647 |

### Input di drama-3 e s2.1-pro

Questi input vengono visualizzati quando è selezionato il modello `drama-3` o `s2.1-pro`. I set di parametri sono identici.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `voices` | Slot espandibile: collega da 0 a 5 elementi voce (`voice_1`, `voice_2`, ...). Voci per la sintesi. Lascia vuoto per una voce casuale. Con due o più voci, contrassegna i cambi di speaker nel testo con @Voice1, @Voice2, ecc. | FISHAUDIO_VOICE | No | da 0 a 5 voci |
| `temperature` | Espressività. Valori più alti sono più vari, valori più bassi sono più coerenti. (predefinito: 0.7) | FLOAT | Sì | 0.0 a 1.0 |
| `top_p` | Diversità tramite campionamento nucleus. (predefinito: 0.7) | FLOAT | Sì | 0.01 a 1.0 |
| `speed` | Velocità di parlato. 1.0 è normale, <1.0 più lento, >1.0 più veloce. (predefinito: 1.0) | FLOAT | Sì | 0.5 a 2.0 |
| `volume` | Regolazione del volume in decibel. 0 indica nessuna modifica. (predefinito: 0.0) | FLOAT | Sì | -10.0 a 10.0 |
| `normalize` | Normalizza numeri e testo per inglese e cinese, migliorando la stabilità per numeri e date. (predefinito: true) | BOOLEAN | Sì | true / false |

### Input di s1

Questi input vengono visualizzati quando è selezionato il modello s1.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `voice` | Voce per la sintesi. Lascia scollegato per una voce casuale. | FISHAUDIO_VOICE | No | Voce singola opzionale |
| `temperature` | Espressività. Valori più alti sono più vari, valori più bassi sono più coerenti. (predefinito: 0.7) | FLOAT | Sì | 0.0 a 1.0 |
| `top_p` | Diversità tramite campionamento nucleus. (predefinito: 0.7) | FLOAT | Sì | 0.01 a 1.0 |
| `speed` | Velocità di parlato. 1.0 è normale, <1.0 più lento, >1.0 più veloce. (predefinito: 1.0) | FLOAT | Sì | 0.5 a 2.0 |
| `volume` | Regolazione del volume in decibel. 0 indica nessuna modifica. (predefinito: 0.0) | FLOAT | Sì | -10.0 a 10.0 |
| `normalize` | Normalizza numeri e testo per inglese e cinese, migliorando la stabilità per numeri e date. (predefinito: true) | BOOLEAN | Sì | true / false |

**Nota:** L'input `text` non deve essere vuoto. I tag speaker (@Voice1, @Voice2, ecc.) non distinguono maiuscole/minuscole e devono fare riferimento a una voce collegata; assegnare un tag a una voce non collegata genera un errore. Quando sono collegate due o più voci, il testo deve fare riferimento a ogni voce collegata almeno una volta, altrimenti il nodo segnala i tag mancanti. Su drama-3 e s2.1-pro, collegare 0 voci usa una voce casuale, 1 voce usa solo quella voce e 2 o più voci abilitano il dialogo multi-speaker. Su s1, viene utilizzata una singola voce opzionale e lasciarla non collegata usa una voce casuale. Gli indicatori possono essere inseriti nel testo: [happy] e [whispering] su s2.1-pro, (happy) su s1, e [directions] in linguaggio naturale e tag di parola `<whisper>...</whisper>` su drama-3.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `audio` | Il parlato generato come file audio. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/it.md)

---
**Source fingerprint (SHA-256):** `adcfe8f994b8fbe07efb3dd3f86c8955ea3cec62cc3f0321efd2b63c0470b7a3`

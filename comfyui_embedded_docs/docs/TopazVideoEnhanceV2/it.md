# Topaz Video Enhance

Il nodo **Topaz Video Enhance V2** dà nuova vita al video con una potente tecnologia di upscaling e recupero. Può aumentare la risoluzione di un video utilizzando diversi modelli di upscaler Topaz, regolare la frequenza dei fotogrammi tramite interpolazione dei fotogrammi e applicare impostazioni di potenziamento creative o realistiche.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Il video di input da elaborare. Deve essere in formato contenitore MP4. | VIDEO | Sì | - |
| `upscaler_model` | Il modello AI utilizzato per eseguire l'upscaling del video. I sottoparametri disponibili dipendono dal modello selezionato. Selezionando `"Disabled"` si disabilita l'upscaling. | DYNAMIC_COMBO | Sì | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` |
| `interpolation_model` | Il modello AI utilizzato per l'interpolazione dei fotogrammi. I sottoparametri disponibili dipendono dal modello selezionato. Selezionando `"Disabled"` si disabilita l'interpolazione. | DYNAMIC_COMBO | Sì | `"Disabled"`<br>`"apo-8"` |
| `dynamic_compression_level` | Livello CQP utilizzato per la compressione video (predefinito: `"Low"`). | COMBO | No | `"Low"`<br>`"Mid"`<br>`"High"` |

Le sezioni seguenti descrivono i sottoparametri visualizzati per ciascuna opzione dei selettori `upscaler_model` e `interpolation_model`. Le opzioni `"Disabled"` non mostrano parametri aggiuntivi.

### Input di Astra 2

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Risoluzione di output desiderata per l'upscaling. | COMBO | Sì (quando è selezionato "Astra 2") | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Intensità creativa dell'upscaling (predefinito: 0.5). | FLOAT | No | 0.0 a 1.0 (passo 0.1) |
| `upscaler_model.prompt` | Prompt facoltativo descrittivo (non istruttivo) della scena. Quando impostato, limita l'input a 450 fotogrammi (~15 s a 30 fps) (predefinito: vuoto). | STRING | No | - |
| `upscaler_model.sharp` | Nitidezza di pre-potenziamento: 0.0=sfocatura gaussiana, 0.5=passthrough (predefinito), 1.0=nitidezza USM. | FLOAT | No | 0.0 a 1.0 (passo 0.01) |
| `upscaler_model.realism` | Spinge l'output verso il realismo fotografico. Lasciare a 0 per usare il valore predefinito del modello (predefinito: 0.0). | FLOAT | No | 0.0 a 1.0 (passo 0.01) |

### Input di Starlight (Astra) Fast

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Risoluzione di output desiderata per l'upscaling. | COMBO | Sì (quando questo modello è selezionato) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### Input di Starlight (Astra) Creative

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Risoluzione di output desiderata per l'upscaling. | COMBO | Sì (quando questo modello è selezionato) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Intensità creativa dell'upscaling (predefinito: `"low"`). | COMBO | No | `"low"`<br>`"middle"`<br>`"high"` |

### Input di Starlight Precise 2.5

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Risoluzione di output desiderata per l'upscaling. | COMBO | Sì (quando questo modello è selezionato) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### Input di apo-8

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `interpolation_model.interpolation_frame_rate` | Frequenza dei fotogrammi di output (predefinita: 60). | INT | Sì (quando è selezionato "apo-8") | 15 a 240 |
| `interpolation_model.interpolation_slowmo` | Fattore di slow-motion applicato al video di input. Ad esempio, 2 rende l'output due volte più lento e raddoppia la durata (predefinito: 1). | INT | No | 1 a 16 |
| `interpolation_model.interpolation_duplicate` | Analizza l'input per individuare fotogrammi duplicati e li rimuove (predefinito: False). | BOOLEAN | No | True<br>False |
| `interpolation_model.interpolation_duplicate_threshold` | Sensibilità di rilevamento per fotogrammi duplicati (predefinito: 0.01). | FLOAT | No | 0.001 a 0.1 (passo 0.001) |

**Vincoli importanti:**

- Almeno uno tra `upscaler_model` e `interpolation_model` deve essere abilitato. Se entrambi sono impostati su `"Disabled"`, il nodo genera un errore perché non c'è nulla da elaborare.
- L'input `video` deve essere in formato contenitore MP4.
- Il modello `"Astra 2"` è limitato a 9000 fotogrammi di input. Quando è impostato un `prompt`, il limite è di 450 fotogrammi di input (~15 secondi a 30 fps). Il nodo genera un errore se il video supera il limite applicabile.
- `upscaler_model.upscaler_resolution` è obbligatorio ogni volta che viene selezionato un modello di upscaler diverso da `"Disabled"`. `"FullHD (1080p)"` punta a un risultato 1080p e `"4K (2160p)"` punta a un risultato 2160p; la larghezza e l'altezza esatte dell'output vengono calcolate dal rapporto d'aspetto dell'input, limitate a un lato lungo massimo di 1920 o 3840 pixel rispettivamente, e arrotondate a un numero pari.
- `interpolation_model.interpolation_frame_rate` è obbligatorio ogni volta che `interpolation_model` è `"apo-8"`.
- I file molto grandi non sono attualmente supportati; i caricamenti sono limitati a una singola parte, altrimenti il nodo genera un errore.
- Diversi parametri (`sharp`, `realism`, `interpolation_slowmo`, `interpolation_duplicate`, `interpolation_duplicate_threshold`) sono contrassegnati come avanzati nell'interfaccia utente e potrebbero essere nascosti per impostazione predefinita.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il video potenziato dopo l'applicazione dei filtri di upscaling e/o interpolazione selezionati. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/it.md)

---
**Source fingerprint (SHA-256):** `14627dc772a6a46a645517bd34b545e0986a84561e24bdfe810b67f791ee47e3`

# GeminiNodeV2

Genera risposte testuali con i modelli Gemini di Google. Fornisci un prompt testuale e, facoltativamente, una o più immagini, clip audio, video o file come contesto multimodale. Il nodo invia il prompt e qualsiasi media allegato al modello selezionato e restituisce la risposta testuale del modello.

**Nota:** questo nodo è contrassegnato come deprecato nel codice sorgente.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `model` | Il modello Gemini utilizzato per generare la risposta. Selezionando un modello, vengono mostrati i relativi input qui sotto. | DYNAMIC_COMBO | Sì | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `prompt` | Input testuale per il modello. Includere istruzioni dettagliate, domande o contesto. (predefinito: "") | STRING | Sì | Deve contenere almeno un carattere non di spaziatura |
| `seed` | Seme per il campionamento. Imposta a 0 per un seme casuale. L'output deterministico non è garantito. (predefinito: 42) | INT | Sì | da 0 a 2147483647 |
| `system_prompt` | Istruzioni di base che determinano il comportamento del modello. (predefinito: "") | STRING | No |  |

### Input di Gemini 3.8 Flash

Questi input vengono visualizzati quando `model` è impostato su `"Gemini 3.8 Flash"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `thinking_level` | Quanto intensamente il modello ragiona internamente prima di rispondere. HIGH migliora la qualità su attività difficili, ma consuma più token (di ragionamento) ed è più lento. (predefinito: "MEDIUM") | COMBO | Sì | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `max_output_tokens` | Numero massimo di token da generare, incluso il ragionamento interno del modello. Con thinking_level HIGH, un valore basso può non lasciare spazio alla risposta; aumenta questo valore se le risposte risultano vuote o troncate. Il modello si arresta in anticipo quando ha terminato, quindi un limite più alto non comporta costi aggiuntivi per le risposte brevi. (predefinito: 32768) | INT | Sì | da 16 a 65536 |

**Nota:** questo modello non espone i controlli di campionamento `temperature` o `top_p`.

### Input di Gemini 3.7 Flash

Questi input vengono visualizzati quando `model` è impostato su `"Gemini 3.7 Flash"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `thinking_level` | Quanto intensamente il modello ragiona internamente prima di rispondere. HIGH migliora la qualità su attività difficili, ma consuma più token (di ragionamento) ed è più lento. (predefinito: "MEDIUM") | COMBO | Sì | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Controlla la casualità. Valori più bassi sono più focalizzati/deterministici, valori più alti sono più creativi. (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 2.0 |
| `top_p` | Campionamento nucleus: campiona dal più piccolo insieme di token la cui probabilità cumulativa raggiunge top_p. (predefinito: 0.95) | FLOAT | Sì | da 0.0 a 1.0 |
| `max_output_tokens` | Numero massimo di token da generare, incluso il ragionamento interno del modello. Con thinking_level HIGH, un valore basso può non lasciare spazio alla risposta; aumenta questo valore se le risposte risultano vuote o troncate. Il modello si arresta in anticipo quando ha terminato, quindi un limite più alto non comporta costi aggiuntivi per le risposte brevi. (predefinito: 32768) | INT | Sì | da 16 a 65536 |

### Input di Gemini 3.5 Flash

Questi input vengono visualizzati quando `model` è impostato su `"Gemini 3.5 Flash"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `thinking_level` | Quanto intensamente il modello ragiona internamente prima di rispondere. HIGH migliora la qualità su attività difficili, ma consuma più token (di ragionamento) ed è più lento. (predefinito: "MEDIUM") | COMBO | Sì | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Controlla la casualità. Valori più bassi sono più focalizzati/deterministici, valori più alti sono più creativi. (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 2.0 |
| `top_p` | Campionamento nucleus: campiona dal più piccolo insieme di token la cui probabilità cumulativa raggiunge top_p. (predefinito: 0.95) | FLOAT | Sì | da 0.0 a 1.0 |
| `max_output_tokens` | Numero massimo di token da generare, incluso il ragionamento interno del modello. Con thinking_level HIGH, un valore basso può non lasciare spazio alla risposta; aumenta questo valore se le risposte risultano vuote o troncate. Il modello si arresta in anticipo quando ha terminato, quindi un limite più alto non comporta costi aggiuntivi per le risposte brevi. (predefinito: 32768) | INT | Sì | da 16 a 65536 |

### Input di Gemini 3.1 Pro

Questi input vengono visualizzati quando `model` è impostato su `"Gemini 3.1 Pro"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `thinking_level` | Quanto intensamente il modello ragiona internamente prima di rispondere. HIGH migliora la qualità su attività difficili, ma consuma più token (di ragionamento) ed è più lento. (predefinito: "HIGH") | COMBO | Sì | `"LOW"`<br>`"HIGH"` |
| `temperature` | Controlla la casualità. Valori più bassi sono più focalizzati/deterministici, valori più alti sono più creativi. (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 2.0 |
| `top_p` | Campionamento nucleus: campiona dal più piccolo insieme di token la cui probabilità cumulativa raggiunge top_p. (predefinito: 0.95) | FLOAT | Sì | da 0.0 a 1.0 |
| `max_output_tokens` | Numero massimo di token da generare, incluso il ragionamento interno del modello. Con thinking_level HIGH, un valore basso può non lasciare spazio alla risposta; aumenta questo valore se le risposte risultano vuote o troncate. Il modello si arresta in anticipo quando ha terminato, quindi un limite più alto non comporta costi aggiuntivi per le risposte brevi. (predefinito: 32768) | INT | Sì | da 16 a 65536 |

### Input di Gemini 3.1 Flash-Lite

Questi input vengono visualizzati quando `model` è impostato su `"Gemini 3.1 Flash-Lite"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `thinking_level` | Quanto intensamente il modello ragiona internamente prima di rispondere. HIGH migliora la qualità su attività difficili, ma consuma più token (di ragionamento) ed è più lento. (predefinito: "LOW") | COMBO | Sì | `"LOW"`<br>`"HIGH"` |
| `temperature` | Controlla la casualità. Valori più bassi sono più focalizzati/deterministici, valori più alti sono più creativi. (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 2.0 |
| `top_p` | Campionamento nucleus: campiona dal più piccolo insieme di token la cui probabilità cumulativa raggiunge top_p. (predefinito: 0.95) | FLOAT | Sì | da 0.0 a 1.0 |
| `max_output_tokens` | Numero massimo di token da generare, incluso il ragionamento interno del modello. Con thinking_level HIGH, un valore basso può non lasciare spazio alla risposta; aumenta questo valore se le risposte risultano vuote o troncate. Il modello si arresta in anticipo quando ha terminato, quindi un limite più alto non comporta costi aggiuntivi per le risposte brevi. (predefinito: 32768) | INT | Sì | da 16 a 65536 |

### Input di media e file

I seguenti input sono condivisi da tutti i modelli e vengono visualizzati insieme agli input specifici del modello.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `images` | Slot espandibile: collega da 1 a 16 immagini (`image_1` ... `image_16`). Immagini facoltative da usare come contesto per il modello. Fino a 16 immagini. | IMAGE | No | da 0 a 16 immagini |
| `audio` | Slot espandibile: collega una clip audio (`audio_1`). Clip audio facoltativa da usare come contesto per il modello. | AUDIO | No | da 0 a 1 clip |
| `video` | Slot espandibile: collega una clip video (`video_1`). Clip video facoltativa da usare come contesto per il modello. | VIDEO | No | da 0 a 1 clip |
| `files` | File facoltativi da usare come contesto per il modello. Accetta input dal nodo Gemini Input Files. | GEMINI_INPUT_FILES | No |  |

**Nota:** quando vengono allegati media (immagini, audio o video), il nodo carica i primi 10 elementi multimediali nello storage ComfyAPI e li passa come URL; questo budget di URL è condiviso tra tutti i tipi di media e viene consumato in ordine (prima video, poi audio, poi immagini). Eventuali media rimanenti vengono codificati inline come dati base64, con un payload inline combinato massimo di 18 MB. Se il payload inline supera 18 MB, il nodo genera un errore. Il parametro `prompt` deve contenere almeno un carattere non di spaziatura. Impostando `seed` su 0 si richiede un seme casuale.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | La risposta testuale generata dal modello Gemini. Se il modello non produce testo, viene restituita la stringa "Empty response from Gemini model...". | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `8ae14c6465569695e1e99b0040cb2c745e5f3d9ddcd3b03013530dc7e7135b87`

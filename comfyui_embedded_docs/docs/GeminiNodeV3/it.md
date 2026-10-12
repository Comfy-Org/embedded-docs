# GeminiNodeV3

Genera risposte testuali con i modelli Gemini di Google. Fornisci un prompt testuale e, facoltativamente, una o più immagini, clip audio, video o file come contesto multimodale. Il modello selezionato determina quali impostazioni aggiuntive vengono visualizzate.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello Gemini utilizzato per generare la risposta. Il modello selezionato determina quali input aggiuntivi vengono mostrati. | DYNAMIC_COMBO | Sì | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |

### Input multimediali

Questi input multimediali espandibili sono disponibili per ogni opzione di modello.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Immagini opzionali da usare come contesto per il modello. Fino a 16 immagini. Slot espandibile: collega le immagini da `image_1` a `image_16`. | IMAGE | No | Fino a 16 immagini |
| `audio` | Clip audio opzionale da usare come contesto per il modello. Slot espandibile: `audio_1`. | AUDIO | No | 1 clip audio |
| `video` | Clip video opzionale da usare come contesto per il modello. Slot espandibile: `video_1`. | VIDEO | No | 1 clip video |

### Input di Gemini 3.8 Flash

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Input testuale per il modello. Includi istruzioni dettagliate, domande o contesto. Non deve essere vuoto. | STRING | Sì | Testo multilinea (deve contenere almeno un carattere diverso da spazi bianchi) |
| `video_processing` | Come il modello legge il video allegato. `static` campiona i fotogrammi a una frequenza fissa e li invia tutti come contesto; `agentic` consente al modello di esplorare autonomamente la sequenza temporale e caricare solo i fotogrammi, l'audio o la trascrizione di cui ha bisogno, il che comporta molti meno token di input sui video lunghi. | COMBO | Sì | `"static"`<br>`"agentic"` (predefinito: `"static"`) |
| `files` | File opzionali da usare come contesto per il modello. Accetta input dal nodo Gemini Input Files. | GEMINI_INPUT_FILES | No | N/A |
| `thinking_level` | Quanto intensamente il modello ragiona internamente prima di rispondere. HIGH migliora la qualità nelle attività difficili, ma consuma più token (di ragionamento) ed è più lento. | COMBO | Sì | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (predefinito: `"MEDIUM"`) |
| `max_output_tokens` | Numero massimo di token da generare, inclusi i ragionamenti interni del modello. Con thinking_level HIGH, un valore basso può non lasciare spazio alla risposta; aumenta questo valore se le risposte risultano vuote o troncate. Il modello si arresta prima quando ha finito, quindi un limite più alto non comporta costi aggiuntivi per risposte brevi. | INT | Sì | 16-65536 (predefinito: 32768) |
| `seed` | Seme per il campionamento. Imposta a 0 per un seme casuale. L'output deterministico non è garantito. | INT | Sì | 0-2147483647 (predefinito: 42) |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento del modello. | STRING | Sì | Testo multilinea (predefinito: vuoto) |

### Input di Gemini 3.7 Flash

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Input testuale per il modello. Includi istruzioni dettagliate, domande o contesto. Non deve essere vuoto. | STRING | Sì | Testo multilinea (deve contenere almeno un carattere diverso da spazi bianchi) |
| `files` | File opzionali da usare come contesto per il modello. Accetta input dal nodo Gemini Input Files. | GEMINI_INPUT_FILES | No | N/A |
| `thinking_level` | Quanto intensamente il modello ragiona internamente prima di rispondere. HIGH migliora la qualità nelle attività difficili, ma consuma più token (di ragionamento) ed è più lento. | COMBO | Sì | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (predefinito: `"MEDIUM"`) |
| `temperature` | Controlla la casualità. Valori più bassi sono più focalizzati/deterministici, valori più alti sono più creativi. | FLOAT | Sì | 0.0-2.0 (predefinito: 1.0) |
| `top_p` | Campionamento nucleus: campiona dal più piccolo insieme di token la cui probabilità cumulativa raggiunge top_p. | FLOAT | Sì | 0.0-1.0 (predefinito: 0.95) |
| `max_output_tokens` | Numero massimo di token da generare, inclusi i ragionamenti interni del modello. Con thinking_level HIGH, un valore basso può non lasciare spazio alla risposta; aumenta questo valore se le risposte risultano vuote o troncate. Il modello si arresta prima quando ha finito, quindi un limite più alto non comporta costi aggiuntivi per risposte brevi. | INT | Sì | 16-65536 (predefinito: 32768) |
| `seed` | Seme per il campionamento. Imposta a 0 per un seme casuale. L'output deterministico non è garantito. | INT | Sì | 0-2147483647 (predefinito: 42) |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento del modello. | STRING | Sì | Testo multilinea (predefinito: vuoto) |

### Input di Gemini 3.5 Flash

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Input testuale per il modello. Includi istruzioni dettagliate, domande o contesto. Non deve essere vuoto. | STRING | Sì | Testo multilinea (deve contenere almeno un carattere diverso da spazi bianchi) |
| `files` | File opzionali da usare come contesto per il modello. Accetta input dal nodo Gemini Input Files. | GEMINI_INPUT_FILES | No | N/A |
| `thinking_level` | Quanto intensamente il modello ragiona internamente prima di rispondere. HIGH migliora la qualità nelle attività difficili, ma consuma più token (di ragionamento) ed è più lento. | COMBO | Sì | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` (predefinito: `"MEDIUM"`) |
| `temperature` | Controlla la casualità. Valori più bassi sono più focalizzati/deterministici, valori più alti sono più creativi. | FLOAT | Sì | 0.0-2.0 (predefinito: 1.0) |
| `top_p` | Campionamento nucleus: campiona dal più piccolo insieme di token la cui probabilità cumulativa raggiunge top_p. | FLOAT | Sì | 0.0-1.0 (predefinito: 0.95) |
| `max_output_tokens` | Numero massimo di token da generare, inclusi i ragionamenti interni del modello. Con thinking_level HIGH, un valore basso può non lasciare spazio alla risposta; aumenta questo valore se le risposte risultano vuote o troncate. Il modello si arresta prima quando ha finito, quindi un limite più alto non comporta costi aggiuntivi per risposte brevi. | INT | Sì | 16-65536 (predefinito: 32768) |
| `seed` | Seme per il campionamento. Imposta a 0 per un seme casuale. L'output deterministico non è garantito. | INT | Sì | 0-2147483647 (predefinito: 42) |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento del modello. | STRING | Sì | Testo multilinea (predefinito: vuoto) |

### Input di Gemini 3.1 Pro

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Input testuale per il modello. Includi istruzioni dettagliate, domande o contesto. Non deve essere vuoto. | STRING | Sì | Testo multilinea (deve contenere almeno un carattere diverso da spazi bianchi) |
| `files` | File opzionali da usare come contesto per il modello. Accetta input dal nodo Gemini Input Files. | GEMINI_INPUT_FILES | No | N/A |
| `thinking_level` | Quanto intensamente il modello ragiona internamente prima di rispondere. HIGH migliora la qualità nelle attività difficili, ma consuma più token (di ragionamento) ed è più lento. | COMBO | Sì | `"LOW"`<br>`"HIGH"` (predefinito: `"HIGH"`) |
| `temperature` | Controlla la casualità. Valori più bassi sono più focalizzati/deterministici, valori più alti sono più creativi. | FLOAT | Sì | 0.0-2.0 (predefinito: 1.0) |
| `top_p` | Campionamento nucleus: campiona dal più piccolo insieme di token la cui probabilità cumulativa raggiunge top_p. | FLOAT | Sì | 0.0-1.0 (predefinito: 0.95) |
| `max_output_tokens` | Numero massimo di token da generare, inclusi i ragionamenti interni del modello. Con thinking_level HIGH, un valore basso può non lasciare spazio alla risposta; aumenta questo valore se le risposte risultano vuote o troncate. Il modello si arresta prima quando ha finito, quindi un limite più alto non comporta costi aggiuntivi per risposte brevi. | INT | Sì | 16-65536 (predefinito: 32768) |
| `seed` | Seme per il campionamento. Imposta a 0 per un seme casuale. L'output deterministico non è garantito. | INT | Sì | 0-2147483647 (predefinito: 42) |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento del modello. | STRING | Sì | Testo multilinea (predefinito: vuoto) |

### Input di Gemini 3.1 Flash-Lite

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Input testuale per il modello. Includi istruzioni dettagliate, domande o contesto. Non deve essere vuoto. | STRING | Sì | Testo multilinea (deve contenere almeno un carattere diverso da spazi bianchi) |
| `files` | File opzionali da usare come contesto per il modello. Accetta input dal nodo Gemini Input Files. | GEMINI_INPUT_FILES | No | N/A |
| `thinking_level` | Quanto intensamente il modello ragiona internamente prima di rispondere. HIGH migliora la qualità nelle attività difficili, ma consuma più token (di ragionamento) ed è più lento. | COMBO | Sì | `"LOW"`<br>`"HIGH"` (predefinito: `"LOW"`) |
| `temperature` | Controlla la casualità. Valori più bassi sono più focalizzati/deterministici, valori più alti sono più creativi. | FLOAT | Sì | 0.0-2.0 (predefinito: 1.0) |
| `top_p` | Campionamento nucleus: campiona dal più piccolo insieme di token la cui probabilità cumulativa raggiunge top_p. | FLOAT | Sì | 0.0-1.0 (predefinito: 0.95) |
| `max_output_tokens` | Numero massimo di token da generare, inclusi i ragionamenti interni del modello. Con thinking_level HIGH, un valore basso può non lasciare spazio alla risposta; aumenta questo valore se le risposte risultano vuote o troncate. Il modello si arresta prima quando ha finito, quindi un limite più alto non comporta costi aggiuntivi per risposte brevi. | INT | Sì | 16-65536 (predefinito: 32768) |
| `seed` | Seme per il campionamento. Imposta a 0 per un seme casuale. L'output deterministico non è garantito. | INT | Sì | 0-2147483647 (predefinito: 42) |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento del modello. | STRING | Sì | Testo multilinea (predefinito: vuoto) |

Nota: per Gemini 3.8 Flash, `temperature` e `top_p` non sono disponibili, e `video_processing` è disponibile solo per questa opzione di modello. Le opzioni e il valore predefinito di `thinking_level` variano in base al modello, come elencato sopra.

Nota: l'input `prompt` non deve essere vuoto. Il nodo verifica che contenga almeno un carattere diverso da spazi bianchi.

Nota: il nodo carica fino ai primi 10 elementi multimediali come URL, dando priorità a video, poi audio, poi immagini. Gli eventuali elementi multimediali rimanenti vengono inviati inline come base64. Il totale dei contenuti multimediali inline è limitato a 18 MB; se viene superato, il nodo genera un errore che invita a ridurre il numero o le dimensioni dei contenuti multimediali allegati.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `STRING` | La risposta testuale generata dal modello Gemini selezionato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV3/it.md)

---
**Source fingerprint (SHA-256):** `d04d1e97a9c213297899291ad30db14a9f946b07506d0377fead4e29510c5ad9`

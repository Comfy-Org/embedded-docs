# Nano Banana 2

Questo nodo genera o modifica immagini inviando un prompt testuale all'API Vertex AI di Google tramite i modelli di immagini Gemini. Crea nuove immagini da una descrizione o modifica immagini esistenti usando immagini di riferimento opzionali.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Seleziona il modello di immagini Gemini da usare. Il modello scelto determina le opzioni di risoluzione disponibili e gli input specifici del modello. | DYNAMIC_COMBO | Sì | `"Gemini Nano Banana 2.1"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `prompt` | Prompt testuale che descrive l'immagine da generare o le modifiche da applicare. Includi eventuali vincoli, stili o dettagli che il modello deve seguire. Non deve essere vuoto. (predefinito: vuoto) | STRING | Sì | N/A |
| `seed` | Quando il seed è fissato a un valore specifico, il modello compie il massimo sforzo per fornire la stessa risposta a richieste ripetute. Non è garantito un output deterministico. Inoltre, cambiare il modello o le impostazioni dei parametri, come la temperatura, può causare variazioni nella risposta anche usando lo stesso valore di seed. Per impostazione predefinita, viene usato un valore di seed casuale. (predefinito: 42) | INT | Sì | da 0 a 18446744073709551615 |
| `response_modalities` | Determina il formato della risposta. IMAGE restituisce solo un'immagine; IMAGE+TEXT restituisce un'immagine e una risposta testuale. (predefinito: IMAGE) Parametro avanzato. | COMBO | Sì | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento di un'IA. Il valore predefinito è un prompt integrato che istruisce il modello a produrre sempre un'immagine. Parametro avanzato. | STRING | No | N/A |
| `temperature` | Controlla la casualità nella generazione. Valori più bassi sono più focalizzati/deterministici. (predefinito: 1.0) Parametro avanzato. | FLOAT | No | da 0.0 a 2.0 (passo 0.01) |
| `top_p` | Soglia di campionamento nucleus. Valori più bassi sono più focalizzati, più alti più diversificati. (predefinito: 0.95) Parametro avanzato. | FLOAT | No | da 0.0 a 1.0 (passo 0.01) |

### Input di Gemini Nano Banana 2.1

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Se impostato su 'auto', corrisponde alle proporzioni dell'immagine di input; se non viene fornita alcuna immagine, di solito viene generato un formato 16:9. (predefinito: auto) | COMBO | Sì | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Risoluzione di output desiderata. | COMBO | Sì | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | Seleziona il livello di pensiero usato dal modello. | COMBO | Sì | `"MINIMAL"`<br>`"MEDIUM"`<br>`"HIGH"` |

### Input di Nano Banana 2 (Gemini 3.1 Flash Image)

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Se impostato su 'auto', corrisponde alle proporzioni dell'immagine di input; se non viene fornita alcuna immagine, di solito viene generato un formato 16:9. (predefinito: auto) | COMBO | Sì | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Risoluzione di output desiderata. | COMBO | Sì | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | Seleziona il livello di pensiero usato dal modello. | COMBO | Sì | `"MINIMAL"`<br>`"HIGH"` |

### Input di Nano Banana 2 Lite

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Se impostato su 'auto', corrisponde alle proporzioni dell'immagine di input; se non viene fornita alcuna immagine, di solito viene generato un formato 16:9. (predefinito: auto) | COMBO | Sì | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Risoluzione di output desiderata. | COMBO | Sì | `"1K"` |
| `thinking_level` | Seleziona il livello di pensiero usato dal modello. | COMBO | Sì | `"MINIMAL"`<br>`"HIGH"` |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `images` | Immagini di riferimento opzionali. Fino a 14 immagini in totale. Slot espandibile: collega da `image_1` a `image_14`. | IMAGE | No | da 0 a 14 immagini |
| `files` | File opzionali da usare come contesto per il modello. Accetta input dal nodo Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | No | N/A |

**Nota:** È possibile collegare un massimo di 14 immagini di riferimento all'input `images`; superare questo limite genera un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `IMAGE` | L'immagine generata o modificata. | IMAGE |
| `STRING` | Una descrizione testuale o didascalia generata dal modello. Vuota quando non viene restituito testo, ad esempio quando `response_modalities` è impostato su `IMAGE`. | STRING |
| `thought_image` | Prima immagine dal processo di pensiero del modello. Disponibile solo con la modalità IMAGE+TEXT. | IMAGE |

**Nota:** L'output `STRING` è vuoto quando `response_modalities` è impostato su `IMAGE`. Se il modello non genera un'immagine in questa modalità, il nodo genera un errore suggerendo di passare a IMAGE+TEXT per visualizzare il ragionamento del modello.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/it.md)

---
**Source fingerprint (SHA-256):** `238d661259e99fd0ce8cae227d873713bbad60aa5eccb32447be464317e39ddd`

# Recraft V4 Da Testo a Immagine

Genera immagini da prompt testuali utilizzando i modelli Recraft V4 e V4.1. Invia il prompt e le impostazioni selezionate all'API Recraft e restituisce l'immagine o le immagini generate. Se vengono utilizzate immagini di riferimento di stile, viene restituito anche l'ID dello stile creato.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello da utilizzare per la generazione. I modelli recraftv4_styles sono progettati per una generazione coerente con lo stile e richiedono sempre uno style_id o style_references. `recraftv4_1_flash` è il modello più veloce ed economico e non supporta alcuno stile. | DYNAMIC_COMBO | Sì | "recraftv4_1"<br>"recraftv4_1_flash"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | Prompt per la generazione dell'immagine. Massimo 10.000 caratteri. | STRING | Sì | da 1 a 10000 caratteri |
| `negative_prompt` | Questo input viene ignorato: il prompt negativo non è supportato dai modelli Recraft V4 e V4.1. | STRING | Sì | N/A |
| `n` | Il numero di immagini da generare (predefinito: 1). | INT | Sì | 1 a 6 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seed (predefinito: 0). | INT | Sì | 0 a 18446744073709551615 |
| `recraft_controls` | Controlli aggiuntivi opzionali sulla generazione tramite il nodo Recraft Controls. | CUSTOM | No | N/A |
| `style_id` | UUID di uno stile Recraft V4 da applicare, ad es. dal nodo Recraft V4 Create Style o dall'output style_id di un'esecuzione precedente. Non può essere combinato con style_references (predefinito: vuoto). | STRING | No | Stringa UUID valida |
| `style_match` | Quanto fedelmente seguire lo stile: preciso lo riproduce nei dettagli, flessibile corrisponde all'aspetto generale. Utilizzato solo quando viene fornito uno stile (predefinito: "precise"). | COMBO | No | "precise"<br>"flexible" |

### Input di recraftv4_1, recraftv4_1_flash, recraftv4_1_utility, recraftv4 e recraftv4_styles

Questi modelli condividono lo stesso parametro `size`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size` | La dimensione dell'immagine generata (predefinito: "1024x1024"). | COMBO | Sì | Molteplici opzioni disponibili (dimensioni standard Recraft V4; include "1024x1024") |

### Input di recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro e recraftv4_styles_pro

Questi modelli condividono lo stesso parametro `size`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size` | La dimensione dell'immagine generata (predefinito: "2048x2048"). | COMBO | Sì | Molteplici opzioni disponibili (dimensioni pro Recraft V4; include "2048x2048") |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `style_references` | Immagini di riferimento per creare uno stile al volo, fatturate in aggiunta alla generazione. Lo stile creato viene restituito come style_id per il riutilizzo. Non può essere combinato con style_id. Slot espandibile: collega da 1 a N immagini (style_reference_1, style_reference_2, ...). | IMAGE | No | da 0 al numero massimo di immagini di riferimento consentite dall'API Recraft; la dimensione totale codificata non deve superare i 10 MB |

**Nota:** Il parametro `size` è un input dinamico le cui opzioni disponibili cambiano in base al `model` selezionato. I modelli `recraftv4_styles` e `recraftv4_styles_pro` richiedono sempre uno stile: collega immagini di riferimento di stile o fornisci uno `style_id`. Gli input `style_id` e `style_references` sono mutuamente esclusivi — fornisci solo uno di essi. Uno `style_id` deve essere un UUID valido. L'input `style_match` viene utilizzato solo quando viene fornito uno stile. Le immagini di riferimento di stile vengono fatturate in aggiunta alla generazione e la loro dimensione totale codificata non deve superare i 10 MB. Il valore `seed` non garantisce output di immagini riproducibili. Se utilizzi un ID stile dalla Infinite Style Library, assicurati che non sia uno stile Vector art, poiché potrebbe restituire dati SVG anziché un'immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | L'immagine generata o il batch di immagini. | IMAGE |
| `style_id` | L'ID dello stile utilizzato o creato da questa generazione. Quando vengono fornite immagini di riferimento di stile, lo stile creato viene restituito qui per il riutilizzo; stringa vuota quando non viene utilizzato alcuno stile. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/it.md)

---
**Source fingerprint (SHA-256):** `690286e663f27b525e58f81a7f883e490dacd48c1a34ee7b8e9ad4efd9935ff1`

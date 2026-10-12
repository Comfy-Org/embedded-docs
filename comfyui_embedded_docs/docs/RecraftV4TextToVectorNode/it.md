# Recraft V4 Da Testo a Vettore

Il nodo Recraft V4 Text to Vector genera illustrazioni Scalable Vector Graphics (SVG) a partire da una descrizione testuale utilizzando i modelli Recraft V4 e V4.1. Si connette all'API Recraft per generare uno o più file SVG in base al prompt e può applicare uno stile vettoriale esistente o crearne uno nuovo da immagini di riferimento — quando vengono utilizzate immagini di riferimento, lo stile creato viene restituito come `style_id` per il riutilizzo.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello da usare per la generazione. I modelli recraftv4_styles sono progettati per una generazione coerente con lo stile e richiedono sempre uno style_id o style_references. La selezione di un modello modifica le opzioni `size` disponibili. | DYNAMIC_COMBO | Sì | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"`<br>`"recraftv4_styles_vector"`<br>`"recraftv4_styles_pro_vector"` |
| `prompt` | Prompt per la generazione dell'immagine. Massimo 10.000 caratteri. | STRING | Sì | N/A |
| `negative_prompt` | Questo input viene ignorato: il prompt negativo non è supportato dai modelli Recraft V4 e V4.1. | STRING | Sì | N/A |
| `n` | Il numero di immagini da generare (predefinito: 1). | INT | Sì | Da 1 a 6 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi non sono deterministici indipendentemente dal seed (predefinito: 0). | INT | Sì | Da 0 a 18446744073709551615 |
| `recraft_controls` | Controlli aggiuntivi opzionali sulla generazione tramite il nodo Recraft Controls. | CUSTOM | No | N/A |
| `style_id` | UUID di uno stile vettoriale Recraft V4 da applicare, ad es. dal nodo Recraft V4 Create Style o dall'output style_id di un'esecuzione precedente. Non può essere combinato con style_references. | STRING | No | N/A |
| `style_match` | Quanto fedelmente seguire lo stile: precise lo riproduce in dettaglio, flexible corrisponde all'aspetto generale. Usato solo quando viene fornito uno stile (predefinito: "precise"). | COMBO | No | `"precise"`<br>`"flexible"` |

### Input di recraftv4_1_vector, recraftv4_1_utility_vector, recraftv4 e recraftv4_styles_vector

Questi modelli condividono le stesse opzioni `size`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `size` | La dimensione dell'immagine generata. Il valore predefinito è `"1024x1024"`. | COMBO | Sì | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### Input di recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector, recraftv4_pro e recraftv4_styles_pro_vector

Questi modelli condividono le stesse opzioni `size`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `size` | La dimensione dell'immagine generata. Il valore predefinito è `"2048x2048"`. | COMBO | Sì | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Immagini di riferimento per creare al volo uno stile vettoriale, fatturate in aggiunta alla generazione. Lo stile creato viene restituito come style_id per il riutilizzo. Non può essere combinato con style_id. | IMAGE | No | Slot espandibile: collega 1..N immagini di riferimento (fino al massimo del nodo) |

**Nota:** Il parametro `size` è un input dinamico le cui opzioni disponibili cambiano in base al `model` selezionato. Il valore `seed` non garantisce risultati riproducibili dall'API esterna. I modelli `recraftv4_styles_vector` e `recraftv4_styles_pro_vector` richiedono sempre uno stile: fornisci uno `style_id` o collega almeno un'immagine a `style_references`. `style_id` e `style_references` non possono essere usati insieme — fornirli entrambi genera un errore, e `style_id` deve essere un UUID valido. Le immagini di riferimento per lo stile sono limitate in numero e la loro dimensione totale codificata non deve superare 10 MB.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `output` | L'immagine o le immagini Scalable Vector Graphics (SVG) generate. | SVG |
| `style_id` | UUID dello stile restituito dall'API Recraft. Quando vengono fornite immagini di riferimento, lo stile creato viene restituito qui per il riutilizzo; altrimenti una stringa vuota. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/it.md)

---
**Source fingerprint (SHA-256):** `182a40b206b164cf2e96c7344d23e4906b7d61b90e3000743a3fd31941e08539`

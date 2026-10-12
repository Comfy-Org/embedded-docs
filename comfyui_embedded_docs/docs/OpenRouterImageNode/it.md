# OpenRouterImageNode

Questo nodo genera o modifica immagini tramite OpenRouter utilizzando i modelli MAI-Image-2.6 di Microsoft. Supporta la generazione da testo a immagine e la modifica guidata da immagini con un massimo di cinque immagini di riferimento, in sette rapporti d'aspetto a risoluzione 1K o 1.5K.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello di immagini OpenRouter utilizzato per generare l'immagine. Selezionando un modello vengono mostrate le opzioni specifiche del modello elencate di seguito. | DYNAMIC_COMBO | Sì | `microsoft/mai-image-2.6`<br>`microsoft/mai-image-2.6-flash` |

### Input di Mai Image 2.6 e Mai Image 2.6 Flash

Condivisi da entrambe le opzioni di modello (`microsoft/mai-image-2.6` e `microsoft/mai-image-2.6-flash`), che espongono lo stesso insieme di parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrive l'immagine da generare, oppure la modifica da applicare alle immagini di riferimento. Fino a 20000 caratteri. Predefinito: `""` (vuoto). Sono richiesti almeno 1 carattere dopo aver rimosso gli spazi bianchi circostanti. | STRING | Sì | Da 1 a 20000 caratteri |
| `aspect_ratio` | Rapporto d'aspetto dell'immagine generata, applicato anche quando sono collegate immagini di riferimento. Predefinito: `"1:1"`. `"auto"` lascia che il modello scelga il rapporto per testo a immagine (renderizzato alla dimensione 1.5K) e mantiene il rapporto d'aspetto della prima immagine di riferimento durante la modifica. | COMBO | Sì | `"1:1"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"auto"` |
| `resolution` | Livello di dimensione dell'output. 1K corrisponde a circa 1 megapixel (1:1 è 1024x1024, 16:9 è 1360x768); 1.5K corrisponde a circa 2,3 megapixel (1:1 è 1536x1536, 16:9 è 2048x1152). Predefinito: `"1K"`. Ignorato quando `aspect_ratio` è `"auto"`. | COMBO | Sì | `"1K"`<br>`"1.5K"` |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; l'API non ha un seed, quindi i risultati effettivi sono non deterministici indipendentemente da questo valore. Predefinito: `42`. | INT | Sì | Da 0 a 2147483647 |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image_1` ... `image_5` | Slot espandibile: collega da 1 a 5 immagini di riferimento per la modifica guidata da immagini; un input in batch conta una volta per immagine. Gli slot sono opzionali e possono essere lasciati vuoti (minimo 0 collegati). | IMAGE | No | Da 0 a 5 immagini |

**Note:**

- È supportato un massimo di 5 immagini di riferimento in totale su tutti gli slot collegati; un input in batch conta una volta per immagine.
- Il `prompt` deve contenere almeno 1 carattere dopo aver rimosso gli spazi bianchi circostanti e non può superare i 20000 caratteri.
- Le immagini di riferimento vengono inviate come dati PNG e sono limitate a un totale di 2048 x 2048 pixel.
- L'impostazione `aspect_ratio` viene applicata all'output anche quando sono collegate immagini di riferimento.
- Quando `aspect_ratio` è `"auto"`, l'impostazione `resolution` viene ignorata. Senza immagini di riferimento, il modello sceglie il rapporto per testo a immagine e renderizza alla dimensione 1.5K; con immagini di riferimento collegate, viene mantenuto il rapporto d'aspetto della prima immagine di riferimento.
- Il valore del seed non influisce sul risultato dell'API; determina solo se il nodo viene rieseguito.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `IMAGE` | L'immagine generata o modificata. Se il servizio restituisce più immagini, queste vengono combinate in un singolo output IMAGE in batch. Viene generato un errore se non viene restituita alcuna immagine o se un'immagine restituita non può essere decodificata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterImageNode/it.md)

---
**Source fingerprint (SHA-256):** `d201c18deccd2523041a24427996f51127ca201dfe10fad60c6f768ab79bf852`

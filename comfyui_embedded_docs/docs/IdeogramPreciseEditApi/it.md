# Ideogram 4.5 Modifica precisa

Modifica di un'immagine guidata da un prompt testuale con la modifica precisa di Ideogram 4.6 o 4.5: cambia solo ciò che il prompt richiede. Una modifica di regione mantiene l'immagine 1 alle sue dimensioni e risoluzione esatte. Una modifica dell'intera immagine ridimensiona l'immagine 1 prima del caricamento quando supera il limite del modello, quindi il risultato può essere più piccolo dell'input: 16,7 MP o 8192 pixel per lato su 4.6, circa 4 MP o 4608 pixel per lato su 4.5. L'immagine 1 è l'immagine da modificare e fino ad altre 4 immagini possono essere collegate come riferimenti. È anche possibile modificare da sola una singola regione dell'immagine 1, selezionata tramite una maschera o tramite bounding box, e ciò restituisce l'immagine a dimensione piena.

## Input

La selezione di un `model` determina quali input vengono visualizzati. Entrambi i modelli modificano una regione tramite `context_window`, ma 4.6 riceve la maschera su `mask` mentre 4.5 la riceve su `context_window_mask`, e 4.6 usa `"auto"` come valore predefinito anziché `"none"`.

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modello da utilizzare. `"ideogram-4.6"` gestisce sorgenti più grandi e regioni più ampie; `"ideogram-4.5"` è il modello precedente (predefinito: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sì | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Slot espandibile: l'immagine 1 è l'immagine da modificare e le immagini da 2 a 5 sono riferimenti opzionali (`image_1` ... `image_5`). Fai riferimento a esse nel prompt come @Image1, @Image2, ...; un input in batch conta una volta per immagine. Ogni immagine deve avere un rapporto d'aspetto compreso tra 1:6 e 6:1, con l'eccezione che l'immagine 1 non viene controllata per il rapporto d'aspetto mentre è in uso una finestra di contesto. | IMAGE | Sì | 1 a 5 immagini |
| `prompt` | Istruzioni di modifica. Supporta riferimenti in stile @Image1 alle immagini collegate (predefinito: stringa vuota). | STRING | Sì | 1 a 10000 caratteri |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo (predefinito: `"medium"`). | COMBO | Sì | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seed per la generazione. Su 4.6 le stesse immagini, prompt, impostazioni e seed danno lo stesso risultato o un risultato molto simile; su 4.5 danno lo stesso risultato (predefinito: 42). | INT | Sì | 0 a 2147483647 |

### Input di Ideogram 4.6

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Regione dell'immagine 1 da modificare. `"auto"` modifica la regione attorno alla maschera e mantiene l'immagine 1 a dimensione piena, oppure l'intera immagine quando non è collegata alcuna maschera; `"none"` modifica l'intera immagine; `"custom"` modifica la regione da `context_window_bboxes` e mantiene l'immagine 1 a dimensione piena (predefinito: `"auto"`). Una `mask` collegata viene inviata in tutte e tre le modalità, inclusa `"none"`. | COMBO | No | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Regione dell'immagine 1 da modificare, ad esempio l'output di Create Bounding Boxes. Obbligatorio quando `context_window` è `"custom"`; non utilizzato altrimenti. Più riquadri vengono uniti in un'unica regione, che viene estesa fino ad almeno 256 pixel per lato e allungata ulteriormente solo quando necessario per rimanere entro il rapporto d'aspetto massimo di 6:1. La regione può essere fino a 8192 pixel per lato e circa 16,7 MP (ad es. 4096x4096); l'area viene verificata dopo che ciascun lato è arrotondato per eccesso a un multiplo di 32, quindi una regione 4097x4095 viene rifiutata anche se la sua area non arrotondata è inferiore a 16,7 MP. | BOUNDING_BOX | No | - |
| `mask` | Il bianco indica cosa modificare; la regione di modifica viene posizionata attorno a esso. La maschera deve contenere sia aree bianche (modifica) sia aree nere (mantieni). Viene inviata ogni volta che è collegata, in ogni modalità di `context_window`, e riduce il limite di immagini a 4 (vedi i vincoli di seguito). | MASK | No | - |

### Input di Ideogram 4.5

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Regione dell'immagine 1 da modificare. `"none"` modifica l'intera immagine. `"auto"` modifica una regione attorno a `context_window_mask` e `"custom"` la regione da `context_window_bboxes`; entrambe mantengono l'immagine 1 a dimensione piena e lasciano invariato il resto dell'immagine (predefinito: `"none"`). | COMBO | No | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Regione dell'immagine 1 da modificare, ad esempio l'output di Create Bounding Boxes. Obbligatorio quando `context_window` è `"custom"`; non utilizzato altrimenti. Più riquadri vengono uniti in un'unica regione, che viene estesa fino ad almeno 256 pixel per lato e allungata ulteriormente solo quando necessario per rimanere entro il rapporto d'aspetto massimo di 6:1, quindi un riquadro piccolo come 32x32 modifica anche i pixel circostanti. La regione può essere fino a 4608 pixel per lato e circa 4 MP (ad es. 2048x2048), verificata dopo che ciascun lato è arrotondato per eccesso a un multiplo di 32. | BOUNDING_BOX | No | - |
| `context_window_mask` | Il bianco indica cosa modificare; la regione di modifica viene posizionata attorno a esso. Obbligatorio quando `context_window` è `"auto"`; non utilizzato altrimenti. La maschera deve contenere sia aree bianche (modifica) sia aree nere (mantieni). | MASK | No | - |

### Vincoli dei parametri

- **Numero di immagini:** almeno 1 e al massimo 5 immagini; un input in batch conta una volta per immagine. Quando il nodo usa una maschera, sono accettate al massimo 4 immagini, cioè l'immagine 1 e 3 riferimenti. Su 4.6 una `mask` collegata viene usata in ogni modalità; su 4.5 la maschera è `context_window_mask` e viene usata solo in `"auto"`, quindi `"none"` e `"custom"` accettano comunque 5 immagini con una maschera collegata.
- **Dimensione dell'output:** il nodo non ha input di dimensione, larghezza o altezza. Una modifica di regione restituisce l'immagine completa alla dimensione dell'immagine 1. Una modifica dell'intera immagine restituisce la dimensione dell'immagine 1 così come caricata: su 4.6 un'immagine superiore a 16,7 MP o 8192 pixel per lato viene prima ridimensionata, e su 4.5 lo stesso avviene oltre circa 4 MP o 4608 pixel per lato.
- **Dimensione della sorgente per la regione:** con una finestra di contesto in uso, l'immagine 1 può avere fino a 67.108.864 pixel in totale (circa 67 MP), ad esempio 8192x8192 o 10000x5000; il limite riguarda l'area, non un lato.
- **Limiti della regione:** una regione da `context_window_bboxes` può essere fino a 8192 pixel per lato e circa 16,7 MP su 4.6, e fino a 4608 pixel per lato e circa 4 MP su 4.5. I riquadri generano un errore solo quando la loro regione unita cade all'esterno dell'immagine 1, quindi un riquadro a sinistra dell'immagine e un altro a destra si uniscono in una regione che copre l'immagine.
- **Tag del prompt:** `@ImageN` viene confrontato senza distinzione tra maiuscole e minuscole e non deve superare il numero di immagini collegate; il prompt non deve essere composto solo da spazi e deve contenere al massimo 10000 caratteri.
- **Limite di caricamento:** l'immagine 1, la maschera e i riferimenti insieme devono rientrare nel limite di caricamento di 50 MB di Ideogram. Una modifica con 4.6 e una modifica di regione con 4.5 ricodificano l'immagine 1 come JPEG quando i file non rientrano e generano un errore se ancora non rientrano; una modifica dell'intera immagine con 4.5 invia sempre PNG e non ha questo fallback.
- **Sicurezza dei contenuti:** se il filtro di sicurezza dei contenuti di Ideogram blocca il risultato, il nodo genera un errore invece di restituire un'immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `IMAGE` | L'immagine modificata come batch, alla dimensione dell'immagine 1. Una modifica dell'intera immagine restituisce un'immagine più piccola quando la sorgente supera il limite di caricamento: 16,7 MP o 8192 pixel per lato su 4.6, circa 4 MP o 4608 pixel per lato su 4.5. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/it.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`

# Ideogram 4.5 Modifica precisa

Modifica un'immagine guidata da un prompt testuale con la modifica precisa di Ideogram 4.6 o 4.5: cambia solo ciò che il prompt richiede, i pixel non toccati restano identici e l'output mantiene le dimensioni dell'immagine 1. Una modifica dell'intera immagine su 4.6 restituisce un'immagine più piccola quando la sorgente supera 16,7 MP o 8192 pixel per lato, perché viene ridimensionata prima del caricamento. L'immagine 1 è l'immagine da modificare e fino a 4 immagini aggiuntive possono essere collegate come riferimenti. Una singola regione dell'immagine 1 può anche essere modificata da sola, selezionata tramite una maschera o tramite bounding box; in questo caso l'immagine viene restituita a dimensione piena.

## Input

La selezione di un `model` determina quali input compaiono. Entrambi i modelli modificano una regione tramite `context_window`, ma 4.6 riceve la maschera tramite `mask` mentre 4.5 la riceve tramite `context_window_mask`, e 4.6 ha `"auto"` come valore predefinito anziché `"none"`.

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da usare. `"ideogram-4.6"` gestisce sorgenti più grandi e regioni più ampie; `"ideogram-4.5"` è il modello precedente (predefinito: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sì | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Slot espandibile: l'immagine 1 è l'immagine da modificare e le immagini da 2 a 5 sono riferimenti opzionali (`image_1` ... `image_5`). Si fa riferimento a esse nel prompt come @Image1, @Image2, ...; un input in batch conta una volta per immagine. Ogni immagine deve avere un rapporto d'aspetto compreso tra 1:6 e 6:1, tranne il fatto che l'immagine 1 non viene controllata per il rapporto d'aspetto quando è in uso una finestra di contesto. | IMAGE | Sì | 1 a 5 immagini |
| `prompt` | Istruzioni di modifica. Supporta riferimenti in stile @Image1 alle immagini collegate (predefinito: stringa vuota). | STRING | Sì | 1 a 10000 caratteri |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo (predefinito: `"medium"`). | COMBO | Sì | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seme per la generazione. Le stesse immagini, prompt, impostazioni e seed danno lo stesso risultato o un risultato molto simile (predefinito: 42). | INT | Sì | 0 a 2147483647 |

### Input di Ideogram 4.6

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `context_window` | Regione dell'immagine 1 da modificare. `"auto"` modifica la regione attorno alla maschera e mantiene l'immagine 1 a dimensione piena, oppure l'intera immagine quando non è collegata alcuna maschera; `"none"` modifica l'intera immagine; `"custom"` modifica la regione da `context_window_bboxes` e mantiene l'immagine 1 a dimensione piena (predefinito: `"auto"`). | COMBO | No | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Regione dell'immagine 1 da modificare, ad esempio l'output di Create Bounding Boxes. Obbligatorio quando `context_window` è `"custom"`; non usato altrimenti. Diversi riquadri vengono uniti in un'unica regione, che viene ampliata fino ad almeno 256 pixel per lato e a un rapporto d'aspetto di 6:1. La regione può arrivare fino a 8192 pixel per lato e circa 16,7 MP (ad es. 4096x4096). | BOUNDING_BOX | No | - |
| `mask` | Le aree bianche indicano cosa modificare; la regione di modifica viene posizionata attorno a esse. La maschera deve contenere sia aree bianche (modifica) sia aree nere (mantieni). Viene inviata ogni volta che è collegata, in ogni modalità di `context_window`, e riduce il limite di immagini a 4 (vedere i vincoli di seguito). | MASK | No | - |

### Input di Ideogram 4.5

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `context_window` | Regione dell'immagine 1 da modificare. `"none"` modifica l'intera immagine. `"auto"` modifica una regione attorno a `context_window_mask` e `"custom"` la regione da `context_window_bboxes`; entrambe mantengono l'immagine 1 a dimensione piena e lasciano invariato il resto dell'immagine (predefinito: `"none"`). | COMBO | No | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Regione dell'immagine 1 da modificare, ad esempio l'output di Create Bounding Boxes. Obbligatorio quando `context_window` è `"custom"`; non usato altrimenti. La regione può arrivare fino a 4608 pixel per lato e circa 4 MP (ad es. 2048x2048). | BOUNDING_BOX | No | - |
| `context_window_mask` | Le aree bianche indicano cosa modificare; la regione di modifica viene posizionata attorno a esse. Obbligatoria quando `context_window` è `"auto"`; non usata altrimenti. La maschera deve contenere sia aree bianche (modifica) sia aree nere (mantieni). | MASK | No | - |

### Vincoli sui parametri

- **Numero di immagini:** almeno 1 e al massimo 5 immagini; un input in batch conta una volta per immagine. Ogni volta che è collegata una maschera, vengono accettate al massimo 4 immagini, cioè l'immagine 1 e 3 riferimenti.
- **Dimensione dell'output:** il nodo non ha input di dimensione, larghezza o altezza. Una modifica di regione restituisce l'immagine completa alla dimensione dell'immagine 1. Una modifica dell'intera immagine restituisce la dimensione dell'immagine 1 così come caricata: su 4.6 un'immagine superiore a 16,7 MP o 8192 pixel per lato viene prima ridimensionata, e su 4.5 lo stesso avviene oltre circa 4 MP o 4608 pixel per lato.
- **Dimensione della sorgente della regione:** con una finestra di contesto in uso, l'immagine 1 può arrivare fino a 8192x8192 pixel (circa 67 MP); sorgenti più grandi generano un errore.
- **Limiti della regione:** una regione da `context_window_bboxes` può arrivare fino a 8192 pixel per lato e circa 16,7 MP su 4.6, e fino a 4608 pixel per lato e circa 4 MP su 4.5. I riquadri che si trovano interamente al di fuori dell'immagine 1 generano un errore.
- **Tag del prompt:** `@ImageN` viene confrontato senza distinzione tra maiuscole e minuscole e non deve superare il numero di immagini collegate; il prompt non deve essere composto solo da spazi bianchi e deve essere lungo al massimo 10000 caratteri.
- **Limite di caricamento:** l'immagine 1, la maschera e i riferimenti insieme devono rientrare nei 50 MB di caricamento di Ideogram; l'immagine 1 viene ricodificata come JPEG quando necessario e il nodo genera un errore se non rientra comunque nel limite.
- **Sicurezza dei contenuti:** se il filtro di sicurezza dei contenuti di Ideogram blocca il risultato, il nodo genera un errore invece di restituire un'immagine.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine modificata come batch, alla dimensione dell'immagine 1. Con 4.6 una modifica dell'intera immagine torna più piccola se la sorgente supera 16.7 MP o 8192 pixel per lato. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/it.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`

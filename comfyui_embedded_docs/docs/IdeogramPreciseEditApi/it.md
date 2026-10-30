# Ideogram 4.5 Modifica precisa

Modifica un'immagine guidata da un prompt testuale con la modifica precisa di Ideogram 4.5: cambia solo ciò che il prompt richiede, i pixel non toccati restano identici e l'output mantiene le dimensioni dell'immagine 1. L'immagine 1 è l'immagine da modificare e fino a 4 ulteriori immagini possono essere collegate come riferimenti. Una singola regione dell'immagine 1 può anche essere modificata autonomamente, selezionata tramite una maschera o bounding box, restituendo l'immagine a dimensione piena.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `modello` | Modello da usare. (predefinito: `"ideogram-4.5"`) | DYNAMIC_COMBO | Sì | `"ideogram-4.5"` |
| `images` | Slot espandibile: l'immagine 1 è l'immagine da modificare e le immagini da 2 a 5 sono riferimenti opzionali (`image_1` ... `image_5`). Fai riferimento a esse nel prompt come @Image1, @Image2, ...; un input in batch conta una volta per immagine. Ogni immagine deve avere un rapporto d'aspetto compreso tra 1:6 e 6:1, tranne che l'immagine 1 non viene controllata per il rapporto d'aspetto mentre è in uso una finestra di contesto. | IMAGE | Sì | da 1 a 5 immagini |
| `prompt` | Istruzioni di modifica. Supporta riferimenti in stile @Image1 alle immagini collegate. (predefinito: stringa vuota) | STRING | Sì | da 1 a 10000 caratteri |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo. (predefinito: `"medium"`) | COMBO | Sì | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seme per la generazione. Le stesse immagini, prompt, impostazioni e seed danno lo stesso risultato. (predefinito: 42) | INT | Sì | da 0 a 2147483647 |
| `context_window` | Regione dell'immagine 1 da modificare. `"none"` modifica l'intera immagine. `"auto"` modifica una regione attorno a `context_window_mask` e `"custom"` la regione da `context_window_bboxes`; entrambe mantengono l'immagine 1 a dimensione piena e lasciano invariato il resto dell'immagine. (predefinito: `"none"`) | COMBO | No | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Regione dell'immagine 1 da modificare, ad esempio l'output di Create Bounding Boxes. Obbligatorio quando `context_window` è `"custom"`; non usato altrimenti. Diverse box vengono unite in un'unica regione, che viene ampliata fino ad almeno 256 pixel per lato e a un rapporto d'aspetto di 6:1. La regione può essere fino a 4608 pixel per lato e circa 4 MP (ad es. 2048x2048). | BOUNDING_BOX | No | - |
| `context_window_mask` | Il bianco indica cosa modificare; la regione di modifica viene posizionata attorno a esso. Obbligatorio quando `context_window` è `"auto"`; non usato altrimenti. La maschera deve contenere sia aree bianche (modifica) sia aree nere (mantieni). | MASK | No | - |

### Vincoli sui parametri

- **Numero di immagini:** almeno 1 e al massimo 5 immagini; un input in batch conta una volta per immagine. L'immagine 1 è l'immagine da modificare e le immagini da 2 a 5 sono riferimenti. Con `context_window_mask` sono accettate al massimo 4 immagini, ovvero l'immagine 1 e 3 riferimenti.
- **Dimensioni dell'output:** il risultato mantiene le dimensioni dell'immagine 1, quindi questo nodo non ha input di dimensione, larghezza o altezza. Ciò vale anche quando viene modificata una regione: l'immagine completa viene restituita con la sola regione modificata.
- **Rapporto d'aspetto delle immagini:** ogni immagine non deve essere più larga di 6 volte la sua altezza né più alta di 6 volte la sua larghezza (tra 1:6 e 6:1). L'immagine 1 è esente mentre `context_window` è `"auto"` o `"custom"`, perché viene inviata solo la regione selezionata.
- **Dimensioni della sorgente della regione:** con una finestra di contesto in uso, l'immagine 1 può arrivare a 8192x8192 pixel (circa 67 MP); sorgenti più grandi generano un errore. Senza una finestra di contesto, le immagini più grandi di circa 4 MP o 4608 px sul lato lungo vengono ridimensionate prima di essere inviate.
- **Limiti della regione:** una regione da `context_window_bboxes` può essere fino a 4608 pixel per lato e circa 4 MP; i box che si trovano interamente al di fuori dell'immagine 1 generano un errore.
- **Tag del prompt:** `@ImageN` viene confrontato senza distinzione tra maiuscole e minuscole e non deve superare il numero di immagini collegate; il prompt non deve essere composto solo da spazi bianchi e deve contenere al massimo 10000 caratteri.
- **Limite di caricamento:** l'immagine 1, la maschera e i riferimenti insieme devono rientrare nel limite di caricamento di 50 MB di Ideogram; l'immagine 1 viene ricodificata come JPEG quando necessario e il nodo genera un errore se ancora non rientra nel limite.
- **Sicurezza dei contenuti:** se il filtro di sicurezza dei contenuti di Ideogram blocca il risultato, il nodo genera un errore invece di restituire un'immagine.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine modificata come batch, alle dimensioni dell'immagine 1. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/it.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`

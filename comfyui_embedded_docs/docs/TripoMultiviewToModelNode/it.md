# Tripo: Multiview a Modello

Questo nodo genera modelli 3D in modo sincrono utilizzando l'API di Tripo, elaborando fino a quattro immagini che mostrano viste diverse di un oggetto (frontale, sinistra, posteriore, destra). Richiede un'immagine frontale e almeno una vista aggiuntiva (sinistra, posteriore o destra) per costruire il modello 3D. La texture, il materiale PBR, la qualità della geometria e il formato di output possono essere controllati dal nodo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | Immagine della vista frontale dell'oggetto. | IMAGE | Sì | - |
| `image_left` | Immagine della vista sinistra dell'oggetto. | IMAGE | No | - |
| `image_back` | Immagine della vista posteriore dell'oggetto. | IMAGE | No | - |
| `image_right` | Immagine della vista destra dell'oggetto. | IMAGE | No | - |
| `model_version` | La versione del modello da utilizzare per la generazione. | COMBO | No | Opzioni multiple disponibili |
| `orientation` | Impostazione dell'orientamento per il modello 3D (predefinito: `"default"`). | COMBO | No | Opzioni multiple disponibili |
| `texture` | Genera mappe di texture. Se disattivato, restituisce solo la geometria e ignora pbr. (predefinito: True) | BOOLEAN | No | - |
| `pbr` | Mappe del materiale PBR (colore base, metallico, rugosità, normale). Richiede texture. (predefinito: True) | BOOLEAN | No | - |
| `model_seed` | Seme casuale per la generazione del modello (predefinito: 42). | INT | No | 0 to 2,147,483,647 |
| `texture_seed` | Seme casuale per la generazione della texture (predefinito: 42). | INT | No | 0 to 2,147,483,647 |
| `texture_quality` | Livello di qualità per la generazione della texture (predefinito: `"standard"`). `"detailed"` = texture HD, `"extreme"` = texture Ultra 8K. | COMBO | No | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Metodo utilizzato per allineare le texture al modello (predefinito: `"original_image"`). | COMBO | No | `"original_image"`<br>`"geometry"` |
| `face_limit` | Numero massimo di facce. -1 lascia che Tripo scelga in modo adattivo (circa 1.4M facce su v3.x standard, 2M su detailed). Tripo applica un limite silenziosamente: v2.5 a 500,000, mesh quad a 150,000. (predefinito: -1) | INT | No | -1 to 2,000,000 |
| `quad` | Output con mesh quad. Tripo fornisce mesh quad come FBX, quindi il risultato arriva sull'output FBX e l'output GLB rimane vuoto. (predefinito: False) | BOOLEAN | No | - |
| `geometry_quality` | Livello di qualità per la generazione della geometria (predefinito: `"standard"`). | COMBO | No | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Mesh low-poly con topologia pulita e dallo stile artigianale (500-20,000 facce, quad 500-10,000). Ideale per soggetti semplici; quelli complessi potrebbero fallire. (predefinito: False) | BOOLEAN | No | - |
| `auto_size` | Ridimensiona i modelli con texture alle loro dimensioni reali in metri. Tripo memorizza la dimensione come trasformazione di scena del modello e la integra quando il modello viene convertito, sottoposto a rigging o a retargeting; ignorato senza texture. (predefinito: False) | BOOLEAN | No | - |

**Nota:** L'immagine frontale (`image`) è sempre obbligatoria e deve essere fornita anche almeno una tra `image_left`, `image_back` o `image_right`. Disattivando `texture` si disattiva automaticamente anche `pbr`, poiché `pbr` richiede texture. Quando `smart_low_poly` è abilitato e `face_limit` non è lasciato a -1, `face_limit` deve essere compreso tra 500 e 20,000 per mesh triangolari o tra 500 e 10,000 per mesh quad.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `model_file` | Percorso file o identificatore per il modello 3D generato (solo per compatibilità con versioni precedenti). | STRING |
| `model task_id` | Identificatore dell'attività per monitorare il processo di generazione del modello. | MODEL_TASK_ID |
| `GLB` | Il file del modello 3D generato in formato GLB. Vuoto quando `quad` è abilitato. | FILE3DGLB |
| `FBX` | Il file del modello 3D generato in formato FBX. Popolato solo quando `quad` è abilitato. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `b66df4cad6167fa27edf1fe21b96cb47af90027b3fbe0a3c9c14101506281ed7`

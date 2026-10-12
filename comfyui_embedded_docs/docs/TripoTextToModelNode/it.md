# TripoTextToModelNode

Questo nodo legacy genera modelli 3D finiti a partire da una descrizione testuale utilizzando l'API di Tripo. Attende il completamento della generazione e restituisce il file del modello, opzionalmente con texture e materiali PBR. È contrassegnato come deprecato e viene mantenuto per i flussi di lavoro più datati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrizione testuale del modello 3D da generare (multiriga). Questo parametro è obbligatorio e non può essere vuoto. | STRING | Sì | - |
| `negative_prompt` | Descrizione testuale di ciò che si desidera evitare nel modello generato (multiriga). Fino a 255 caratteri. Viene inviato all'API solo quando non è vuoto. | STRING | No | Up to 255 characters |
| `model_version` | Versione del modello Tripo da utilizzare per la generazione (predefinito: v3_1_20260211). | COMBO | No | Multiple options available |
| `style` | Non più supportato da Tripo e ignorato. Mantenuto per i flussi di lavoro più datati (predefinito: "None"). | COMBO | No | Multiple options available |
| `texture` | Genera le mappe di texture. Se disattivato restituisce la geometria nuda e ignora `pbr` (predefinito: True). | BOOLEAN | No | true / false |
| `pbr` | Mappe dei materiali PBR (colore di base, metallico, rugosità, normale). Richiede `texture`; viene forzato su off quando `texture` è disattivato (predefinito: True). | BOOLEAN | No | true / false |
| `image_seed` | Seme utilizzato per la fase di generazione dell'immagine (predefinito: 42). | INT | No | 0 to 2147483647 |
| `model_seed` | Seme utilizzato per la fase di generazione del modello (predefinito: 42). | INT | No | 0 to 2147483647 |
| `texture_seed` | Seme utilizzato per la fase di generazione della texture (predefinito: 42). | INT | No | 0 to 2147483647 |
| `texture_quality` | Qualità delle texture generate. detailed = texture HD, extreme = texture 8K Ultra (predefinito: standard). | COMBO | No | "standard"<br>"detailed"<br>"extreme" |
| `face_limit` | Numero massimo di facce. -1 lascia che Tripo scelga in modo adattivo (circa 1,4 milioni di facce su v3.x standard, 2 milioni su detailed). Tripo applica dei limiti silenziosamente: v2.5 a 500.000, mesh quad a 150.000. (predefinito: -1) | INT | No | -1 to 2000000 |
| `quad` | Output con mesh a quad. Tripo consegna le mesh a quad in formato FBX, quindi il risultato arriva sull'output FBX e l'output GLB rimane vuoto. (predefinito: False) | BOOLEAN | No | true / false |
| `geometry_quality` | Qualità della geometria generata (predefinito: standard). | COMBO | No | "standard"<br>"detailed" |
| `smart_low_poly` | Mesh low-poly con topologia pulita in stile artigianale (da 500 a 20.000 facce, quad da 500 a 10.000). Ideale per soggetti semplici; quelli complessi potrebbero fallire. (predefinito: False) | BOOLEAN | No | true / false |
| `auto_size` | Ridimensiona i modelli texturizzati alle loro dimensioni reali in metri. Tripo memorizza la dimensione come trasformazione di scena del modello e la incorpora quando il modello viene convertito, riggato o ritargettato; ignorato senza texture. (predefinito: True) | BOOLEAN | No | true / false |

**Note:**
- Questo nodo è deprecato e contrassegnato come nodo legacy. Viene mantenuto per la compatibilità con i flussi di lavoro più datati.
- Il parametro `prompt` è obbligatorio: un prompt vuoto fa sì che il nodo generi un errore.
- `pbr` richiede `texture`. Quando `texture` è disattivato, il nodo forza `pbr` su off e ne ignora il valore. Anche `auto_size` non ha alcun effetto senza `texture`.
- Quando `smart_low_poly` è abilitato e `face_limit` è impostato su un valore diverso da -1, il limite di facce deve essere compreso tra 500 e 20.000 per l'output a triangoli, oppure tra 500 e 10.000 quando `quad` è abilitato; in caso contrario il nodo genera un errore.
- Quando `quad` è abilitato, la mesh a quad generata viene consegnata in formato FBX, quindi l'output FBX viene popolato e l'output GLB rimane vuoto.
- Il parametro `style` viene accettato ma ignorato.

## Output

| Nome Output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_file` | Il nome del file del modello 3D generato nel formato `<task_id>.<format>`, mantenuto solo per compatibilità con le versioni precedenti. | STRING |
| `model task_id` | L'identificativo univoco dell'attività per il processo di generazione del modello. | MODEL_TASK_ID |
| `GLB` | Il modello 3D generato in formato GLB. Vuoto quando `quad` è abilitato. | FILE3DGLB |
| `FBX` | Il modello 3D generato in formato FBX. Popolato solo quando `quad` è abilitato. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `c26c8437ea66d08f7f39865fedeaaf4cf8583ca64b368f3b767ea18918dd6c08`

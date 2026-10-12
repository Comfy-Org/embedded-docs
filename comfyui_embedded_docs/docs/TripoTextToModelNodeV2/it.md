# TripoTextToModelNodeV2

Genera un modello 3D da una descrizione testuale utilizzando il servizio Tripo. Il nodo invia il prompt e le impostazioni a Tripo, attende il completamento dell'attività di generazione e restituisce il file 3D finito insieme all'identificatore dell'attività.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | La descrizione testuale del modello da generare. Non deve essere vuota. | STRING | Sì | Testo multiriga |
| `negative_prompt` | Testo che descrive ciò che non deve apparire nel modello generato. Fino a 255 caratteri. | STRING | No | Testo multiriga, max 255 caratteri |
| `model_version` | La versione del modello Tripo utilizzata per la generazione (predefinito: `v3.1_20260211`). | COMBO | No | Elenco delle versioni del modello Tripo supportate |
| `texture` | Genera le mappe di texture. Disattivato restituisce la geometria nuda e ignora `pbr` (predefinito: True). | BOOLEAN | No | True<br>False |
| `pbr` | Mappe di materiale PBR (colore di base, metallico, rugosità, normale). Richiede `texture` (predefinito: True). | BOOLEAN | No | True<br>False |
| `image_seed` | Valore di seed per la generazione dell'immagine (predefinito: 42). | INT | No | 0 - 2147483647 |
| `model_seed` | Valore di seed per la generazione del modello (predefinito: 42). | INT | No | 0 - 2147483647 |
| `texture_seed` | Valore di seed per la generazione della texture (predefinito: 42). | INT | No | 0 - 2147483647 |
| `texture_quality` | Livello di dettaglio della texture (predefinito: "standard"). "detailed" = texture HD, "extreme" = texture 8K Ultra. | COMBO | No | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `face_limit` | Numero massimo di facce. -1 lascia che Tripo scelga in modo adattivo (circa 1,4M di facce su v3.x standard, 2M su detailed). Tripo limita silenziosamente: v2.5 a 500.000, mesh quad a 150.000 (predefinito: -1). | INT | No | -1 - 2000000 |
| `quad` | Output con mesh quad. Tripo fornisce le mesh quad come FBX, quindi il risultato arriva sull'output FBX e l'output GLB rimane vuoto (predefinito: False). | BOOLEAN | No | True<br>False |
| `geometry_quality` | Livello di dettaglio della geometria (predefinito: "standard"). | COMBO | No | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Mesh low-poly con topologia pulita e in stile artigianale (500-20.000 facce, quad 500-10.000). Ideale per soggetti semplici; quelli complessi potrebbero fallire (predefinito: False). | BOOLEAN | No | True<br>False |
| `auto_size` | Ridimensiona i modelli texturizzati alla loro dimensione reale in metri. Tripo memorizza la dimensione come trasformazione di scena del modello e la incorpora quando il modello viene convertito, riggato o retargetizzato; ignorato senza texture (predefinito: True). | BOOLEAN | No | True<br>False |

### Note

- `prompt` è obbligatorio e non può essere vuoto o contenere solo spazi bianchi.
- Quando `texture` è impostato su False, `pbr` viene forzato a disattivato e `auto_size` non ha alcun effetto.
- Quando `smart_low_poly` è abilitato e `face_limit` non è -1, `face_limit` deve essere compreso tra 500 e 20.000 per mesh triangolari, oppure tra 500 e 10.000 quando `quad` è abilitato.
- Con `quad` abilitato, Tripo restituisce un file FBX, quindi l'output `GLB` rimane vuoto e l'output `FBX` viene popolato.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model task_id` | Identificatore dell'attività di generazione Tripo che ha prodotto il modello. | MODEL_TASK_ID |
| `GLB` | Il modello generato in formato GLB. Vuoto quando `quad` è abilitato. | FILE3D_GLB |
| `FBX` | Il modello generato in formato FBX. Popolato solo quando `quad` è abilitato. | FILE3D_FBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `8af7044188c6dbb87d23298bf7b99fe826bdc7bd7ba0948db2066887274faa00`

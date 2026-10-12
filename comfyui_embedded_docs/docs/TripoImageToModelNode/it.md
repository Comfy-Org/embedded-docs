# Tripo: da immagine a modello (legacy)

Genera modelli 3D in modo sincrono basandosi su una singola immagine usando l'API di Tripo. Fornisci un'immagine di input e il nodo crea da essa un modello 3D completo, con controlli opzionali per versione del modello, generazione delle texture, livello di dettaglio e formato di output. Questa è la versione legacy del nodo image-to-model, mantenuta per i flussi di lavoro precedenti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine di input usata per generare il modello 3D. È necessario fornire un'immagine, altrimenti il nodo genera un errore. | IMAGE | Sì | - |
| `model_version` | La versione del modello da usare per la generazione. | COMBO | No | `"v1.4"`<br>`"v3.0"`<br>`"v3.5"`<br>`"v3.6"` |
| `style` | Non è più supportato da Tripo e viene ignorato. Mantenuto per i flussi di lavoro precedenti. (predefinito: `"None"`) | COMBO | No | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `texture` | Genera mappe di texture. Se disattivato restituisce solo la geometria e ignora `pbr`. (predefinito: True) | BOOLEAN | No | True<br>False |
| `pbr` | Mappe dei materiali PBR (colore base, metallico, rugosità, normale). Richiede `texture`. (predefinito: True) | BOOLEAN | No | True<br>False |
| `model_seed` | Seme casuale per la generazione del modello. (predefinito: 42) | INT | No | da 0 a 2147483647 |
| `orientation` | Impostazione dell'orientamento per il modello generato. (predefinito: `"default"`) | COMBO | No | `"default"`<br>`"front"`<br>`"back"`<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `texture_seed` | Seme casuale per la generazione delle texture. (predefinito: 42) | INT | No | da 0 a 2147483647 |
| `texture_quality` | Livello di qualità per la generazione delle texture: `detailed` = texture HD, `extreme` = texture Ultra 8K. (predefinito: `"standard"`) | COMBO | No | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Metodo di allineamento per la mappatura delle texture. (predefinito: `"original_image"`) | COMBO | No | `"original_image"`<br>`"geometry"` |
| `face_limit` | Numero massimo di facce. -1 lascia che Tripo scelga in modo adattivo (circa 1,4M di facce su v3.x standard, 2M su detailed). Tripo applica limiti silenziosamente: v2.5 a 500.000, mesh quad a 150.000. (predefinito: -1) | INT | No | da -1 a 2000000 |
| `quad` | Output mesh quad. Tripo fornisce le mesh quad come FBX, quindi il risultato arriva sull'output FBX e l'output GLB rimane vuoto. (predefinito: False) | BOOLEAN | No | True<br>False |
| `geometry_quality` | Livello di qualità per la generazione della geometria. (predefinito: `"standard"`) | COMBO | No | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Mesh low-poly con topologia pulita in stile artigianale (500-20.000 facce, quad 500-10.000). Ideale per soggetti semplici; quelli complessi potrebbero fallire. (predefinito: False) | BOOLEAN | No | True<br>False |
| `auto_size` | Ridimensiona i modelli con texture alla loro dimensione reale in metri. Tripo memorizza la dimensione come trasformazione di scena del modello e la incorpora quando il modello viene convertito, sottoposto a rig o retargeting; ignorato senza texture. (predefinito: True) | BOOLEAN | No | True<br>False |

Nota: `image` è obbligatorio; se manca, il nodo genera un RuntimeError. Quando `texture` è False, il modello contiene solo geometria e `pbr` viene forzato a False. Quando `smart_low_poly` è abilitato, `face_limit` deve essere compreso tra 500 e 20.000 per le mesh triangolari, oppure tra 500 e 10.000 quando è abilitato anche `quad`; se il limite non è valido, il nodo genera un ValueError. Impostando `face_limit` a -1 (il valore predefinito) non viene inviato alcun limite esplicito di facce all'API, lasciando che Tripo scelga in modo adattivo.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `model_file` | Il file del modello 3D generato (solo per compatibilità con le versioni precedenti). | STRING |
| `model task_id` | L'ID dell'attività per monitorare il processo di generazione del modello. | MODEL_TASK_ID |
| `GLB` | Il modello 3D generato in formato GLB. Vuoto quando `quad` è abilitato. | FILE3DGLB |
| `FBX` | Il modello 3D generato in formato FBX. Popolato solo quando `quad` è abilitato. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `3b278abfd13329ee58ebab1bfeb47d32d09f4797f3d8628a35a028c3d15a7314`

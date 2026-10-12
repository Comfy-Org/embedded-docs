# TripoConversionNode

Questo nodo converte un modello 3D Tripo esistente in un altro formato di file 3D. Prende l'ID del task di un modello creato o elaborato in precedenza da un'operazione Tripo (come generazione del modello, rigging, retargeting o segmentazione), invia un task di conversione all'API Tripo, attende il completamento di tale task e quindi restituisce il file del modello convertito.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `original_model_task_id` | ID del task del modello Tripo da convertire. Deve provenire da un precedente task Tripo di generazione del modello, rigging, retargeting o segmentazione. Se l'ID è mancante o vuoto, il nodo genera un errore. | STRING | Sì | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `format` | Formato file di destinazione per il modello 3D convertito. | COMBO | Sì | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `quad` | Converte i triangoli in quadrilateri quando abilitato (predefinito: False). | BOOLEAN | No | True o False |
| `face_limit` | Numero massimo di facce nel modello convertito. Imposta a -1 per nessun limite (predefinito: -1). | INT | No | -1 a 2000000 |
| `texture_size` | Risoluzione delle texture di output in pixel (predefinito: 4096). | INT | No | 128 a 8192 |
| `texture_format` | Formato file usato per le texture esportate (predefinito: JPEG). | COMBO | No | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | Forza il modello a essere simmetrico quando abilitato (predefinito: False). | BOOLEAN | No | True o False |
| `flatten_bottom` | Appiattisce la parte inferiore del modello quando abilitato (predefinito: False). | BOOLEAN | No | True o False |
| `flatten_bottom_threshold` | Profondità di appiattimento usata con `flatten_bottom` (predefinito: 0.01). Questo valore viene applicato solo quando `flatten_bottom` è abilitato. | FLOAT | No | 0.01 a 1.0 |
| `pivot_to_center_bottom` | Sposta il punto pivot al centro della base del modello quando abilitato (predefinito: False). | BOOLEAN | No | True o False |
| `scale_factor` | Fattore di scala applicato al modello convertito (predefinito: 1.0). | FLOAT | No | 0.01 e oltre |
| `with_animation` | Mantiene lo scheletro e l'animazione dei modelli con rigging o retargeting (predefinito: True). | BOOLEAN | No | True o False |
| `pack_uv` | Ricompatta le coordinate UV quando abilitato (predefinito: False). | BOOLEAN | No | True o False |
| `bake` | Esegue il bake dei materiali avanzati nelle texture di base per una maggiore compatibilità (predefinito: True). | BOOLEAN | No | True o False |
| `part_names` | Elenco separato da virgole dei nomi delle parti del modello da inviare alla conversione. Le voci vuote vengono ignorate e i nomi duplicati vengono rimossi. Lascia vuoto per omettere questa opzione (predefinito: vuoto). | STRING | No | Elenco separato da virgole di nomi di parti |
| `fbx_preset` | Preset di compatibilità FBX. bake_scale esegue il bake della trasformazione di scala nella geometria (predefinito: blender). | COMBO | No | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `export_vertex_colors` | Esporta i colori dei vertici quando abilitato (predefinito: False). | BOOLEAN | No | True o False |
| `export_orientation` | Asse forward del modello esportato. default mantiene il +x di Tripo (predefinito: default). | COMBO | No | default<br>+x<br>-x<br>+y<br>-y |
| `animate_in_place` | Anima il modello sul posto quando abilitato (predefinito: False). | BOOLEAN | No | True o False |

**Nota:** Ad eccezione di `original_model_task_id` e `format`, tutti gli input sono impostazioni avanzate opzionali. La maggior parte delle impostazioni lasciate ai valori predefiniti viene omessa dalla richiesta di conversione, così che l'API Tripo possa usare il proprio comportamento standard. Le opzioni `with_animation` e `bake` vengono sempre inviate. `flatten_bottom_threshold` viene applicato solo quando `flatten_bottom` è abilitato.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_3d` | Modello convertito nel formato richiesto. OBJ viene fornito da Tripo come archivio ZIP (mesh, materiale e texture). | FILE_3D |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/it.md)

---
**Source fingerprint (SHA-256):** `b6be09bf6b1c5ccd6de5ae56ed28bfe1f0b81c1ca8ff61623e3094917c98d68a`

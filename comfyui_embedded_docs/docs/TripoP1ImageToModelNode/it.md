# Tripo P1: Da Immagine a Modello

Tripo P1: Image to Model converte una singola immagine 2D in un modello 3D utilizzando l'API Tripo P1. È ottimizzato per generare mesh a basso numero di poligoni, pronte per il gioco, e consente di scegliere tra una mesh solo geometria o un modello texturizzato con mappe PBR. Il modello finito viene restituito come file GLB.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `output_mode` | Sceglie il tipo di risultato. "Geometry only" restituisce una mesh non texturizzata; "Textured" aggiunge mappe colore/PBR e rivela impostazioni di texture extra. | DYNAMIC_COMBO | Sì | `"Geometry only"`<br>`"Textured"` |
| `image` | L'immagine 2D di origine utilizzata per generare il modello 3D. È richiesta una singola immagine; il nodo genera un errore se non ne viene fornita nessuna. | IMAGE | Sì | - |
| `enable_image_autofix` | Pre-elabora l'immagine di input per una migliore qualità di generazione. (predefinito: False) | BOOLEAN | No | True<br>False |
| `face_limit` | Numero di facce target, 48-20000. -1 lascia che Tripo scelga in modo adattivo. (predefinito: -1) | INT | No | -1 to 20000 |
| `model_seed` | Seme utilizzato per la generazione della geometria in modo che i risultati possano essere riprodotti. (predefinito: 42) | INT | No | 0 to 2147483647 |
| `auto_size` | Ridimensiona l'output per approssimare i metri del mondo reale. (predefinito: False) | BOOLEAN | No | True<br>False |
| `export_uv` | UV unwrap durante la generazione. Disattiva per esecuzioni solo geometria più veloci. (predefinito: True) | BOOLEAN | No | True<br>False |
| `compress_geometry` | Applica la compressione geometrica meshopt (EXT_meshopt_compression). File più piccoli, ma l'anteprima 3D di ComfyUI non può visualizzarli; decomprimere prima di modificare. (predefinito: False) | BOOLEAN | No | True<br>False |

### Input di Geometry only

Nessun parametro aggiuntivo. L'output è una mesh non texturizzata.

### Input di Textured

Questi parametri vengono visualizzati quando `output_mode` è impostato su "Textured".

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `pbr` | Includi mappe PBR. Quando attivo, anche la texture di base viene forzata. (predefinito: True) | BOOLEAN | Sì | True<br>False |
| `texture_quality` | detailed = texture HD, extreme = texture 8K Ultra. (predefinito: "standard") | COMBO | Sì | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Dai priorità alla fedeltà visiva all'immagine di origine o all'allineamento alla geometria della mesh. (predefinito: "original_image") | COMBO | Sì | `"original_image"`<br>`"geometry"` |
| `orientation` | Ruota l'output per corrispondere all'immagine di origine. Si applica solo quando è texturizzato. (predefinito: "default") | COMBO | Sì | `"default"`<br>`"align_image"` |
| `texture_seed` | Seme utilizzato per la generazione della texture in modo che i risultati texturizzati possano essere riprodotti. (predefinito: 42) | INT | Sì | 0 to 2147483647 |

Nota: quando `output_mode` è "Geometry only", il texturing è disabilitato per la richiesta. In modalità "Textured", viene sempre richiesta una texture a colori; disabilitando `pbr` si rimuovono le mappe PBR ma si mantiene la texture di colore di base, mentre abilitando `pbr` si forza anche l'attivazione della texture di base. `texture_alignment` e `orientation` sono disponibili solo in modalità "Textured".

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_file` | Una stringa contenente il nome del file del modello generato (`<task_id>.glb`). Mantenuto solo per compatibilità con le versioni precedenti. | STRING |
| `model task_id` | L'ID univoco dell'attività restituito dall'API Tripo per il lavoro di generazione completato. | MODEL_TASK_ID |
| `GLB` | Il modello 3D generato in formato GLB. | FILE3DGLB |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`

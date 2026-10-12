# TencentTextToModelNode

Questo nodo usa l'API Hunyuan3D Pro di Tencent per generare un modello 3D da una descrizione testuale. Invia una richiesta per creare un'attività di generazione, esegue il polling del risultato e scarica i file finali del modello nei formati GLB e OBJ.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | La versione del modello Hunyuan3D da utilizzare. L'opzione LowPoly non è disponibile per il modello `3.1`. | COMBO | Sì | `"3.0"`<br>`"3.1"` |
| `prompt` | La descrizione testuale del modello 3D da generare. Supporta fino a 1024 caratteri. | STRING | Sì | - |
| `face_count` | Il numero obiettivo di facce per il modello 3D generato. Predefinito: 500000. | INT | Sì | 3000 - 1500000 |
| `generate_type` | Il tipo di modello 3D da generare. Le opzioni disponibili e i relativi parametri sono:<br>- **Normal**: genera un modello standard. Include un parametro `pbr` (predefinito: `False`).<br>- **LowPoly**: genera un modello a basso numero di poligoni. Include i parametri `polygon_type` (`"triangle"` o `"quadrilateral"`) e `pbr` (predefinito: `False`).<br>- **Geometry**: genera un modello di sola geometria. | DYNAMICCOMBO | Sì | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `seed` | Un valore di seed per la generazione. I risultati non sono deterministici indipendentemente dal seed. Impostare un nuovo seed controlla se il nodo deve essere rieseguito. Predefinito: 0. | INT | No | 0 - 2147483647 |

**Nota:** Il parametro `generate_type` è dinamico. Selezionando `"LowPoly"` verranno mostrati input aggiuntivi per `polygon_type` e `pbr`. Selezionando `"Normal"` verrà mostrato un input per `pbr`. Selezionando `"Geometry"` non verrà mostrato alcun input aggiuntivo.

**Vincolo:** Il tipo di generazione `"LowPoly"` non può essere usato con il modello `"3.1"`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_file` | Un output legacy per compatibilità con le versioni precedenti. | STRING |
| `GLB` | Il modello 3D generato nel formato file GLB. | FILE3DGLB |
| `OBJ` | Il modello 3D generato nel formato file OBJ. | FILE3DOBJ |
| `texture_image` | L'immagine di texture estratta dal file OBJ generato, se disponibile. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `8110b6a70cdd26d5d0dcb791e654a6292895693e25076b982951c65f787422d6`

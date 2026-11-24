# Meshy: Image to Relief

Questo nodo trasforma una foto in un modello a bassorilievo e in una mappa di profondità a 16 bit per stampa 3D, incisione laser e fresatura CNC. Gli elementi scuri su sfondo chiaro vengono messi in rilievo, mentre le aree chiare rimangono basse. Vengono generati e scaricati solo gli output collegati; pertanto, se non è collegato alcun output del modello, l'operazione restituisce solo la mappa di profondità.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Foto da convertire in un rilievo. Gli elementi scuri su sfondo chiaro vengono messi in rilievo. La trasparenza viene rimossa prima del caricamento, quindi appiattisci prima un logo trasparente su uno sfondo bianco. | IMAGE | Sì | Immagine singola |
| `relief_type` | Preset di incisione. `"low"` è un'incisione superficiale per incisione laser, lavorazione CNC e targhe; `"high"` è più profonda per pezzi stampati in 3D. Il preset seleziona il valore di `carving_depth_mm`. | DYNAMIC_COMBO | Sì | `"low"`<br>`"high"` |
| `carving_depth_mm` | Profondità dell'incisione in millimetri. Disponibile quando `relief_type` è impostato (predefinito: 3.0 per `"low"`, 6.0 per `"high"`). | FLOAT | Sì | 0.1 a 60.0 (passo 0.1) |
| `size_mm` | Lunghezza del lato maggiore della foto sul modello, in millimetri, misurata in piano prima di qualsiasi curvatura (predefinito: 60.0). | FLOAT | Sì | 20.0 a 250.0 (passo 1.0) |
| `carving_mode` | `"emboss"` mette in rilievo le parti più vicine della foto, `"engrave"` le incide in incavo. | COMBO | Sì | `"emboss"`<br>`"engrave"` |
| `base` | `"plate"` mantiene una piastra di base sotto il rilievo, `"none"` rimuove lo sfondo e non crea alcuna piastra. Selezionando un'opzione viene mostrato il relativo parametro. | DYNAMIC_COMBO | Sì | `"plate"`<br>`"none"` |
| `base_thickness_mm` | Spessore della piastra di base in millimetri. Disponibile quando `base` è `"plate"` (predefinito: 1.0). | FLOAT | Sì | 0.1 a 10.0 (passo 0.1) |
| `removal_threshold` | Profondità sotto la quale lo sfondo viene asportato, sulla mappa di profondità da 0 a 1. 0.3 mantiene integro un busto, 0.8 lo riduce in frammenti. Disponibile quando `base` è `"none"` (predefinito: 0.01). | FLOAT | Sì | 0.01 a 1.0 (passo 0.01) |
| `bend` | `"convex"` fa incurvare la parte anteriore verso l'esterno, `"concave"` la curva verso l'interno, `"off"` mantiene il rilievo piatto. Selezionando una curvatura vengono mostrati `bend_axis` e `bend_angle`. | DYNAMIC_COMBO | Sì | `"off"`<br>`"convex"`<br>`"concave"` |
| `bend_axis` | `"xz"` curva i bordi sinistro e destro, `"yz"` i bordi superiore e inferiore. Disponibile quando `bend` è `"convex"` o `"concave"`. | COMBO | Sì | `"xz"`<br>`"yz"` |
| `bend_angle` | Ampiezza dell'arco della curvatura in gradi; 360 chiude il rilievo in un cilindro. Disponibile quando `bend` è `"convex"` o `"concave"` (predefinito: 60.0). | FLOAT | Sì | 1.0 a 360.0 (passo 1.0) |
| `seed` | Seed che controlla se il nodo viene rieseguito; il risultato non è deterministico indipendentemente dal seed. Modificalo per richiedere un output che è stato collegato dopo l'ultima esecuzione (predefinito: 42). | INT | Sì | 0 a 2147483647 |
| `mesh_resolution` | Punti della mesh lungo il lato maggiore della foto. A 1024 il GLB è di circa 50 MB e l'STL di circa 105 MB; a 2048 circa 200 MB e 420 MB; una curvatura raddoppia queste dimensioni. (predefinito: 1024; opzione avanzata) | INT | Sì | 512 a 2048 |
| `color_mapping` | Colora i file GLB, OBJ, FBX e USDZ con la foto. STL e 3MF rimangono bianchi. (predefinito: False; opzione avanzata) | BOOLEAN | Sì | True / False |

**Nota:** Un formato di modello viene generato e scaricato solo quando il relativo output è collegato. Se non è collegato alcun output del modello, l'operazione restituisce solo la mappa di profondità; con il solo `preview` il modello viene comunque generato per la miniatura, ma non viene restituito alcun file del modello. `depth_map` mantiene l'intera gamma a 16 bit; Save Image (Advanced) lo scrive come PNG a 16 bit.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `GLB` | Il modello del rilievo scaricato in formato GLB. | FILE3DGLB |
| `STL` | Il modello del rilievo scaricato in formato STL. | FILE3DSTL |
| `OBJ` | Il modello del rilievo scaricato in formato OBJ. | FILE3DOBJ |
| `FBX` | Il modello del rilievo scaricato in formato FBX. | FILE3DFBX |
| `USDZ` | Il modello del rilievo scaricato in formato USDZ. | FILE3DUSDZ |
| `3MF` | Il modello del rilievo scaricato in formato 3MF. | FILE3D |
| `depth_map` | Mappa di profondità con l'intera gamma a 16 bit; Save Image (Advanced) la scrive come PNG a 16 bit. | IMAGE |
| `preview` | Miniatura renderizzata da Meshy per il rilievo finito. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToReliefNode/it.md)

---
**Source fingerprint (SHA-256):** `6f2f0eb49074281b99d7ee10daf3bcc5616c6596c1c4d8491c72739550395f52`

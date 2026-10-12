# SAM3DBody_Render

Renders 3D body pose data into an image using a selectable style. The node accepts pose data from the SAM3D body tracker (MHR) or from an external Y-up rig such as Kimodo, and can composite the result over an optional background image (or a black canvas when none is provided). Available render styles include a shaded 3D mesh, a binary silhouette, 2D and 3D OpenPose-style skeletons, and SCAIL-style body capsules.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `render_style` | Modalità di rendering. 'mesh' = mesh MHR 3D rasterizzata attraverso la camera. 'silhouette' = maschera binaria della mesh. 'openpose_2d' = scheletro 2D piatto. 'openpose_3d' = scheletro OpenPose come modello 3D a facce piatte. 'scail' = capsule 3D SCAIL. (predefinito: "mesh") | DYNAMIC_COMBO | Sì | "mesh"<br>"silhouette"<br>"openpose_2d"<br>"openpose_3d"<br>"scail" |
| `pose_data` | Dati di posa MHR, oppure dati di posa di un rig Y-up esterno (KimodoSample). Tutti gli stili di rendering funzionano per rig esterni che contengono mappe dei giunti OpenPose nel loro `_skeleton_override` (KimodoSample lo fa). | MHR_POSE_DATA o KIMODO_POSE_DATA | Sì | — |
| `background` | Sfondo per fotogramma. Omesso = tela nera. | IMAGE | No | — |
| `width` | Larghezza di output in pixel. 0 = usa image_size nativa dei dati di posa. Se viene impostata solo una tra width/height, l'altra viene derivata preservando le proporzioni originali. (predefinito: 0) | INT | No | 0 to 16384, step 8 |
| `height` | Altezza di output in pixel. 0 = usa image_size nativa dei dati di posa. Se viene impostata solo una tra width/height, l'altra viene derivata preservando le proporzioni originali. (predefinito: 0) | INT | No | 0 to 16384, step 8 |
| `camera_info` | Override di camera 6DOF libera. Quando collegato, la posa viene riproiettata attraverso questa camera (posizione/target/zoom/rotazione/FoV) invece di quella prevista. | LOAD_3D_CAMERA | No | — |

### Input di Mesh

Questi parametri compaiono quando `render_style` è "mesh".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `shader` | Shader preimpostato. 'normals' = normale corrente della superficie nello spazio camera (convenzione OpenGL Y+ per normal map: +X→R, +Y→G, +Z→B). 'rainbow' = jet body-Y in stile RealisDance; le varianti 'rainbow_face_*' sovrascrivono i vertici del viso con colori della normale/per regione; 'depth' = grigio lineare. (predefinito: "default") | DYNAMIC_COMBO | No | "default"<br>"normals"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic"<br>"depth" |
| `rainbow_tilt_z` | Ruota l'asse del jet rainbow attorno a Z (avanti). Differenzia sinistra/destra. Disponibile solo quando `shader` è "rainbow", "rainbow_face_normal" o "rainbow_face_semantic". (predefinito: -35.0) | FLOAT | No | -90.0 to 90.0, step 0.5 |
| `rainbow_tilt_x` | Ruota l'asse del jet rainbow attorno a X (destra). Differenzia davanti/dietro. Disponibile solo quando `shader` è "rainbow", "rainbow_face_normal" o "rainbow_face_semantic". (predefinito: 0.0) | FLOAT | No | -90.0 to 90.0, step 0.5 |
| `opacity` | Alpha della mesh sopra l'immagine di sfondo, oppure sopra il nero quando non ne è collegata alcuna. (predefinito: 1.0) | FLOAT | No | 0.0 to 1.0, step 0.01 |
| `person_palette_falloff` | Desaturazione per persona verso il bianco: la traccia k riceve una miscela pastello (1 - falloff^k) (SCAIL 'seconda persona più morbida'). 1.0 = disattivato. (predefinito: 0.6) | FLOAT | No | 0.1 to 1.0, step 0.05 |
| `region` | 'hands_only' filtra le facce tramite la `hand_vert_mask` precalcolata (pesi LBS rispetto ai KP canonici della mano) — isola la mesh della mano per il debug. Torna alla mesh completa se la maschera è assente. (predefinito: "full_body") | COMBO | No | "full_body"<br>"hands_only" |

### Input di Silhouette

Quando `render_style` è "silhouette", il nodo esegue il rendering di una maschera binaria della mesh 3D. Questa modalità non ha parametri aggiuntivi.

### Input di OpenPose 2D

Questi parametri compaiono quando `render_style` è "openpose_2d".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_px` | Raggio del punto keypoint del corpo (px). (predefinito: 4) | INT | No | 1 to 32, step 1 |
| `stick_width_px` | Semilarghezza dell'ellisse dell'arto del corpo (px). Predefinito DWPose = 4. (predefinito: 4) | INT | No | 1 to 32, step 1 |
| `limb_alpha` | Alpha per arto. Predefinito DWPose = 0.6. (predefinito: 0.6) | FLOAT | No | 0.0 to 1.0, step 0.05 |
| `face_style` | 'full' = tutti i landmark del viso (sapiens-238 se presenti, altrimenti fallback del rig ~30). 'eyes_mouth' = sottoinsieme di fallback del rig (~12 punti: solo occhi + labbra esterne). 'disabled' = nessun punto del viso. (predefinito: "disabled") | COMBO | No | "disabled"<br>"full"<br>"eyes_mouth" |
| `hand_style` | Disegna 21+21 keypoint della mano + bastoncini. 'disabled' = nessuna mano. 'dwpose' = punti blu pieni; 'openpose' = punti arcobaleno. (predefinito: "disabled") | COMBO | No | "disabled"<br>"dwpose"<br>"openpose" |
| `person_palette_falloff` | Desaturazione per persona: la traccia k si mescola verso il bianco di 1 - falloff^k. La traccia 0 rimane vivida; 1.0 disattiva il falloff. (predefinito: 0.6) | FLOAT | No | 0.1 to 1.0, step 0.05 |

### Input di OpenPose 3D

Questi parametri compaiono quando `render_style` è "openpose_3d".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | Raggio della capsula dell'arto in metri (sottile = simile a un bastoncino). (predefinito: 0.015) | FLOAT | No | 0.004 to 0.1, step 0.001 |
| `include_hands` | Disegna 21+21 keypoint della mano come capsule 3D. (predefinito: True) | BOOLEAN | No | True or False |
| `person_palette_falloff` | Desaturazione per persona: la traccia k si mescola verso il bianco di 1 - falloff^k. La traccia 0 rimane vivida; 1.0 disattiva il falloff. (predefinito: 0.6) | FLOAT | No | 0.1 to 1.0, step 0.05 |

### Input di SCAIL

Questi parametri compaiono quando `render_style` è "scail".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | Raggio della capsula in metri (riferimento SCAIL: ~0.022 m). (predefinito: 0.022) | FLOAT | No | 0.005 to 0.2, step 0.001 |
| `hand_style` | Compone mani OpenPose 2D sopra il corpo a capsule 3D (corrisponde a SCAIL — nessuna capsula 3D per le mani). 'disabled' = nessuna mano. 'dwpose' = punti blu pieni per la mano; 'openpose' = punti arcobaleno. I bastoncini rimangono arcobaleno per dito in entrambi i casi. (predefinito: "dwpose") | COMBO | No | "disabled"<br>"dwpose"<br>"openpose" |
| `face_style` | 'full' = tutti i landmark del viso (sapiens-238 se presenti, altrimenti fallback del rig ~30). 'eyes_mouth' = sottoinsieme di fallback del rig (~12 punti: solo occhi + labbra esterne). 'disabled' = nessun punto del viso. (predefinito: "disabled") | COMBO | No | "disabled"<br>"full"<br>"eyes_mouth" |
| `person_palette_falloff` | Desaturazione per persona: la traccia k si mescola verso il bianco di 1 - falloff^k. La traccia 0 rimane vivida; 1.0 disattiva il falloff. (predefinito: 0.6) | FLOAT | No | 0.1 to 1.0, step 0.05 |

### Note

- Se sia `width` sia `height` sono 0, l'output usa la dimensione immagine nativa dei dati di posa. Se ne viene impostato solo uno, l'altro viene derivato preservando il rapporto d'aspetto originale. Un `background` collegato viene ridimensionato per corrispondere alla risoluzione di rendering.
- Quando `camera_info` è collegato, la posa viene riproiettata attraverso quella camera invece di quella prevista.
- In modalità mesh, `rainbow_tilt_z` e `rainbow_tilt_x` sono disponibili solo quando `shader` è impostato su "rainbow", "rainbow_face_normal" o "rainbow_face_semantic".
- In modalità mesh, quando `region` è "hands_only", il filtro della regione della mano richiede che i dati di posa contengano una maschera dei vertici della mano; se la maschera è assente, viene renderizzata invece la mesh completa.
- In modalità scail, le mani vengono disegnate come overlay OpenPose 2D sopra il corpo a capsule 3D anziché come capsule 3D; impostando `hand_style` su "disabled" vengono rimosse completamente.
- Quando la risoluzione di output differisce dalla risoluzione nativa dei dati di posa, le dimensioni dei marker e dei bastoncini di openpose_2d vengono scalate proporzionalmente.
- Se lo sfondo ha meno fotogrammi dei dati di posa, l'ultimo fotogramma dello sfondo viene riutilizzato per i fotogrammi rimanenti.
- L'output contiene un fotogramma per ogni fotogramma di posa in input. Se i dati di posa non contengono fotogrammi, viene restituita una singola immagine nera.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | I fotogrammi renderizzati: i dati di posa disegnati nello stile di rendering selezionato, composti sopra lo sfondo quando ne è collegato uno, oppure sopra il nero altrimenti. Un fotogramma per ogni fotogramma di posa in input, restituiti come un'unica immagine in batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Render/it.md)

---
**Source fingerprint (SHA-256):** `96556283cf07727e6b4bb3549537bf925ed771bab8607f65c93ab54a5f0e9ba5`

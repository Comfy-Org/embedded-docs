# BuildPoseFile

Questo nodo crea un file di animazione 3D pronto per il salvataggio a partire dai dati di posa. È possibile esportare un GLB animato in diversi stili visivi — una mesh completa del corpo, un'anteprima delle sole articolazioni, uno scheletro OpenPose o un rig a capsule SCAIL — oppure salvare invece una clip motion-capture BVH. L'output si collega a un nodo di salvataggio file come Save 3D Model per scrivere il file su disco.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `pose_data` | Dati di posa 3D. Accetta dati di posa MHR (parametri model/shape/expression, keypoint MHR70, colori canonici, maschera vertici mano) o dati di posa Kimodo (rig esterno Y-up con vertici previsti per frame e camera). | MHR_POSE_DATA / KIMODO_POSE_DATA | Sì | — |
| `format` | Formato di output, entrambi passati a Save 3D Model per scrivere su disco. 'glb' = GLB animato (mesh / bones / openpose / scail). 'bvh' = clip mocap BVH (un solo scheletro; richiede il modello). (predefinito: glb) | DYNAMIC_COMBO | Sì | "glb"<br>"bvh" |
| `sam3d_body_model` | Modello corpo SAM3D opzionale. Richiesto per i formati 'bvh', 'body_mesh' e 'bones_only' a meno che i dati di posa non contengano un override dello scheletro. | SAM3D_BODY_MODEL | No | — |
| `fps` | Frequenza dei fotogrammi dell'animazione. (predefinito: 24.0) | FLOAT | Sì | 1.0-240.0 |
| `camera_translation` | Incorpora pred_cam_t nella traslazione della radice: 'off' = posizione di bind; 'centered' = delta dal fotogramma 0; 'absolute' = grezza (Z è la profondità della camera — di solito a metri di distanza). (predefinito: off) | COMBO | Sì | "off"<br>"centered"<br>"absolute" |
| `track_index` | Selezione traccia: -1 = tutte le tracce; ≥0 = traccia singola. (predefinito: -1) | INT | Sì | da -1 a 15 |

### Input GLB

Questi input compaiono quando `format` è impostato su "glb".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `mesh_style` | Stile visivo del GLB: 'body_mesh' = Armature reale (127 ossa, skinning, keyframe TRS, 72 morph facciali; richiede il modello). 'bones_only' = primitive a forma di osso su ciascuna articolazione (armatura di anteprima). 'openpose' = scheletro 3D OpenPose-18 dai keypoint. 'scail' = rig a capsule 3D SCAIL (cilindri aperti con estremità chiuse a filo da sfere articolari). (predefinito: body_mesh) | DYNAMIC_COMBO | Sì | "body_mesh"<br>"bones_only"<br>"openpose"<br>"scail" |
| `bone_smooth_window` | Finestra di smoothing gaussiano sui keyframe di rotazione per osso / tracce keypoint. 0 = disattivato. 7-15 attenua rotazioni/instabilità dove Smooth a monte non intercetta i picchi. (predefinito: 0) | INT | Sì | 0-51, passo 2 |

#### Input di Body Mesh

Compaiono quando `mesh_style` è "body_mesh".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `bone_vis` | Forma della visualizzazione osso, rigidamente skinnata a ciascuna articolazione. 'off' = nessuna visualizzazione osso; 'octahedrons' = ossa direzionali in stile Blender. (predefinito: off) | DYNAMIC_COMBO | Sì | "off"<br>"octahedrons" |
| `bone_vis_radius_m` | Compare quando `bone_vis` = "octahedrons". Raggio in m (raggio della sfera / metà larghezza dell'ottaedro). (predefinito: 0.02) | FLOAT | Sì | 0.005-0.5 |
| `bone_vis_color` | Compare quando `bone_vis` = "octahedrons". Colori per vertice per osso (materiale non illuminato). 'white' = nessuno, 'rainbow_y' = gradiente jet dalla testa ai piedi. (predefinito: rainbow_y) | COMBO | Sì | "white"<br>"rainbow_y" |
| `shader` | Incorpora colori per vertice corrispondenti agli shader del nodo Render (COLOR_0 + KHR_materials_unlit). 'default' = nessun colore. (predefinito: default) | DYNAMIC_COMBO | Sì | "default"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic" |
| `rainbow_tilt_z` | Compare quando `shader` è una variante rainbow. Ruota l'asse del gradiente rainbow attorno a Z (avanti). Differenzia sinistra/destra. (predefinito: -35.0) | FLOAT | Sì | da -90.0 a 90.0 |
| `rainbow_tilt_x` | Compare quando `shader` è una variante rainbow. Ruota l'asse del gradiente rainbow attorno a X (destra). Differenzia davanti/dietro. (predefinito: 0.0) | FLOAT | Sì | da -90.0 a 90.0 |
| `person_palette_falloff` | Compare quando `shader` è una variante rainbow. Desaturazione per persona: ciascuna traccia riceve una miscela pastello (1 - falloff^k). (predefinito: 0.6) | FLOAT | Sì | 0.1-1.0 |

#### Input di Bones Only

Compaiono quando `mesh_style` è "bones_only".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `bone_vis` | Forma della visualizzazione osso, rigidamente skinnata a ciascuna articolazione. 'octahedrons' = ossa direzionali in stile Blender (articolazione → figlio primario). | DYNAMIC_COMBO | Sì | "octahedrons" |
| `bone_vis_radius_m` | Raggio in m (raggio della sfera / metà larghezza dell'ottaedro). (predefinito: 0.02) | FLOAT | Sì | 0.005-0.5 |
| `bone_vis_color` | Colori per vertice per osso (materiale non illuminato). 'white' = nessuno, 'rainbow_y' = gradiente jet dalla testa ai piedi. (predefinito: rainbow_y) | COMBO | Sì | "white"<br>"rainbow_y" |

#### Input di OpenPose

Compaiono quando `mesh_style` è "openpose".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_m` | Raggio della sfera in m. (predefinito: 0.010) | FLOAT | Sì | 0.005-0.1 |
| `stick_radius_m` | Metà larghezza dell'arto in m. Limitata automaticamente a bone_length x 0.1. (predefinito: 0.008) | FLOAT | Sì | 0.002-0.05 |
| `include_hands` | Aggiunge mani OpenPose 21+21 (polso + 5 dita x 4 articolazioni, base→punta) provenienti da pred_keypoints_3d. (predefinito: False) | BOOLEAN | Sì | True / False |
| `hand_marker_radius_m` | Raggio della sfera della mano in m. (predefinito: 0.005) | FLOAT | Sì | 0.001-0.1 |
| `hand_stick_radius_m` | Metà larghezza dell'arto della mano in m. (predefinito: 0.003) | FLOAT | Sì | 0.001-0.05 |
| `face_style` | Punti di riferimento del contorno del viso campionati da pred_vertices a ID vertice fissi della mesh della testa (richiede canonical_colors su pose_data). 'full' = tutti i ~30 punti; 'eyes_mouth' = solo occhi + labbra esterne. (predefinito: disabled) | COMBO | Sì | "disabled"<br>"full"<br>"eyes_mouth" |
| `face_marker_radius_m` | Raggio del punto del viso. 0 = automatico = 0.3 x marker_radius_m. (predefinito: 0.0) | FLOAT | Sì | 0.0-0.05 |

#### Input di SCAIL

Compaiono quando `mesh_style` è "scail".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `stick_radius_m` | Raggio del cilindro in m. Le ossa sono cilindri aperti a raggio costante; le sfere articolari (dimensionate automaticamente per corrispondere) chiudono le estremità aperte. Riferimento SCAIL = 0.0215 m. (predefinito: 0.022) | FLOAT | Sì | 0.002-0.1 |
| `marker_radius_m` | Raggio della sfera articolare. 0 = automatico = stick_radius_m (chiusura a filo). (predefinito: 0.0) | FLOAT | Sì | 0.0-0.1 |
| `material_roughness` | Rugosità PBR. Rif. SCAIL = 0.3. 1 = opaco; 0 = cromato. (predefinito: 0.3) | FLOAT | Sì | 0.0-1.0 |
| `include_hands` | Aggiunge 21+21 keypoint della mano + bastoncini a capsula per traccia. (predefinito: False) | BOOLEAN | Sì | True / False |
| `hand_marker_radius_m` | Raggio della sfera della mano in m. (predefinito: 0.005) | FLOAT | Sì | 0.001-0.05 |
| `hand_stick_radius_m` | Raggio del cilindro della mano in m. (predefinito: 0.003) | FLOAT | Sì | 0.001-0.05 |
| `face_style` | Punti di riferimento del contorno del viso campionati da pred_vertices (richiede canonical_colors su pose_data). 'full' = tutti i ~30 punti; 'eyes_mouth' = solo occhi + labbra esterne. (predefinito: disabled) | COMBO | Sì | "disabled"<br>"full"<br>"eyes_mouth" |

### Input BVH

Compaiono quando `format` è impostato su "bvh".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `units` | Unità di OFFSET/posizione BVH. 'cm' è lo standard mocap. (predefinito: cm) | COMBO | Sì | "cm"<br>"m" |

**Note:**

- Il formato `bvh` e gli stili mesh `body_mesh` e `bones_only` richiedono l'input `sam3d_body_model`, a meno che i `pose_data` stessi contengano un override dello scheletro (un dizionario `_skeleton_override`, per esempio da un nodo KimodoSample). Il nodo genera un errore se nessuno dei due è disponibile. Gli stili `openpose` e `scail` sono indipendenti dal rig e funzionano direttamente dai keypoint senza il modello del corpo.
- Nel formato `bvh`, l'output contiene un singolo scheletro. Quando `track_index` è -1 (tutte le tracce), viene usata la prima traccia.
- Le opzioni `full` e `eyes_mouth` di `face_style` richiedono `canonical_colors` sui dati di posa, presente quando i dati di posa provengono dalla pipeline MHR insieme al modello del corpo.
- `bone_smooth_window` avanza a passi di 2 tra 0 e 51.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `model_3d` | Il file di animazione generato: un GLB animato o una clip mocap BVH, pronto per essere salvato su disco con un nodo come Save 3D Model. | 3D_FILE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildPoseFile/it.md)

---
**Source fingerprint (SHA-256):** `f3672f0749c4f9affcc92da98198c5b142f6fcd9f5e317ab43dd7e53533c0fa3`

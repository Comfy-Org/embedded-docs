# Load3DAnimation

Il nodo Load3DAnimation è un nodo principale per il caricamento e l'elaborazione di file di modelli 3D. Quando si carica il nodo, recupera automaticamente le risorse 3D disponibili da `ComfyUI/input/3d/`. È inoltre possibile caricare file 3D supportati per l'anteprima utilizzando la funzione di caricamento.

> - La maggior parte delle funzioni di questo nodo è la stessa del nodo Load 3D, ma questo nodo supporta il caricamento di modelli con animazioni e puoi visualizzare in anteprima le animazioni corrispondenti nel nodo.
> - Il contenuto di questa documentazione è lo stesso del nodo Load3D, perché, a parte l'anteprima e la riproduzione delle animazioni, le loro capacità sono identiche.

**Formati supportati**
Attualmente, questo nodo supporta diversi formati di file 3D, tra cui `.gltf`, `.glb`, `.obj`, `.fbx` e `.stl`.

**Preferenze dei nodi 3D**
Alcune preferenze correlate ai nodi 3D possono essere configurate nel menu delle impostazioni di ComfyUI. Fai riferimento alla seguente documentazione per le impostazioni corrispondenti:

[Menu Impostazioni](https://docs.comfy.org/interface/settings/3d)

Oltre ai normali output del nodo, Load3D dispone di numerose impostazioni relative alla vista 3D nel menu del canvas.

## Input

| Nome parametro | Descrizione | Tipo | Predefinito | Intervallo |
| --- | --- | --- | --- | --- |
| model_file | Percorso del file del modello 3D, supporta il caricamento, per impostazione predefinita legge i file del modello da `ComfyUI/input/3d/` | Selezione file | - | Formati supportati |
| width | Larghezza di rendering del canvas | INT | 1024 | 1-4096 |
| height | Altezza di rendering del canvas | INT | 1024 | 1-4096 |

## Output

| Nome parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| image | Immagine renderizzata sul canvas | IMAGE |
| mask | Maschera contenente la posizione corrente del modello | MASK |
| mesh_path | Percorso del file del modello | STRING |
| normal | Mappa normale | IMAGE |
| lineart | Immagine line art di output; il corrispondente `edge_threshold` può essere regolato nel menu del modello del canvas | IMAGE |
| camera_info | Informazioni sulla camera | LOAD3D_CAMERA |
| recording_video | Video registrato (solo quando esiste una registrazione) | VIDEO |

Anteprima di tutti gli output:
![Dimostrazione operazioni di vista](../Load3D/asset/load3d_outputs.webp)

## Descrizione dell'area canvas

L'area canvas del nodo Load3D contiene numerose operazioni di vista, tra cui:

- Impostazioni della vista di anteprima (griglia, colore di sfondo, vista di anteprima)
- Controllo camera: controlla FOV, tipo di camera
- Intensità di illuminazione globale: regola l'intensità della luce
- Registrazione video: registra ed esporta video
- Esportazione modello: supporta i formati `GLB`, `OBJ`, `STL`
- E altro ancora

![Interfaccia del nodo Load 3D](../Load3D/asset/load3d_ui.jpg)

1. Contiene diversi menu e menu nascosti del nodo Load 3D
2. Menu per `ridimensionamento della finestra di anteprima` e `registrazione video del canvas`
3. Assi di controllo della vista 3D
4. Miniatura di anteprima
5. Impostazioni delle dimensioni dell'anteprima: scala la visualizzazione dell'anteprima impostando le dimensioni e ridimensionando poi la finestra

### 1. Operazioni di vista

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  Il tuo browser non supporta la riproduzione video.
</video>

Operazioni di controllo della vista:

- Clic sinistro + trascina: ruota la vista
- Clic destro + trascina: sposta la vista
- Rotellina centrale o clic centrale + trascina: ingrandisci/riduci
- Assi delle coordinate: cambia vista

### 2. Funzioni del menu sinistro

![Menu](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

Nel canvas, alcune impostazioni sono nascoste nel menu. Fai clic sul pulsante del menu per espandere i diversi menu

- 1. Scena: contiene griglia della finestra di anteprima, colore di sfondo, impostazioni di anteprima
- 2. Modello: modalità di rendering del modello, materiali texture, impostazioni della direzione verso l'alto
- 3. Camera: passa tra vista ortografica e prospettica e imposta l'ampiezza dell'angolo prospettico
- 4. Luce: intensità di illuminazione globale della scena
- 5. Esporta: esporta il modello in altri formati (GLB, OBJ, STL)

#### Scena

![menu scena](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

Il menu Scena fornisce alcune funzioni di base per le impostazioni della scena

1. Mostra/Nascondi griglia
2. Imposta colore di sfondo
3. Fai clic per caricare un'immagine di sfondo
4. Nascondi l'anteprima

#### Modello

![Menu_Scene](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

Il menu Modello fornisce alcune funzioni relative al modello

1. **Direzione verso l'alto**: determina quale asse è la direzione verso l'alto per il modello
2. **Modalità materiale**: cambia le modalità di rendering del modello - Originale, Normale, Wireframe, Lineart

#### Camera

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

Questo menu fornisce il passaggio tra vista ortografica e prospettica e le impostazioni dell'ampiezza dell'angolo prospettico

1. **Camera**: passa rapidamente tra la vista ortografica e quella prospettica
2. **FOV**: regola l'angolo FOV

#### Luce

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

Tramite questo menu, puoi regolare rapidamente l'intensità di illuminazione globale della scena

#### Esporta

![menu_export](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

Questo menu fornisce la possibilità di convertire ed esportare rapidamente i formati del modello

### 3. Funzioni del menu destro

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/recording.mp4" type="video/mp4">
  Il tuo browser non supporta la riproduzione video.
</video>

Il menu destro ha due funzioni principali:

1. **Reimposta proporzioni vista**: dopo aver fatto clic sul pulsante, la vista regolerà le proporzioni dell'area di rendering del canvas in base alla larghezza e all'altezza impostate
2. **Registrazione video**: consente di registrare le operazioni correnti della vista 3D come video, consente l'importazione e può essere inviato come `recording_video` ai nodi successivi

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAnimation/it.md)

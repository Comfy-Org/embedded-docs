# Carica 3D & Animazione

Il nodo Load3D è un nodo principale per il caricamento e l'elaborazione di file di modelli 3D. Quando si carica il nodo, recupera automaticamente le risorse 3D disponibili da `ComfyUI/input/3d/`. È inoltre possibile caricare file 3D supportati per l'anteprima utilizzando la funzione di caricamento.

**Formati supportati**
Attualmente, questo nodo supporta diversi formati di file 3D, tra cui `.gltf`, `.glb`, `.obj`, `.fbx` e `.stl`.

**Preferenze dei nodi 3D**
Alcune preferenze correlate per i nodi 3D possono essere configurate nel menu delle impostazioni di ComfyUI. Fare riferimento alla seguente documentazione per le impostazioni corrispondenti:

[Menu delle impostazioni](https://docs.comfy.org/interface/settings/3d)

Oltre agli output regolari del nodo, Load3D presenta numerose impostazioni relative alla visualizzazione 3D nel menu della tela.

## Input

| Nome parametro | Descrizione | Tipo | Predefinito | Intervallo |
| --- | --- | --- | --- | --- |
| model_file | Percorso del file del modello 3D, supporta il caricamento, per impostazione predefinita legge i file del modello da `ComfyUI/input/3d/` | Selezione file | - | Formati supportati |
| width | Larghezza di rendering della tela | INT | 1024 | 1-4096 |
| height | Altezza di rendering della tela | INT | 1024 | 1-4096 |

## Output

| Nome parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| image | Immagine renderizzata della tela | IMAGE |
| mask | Maschera contenente la posizione corrente del modello | MASK |
| mesh_path | Percorso del file del modello | STRING |
| normal | Mappa normale | IMAGE |
| lineart | Output immagine line art, il corrispondente `edge_threshold` può essere regolato nel menu del modello della tela | IMAGE |
| camera_info | Informazioni sulla telecamera | LOAD3D_CAMERA |
| recording_video | Video registrato (solo quando esiste una registrazione) | VIDEO |

Anteprima di tutti gli output:
![Demo operazioni di visualizzazione](./asset/load3d_outputs.webp)

## Descrizione dell'area della tela

L'area della tela del nodo Load3D contiene numerose operazioni di visualizzazione, tra cui:

- Impostazioni di visualizzazione dell'anteprima (griglia, colore di sfondo, vista di anteprima)
- Controllo della telecamera: Controllo FOV, tipo di telecamera
- Intensità di illuminazione globale: Regola l'intensità dell'illuminazione
- Registrazione video: Registra ed esporta video
- Esportazione del modello: Supporta i formati `GLB`, `OBJ`, `STL`
- E altro ancora

![Interfaccia del nodo Load 3D](./asset/load3d_ui.jpg)

1. Contiene diversi menu e menu nascosti del nodo Load 3D
2. Menu per `ridimensionamento della finestra di anteprima` e `registrazione video della tela`
3. Assi di operazione della vista 3D
4. Miniatura di anteprima
5. Impostazioni dimensioni anteprima, ridimensiona la visualizzazione dell'anteprima impostando le dimensioni e quindi ridimensionando la finestra

### 1. Operazioni di visualizzazione

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  Il tuo browser non supporta la riproduzione di video.
</video>

Operazioni di controllo della vista:

- Clic sinistro + trascina: Ruota la vista
- Clic destro + trascina: Sposta la vista
- Scorrimento della rotellina o clic centrale + trascina: Zoom avanti/indietro
- Assi delle coordinate: Cambia vista

### 2. Funzioni del menu sinistro

![Menu](./asset/menu.webp)

Nella tela, alcune impostazioni sono nascoste nel menu. Fare clic sul pulsante del menu per espandere i diversi menu

- 1. Scena: Contiene la griglia della finestra di anteprima, il colore di sfondo, le impostazioni di anteprima
- 2. Modello: Modalità di rendering del modello, materiali texture, impostazioni della direzione verso l'alto
- 3. Telecamera: Passa tra viste ortografiche e prospettiche e imposta la dimensione dell'angolo prospettico
- 4. Luce: Intensità di illuminazione globale della scena
- 5. Esporta: Esporta il modello in altri formati (GLB, OBJ, STL)

#### Scena

![menu scena](./asset/menu_scene.webp)

Il menu Scena fornisce alcune funzioni di base per l'impostazione della scena

1. Mostra/Nascondi griglia
2. Imposta colore di sfondo
3. Fai clic per caricare un'immagine di sfondo
4. Nascondi l'anteprima

#### Modello

![Menu_Scene](./asset/menu_model.webp)

Il menu Modello fornisce alcune funzioni relative al modello

1. **Direzione verso l'alto**: Determina quale asse è la direzione verso l'alto per il modello
2. **Modalità materiale**: Cambia le modalità di rendering del modello - Originale, Normale, Wireframe, Lineart

#### Telecamera

![menu_modelmenu_camera](./asset/menu_camera.webp)

Questo menu fornisce il passaggio tra viste ortografiche e prospettiche e le impostazioni della dimensione dell'angolo prospettico

1. **Telecamera**: Passa rapidamente tra viste ortografiche e ortografiche
2. **FOV**: Regola l'angolo FOV

#### Luce

![menu_modelmenu_camera](./asset/menu_light.webp)

Attraverso questo menu, è possibile regolare rapidamente l'intensità di illuminazione globale della scena

#### Esporta

![menu_export](./asset/menu_export.webp)

Questo menu fornisce la possibilità di convertire ed esportare rapidamente i formati del modello

### 3. Funzioni del menu destro

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  Il tuo browser non supporta la riproduzione di video.
</video>

Il menu destro ha due funzioni principali:

1. **Reimposta proporzioni vista**: Dopo aver fatto clic sul pulsante, la vista regolerà le proporzioni dell'area di rendering della tela in base alla larghezza e all'altezza impostate
2. **Registrazione video**: Consente di registrare le operazioni correnti della vista 3D come video, consente l'importazione e può essere emesso come `recording_video` ai nodi successivi

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3D/it.md)

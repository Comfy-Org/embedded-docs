# Preview3D

Il nodo Preview3D è principalmente utilizzato per visualizzare in anteprima gli output di modelli 3D. Questo nodo accetta due input: uno è `camera_info` dal nodo Load3D, e l'altro è il percorso del file del modello 3D. Il percorso del file del modello deve trovarsi nella cartella `ComfyUI/output`.

**Formati supportati**
Attualmente, questo nodo supporta diversi formati di file 3D, tra cui `.gltf`, `.glb`, `.obj`, `.fbx` e `.stl`.

**Preferenze dei nodi 3D**
Alcune preferenze correlate ai nodi 3D possono essere configurate nel menu delle impostazioni di ComfyUI. Fare riferimento alla seguente documentazione per le impostazioni corrispondenti:
[Menu delle impostazioni](https://docs.comfy.org/interface/settings/3d)

## Input

| Nome parametro | Descrizione | Tipo |
| --- | --- | --- |
| camera_info | Informazioni sulla camera | LOAD3D_CAMERA |
| model_file | Percorso del file del modello sotto `ComfyUI/output/` | LOAD3D_CAMERA |

## Descrizione dell'area Canvas

Attualmente, i nodi correlati al 3D nel frontend di ComfyUI condividono lo stesso componente canvas, quindi le loro operazioni di base sono per lo più coerenti, fatta eccezione per alcune differenze funzionali.

> I seguenti contenuti e l'interfaccia si basano principalmente sul nodo Load3D. Per le funzionalità specifiche, fare riferimento all'interfaccia effettiva del nodo.

L'area Canvas include varie operazioni di visualizzazione, come:

- Impostazioni di visualizzazione dell'anteprima (griglia, colore di sfondo, vista di anteprima)
- Controllo camera: FOV, tipo di camera
- Intensità di illuminazione globale: regola l'illuminazione
- Esportazione del modello: supporta i formati `GLB`, `OBJ`, `STL`
- ecc.

![Interfaccia del nodo Load 3D](./asset/preview3d_canvas.jpg)

1. Contiene diversi menu e menu nascosti del nodo Load 3D
2. Asse di controllo della vista 3D

### 1. Operazioni di visualizzazione

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  Il browser non supporta la riproduzione video.
</video>

Operazioni di controllo della vista:

- Clic sinistro + trascina: ruota la vista
- Clic destro + trascina: panoramica della vista
- Rotellina centrale o clic centrale + trascina: zoom avanti/indietro
- Asse delle coordinate: cambia vista

### 2. Funzioni del menu sinistro

![Menu](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

Nell'area di anteprima, alcuni menu di controllo della vista sono nascosti nel menu. Fare clic sul pulsante del menu per espandere i diversi menu.

- 1. Scena: contiene la griglia della finestra di anteprima, il colore di sfondo e le impostazioni della miniatura
- 2. Modello: modalità di rendering del modello, materiale della texture, impostazioni della direzione verso l'alto
- 3. Camera: passa tra vista ortografica e prospettica, imposta l'angolo prospettico
- 4. Luce: intensità di illuminazione globale della scena
- 5. Esporta: esporta il modello in altri formati (GLB, OBJ, STL)

#### Scena

![scene menu](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

Il menu Scena fornisce alcune funzioni di impostazione di base della scena:

1. Mostra/nascondi griglia
2. Imposta il colore di sfondo
3. Fare clic per caricare un'immagine di sfondo
4. Nascondi miniatura di anteprima

#### Modello

![Menu_Scene](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

Il menu Modello fornisce alcune funzioni relative al modello:

1. **Direzione verso l'alto**: determina quale asse rappresenta la direzione verso l'alto per il modello
2. **Modalità materiale**: cambia le modalità di rendering del modello - Original, Normal, Wireframe, Lineart

#### Camera

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

Questo menu consente di passare tra vista ortografica e prospettica e di impostare l'ampiezza dell'angolo prospettico:

1. **Camera**: passa rapidamente tra vista ortografica e prospettica
2. **FOV**: regola l'angolo FOV

#### Luce

![menu_modelmenu_camera](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

Tramite questo menu è possibile regolare rapidamente l'intensità di illuminazione globale della scena

#### Esporta

![menu_export](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

Questo menu offre la possibilità di convertire ed esportare rapidamente i formati del modello

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3D/it.md)

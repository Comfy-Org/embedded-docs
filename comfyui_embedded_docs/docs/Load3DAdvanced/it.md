# Carica 3D (Avanzato)

Il nodo Load 3D (Advanced) carica un file di modello 3D dalla directory `input/3d` di ComfyUI e fornisce i dati del modello insieme al posizionamento del modello e alle informazioni sulla camera catturate nello stato del viewport del visualizzatore 3D. Supporta i formati di file 3D comuni e consente di impostare la larghezza e l'altezza di rendering del viewport in pixel. Questo nodo è sperimentale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_file` | Il file di modello 3D da caricare. Seleziona "none" per saltare il caricamento di un file di modello. I file possono anche essere caricati tramite il widget. | COMBO | Sì | `"none"`<br>File di modello 3D disponibili nella directory `input/3d` |
| `viewport_state` | Lo stato corrente del viewport contenente le informazioni su camera e modello dal visualizzatore 3D. | LOAD3D | Sì | - |
| `width` | Larghezza di rendering del viewport in pixel (predefinito: 1024). | INT | Sì | Min: 1<br>Max: 4096<br>Predefinito: 1024<br>Passo: 1 |
| `height` | Altezza di rendering del viewport in pixel (predefinito: 1024). | INT | Sì | Min: 1<br>Max: 4096<br>Predefinito: 1024<br>Passo: 1 |

**Note sui parametri:**
- Il parametro `model_file` elenca solo i file con le seguenti estensioni: .gltf, .glb, .obj, .fbx, .stl
- I file devono essere inseriti nella directory `input/3d` della tua installazione ComfyUI; vengono cercate anche le sottocartelle e i percorsi dei file sono mostrati relativamente alla directory di input
- Se `model_file` è "none", non viene caricato alcun dato del modello e l'output `model_3d` sarà vuoto
- Se `model_file` è impostato su un file che non esiste, il nodo restituisce un errore di validazione: "Invalid 3D model file: {model_file}"
- Se `viewport_state` non è un oggetto stato del viewport valido, viene considerato vuoto, quindi `model_3d_info` diventa una lista vuota e `camera_info` viene restituito vuoto

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model_3d` | File di modello 3D caricato (glb/obj/stl/ecc.). Vuoto se non è stato selezionato alcun file di modello. | FILE3DANY |
| `model_3d_info` | Posizionamento di ciascun modello nella scena: posizione, rotazione e scala (spazio mondo con Y verso l'alto). | LOAD3DMODELINFO |
| `camera_info` | Informazioni sulla camera del viewport: posizione, destinazione look-at, zoom e tipo. | LOAD3DCAMERA |
| `width` | Larghezza di rendering del viewport in pixel. | INT |
| `height` | Altezza di rendering del viewport in pixel. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/it.md)

---
**Source fingerprint (SHA-256):** `c79c53dde0c8b3afb7df7b972df749f5040c92d48b47e355c4497d9b0cbf1c22`

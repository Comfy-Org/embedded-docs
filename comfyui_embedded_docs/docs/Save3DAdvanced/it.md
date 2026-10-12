# Save3DAdvanced

Salva un modello 3D in un file nella directory di output di ComfyUI e genera un'anteprima della scena salvata. Passa inoltre il modello 3D, il suo posizionamento nella scena, le informazioni sulla camera e le dimensioni del viewport ai nodi a valle. Quando il posizionamento del modello o le informazioni sulla camera non sono collegati, il nodo usa i valori memorizzati nello stato del viewport.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_3d` | File modello 3D da un nodo 3D a monte. | FILE3D | Sì | GLB<br>GLTF<br>FBX<br>OBJ<br>STL<br>USDZ<br>Any |
| `filename_prefix` | Prefisso usato per il nome del file salvato (predefinito: "3d/ComfyUI"). | STRING | Sì | Testo libero |
| `viewport_state` | Stato del viewport contenente informazioni sulla camera e sul posizionamento del modello, tipicamente da un nodo Load 3D. | LOAD3D | Sì | - |
| `model_3d_info` | Posizionamento di ciascun modello nella scena: posizione, rotazione e scala (spazio mondo con Y verso l'alto). Sostituisce il posizionamento del modello memorizzato in `viewport_state` quando collegato. | LOAD3DMODELINFO | No | - |
| `camera_info` | Informazioni sulla camera del viewport: posizione, target di puntamento, zoom e tipo. Sostituisce le informazioni sulla camera memorizzate in `viewport_state` quando collegato. | LOAD3DCAMERA | No | - |
| `width` | Larghezza di rendering del viewport in pixel (predefinito: 1024). | INT | Sì | da 1 a 4096 |
| `height` | Altezza di rendering del viewport in pixel (predefinito: 1024). | INT | Sì | da 1 a 4096 |

Nota: `model_3d_info` e `camera_info` sono opzionali. Quando uno dei due input non è collegato, il nodo usa i valori corrispondenti memorizzati in `viewport_state`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_3d` | Il file modello 3D passato dall'input. | FILE3D |
| `model_3d_info` | Posizionamento di ciascun modello nella scena: posizione, rotazione e scala (spazio mondo con Y verso l'alto). | LOAD3DMODELINFO |
| `camera_info` | Informazioni sulla camera del viewport: posizione, target di puntamento, zoom e tipo. | LOAD3DCAMERA |
| `width` | Il valore di larghezza di rendering passato dall'input. | INT |
| `height` | Il valore di altezza di rendering passato dall'input. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/it.md)

---
**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`

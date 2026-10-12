# Anteprima 3D (Avanzata)

Questo nodo mostra un'anteprima di un modello 3D nell'interfaccia utente senza salvare il file nella cartella di output di ComfyUI. Salva il modello in un file temporaneo e inoltra i dati del modello, le informazioni sul modello, le informazioni sulla camera e le dimensioni dell'anteprima per ulteriori elaborazioni a valle.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `model_3d` | File di modello 3D da un nodo 3D a monte. | FILE3D | Sì | GLB, GLTF, FBX, OBJ, STL, USDZ o qualsiasi formato 3D supportato |
| `model_3d_info` | Posizionamento di ciascun modello nella scena: posizione, rotazione e scala (spazio mondo con Y verso l'alto). Opzionale. Opzione avanzata. | LOAD3DMODELINFO | No | - |
| `viewport_state` | Lo stato corrente della viewport contenente le informazioni sulla camera e sui modelli. | LOAD3D | Sì | - |
| `camera_info` | Informazioni sulla camera della viewport: posizione, punto di mira, zoom e tipo. Opzionale. Opzione avanzata. | LOAD3DCAMERA | No | - |
| `width` | Larghezza di render della viewport in pixel. Predefinito: 1024. | INT | Sì | 1 to 4096 |
| `height` | Altezza di render della viewport in pixel. Predefinito: 1024. | INT | Sì | 1 to 4096 |

Nota: quando `camera_info` o `model_3d_info` non sono connessi, i loro valori vengono presi da `viewport_state` quando disponibili. Se `viewport_state` non contiene informazioni sulla camera, `camera_info` è None. Se `viewport_state` non contiene informazioni sul modello, `model_3d_info` ha come valore predefinito una lista vuota. Se `viewport_state` non è un dizionario, viene trattato come vuoto.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_3d` | File di modello 3D (glb/obj/stl/ecc.) da un nodo 3D a monte, inoltrato senza modifiche. | FILE3D |
| `model_3d_info` | Posizionamento di ciascun modello nella scena: posizione, rotazione e scala (spazio mondo con Y verso l'alto). Usa il valore di input oppure, in mancanza, il valore memorizzato in `viewport_state`. | LOAD3DMODELINFO |
| `camera_info` | Informazioni sulla camera della viewport: posizione, punto di mira, zoom e tipo. Usa il valore di input oppure, in mancanza, il valore memorizzato in `viewport_state`. | LOAD3DCAMERA |
| `width` | Larghezza di render della viewport in pixel. | INT |
| `height` | Altezza di render della viewport in pixel. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/it.md)

---
**Source fingerprint (SHA-256):** `f2d3d35ed35fe68edebcde8fd8421d26850b04e3ae5b7147f1020c8ed904c480`

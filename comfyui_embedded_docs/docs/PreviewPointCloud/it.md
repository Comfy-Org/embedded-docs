# PreviewPointCloud

Il nodo Preview Point Cloud consente di visualizzare un file di nuvola di punti 3D nell'interfaccia di ComfyUI senza salvarlo nella directory di output di ComfyUI. Salva la nuvola di punti in una posizione temporanea e la visualizza in una finestra di anteprima 3D, passando anche i dati del modello, le informazioni sul modello, le informazioni sulla fotocamera e le dimensioni dell'anteprima per ulteriori elaborazioni.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_3d` | File di nuvola di punti (.ply) | FILE3D | Sì | - |
| `model_3d_info` | Informazioni sul modello 3D | LOAD3DMODELINFO | No | - |
| `viewport_state` | Lo stato corrente del viewport 3D | LOAD3D | Sì | - |
| `camera_info` | Informazioni sulla fotocamera per la vista 3D | LOAD3DCAMERA | No | - |
| `width` | Larghezza della finestra di anteprima (predefinito: 1024) | INT | Sì | 1 a 4096 |
| `height` | Altezza della finestra di anteprima (predefinito: 1024) | INT | Sì | 1 a 4096 |

Nota: `model_3d_info` e `camera_info` sono input avanzati opzionali. Quando non sono connessi, il nodo ricorre ai valori corrispondenti memorizzati in `viewport_state`. Il file della nuvola di punti viene scritto nella directory temporanea di ComfyUI anziché nella directory di output. Questo è un nodo di output (terminale), quindi viene usato principalmente per visualizzare l'anteprima nell'interfaccia.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_3d` | I dati del modello della nuvola di punti | FILE3D |
| `model_3d_info` | Informazioni sul modello 3D | LOAD3DMODELINFO |
| `camera_info` | Informazioni sulla fotocamera per la vista 3D | LOAD3DCAMERA |
| `width` | Larghezza della finestra di anteprima | INT |
| `height` | Altezza della finestra di anteprima | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/it.md)

---
**Source fingerprint (SHA-256):** `a0b13d9d5658343a6a7c25408d5e5cd9249c92264b76aa448a6553b370f4d782`

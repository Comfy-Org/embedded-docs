# PreviewGaussianSplat

Il nodo PreviewGaussianSplat visualizza un file 3D gaussian splat in una finestra di anteprima senza salvarlo nella directory di output di ComfyUI. Accetta un file di modello 3D in vari formati gaussian splat, salva una copia temporanea per l'anteprima e passa i dati del modello per ulteriori elaborazioni nel workflow. Questo nodo è contrassegnato come sperimentale e funge da nodo di output.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_3d` | Un file 3D gaussian splat. | FILE3D | Sì | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | Informazioni opzionali di metadati sul modello 3D. Quando non è collegato, il nodo usa le informazioni sul modello da `viewport_state`. | LOAD3DMODELINFO | No | - |
| `viewport_state` | Lo stato corrente del viewport 3D, incluse le informazioni su camera e modello. | LOAD3D | Sì | - |
| `camera_info` | Informazioni opzionali sulla camera per l'anteprima. Quando non è collegato, il nodo usa le informazioni sulla camera da `viewport_state`. | LOAD3DCAMERA | No | - |
| `width` | La larghezza del rendering di anteprima in pixel (predefinito: 1024). | INT | Sì | 1 a 4096 |
| `height` | L'altezza del rendering di anteprima in pixel (predefinito: 1024). | INT | Sì | 1 a 4096 |

Nota: quando `camera_info` o `model_3d_info` non vengono forniti, il nodo utilizza le informazioni su camera e modello memorizzate in `viewport_state`. Se `viewport_state` non è un oggetto di stato del viewport valido, viene considerato vuoto.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model_3d` | Il file 3D gaussian splat di input, passato invariato. | FILE3D |
| `model_3d_info` | Informazioni di metadati sul modello 3D, provenienti dall'input o derivate dallo stato del viewport. | LOAD3DMODELINFO |
| `camera_info` | Informazioni sulla camera per l'anteprima, provenienti dall'input o derivate dallo stato del viewport. | LOAD3DCAMERA |
| `width` | La larghezza del rendering di anteprima. | INT |
| `height` | L'altezza del rendering di anteprima. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/it.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`

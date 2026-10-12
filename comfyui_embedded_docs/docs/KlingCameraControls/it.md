# KlingCameraControls

Il nodo Kling Camera Controls consente di configurare vari parametri di movimento e rotazione della camera per creare effetti di controllo del movimento nella generazione video. Fornisce controlli per il posizionamento, la rotazione e lo zoom della camera per simulare diversi movimenti di camera.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `camera_control_type` | Specifica il tipo di configurazione del controllo della camera da usare | COMBO | Sì | `"simple"`<br>`"advanced"` |
| `horizontal_movement` | Controlla il movimento della camera lungo l'asse orizzontale (asse x). Un valore negativo indica sinistra, positivo indica destra (predefinito: 0.0) | FLOAT | No | -10.0 to 10.0 |
| `vertical_movement` | Controlla il movimento della camera lungo l'asse verticale (asse y). Un valore negativo indica verso il basso, positivo verso l'alto (predefinito: 0.0) | FLOAT | No | -10.0 to 10.0 |
| `pan` | Controlla la rotazione della camera sul piano verticale (asse x). Un valore negativo indica rotazione verso il basso, positivo verso l'alto (predefinito: 0.5) | FLOAT | No | -10.0 to 10.0 |
| `tilt` | Controlla la rotazione della camera sul piano orizzontale (asse y). Un valore negativo indica rotazione a sinistra, positivo a destra (predefinito: 0.0) | FLOAT | No | -10.0 to 10.0 |
| `roll` | Controlla la quantità di rollio della camera (asse z). Un valore negativo indica in senso antiorario, positivo in senso orario (predefinito: 0.0) | FLOAT | No | -10.0 to 10.0 |
| `zoom` | Controlla la variazione della lunghezza focale della camera. Un valore negativo indica un campo visivo più stretto, positivo un campo visivo più ampio (predefinito: 0.0) | FLOAT | No | -10.0 to 10.0 |

**Nota:** Almeno uno dei parametri di controllo della camera (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll` o `zoom`) deve avere un valore diverso da zero affinché la configurazione sia valida.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `camera_control` | Restituisce le impostazioni del controllo camera configurate per l'uso nella generazione video | CAMERA_CONTROL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/it.md)

---
**Source fingerprint (SHA-256):** `dbba1083b662bb2563c77dec857e4f3123e4e53d58a1d51f2646288af28ebba0`

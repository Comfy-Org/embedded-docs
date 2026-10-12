# Crea Info Camera

Il nodo Create Camera Info costruisce una struttura di informazioni della camera per il rendering 3D. Supporta tre modalità per definire la camera: orbita (imbardata/beccheggio/distanza attorno a un target), look_at (posizione esplicita nel mondo) e quaternione (posizione più rotazione). Il sistema di coordinate è destrorso con Y come asse verticale.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `mode` | Come definire la camera: angoli di orbita, una posizione esplicita o una posizione + quaternione. | DYNAMIC_COMBO | Sì | `"orbit"`<br>`"look_at"`<br>`"quaternion"` |
| `target_x` | Punto di mira (perno/obiettivo dell'orbita). In modalità orbita, spostalo per pan/traslare l'intera camera. Ignorato in modalità quaternione. Impostazione predefinita all'origine. (predefinito: 0.0) | FLOAT | No | -1000.0 to 1000.0 |
| `target_y` | Componente Y del punto di mira. (predefinito: 0.0) | FLOAT | No | -1000.0 to 1000.0 |
| `target_z` | Componente Z del punto di mira. (predefinito: 0.0) | FLOAT | No | -1000.0 to 1000.0 |
| `roll` | Rollio della camera attorno all'asse di vista, in gradi. (predefinito: 0.0) | FLOAT | No | -180.0 to 180.0 |
| `fov` | Campo visivo verticale in gradi. (predefinito: 35.0) | FLOAT | No | 1.0 to 120.0 |
| `zoom` | Zoom digitale (moltiplicatore di lunghezza focale). Valori maggiori di 1 ingrandiscono senza spostare la camera. (predefinito: 1.0) | FLOAT | No | 0.01 to 100.0 |
| `camera_type` | Proiezione utilizzata da Render Splat: prospettica (scorcio) o ortografica (parallela). (predefinito: "perspective") | COMBO | No | `"perspective"`<br>`"orthographic"` |

### Parametri specifici della modalità

Quando `mode` è impostato su `"orbit"`, i seguenti parametri diventano disponibili:

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `yaw` | Angolo di rotazione orizzontale attorno al target. (predefinito: 35.0) | FLOAT | Sì | -360.0 to 360.0 |
| `pitch` | Angolo di rotazione verticale attorno al target. (predefinito: 30.0) | FLOAT | Sì | -89.0 to 89.0 |
| `distance` | Distanza della camera dal target. (predefinito: 4.0) | FLOAT | Sì | 0.01 to 1000.0 |

Quando `mode` è impostato su `"look_at"`, i seguenti parametri diventano disponibili:

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `position_x` | Posizione della camera nello spazio mondo (destrorso, Y-up). (predefinito: 4.0) | FLOAT | Sì | -1000.0 to 1000.0 |
| `position_y` | Componente Y della posizione della camera. (predefinito: 4.0) | FLOAT | Sì | -1000.0 to 1000.0 |
| `position_z` | Componente Z della posizione della camera. (predefinito: 4.0) | FLOAT | Sì | -1000.0 to 1000.0 |

Quando `mode` è impostato su `"quaternion"`, i seguenti parametri diventano disponibili:

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `position_x` | Posizione della camera nello spazio mondo (destrorso, Y-up). (predefinito: 4.0) | FLOAT | Sì | -1000.0 to 1000.0 |
| `position_y` | Componente Y della posizione della camera. (predefinito: 4.0) | FLOAT | Sì | -1000.0 to 1000.0 |
| `position_z` | Componente Z della posizione della camera. (predefinito: 4.0) | FLOAT | Sì | -1000.0 to 1000.0 |
| `quat_x` | Componente X del quaternione di rotazione mondiale della camera. (predefinito: 0.0) | FLOAT | Sì | -1.0 to 1.0 |
| `quat_y` | Componente Y del quaternione di rotazione mondiale della camera. (predefinito: 0.0) | FLOAT | Sì | -1.0 to 1.0 |
| `quat_z` | Componente Z del quaternione di rotazione mondiale della camera. (predefinito: 0.0) | FLOAT | Sì | -1.0 to 1.0 |
| `quat_w` | Quaternione di rotazione mondiale della camera (three.js: guarda lungo il -Z locale). Normalizzato automaticamente. (predefinito: 1.0) | FLOAT | Sì | -1.0 to 1.0 |

**Nota:** I parametri `target_x`, `target_y` e `target_z` vengono ignorati quando `mode` è impostato su `"quaternion"`. In modalità `"orbit"`, questi parametri target definiscono il punto perno attorno al quale orbita la camera.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `camera_info` | Struttura di informazioni della camera contenente posizione, rotazione, campo visivo, zoom e tipo di proiezione per il rendering 3D. | LOAD3DCAMERA |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraInfo/it.md)

---
**Source fingerprint (SHA-256):** `5a9703e8e01ad2cd92a97da8d892c278765a9cef8bcd38e3336d1f73717d9895`

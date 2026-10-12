# TencentImageToModelNode

Questo nodo utilizza l'API Hunyuan3D Pro di Tencent per generare un modello 3D da una o più immagini di input. Elabora le immagini, le invia all'API e restituisce i file del modello 3D generato nei formati GLB e OBJ, insieme a mappe di texture opzionali.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | La versione del modello Hunyuan3D da utilizzare. L'opzione LowPoly non è disponibile per il modello `3.1`. | COMBO | Sì | `"3.0"`<br>`"3.1"` |
| `image` | L'immagine di input principale utilizzata per generare il modello 3D. Deve avere dimensioni minime di 128x128 pixel. | IMAGE | Sì | - |
| `image_left` | Un'immagine opzionale del lato sinistro dell'oggetto per la generazione multi-vista. Deve avere dimensioni minime di 128x128 pixel. | IMAGE | No | - |
| `image_right` | Un'immagine opzionale del lato destro dell'oggetto per la generazione multi-vista. Deve avere dimensioni minime di 128x128 pixel. | IMAGE | No | - |
| `image_back` | Un'immagine opzionale del lato posteriore dell'oggetto per la generazione multi-vista. Deve avere dimensioni minime di 128x128 pixel. | IMAGE | No | - |
| `face_count` | Il numero obiettivo di facce per il modello 3D generato (predefinito: 500000). | INT | Sì | 3000 - 1500000 |
| `generate_type` | Il tipo di modello 3D da generare. Selezionando un'opzione vengono rivelati ulteriori parametri correlati. | DYNAMICCOMBO | Sì | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `generate_type.pbr` | Abilita la generazione di materiali PBR (Physically Based Rendering). Questo parametro è visibile solo quando `generate_type` è impostato su "Normal" o "LowPoly" (predefinito: False). | BOOLEAN | No | - |
| `generate_type.polygon_type` | Il tipo di poligono da utilizzare per la mesh. Questo parametro è visibile solo quando `generate_type` è impostato su "LowPoly". | COMBO | No | `"triangle"`<br>`"quadrilateral"` |
| `seed` | Un valore di seed per il processo di generazione. Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 0). | INT | Sì | 0 - 2147483647 |

**Nota:** Tutte le immagini di input devono avere una larghezza e un'altezza minime di 128 pixel. Le immagini vengono automaticamente ridimensionate verso il basso se superano i 4900 pixel sul lato più lungo.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `model_file` | Un output legacy per la compatibilità con le versioni precedenti. | STRING |
| `GLB` | Il modello 3D generato nel formato file GLB (Binary GL Transmission Format). | FILE3DGLB |
| `OBJ` | Il modello 3D generato nel formato file OBJ (Wavefront). | FILE3DOBJ |
| `texture_image` | L'immagine di texture per il modello 3D generato. | IMAGE |
| `optional_metallic` | La mappa metallica per i materiali PBR. Restituisce un'immagine nera se non disponibile. | IMAGE |
| `optional_normal` | La mappa delle normali per i materiali PBR. Restituisce un'immagine nera se non disponibile. | IMAGE |
| `optional_roughness` | La mappa di rugosità per i materiali PBR. Restituisce un'immagine nera se non disponibile. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `fe422cfa714dbff7cd5dabb286d93d59afe9a01daf711ca09ebcf47ef100a52e`

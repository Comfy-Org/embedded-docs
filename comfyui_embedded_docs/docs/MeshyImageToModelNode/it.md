# Meshy: Da Immagine a Modello

Il nodo Meshy: Image to Model utilizza l'API Meshy per generare un modello 3D da una singola immagine di input. Carica l'immagine, invia un'attività di elaborazione e restituisce i file del modello 3D generato (GLB e FBX) insieme all'ID dell'attività per riferimento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Specifica la versione del modello AI da utilizzare per la generazione. | COMBO | Sì | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `image` | L'immagine di input da convertire in un modello 3D. | IMAGE | Sì | - |
| `should_remesh` | Se impostato su `"false"`, restituisce una mesh triangolare non elaborata. | DYNAMIC_COMBO | Sì | `"true"`<br>`"false"` |
| `topology` | La topologia poligonale di destinazione per il modello rimagliato. Questo input è disponibile solo quando `should_remesh` è impostato su `"true"`. | COMBO | No* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Il numero obiettivo di poligoni per il modello rimagliato. Questo input è disponibile solo quando `should_remesh` è impostato su `"true"`. Predefinito: 300000. | INT | No* | 100 - 300000 |
| `symmetry_mode` | Controlla la simmetria applicata al modello 3D generato. | COMBO | Sì | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Determina se vengono generate le texture. Impostandolo su `"false"` si salta la fase di texturizzazione e si restituisce una mesh senza texture. | DYNAMIC_COMBO | Sì | `"true"`<br>`"false"` |
| `enable_pbr` | Genera mappe PBR (metallico, rugosità, normale) oltre al colore di base. Questo input è disponibile solo quando `should_texture` è impostato su `"true"`. Predefinito: `False`. | BOOLEAN | No* | - |
| `texture_prompt` | Fornisce un prompt testuale per guidare il processo di texturizzazione. Massimo 600 caratteri. Non può essere usato contemporaneamente a `texture_image`. Questo input è disponibile solo quando `should_texture` è impostato su `"true"`. Predefinito: stringa vuota. | STRING | No* | - |
| `texture_image` | È possibile usare solo uno tra `texture_image` o `texture_prompt` alla volta. Questo input è disponibile solo quando `should_texture` è impostato su `"true"`. | IMAGE | No* | - |
| `texture_resolution` | Risoluzione della texture del colore di base. Risoluzioni più alte catturano più dettaglio superficiale. Questo input è disponibile solo quando `should_texture` è impostato su `"true"`. | COMBO | No* | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | Specifica la modalità posa per il modello generato. Questo è un parametro avanzato. | COMBO | Sì | `""` (vuoto)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 0. | INT | Sì | 0 - 2147483647 |
| `ultra_mode` | Esegue un passaggio di rifinitura extra per una geometria a fedeltà più elevata con dettaglio superficiale più fine. Predefinito: `False`. | BOOLEAN | Sì | - |
| `ultra_resolution` | Risoluzione del passaggio ultra: `"2k"` lo esegue a 2048³, `"4k"` a 4096³ per il massimo dettaglio superficiale. 4k richiede il modello `"meshy-7.1"` o `"latest"`. Usato solo quando `ultra_mode` è abilitato (predefinito: `"2k"`). | COMBO | No | `"2k"`<br>`"4k"` |

**Nota sui vincoli dei parametri:**

* Gli input `topology` e `target_polycount` sono disponibili solo quando `should_remesh` è impostato su `"true"`.
* Gli input `enable_pbr`, `texture_prompt`, `texture_image` e `texture_resolution` sono disponibili solo quando `should_texture` è impostato su `"true"`.
* Quando `should_texture` è impostato su `"true"`, `texture_prompt` e `texture_image` non possono essere usati contemporaneamente. Se vengono forniti entrambi, il nodo genera un errore.
* `texture_prompt` ha una lunghezza massima di 600 caratteri.
* Quando `ultra_mode` è abilitato, il parametro `model` deve essere impostato su `"meshy-7.1"`, `"meshy-7"` o `"latest"`; qualsiasi altro modello genera un errore. Con `"meshy-7"` il passaggio ultra viene sempre eseguito a 2048³, e la risoluzione ultra `"4k"` richiede `"meshy-7.1"` o `"latest"`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model_file` | Il nome file del modello GLB generato. Mantenuto solo per retrocompatibilità. | STRING |
| `meshy_task_id` | L'identificatore univoco dell'attività API Meshy, che può essere utilizzato come riferimento o per la risoluzione dei problemi. | MESHY_TASK_ID |
| `GLB` | Il modello 3D generato nel formato file GLB. | FILE3DGLB |
| `FBX` | Il modello 3D generato nel formato file FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `38528b48c3f792a459008a52f65fae248ef1dadafb37fe4dc6b697d25bc89f4f`

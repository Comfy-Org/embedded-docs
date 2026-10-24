# Meshy: Image to Model (Smart Topology)

Questo nodo genera una mesh triangolare pronta per i videogiochi da un'immagine di riferimento, con un numero target di facce, tramite Meshy T2.5. La topologia viene costruita in base al polycount richiesto invece di essere decimata successivamente, quindi il risultato è pronto per un motore di gioco senza una passata di retopologia separata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | La versione del modello Meshy da usare per la generazione. | COMBO | Sì | `"meshy-t2.5"` |
| `image` | L'immagine di riferimento da cui viene generato il modello. | IMAGE | Sì | - |
| `target_polycount` | Numero approssimativo di triangoli nella mesh generata. Predefinito: 15000. | INT | Sì | 100 a 30000 |
| `should_texture` | Determina se vengono generate le texture. `"false"` salta la fase di texturing e restituisce una mesh non texturizzata. | DYNAMIC_COMBO | Sì | `"true"`<br>`"false"` |
| `enable_pbr` | Genera mappe PBR (metallic, roughness, normal) oltre al colore di base. Questo input è disponibile solo quando `should_texture` è impostato su `"true"`. Predefinito: `False`. | BOOLEAN | No | - |
| `texture_prompt` | Prompt testuale per guidare il processo di texturing. Massimo 800 caratteri. Non può essere usato contemporaneamente a `texture_image`. Questo input è disponibile solo quando `should_texture` è impostato su `"true"`. Predefinito: `""` (stringa vuota). | STRING | No | 1 a 800 caratteri |
| `texture_image` | Immagine di riferimento per il processo di texturing. È possibile usare solo uno tra `texture_image` e `texture_prompt` contemporaneamente. Questo input è disponibile solo quando `should_texture` è impostato su `"true"`. | IMAGE | No | - |
| `texture_resolution` | Risoluzione delle texture. Risoluzioni più alte catturano più dettagli della superficie. Questo input è disponibile solo quando `should_texture` è impostato su `"true"`. | COMBO | No | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | La posa del personaggio generato. Una stringa vuota richiede che non venga applicata alcuna posa specifica. Questa è un'impostazione avanzata. Predefinito: `""` (stringa vuota). | COMBO | Sì | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

**Nota:** Gli input `enable_pbr`, `texture_prompt`, `texture_image` e `texture_resolution` sono disponibili solo quando `should_texture` è impostato su `"true"`.

**Vincoli:**

* `target_polycount` è il numero di triangoli da cui viene costruita la mesh, non un limite applicato dopo la generazione.
* Quando `should_texture` è impostato su `"true"`, `texture_prompt` e `texture_image` non possono essere usati contemporaneamente. Se vengono forniti entrambi, il nodo genera un errore.
* `texture_prompt` ha una lunghezza massima di 800 caratteri.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `meshy_task_id` | L'identificatore univoco del task API Meshy. | MESHY_TASK_ID |
| `GLB` | Il modello 3D generato in formato GLB. | FILE3DGLB |
| `FBX` | Il modello 3D generato in formato FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelSmartTopologyNode/it.md)

---
**Source fingerprint (SHA-256):** `e78034a591825ec6e105df1942cf501e882ac780cc2584bfa04b424ecc34a02e`

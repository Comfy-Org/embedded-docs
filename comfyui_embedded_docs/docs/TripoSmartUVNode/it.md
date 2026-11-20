# Tripo: Smart UV

Tripo: Smart UV esegue nuovamente l'unwrap delle UV di un modello e rimappa le sue texture, il rig e l'animazione sul nuovo layout. Usalo quando il layout UV originale di un modello non è utilizzabile, ad esempio dopo la retopologia o quando è necessario rifare le cuciture delle texture. Il modello di input non deve superare gli 80.000 triangoli (un quad conta come due), quindi riduci prima i modelli più grandi con Tripo: Retopology o con un `face_limit`.

> **Nota:** Tripo conserva i registri delle attività sui propri server per 7 giorni (a partire dal 1° dicembre 2026). Un ID attività più vecchio di tale periodo non può più essere risolto, quindi la riesecuzione di un workflow salvato dopo la scadenza fallisce in questo nodo. Esegui nuovamente il nodo Tripo precedente per creare un nuovo ID attività, oppure reimporta il modello scaricato con **Tripo: Import Model**.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_task_id` | ID attività del modello di cui eseguire nuovamente l'unwrap. Accetta un ID attività di modello da un nodo di generazione Tripo, oppure un ID attività di rig, retarget o segment. | MODEL_TASK_ID | Sì | ID attività Tripo |
| `bake` | Esegue il bake delle texture esistenti sul nuovo layout UV. Se disattivato, salta il bake e restituisce il modello senza le sue texture di colore (predefinito: True). | BOOLEAN | Sì | `True`<br>`False` |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model task_id` | ID attività dell'attività UV completata. Può essere passato ad altri nodi Tripo, ad esempio Tripo: Texture. | MODEL_TASK_ID |
| `GLB` | Il modello con unwrap eseguito nuovamente in formato GLB. Vuoto quando il modello di origine è FBX. | FILE_3D_GLB |
| `FBX` | Il modello con unwrap eseguito nuovamente in formato FBX. Valorizzato solo quando il modello di origine è FBX, ad esempio una mesh quad. | FILE_3D_FBX |
| `UV atlas` | Il layout UV renderizzato del modello come immagine. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/it.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`

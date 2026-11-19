# Tripo: Smart UV

Tripo: Smart UV esegue nuovamente l'unwrap delle UV di un modello e rimappa le sue texture, rig e animazione sul nuovo layout. Usalo quando il layout UV originale di un modello è inutilizzabile, ad esempio dopo la retopologia o quando le cuciture delle texture devono essere rifatte. Il modello di input non deve superare 80.000 triangoli (un quad conta come due), quindi riduci i modelli più grandi con Tripo: Retopology o un `face_limit` prima.

> **Nota:** Tripo conserva i record dei task sui suoi server per 7 giorni (in vigore dal 1° dicembre 2026). Un ID del task più vecchio di così non può più essere risolto, quindi rieseguire un workflow salvato dopo la finestra fallisce a questo nodo. Esegui di nuovo il nodo Tripo precedente per creare un nuovo ID del task, oppure reimporta il modello scaricato con **Tripo: Import Model**.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | ID del task del modello su cui eseguire nuovamente l'unwrap. Accetta un ID del task del modello da un nodo di generazione Tripo, oppure un ID del task di rig, retarget o segment. | MODEL_TASK_ID | Sì | ID del task Tripo |
| `bake` | Esegui il bake delle texture esistenti sul nuovo layout UV. Off salta il bake e restituisce il modello senza le sue texture a colori (predefinito: True). | BOOLEAN | Sì | `True`<br>`False` |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `model task_id` | ID del task UV completato. Può essere passato ad altri nodi Tripo, ad esempio Tripo: Texture. | MODEL_TASK_ID |
| `GLB` | Il modello con unwrap rieseguito in formato GLB. Vuoto quando il modello sorgente è FBX. | GLB FILE |
| `FBX` | Il modello con unwrap rieseguito in formato FBX. Popolato solo quando il modello sorgente è FBX, ad esempio una mesh quad. | FBX FILE |
| `UV atlas` | Il layout UV renderizzato del modello come immagine. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/it.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`

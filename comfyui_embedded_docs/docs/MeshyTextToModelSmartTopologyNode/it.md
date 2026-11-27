# Meshy: Text to Model (Smart Topology)

Questo nodo genera una mesh triangolare pronta per il gioco con un numero di facce target utilizzando Meshy T2.5. La topologia viene costruita con il polycount richiesto anziché essere decimata successivamente, quindi il risultato è pronto per un motore di gioco senza un passaggio di retopologia separato.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `modello` | La versione del modello Meshy da utilizzare per la generazione. | COMBO | Sì | `"meshy-t2.5"` |
| `prompt` | La descrizione testuale del modello 3D da generare. | STRING | Sì | da 1 a 800 caratteri |
| `target_polycount` | Numero approssimativo di triangoli nella mesh generata. Predefinito: 15000. | INT | Sì | da 100 a 30000 |
| `modalità posa` | La posa del personaggio generato. Una stringa vuota richiede nessuna posa specifica. Questa è un'impostazione avanzata. Predefinito: `""` (stringa vuota). | COMBO | Sì | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seme` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | da 0 a 2147483647 |

**Vincoli:**

* Il prompt deve contenere tra 1 e 800 caratteri.
* `target_polycount` è il numero di triangoli con cui viene costruita la mesh, non un limite applicato dopo la generazione.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `meshy_task_id` | L'identificatore univoco dell'attività API Meshy. | MESHY_TASK_ID, STRING |
| `GLB` | Il modello 3D generato in formato GLB. | FILE3DGLB |
| `FBX` | Il modello 3D generato in formato FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelSmartTopologyNode/it.md)

---
**Source fingerprint (SHA-256):** `a49cdddcb2e50ce21d84a51c552bb06f049b62c316532eddd16a0c7c8416a8e4`

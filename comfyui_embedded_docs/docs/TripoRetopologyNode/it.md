# Tripo: Retopologia

Tripo: Retopology prende un modello 3D ad alta poligonazione generato da un nodo Tripo precedente e lo ricostruisce come versione a bassa poligonazione con topologia pulita. Invia il modello al servizio di retopologia Tripo, attende il completamento dell'attività, quindi scarica il modello finito ed espone il suo ID attività per l'uso da parte di altri nodi Tripo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_task_id` | ID attività del modello sorgente ad alta poligonazione. Accetta un ID attività del modello da un nodo di generazione Tripo o un ID attività di segmentazione da Tripo: Segment Model. | STRING | Sì | ID attività Tripo |
| `face_limit` | Numero di facce obiettivo: da 500 a 20.000 triangoli o da 500 a 10.000 quad. -1 lascia scegliere a Tripo. (predefinito: -1) | INT | Sì | -1 (automatico)<br>da 500 a 20.000 (triangoli)<br>da 500 a 10.000 (quad) |
| `quad` | Output mesh a quad. Tripo fornisce le mesh a quad come FBX, quindi il risultato arriva sull'output FBX e l'output GLB rimane vuoto. (predefinito: False) | BOOLEAN | Sì | True<br>False (predefinito) |
| `bake` | Esegue il bake delle texture di origine sulla mesh a bassa poligonazione. (predefinito: True) | BOOLEAN | No | True (predefinito)<br>False |
| `part_names` | Nomi delle parti separati da virgole da Tripo: Segment Model. Vuoto elabora l'intero modello. (predefinito: "") | STRING | No | Nomi delle parti del modello o vuoto |

Nota: quando `face_limit` è impostato a -1, Tripo decide automaticamente il numero di facce. Quando `quad` è abilitato, il limite massimo di facce è 10.000 quad invece di 20.000 triangoli, e il risultato viene fornito come FBX (l'output GLB rimane vuoto). Quando `part_names` è vuoto, viene elaborato l'intero modello. Se `face_limit` ha un valore diverso da -1 e non rientra nell'intervallo consentito, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_file` | Output retrocompatibile che identifica il file del modello completato. I flussi di lavoro più recenti dovrebbero usare gli output GLB o FBX. | STRING |
| `model task_id` | ID attività del risultato di retopologia completato. Può essere passato ad altri nodi Tripo per fare riferimento a questo modello. | STRING |
| `GLB` | Il modello a bassa poligonazione retopologizzato in formato GLB. Vuoto quando `quad` è abilitato. | GLB FILE |
| `FBX` | Il modello a bassa poligonazione retopologizzato in formato FBX. Popolato solo quando `quad` è abilitato. | FBX FILE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/it.md)

---
**Source fingerprint (SHA-256):** `b0e967eb4987a70242b6cfce93f09e0caffb7f4bdd3e4f1439e68f33f9138bb5`

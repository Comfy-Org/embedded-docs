# TripoRefineNode

Il TripoRefineNode perfeziona i modelli 3D in bozza creati specificamente dai modelli Tripo v1.4. Richiede un ID attività del modello e lo elabora tramite l'API Tripo per generare una versione migliorata del modello. Questo nodo è progettato per funzionare esclusivamente con modelli in bozza prodotti dai modelli Tripo v1.4.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_task_id` | Deve essere un modello Tripo v1.4 | MODEL_TASK_ID | Sì | - |

**Nota:** Questo nodo accetta solo modelli in bozza creati dai modelli Tripo v1.4. L'utilizzo di modelli di altre versioni può causare errori.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_file` | Il percorso del file o il riferimento al modello perfezionato (solo per compatibilità con le versioni precedenti) | STRING |
| `model task_id` | L'identificatore dell'attività per l'operazione sul modello perfezionato | MODEL_TASK_ID |
| `GLB` | Il modello 3D perfezionato in formato GLB | FILE3DGLB |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/it.md)

---
**Source fingerprint (SHA-256):** `502064a5f153ed05b985f859f27b26eb5219427a17b876cfebedfdcf3194fe12`

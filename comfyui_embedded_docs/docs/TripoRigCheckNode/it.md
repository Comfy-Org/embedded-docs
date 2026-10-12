# Tripo: Controllo rig

Questo nodo invia l'ID di un'attività completata di modello 3D Tripo all'API Tripo e verifica se quel modello può essere riggato. Attende il completamento della verifica e restituisce un risultato sì/no insieme al tipo di scheletro consigliato da Tripo per il modello.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_task_id` | L'ID dell'attività Tripo del modello da analizzare. Identifica un modello che è stato precedentemente generato, importato o altrimenti creato tramite un'attività Tripo. | MODEL_TASK_ID | Sì | N/A |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `riggable` | Indica se il modello può essere riggato. | BOOLEAN |
| `rig_type` | Scheletro consigliato: biped, quadruped, hexapod, octopod, avian, serpentine o aquatic; 'others' quando il modello non può essere riggato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigCheckNode/it.md)

---
**Source fingerprint (SHA-256):** `3aa0bc194e887804b92ca1f9f2b12997c73e111fb282c5de96e55f664c21545e`

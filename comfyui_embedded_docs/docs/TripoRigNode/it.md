# Tripo: Rigga modello

Questo nodo prende un modello 3D Tripo esistente e ne crea una versione riggata, ovvero il modello riceve uno scheletro per poter essere animato. Fornisci l'ID attività del modello da riggare, scegli la versione del rig, il tipo di scheletro, lo stile di denominazione delle ossa e il formato del file di output; il nodo invia il lavoro a Tripo, attende il completamento e restituisce il risultato scaricato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `original_model_task_id` | L'ID attività del modello 3D originale da riggare. Di solito è l'ID prodotto da un nodo Tripo di generazione del modello precedente. | MODEL_TASK_ID | Sì | - |
| `model_version` | Versione del modello di rig da usare. v1.0: solo personaggi umanoidi (bipedi), oltre 90 preset di animazione. v2.5: creature non umanoidi (quadrupedi, esapodi, octopodi, aviani, serpentiformi, acquatici). Predefinito: `v1.0-20240301`. | COMBO | No | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | Tipo di scheletro. "auto" esegue prima il controllo gratuito del rig di Tripo e usa il tipo consigliato. Predefinito: "auto". | COMBO | No | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | Denominazione delle ossa: nativa Tripo o compatibile Mixamo. Tripo non può eseguire il retargeting dei suoi preset di animazione su un rig v1.0 creato con la specifica mixamo; usa tripo per Tripo: Retarget rigged model. Predefinito: "tripo". | COMBO | No | "tripo"<br>"mixamo" |
| `out_format` | Formato del file di output; il risultato arriva sull'output corrispondente. Predefinito: "glb". | COMBO | No | "glb"<br>"fbx" |

**Nota:** La versione del modello v1.0 (`v1.0-20240301`) supporta solo scheletri bipedi. Se con questa versione viene usato un `rig_type` non bipede, il nodo genera un errore e indica di usare `v2.5-20260210` invece.

**Nota:** Quando `rig_type` è "auto", Tripo controlla prima se il modello può essere riggato e sceglie il tipo di scheletro consigliato. Se Tripo segnala che il modello non può essere riggato, il nodo fallisce con un errore.

**Nota:** Il nodo si aspetta che Tripo restituisca un file GLB o FBX. Se Tripo restituisce qualsiasi altro tipo di file, il nodo genera un errore.

**Nota:** Solo l'output corrispondente a `out_format` viene popolato: `GLB` quando `out_format` è "glb", e `FBX` quando `out_format` è "fbx". L'altro output 3D è vuoto.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_file` | Il nome del file del modello riggato generato (ID attività più estensione del formato). Mantenuto solo per compatibilità con le versioni precedenti. | STRING |
| `rig task_id` | L'ID attività per tracciare il processo di generazione del rig. | RIG_TASK_ID |
| `GLB` | Il modello riggato come file 3D GLB. Popolato quando `out_format` è "glb". | FILE3DGLB |
| `FBX` | Il modello riggato come file 3D FBX. Popolato quando `out_format` è "fbx". | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/it.md)

---
**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`

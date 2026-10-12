# MeshSmoothNormals

Calcola normali morbide per vertice per una mesh e le allega. Le mesh senza normali vengono ombreggiate in modo piatto (per faccia) dai visualizzatori glTF; questo nodo le fa ombreggiare in modo morbido. Con un angolo di piega inferiore a 180, i bordi più netti della soglia vengono mantenuti duri dividendo i vertici lungo di essi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | La mesh di input da elaborare. | MESH | Sì | - |
| `crease_angle` | I bordi il cui angolo diedro supera questo valore (gradi) rimangono duri (i vertici vengono divisi). 180 = completamente morbido; un valore inferiore preserva i bordi netti (ad es. ~30-60 per superfici dure). Predefinito: 180.0. | FLOAT | Sì | 0.0 a 180.0 (passo 1.0) |

Quando `crease_angle` è 180 o superiore, la topologia della mesh rimane invariata. Quando è impostato a un valore inferiore a 180, i vertici vengono divisi lungo i bordi duri, il che può aumentare il numero di vertici. Quando i vertici vengono divisi, i dati per vertice (colori, UV e tangenti) vengono duplicati per corrispondere al nuovo layout dei vertici, e la mesh risultante viene ricostruita come batch a dimensione variabile.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `mesh` | La mesh di input con i dati delle normali morbide assegnati, oppure con vertici divisi e normali quando è impostato un angolo di piega. | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/it.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`

# Esegui Tracciamento Video SAM3

Traccia oggetti attraverso fotogrammi video utilizzando il tracker basato su memoria di SAM3. Il nodo elabora una sequenza di fotogrammi video e mantiene le identità degli oggetti attraverso i fotogrammi, utilizzando maschere iniziali o prompt testuali per definire cosa tracciare, e può rilevare nuovi oggetti lungo il percorso utilizzando il condizionamento testuale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `images` | Fotogrammi video come immagini in batch | IMAGE | Sì | Fotogrammi video in batch |
| `model` | Il modello SAM3 da utilizzare per il tracciamento | MODEL | Sì | Modello SAM3 |
| `initial_mask` | Maschera/e per il primo fotogramma da tracciare (una per oggetto) | MASK | No | Una maschera per oggetto |
| `conditioning` | Condizionamento testuale per rilevare nuovi oggetti durante il tracciamento | CONDITIONING | No | Condizionamento testuale |
| `detection_threshold` | Soglia di punteggio per il rilevamento basato su prompt testuale (predefinito: 0.5) | FLOAT | No | 0.0 to 1.0 (step 0.01) |
| `max_objects` | Numero massimo di oggetti tracciati. Le maschere iniziali contano verso questo limite. 0 utilizza il limite interno di 64. (predefinito: 4) | INT | No | 0 to 64 |
| `detect_interval` | Esegui il rilevamento ogni N fotogrammi (1=ogni fotogramma). Valori più alti risparmiano calcolo. (predefinito: 1) | INT | No | 1 o superiore |

**Nota:** È necessario fornire `initial_mask` o `conditioning`. Se entrambi sono omessi, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `track_data` | Dati di tracciamento contenenti maschere degli oggetti e metadati attraverso tutti i fotogrammi video | SAM3_TRACK_DATA |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/it.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`

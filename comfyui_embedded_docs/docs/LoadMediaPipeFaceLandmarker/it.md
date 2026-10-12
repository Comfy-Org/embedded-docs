# LoadMediaPipeFaceLandmarker

Questo nodo carica un modello MediaPipe Face Landmarker v2, che rileva volti e landmark facciali (come occhi, naso e bocca) nelle immagini. Il modello caricato raggruppa due varianti di rilevamento (short-range e full-range) insieme a dati mesh condivisi, blendshapes e geometria canonica usati per l'analisi facciale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_name` | Modello di rilevamento dei volti da models/detection/. | COMBO | Sì | Elenco dei nomi file dei modelli disponibili trovati nella directory `models/detection/` |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `FACE_DETECTION_MODEL` | Un oggetto modello FaceLandmarker caricato che contiene entrambe le varianti di rilevamento (short/full), set di connessioni per la topologia facciale, dati canonici e patcher del modello per la gestione GPU. | FACE_DETECTION_MODEL |

**Nota:** L'output è un oggetto complesso che può essere utilizzato da altri nodi per attività di rilevamento dei volti ed estrazione dei landmark. Contiene due varianti di rilevamento: "short" per il rilevamento a distanza ravvicinata e "full" per il rilevamento a gamma completa.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/it.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`

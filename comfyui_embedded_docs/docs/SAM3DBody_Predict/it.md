# Esegui previsione corpo SAM3D

SAM3D Body Prediction esegue la stima della posa 3D del corpo e delle mani sulle immagini di input, rilevando una o più persone per fotogramma. È possibile fornire dati di tracciamento o bounding box per migliorare il rilevamento; quando non viene fornito nessuno dei due, il nodo ricade sul rilevamento a persona singola sull'intero fotogramma.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `sam3d_body_model` | Il modello del corpo SAM3D da utilizzare per la previsione. | SAM3D_BODY_MODEL | Sì | — |
| `image` | Immagine o batch di immagini su cui eseguire la previsione del corpo. | IMAGE | Sì | — |
| `track_data` | Dati di tracciamento da SAM3 Video Track, necessari per il rilevamento multi-persona. | SAM3_TRACK_DATA | No | — |
| `bboxes` | Bounding box per fotogramma utilizzati per un rilevamento migliore. Possono essere usati come alternativa ai dati di tracciamento. | BBOX | No | — |
| `run_hand_refinement` | Migliora la posa delle mani al costo di tempo di inferenza e utilizzo di memoria extra. Predefinito: true. | BOOLEAN | No | true<br>false |
| `fov` | FoV verticale in gradi. Influisce sulla profondità prevista e sulla scala assoluta. 0 = ricade su ~53° (16:9). Predefinito: 0.0. | FLOAT | No | 0.0 o superiore |
| `batch_size` | Numero massimo di ritagli di persone da elaborare in un batch. Valori più grandi usano più VRAM per un'inferenza più rapida. Predefinito: 64. | INT | No | da 1 a 512 |

Nota: quando viene fornito `track_data`, ha la precedenza su `bboxes`. Se non vengono forniti né `track_data` né `bboxes`, il nodo ricade sul rilevamento a persona singola sull'intero fotogramma. Le bounding box possono essere fornite per un singolo fotogramma (applicate a ogni fotogramma) o per fotogramma.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `mhr_pose_data` | Pacchetto di dati di posa del corpo contenente i risultati del rilevamento della posa per fotogramma, la geometria del volto, le dimensioni dell'immagine di input, i colori canonici dei vertici e una maschera dei vertici delle mani. | MHR_POSE_DATA |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Predict/it.md)

---
**Source fingerprint (SHA-256):** `f1039349cd2809423053bffde1c7d119c7c42f217327d23c608b1224d183770e`

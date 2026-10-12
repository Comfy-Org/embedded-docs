# Espressione facciale per corpo SAM3D

Questo nodo aggiunge espressioni facciali a un corpo SAM3D rilevando i volti in un'immagine con il MediaPipe Face Landmarker, associando ciascun volto rilevato a una persona tracciata e mappando i 52 blendshape ARKit sui parametri di espressione a 72 assi di MHR. Poi riesegue il modello del corpo in modo che i vertici della mesh e i keypoint di output riflettano la nuova espressione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `sam3d_body_model` | Il modello del corpo SAM3D contenente il rilevatore di landmark facciali usato per rilevare i volti e rigenerare la mesh del corpo. | SAM3D_BODY_MODEL | Sì | - |
| `mhr_pose_data` | Dati di posa contenenti persone tracciate per frame con bounding box, keypoint e parametri di espressione. Il nodo associa ciascun volto rilevato a una persona e scrive i parametri di espressione aggiornati in questi dati. | MHR_POSE_DATA | Sì | - |
| `image` | Frame immagine usati per rilevare i volti. Se il batch di immagini ha meno frame dei dati di posa, l'ultimo frame viene riutilizzato per i frame rimanenti. | IMAGE | Sì | - |
| `strength` | Moltiplicatore globale su tutti i blendshape. >1 esagera. Predefinito: 1.0. | FLOAT | No | 0.0 a 4.0 (passo 0.05, predefinito 1.0) |
| `mouth_strength` | Moltiplicatore sulle forme di bocca/mascella. jawOpen di MediaPipe satura vicino a 1.0. Predefinito: 1.0. | FLOAT | No | 0.0 a 4.0 (passo 0.05, predefinito 1.0) |
| `eye_strength` | Moltiplicatore sulle forme degli occhi. MediaPipe raramente supera 0.5; spesso sono necessari 2-3x. Predefinito: 2.0. | FLOAT | No | 0.0 a 4.0 (passo 0.05, predefinito 2.0) |
| `brow_strength` | Moltiplicatore sulle forme di sopracciglia/guance/espressione di disprezzo. MediaPipe restituisce ~0.1-0.3; 2-3x. Predefinito: 2.0. | FLOAT | No | 0.0 a 4.0 (passo 0.05, predefinito 2.0) |
| `input_threshold` | Zona morta sull'output grezzo di MediaPipe (sotto = zero, sopra = rimappatura lineare). Predefinito: 0.02. | FLOAT | No | 0.0 a 0.5 (passo 0.01, predefinito 0.02) |
| `blendshape_smooth_window` | Finestra gaussiana sul segnale per frame di MediaPipe prima della mappatura MHR. L'output grezzo di MediaPipe oscilla del 30-70% da un frame all'altro su volti statici. 1 = disabilitato. Usa valori dispari. Predefinito: 7. | INT | No | 1 a 31 (passo 2, predefinito 7) |

Nota: una sottrazione della linea di base per clip viene applicata solo quando almeno 30 frame nella clip contengono persone rilevate. Le lacune di rilevamento fino a 12 frame per persona vengono riempite tramite interpolazione.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `mhr_pose_data` | I dati di posa aggiornati. I parametri di espressione di ciascuna persona tracciata vengono sostituiti con l'espressione facciale mappata e i vertici della mesh e i keypoint vengono rigenerati di conseguenza. | MHR_POSE_DATA |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_FaceExpression/it.md)

---
**Source fingerprint (SHA-256):** `b2299e51be3556e639d5b04fcbee541ecf41e0d84c2c8a0fd4e211b2f6caba0b`

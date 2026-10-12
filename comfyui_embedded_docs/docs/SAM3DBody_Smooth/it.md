# SAM3DBody_Smooth

Smooth SAM3D Body Pose Data riduce il jitter frame-to-frame in una sequenza di pose corporee 3D mediando il movimento nel tempo. I dati di camera e aspetto vengono smussati completamente, mentre la geometria della mesh viene smussata meno quando il soggetto ruota rapidamente, così le rotazioni veloci non vengono appiattite.

## Input

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `mhr_pose_data` | La sequenza di dati di posa MHR da smussare, contenente parametri del modello, parametri di forma, parametri di espressione, layout dei keypoint MHR70 e dati mesh correlati. | MHR_POSE_DATA | Sì | — |
| `strength` | Intensità di smussamento. 0 = grezzo, 1 = smussato. (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo 0.05) |
| `method` | gaussian: media ponderata simmetrica, migliore smussatore per uso generale.<br>savgol: fit polinomiale scorrevole, preserva i picchi netti. (predefinito: "savgol") | COMBO | Sì | "gaussian"<br>"savgol" |
| `window` | Finestra temporale in frame (valori dispari). (predefinito: 7) | INT | Sì | 1 a 51 (valori dispari, passo 2) |
| `rotation_threshold_degrees` | Disattiva lo smussamento per questa velocità di rotazione della radice (gradi/frame) per preservare le rotazioni veloci. 30° è adatto alla maggior parte dei contenuti; valori bassi potrebbero disattivare lo smussamento sul jitter ordinario e influire silenziosamente sulla qualità. 0 = disabilita. (predefinito: 30.0) | FLOAT | Sì | 0.0 a 90.0 (passo 1.0) |

Nota: quando `strength` è 0.0 o inferiore, oppure `window` è 1 o inferiore, il nodo restituisce i dati di input invariati. L'input deve contenere almeno 2 frame e dati keypoint; in caso contrario, il nodo restituisce i dati di input invariati. Quando `rotation_threshold_degrees` è 0.0, l'attenuazione dello smussamento basata sulla rotazione è disabilitata.

## Output

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `mhr_pose_data` | La sequenza di dati di posa MHR smussata con jitter frame-to-frame ridotto. | MHR_POSE_DATA |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/it.md)

---
**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`

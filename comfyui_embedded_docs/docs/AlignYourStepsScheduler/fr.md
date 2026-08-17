# PlanificateurAlignezVosÉtapes

Le nœud AlignYourStepsScheduler crée les valeurs sigma utilisées lors du processus de débruitage pour différents types de modèles de diffusion. Il sélectionne les niveaux de bruit de base pour le modèle choisi, ajuste le nombre d'étapes en fonction du réglage `denoise`, et renvoie un tenseur de valeurs sigma qui se termine par 0.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_type` | Le type de modèle utilisé pour sélectionner les niveaux de bruit de base (par défaut : "SD1") | COMBO | Oui | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | Le nombre total d'étapes d'échantillonnage à générer (par défaut : 10) | INT | Oui | 1 à 10000 |
| `denoise` | Contrôle la part du processus d'échantillonnage utilisée : 1.0 utilise toutes les étapes, les valeurs inférieures utilisent moins d'étapes, et 0.0 renvoie un tenseur sigma vide (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Les valeurs sigma calculées pour le processus de débruitage. Si `denoise` est 0.0, un tenseur vide est renvoyé. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`

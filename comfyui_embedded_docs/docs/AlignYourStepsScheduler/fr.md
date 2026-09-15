# PlanificateurAlignezVosÉtapes

Le nœud AlignYourStepsScheduler génère des valeurs sigma (niveaux de bruit) pour le processus de débruitage en fonction de différents types de modèles. Il calcule les niveaux de bruit appropriés pour chaque étape du processus d'échantillonnage et ajuste le nombre total d'étapes en fonction du paramètre `denoise`, ce qui aide à aligner les étapes d'échantillonnage sur les exigences spécifiques de différents modèles de diffusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `type_de_modèle` | Spécifie le type de modèle à utiliser pour le calcul des sigma (par défaut : "SD1") | COMBO | Oui | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `étapes` | Nombre total d'étapes d'échantillonnage à générer (par défaut : 10) | INT | Oui | 1 à 10000 |
| `débruitage` | Contrôle le niveau de débruitage de l'image, où 1.0 utilise toutes les étapes et des valeurs plus faibles en utilisent moins (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

Remarque : Chaque type de modèle possède un programme de niveaux de bruit intégré contenant 11 valeurs sigma (pour 10 étapes). Lorsque `denoise` vaut 0.0, le nœud renvoie un tenseur sigma vide. Lorsque `denoise` est compris entre 0.0 et 1.0, le nombre effectif d'étapes est calculé comme `round(steps × denoise)`, et seule la partie finale correspondante du programme sigma est utilisée. Si la valeur `steps` demandée ne correspond pas à la longueur du programme intégré, les niveaux de bruit sont interpolés de façon log-linéaire pour correspondre au nombre d'étapes demandé. La valeur sigma finale est toujours définie sur 0.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Renvoie les valeurs sigma calculées pour le processus de débruitage | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`

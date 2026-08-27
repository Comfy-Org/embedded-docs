# PlanificateurAlignezVosÉtapes

Le nœud AlignYourStepsScheduler génère des valeurs sigma pour le processus de débruitage en fonction de différents types de modèles. Il calcule les niveaux de bruit appropriés pour chaque étape du processus d’échantillonnage et ajuste le nombre total d’étapes selon le paramètre `denoise`. Cela permet d’aligner les étapes d’échantillonnage avec les exigences spécifiques des différents modèles de diffusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `type_de_modèle` | Spécifie le type de modèle à utiliser pour le calcul des sigma (par défaut : « SD1 ») | COMBO | Oui | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `étapes` | Le nombre total d’étapes d’échantillonnage à générer (par défaut : 10) | INT | Oui | 1 à 10000 |
| `débruitage` | Contrôle le degré de débruitage de l’image, où 1.0 utilise toutes les étapes et les valeurs inférieures utilisent moins d’étapes (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |

Remarque : Chaque type de modèle possède un calendrier de niveaux de bruit intégré contenant 11 valeurs sigma (pour 10 étapes). Lorsque `denoise` est 0.0, le nœud renvoie un tenseur sigma vide. Lorsque `denoise` est entre 0.0 et 1.0, le nombre effectif d’étapes est calculé comme `round(steps × denoise)`, et seule la dernière partie correspondante du calendrier sigma est utilisée. Si la valeur de `steps` demandée ne correspond pas à la longueur du calendrier intégré, les niveaux de bruit sont interpolés log-linéairement pour correspondre au nombre d’étapes demandé. La valeur finale de sigma est toujours définie à 0.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Renvoie les valeurs sigma calculées pour le processus de débruitage | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`

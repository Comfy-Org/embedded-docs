Le nœud AlignYourStepsScheduler génère des valeurs sigma pour le processus de débruitage en fonction de différents types de modèles. Il calcule les niveaux de bruit appropriés pour chaque étape du processus d'échantillonnage et ajuste le nombre total d'étapes en fonction du paramètre de débruitage. Cela permet d'aligner les étapes d'échantillonnage sur les exigences spécifiques des différents modèles de diffusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `type_de_modèle` | Spécifie le type de modèle à utiliser pour le calcul des sigma (par défaut : "SD1") | STRING | Oui | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `étapes` | Nombre total d'étapes d'échantillonnage à générer (par défaut : 10) | INT | Oui | 1 à 10000 |
| `débruitage` | Contrôle le niveau de débruitage de l'image, où 1,0 utilise toutes les étapes et les valeurs inférieures utilisent moins d'étapes (par défaut : 1,0) | FLOAT | Oui | 0,0 à 1,0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Renvoie les valeurs sigma calculées pour le processus de débruitage | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `112535f9c100ca4e13dcd733e7a371c00c203b38d77bd10beb4355ba3512ec66`

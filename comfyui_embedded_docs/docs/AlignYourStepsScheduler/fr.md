> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/fr.md)

Le nœud AlignYourStepsScheduler génère des valeurs sigma pour le processus de débruitage en fonction des différents types de modèles. Il calcule les niveaux de bruit appropriés pour chaque étape du processus d'échantillonnage et ajuste le nombre total d'étapes en fonction du paramètre de débruitage. Cela permet d'aligner les étapes d'échantillonnage sur les exigences spécifiques des différents modèles de diffusion.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `type_de_modèle` | STRING | COMBO | - | SD1, SDXL, SVD | Spécifie le type de modèle à utiliser pour le calcul des sigma |
| `étapes` | INT | INT | 10 | 1-10000 | Le nombre total d'étapes d'échantillonnage à générer |
| `débruitage` | FLOAT | FLOAT | 1.0 | 0.0-1.0 | Contrôle le niveau de débruitage de l'image, où 1.0 utilise toutes les étapes et les valeurs inférieures utilisent moins d'étapes |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Retourne les valeurs sigma calculées pour le processus de débruitage |

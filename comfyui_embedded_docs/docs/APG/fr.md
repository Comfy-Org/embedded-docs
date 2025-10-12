> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/fr.md)

Le nœud APG (Adaptive Projected Guidance - Guidage Projeté Adaptatif) modifie le processus d'échantillonnage en ajustant la manière dont le guidage est appliqué pendant la diffusion. Il sépare le vecteur de guidage en composantes parallèles et orthogonales par rapport à la sortie conditionnelle, permettant une génération d'image plus contrôlée. Le nœud fournit des paramètres pour mettre à l'échelle le guidage, normaliser son amplitude et appliquer une quantité de mouvement pour des transitions plus fluides entre les étapes de diffusion.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Requis | - | - | Le modèle de diffusion auquel appliquer le guidage projeté adaptatif |
| `eta` | FLOAT | Requis | 1.0 | -10.0 à 10.0 | Contrôle l'échelle du vecteur de guidage parallèle. Comportement CFG par défaut avec une valeur de 1. |
| `norm_threshold` | FLOAT | Requis | 5.0 | 0.0 à 50.0 | Normalise le vecteur de guidage à cette valeur, la normalisation est désactivée avec une valeur de 0. |
| `momentum` | FLOAT | Requis | 0.0 | -5.0 à 1.0 | Contrôle une moyenne mobile du guidage pendant la diffusion, désactivé avec une valeur de 0. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Renvoie le modèle modifié avec le guidage projeté adaptatif appliqué à son processus d'échantillonnage |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SolidMask/fr.md)

Le nœud SolidMask génère un masque uniforme avec une valeur spécifiée sur l'ensemble de sa surface. Il est conçu pour créer des masques de dimensions et d'intensité précises, utiles dans diverses tâches de traitement d'image et de masquage.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `value`   | FLOAT           | Spécifie la valeur d'intensité du masque, influençant son apparence générale et son utilité dans les opérations ultérieures. |
| `width`   | INT             | Détermine la largeur du masque généré, influençant directement sa taille et son rapport hauteur/largeur. |
| `height`  | INT             | Définit la hauteur du masque généré, affectant sa taille et son rapport hauteur/largeur. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `mask`    | MASK            | Produit un masque uniforme avec les dimensions et la valeur spécifiées. |
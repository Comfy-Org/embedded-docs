Ce nœud est conçu pour préparer les images au processus d'outpainting en ajoutant un remplissage autour d'elles. Il ajuste les dimensions de l'image pour garantir la compatibilité avec les algorithmes d'outpainting, facilitant la génération de zones d'image étendues au-delà des limites originales.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | L'entrée 'image' est l'image principale à préparer pour l'outpainting, servant de base pour les opérations de remplissage. |
| `left`    | `INT`       | Spécifie la quantité de remplissage à ajouter au côté gauche de l'image, influençant la zone étendue pour l'outpainting. |
| `top`     | `INT`       | Détermine la quantité de remplissage à ajouter au sommet de l'image, affectant l'expansion verticale pour l'outpainting. |
| `right`   | `INT`       | Définit la quantité de remplissage à ajouter au côté droit de l'image, impactant l'expansion horizontale pour l'outpainting. |
| `bottom`  | `INT`       | Indique la quantité de remplissage à ajouter au bas de l'image, contribuant à l'expansion verticale pour l'outpainting. |
| `feathering` | `INT` | Contrôle la douceur de la transition entre l'image originale et le remplissage ajouté, améliorant l'intégration visuelle pour l'outpainting. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La sortie 'image' représente l'image avec remplissage, prête pour le processus d'outpainting. |
| `mask`    | `MASK`      | La sortie 'mask' indique les zones de l'image originale et le remplissage ajouté, utile pour guider les algorithmes d'outpainting. |

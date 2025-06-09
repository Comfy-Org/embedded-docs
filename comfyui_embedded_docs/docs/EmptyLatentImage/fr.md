Le nœud `EmptyLatentImage` est conçu pour générer une représentation d'espace latent vide avec des dimensions et une taille de lot spécifiées. Ce nœud sert de point de départ fondamental pour la génération ou la manipulation d'images dans l'espace latent, fournissant une base pour des processus ultérieurs de synthèse ou de modification d'images.

## Entrées

| Paramètre   | Data Type | Description |
|-------------|-------------|-------------|
| `width`     | `INT`       | Spécifie la largeur de l'image latente à générer. Ce paramètre influence directement les dimensions spatiales de la représentation latente résultante. |
| `height`    | `INT`       | Détermine la hauteur de l'image latente à générer. Ce paramètre est crucial pour définir les dimensions spatiales de la représentation de l'espace latent. |
| `batch_size`| `INT`       | Contrôle le nombre d'images latentes à générer en un seul lot. Cela permet la génération simultanée de plusieurs représentations latentes, facilitant le traitement par lots. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est un tenseur représentant un lot d'images latentes vides, servant de base pour la génération ou la manipulation ultérieure d'images dans l'espace latent. |

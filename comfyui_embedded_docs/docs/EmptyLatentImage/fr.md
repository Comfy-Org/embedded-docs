> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentImage/fr.md)

Le nœud `EmptyLatentImage` est conçu pour générer une représentation vierge dans l'espace latent, avec des dimensions et une taille de lot spécifiées. Ce nœud constitue une étape fondamentale pour générer ou manipuler des images dans l'espace latent, en fournissant un point de départ pour les processus ultérieurs de synthèse ou de modification d'images.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `width`   | `INT`           | Spécifie la largeur de l'image latente à générer. Ce paramètre influence directement les dimensions spatiales de la représentation latente résultante. |
| `height`  | `INT`           | Détermine la hauteur de l'image latente à générer. Ce paramètre est crucial pour définir les dimensions spatiales de la représentation dans l'espace latent. |
| `batch_size` | `INT`        | Contrôle le nombre d'images latentes à générer en un seul lot. Cela permet de générer simultanément plusieurs représentations latentes, facilitant ainsi le traitement par lots. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `latent`  | `LATENT`        | La sortie est un tenseur représentant un lot d'images latentes vierges, servant de base pour la génération ou la manipulation ultérieure d'images dans l'espace latent. |
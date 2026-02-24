> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/fr.md)

Le nœud Flux2Scheduler génère une séquence de niveaux de bruit (sigmas) pour le processus de débruitage, spécifiquement adaptée au modèle Flux. Il calcule une planification basée sur le nombre d'étapes de débruitage et les dimensions de l'image cible, ce qui influence la progression de l'élimination du bruit pendant la génération d'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `steps` | INT | Oui | 1 à 4096 | Le nombre d'étapes de débruitage à effectuer. Une valeur plus élevée conduit généralement à des résultats plus détaillés mais prend plus de temps à traiter (par défaut : 20). |
| `width` | INT | Oui | 16 à 16384 | La largeur de l'image à générer, en pixels. Cette valeur influence le calcul de la planification du bruit (par défaut : 1024). |
| `height` | INT | Oui | 16 à 16384 | La hauteur de l'image à générer, en pixels. Cette valeur influence le calcul de la planification du bruit (par défaut : 1024). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Une séquence de valeurs de niveau de bruit (sigmas) qui définit la planification du débruitage pour l'échantillonneur. |

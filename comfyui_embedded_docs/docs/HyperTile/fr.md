> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/fr.md)

Le nœud HyperTile applique une technique de tuilage au mécanisme d'attention dans les modèles de diffusion pour optimiser l'utilisation de la mémoire lors de la génération d'images. Il divise l'espace latent en tuiles plus petites et les traite séparément, puis réassemble les résultats. Cela permet de travailler avec des tailles d'image plus grandes sans épuiser la mémoire.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer l'optimisation HyperTile |
| `taille_tuile` | INT | Non | 1-2048 | La taille de tuile cible pour le traitement (par défaut : 256) |
| `taille_échange` | INT | Non | 1-128 | Contrôle la manière dont les tuiles sont réorganisées pendant le traitement (par défaut : 2) |
| `profondeur_max` | INT | Non | 0-10 | Niveau de profondeur maximum auquel appliquer le tuilage (par défaut : 0) |
| `échelle_profondeur` | BOOLEAN | Non | - | Détermine si la taille des tuiles doit être mise à l'échelle en fonction du niveau de profondeur (par défaut : False) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle modifié avec l'optimisation HyperTile appliquée |
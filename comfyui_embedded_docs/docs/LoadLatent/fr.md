> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/fr.md)

Le nœud LoadLatent charge les représentations latentes précédemment sauvegardées à partir de fichiers .latent dans le répertoire d'entrée. Il lit les données du tenseur latent depuis le fichier et applique les ajustements d'échelle nécessaires avant de renvoyer les données latentes pour utilisation dans d'autres nœuds.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `latent` | STRING | Oui | Tous les fichiers .latent dans le répertoire d'entrée | Sélectionne le fichier .latent à charger parmi les fichiers disponibles dans le répertoire d'entrée |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Renvoie les données de représentation latente chargées depuis le fichier sélectionné |

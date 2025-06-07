
Le nœud VAESave est conçu pour sauvegarder les modèles VAE avec leurs métadonnées, y compris les invites et les informations PNG supplémentaires, dans un répertoire de sortie spécifié. Il encapsule la fonctionnalité de sérialiser l'état du modèle et les informations associées dans un fichier, facilitant ainsi la préservation et le partage des modèles entraînés.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `vae`     | VAE       | Le modèle VAE à sauvegarder. Ce paramètre est crucial car il représente le modèle dont l'état doit être sérialisé et stocké. |
| `filename_prefix` | STRING   | Un préfixe pour le nom de fichier sous lequel le modèle et ses métadonnées seront sauvegardés. Cela permet un stockage organisé et une récupération facile des modèles. |

## Sorties

Le nœud n'a pas de sortie.

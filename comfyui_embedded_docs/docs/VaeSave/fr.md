# VAESauvegarder

Voici la traduction en français de la documentation du nœud VAESave :

Le nœud VAESave est conçu pour sauvegarder les modèles VAE ainsi que leurs métadonnées, y compris les prompts et les informations PNG supplémentaires, dans un répertoire de sortie spécifié. Il encapsule la fonctionnalité de sérialisation de l'état du modèle et des informations associées dans un fichier, facilitant ainsi la préservation et le partage des modèles entraînés.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `vae` | Le modèle VAE à sauvegarder. Ce paramètre est crucial car il représente le modèle dont l'état doit être sérialisé et stocké. | VAE |
| `préfixe_de_fichier` | Un préfixe pour le nom du fichier sous lequel le modèle et ses métadonnées seront sauvegardés. Cela permet un stockage organisé et une récupération facile des modèles. | STRING |

## Sorties

Le nœud n'a pas de types de sortie.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAESave/fr.md)

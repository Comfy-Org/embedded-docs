> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/fr.md)

Ce nœud crée un actif d'image personnel pour le service Seedance 2.0 de ByteDance. Il téléverse une image d'entrée et l'enregistre dans un groupe d'actifs spécifié. Si aucun identifiant de groupe n'est fourni, il lancera un processus d'authentification en temps réel dans votre navigateur pour créer un nouveau groupe avant d'ajouter l'actif.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | | L'image à enregistrer comme actif personnel. |
| `group_id` | STRING | Non | | Réutilisez un identifiant de groupe d'actifs Seedance existant pour éviter une vérification humaine répétée pour la même personne. Laissez vide pour exécuter l'authentification en temps réel dans le navigateur et créer un nouveau groupe (par défaut : vide). |

**Contraintes de l'image :**
*   La largeur de l'image doit être comprise entre 300 et 6000 pixels.
*   La hauteur de l'image doit être comprise entre 300 et 6000 pixels.
*   Le rapport d'aspect de l'image doit être compris entre 0,4:1 et 2,5:1.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `asset_id` | STRING | L'identifiant unique pour le nouvel actif d'image créé. |
| `group_id` | STRING | L'identifiant pour le groupe d'actifs. Ce sera l'identifiant `group_id` fourni ou un nouvel identifiant créé. |
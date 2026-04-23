> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateVideoAsset/fr.md)

Ce nœud crée un actif vidéo personnel pour Seedance 2.0. Il télécharge votre vidéo d'entrée et l'enregistre dans un groupe d'actifs spécifié. Si vous ne fournissez pas d'ID de groupe, il vous guidera à travers un processus de vérification en temps réel dans votre navigateur pour créer d'abord un nouveau groupe.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Oui | - | Vidéo à enregistrer comme actif personnel. |
| `group_id` | STRING | Non | - | Réutilisez un ID de groupe d'actifs Seedance existant pour éviter une vérification humaine répétée pour la même personne. Laissez vide pour exécuter l'authentification en temps réel dans le navigateur et créer un nouveau groupe. (par défaut : chaîne vide) |

**Contraintes de la vidéo :**
*   **Durée :** Doit être comprise entre 2 et 15 secondes.
*   **Dimensions :** La largeur et la hauteur doivent chacune être comprises entre 300 et 6000 pixels.
*   **Ratio d'aspect :** Le rapport largeur/hauteur doit être compris entre 0,4 et 2,5.
*   **Pixels totaux :** Le nombre total de pixels (largeur × hauteur) doit être compris entre 409 600 et 927 408.
*   **Fréquence d'images :** Doit être comprise entre 24 et 60 images par seconde (FPS).

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `asset_id` | STRING | L'identifiant unique du nouvel actif vidéo créé. |
| `group_id` | STRING | L'identifiant du groupe d'actifs contenant la nouvelle vidéo. Il s'agira de l'`group_id` fourni ou d'un nouvel identifiant créé. |
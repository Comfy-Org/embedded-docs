> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateVideoAsset/fr.md)

Ce nœud crée un actif vidéo personnel pour Seedance 2.0. Il télécharge votre vidéo d'entrée et l'enregistre dans un groupe d'actifs spécifié. Si vous ne fournissez pas d'identifiant de groupe, il vous guidera dans un processus de vérification d'identité réelle dans votre navigateur pour d'abord créer un nouveau groupe.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `video` | VIDEO | Oui | - | Vidéo à enregistrer en tant qu'actif personnel. |
| `group_id` | STRING | Non | - | Réutiliser un identifiant de groupe d'actifs Seedance existant pour éviter une vérification humaine répétée pour la même personne. Laissez vide pour exécuter l'authentification réelle dans le navigateur et créer un nouveau groupe. (par défaut : chaîne vide) |

**Contraintes vidéo :**
*   **Durée :** Doit être comprise entre 2 et 15 secondes.
*   **Dimensions :** La largeur et la hauteur doivent chacune être comprises entre 300 et 6000 pixels.
*   **Rapport hauteur/largeur :** Le rapport largeur/hauteur doit être compris entre 0,4 et 2,5.
*   **Nombre total de pixels :** Le nombre total de pixels (largeur × hauteur) doit être compris entre 409 600 et 927 408.
*   **Fréquence d'images :** Doit être comprise entre 24 et 60 images par seconde (FPS).

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `group_id` | STRING | L'identifiant unique du nouvel actif vidéo créé. |
| `group_id` | STRING | L'identifiant du groupe d'actifs contenant la nouvelle vidéo. Il s'agira du `group_id` fourni ou d'un nouvel identifiant créé. |

---
**Source fingerprint (SHA-256):** `9da0872cf8df32765e3fb1eef50bc24f53b65e069d8ef2609de1075d89edd605`

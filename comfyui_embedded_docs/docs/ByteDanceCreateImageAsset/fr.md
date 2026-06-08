Ce nœud crée un actif d'image personnel pour le service Seedance 2.0 de ByteDance. Il télécharge une image d'entrée et l'enregistre dans un groupe d'actifs spécifié. Si aucun ID de groupe n'est fourni, il lancera un processus de vérification d'identité réelle dans votre navigateur pour créer un nouveau groupe avant d'ajouter l'actif.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image à enregistrer en tant qu'actif personnel. | IMAGE | Oui |  |
| `group_id` | Réutiliser un ID de groupe d'actifs Seedance existant pour éviter une vérification humaine répétée pour la même personne. Laissez vide pour exécuter l'authentification réelle dans le navigateur et créer un nouveau groupe (par défaut : vide). | STRING | Non |  |

**Contraintes d'image :**
*   La largeur de l'image doit être comprise entre 300 et 6000 pixels.
*   La hauteur de l'image doit être comprise entre 300 et 6000 pixels.
*   Le rapport hauteur/largeur de l'image doit être compris entre 0,4:1 et 2,5:1.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `group_id` | L'identifiant unique de l'actif d'image nouvellement créé. | STRING |
| `group_id` | L'identifiant du groupe d'actifs. Il s'agira du `group_id` fourni ou d'un identifiant nouvellement créé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/fr.md)

---
**Source fingerprint (SHA-256):** `b8b7b4cbbc16a8bb0102982757496ad4e8140bd87155902668c0be0d8b4d3d98`

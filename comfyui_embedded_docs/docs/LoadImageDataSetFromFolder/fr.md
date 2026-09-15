# Charger un Jeu de Données d'Images depuis un Dossier

Ce nœud charge plusieurs images à partir d'un sous-dossier sélectionné dans le répertoire d'entrée principal de ComfyUI et les renvoie sous forme de liste. Il parcourt le dossier choisi à la recherche de fichiers image aux formats PNG, JPG, JPEG ou WEBP, ce qui est utile pour le traitement par lots ou la préparation de jeux de données d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `folder` | Le dossier à partir duquel charger les images. Les options correspondent aux sous-dossiers présents dans le répertoire d'entrée principal de ComfyUI. | COMBO | Oui | Plusieurs options disponibles |

Remarque : Le dossier sélectionné doit être un sous-dossier du répertoire d'entrée principal de ComfyUI ; toute valeur qui se résout en dehors de celui-ci (par exemple, en utilisant `..`, des chemins absolus, des lettres de lecteur ou des liens symboliques) est rejetée. Seuls les fichiers ayant les extensions .png, .jpg, .jpeg ou .webp sont chargés, et la vérification de l'extension est insensible à la casse. Les images chargées sont converties en RGB et mises à l'échelle dans la plage 0-1. Si le dossier sélectionné ne contient aucun fichier image valide, le nœud génère une erreur. Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Liste des images chargées. Le nœud charge tous les fichiers image valides (PNG, JPG, JPEG, WEBP) trouvés dans le dossier sélectionné. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`

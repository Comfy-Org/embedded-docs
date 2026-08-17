# Charger un Jeu de Données d'Images depuis un Dossier

Ce nœud charge un ensemble d'images depuis un dossier sélectionné et les renvoie sous forme de liste. Le dossier doit être un sous-dossier du répertoire d'entrée principal de ComfyUI. Les formats d'image pris en charge sont PNG, JPG, JPEG et WEBP.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `folder` | Le dossier à partir duquel charger les images. Les options disponibles sont les sous-dossiers présents dans le répertoire d'entrée principal de ComfyUI. Toute valeur qui résout à l'extérieur de ce répertoire (par exemple, en utilisant « .. ») est rejetée. | COMBO | Oui | *Plusieurs options disponibles* — les sous-dossiers présents dans le répertoire d'entrée de ComfyUI |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Liste des images chargées. Le nœud charge chaque fichier image valide (PNG, JPG, JPEG, WEBP) trouvé dans le dossier sélectionné et les renvoie sous forme de liste. Si le dossier ne contient aucun fichier image pris en charge, une erreur est levée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`

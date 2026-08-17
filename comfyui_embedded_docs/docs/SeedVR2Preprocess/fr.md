# Prétraitement de l’entrée SeedVR2

Cette nœud rembourre une image redimensionnée pour la préparer pour le modèle SeedVR2. Elle supprime le canal alpha pendant le traitement, qui est ensuite restauré par le nœud compagnon « Post-Process SeedVR2 Output » en utilisant l'image redimensionnée originale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resized_images` | L'image redimensionnée à traiter. | IMAGE | Oui | - |

Remarque : L'entrée peut être une image unique ou une séquence d'images (par exemple, des images d'une vidéo). Son bord le plus court doit mesurer au moins 2 pixels. Pendant le traitement, le canal alpha (s'il est présent) est supprimé, les valeurs des pixels sont limitées à [0, 1], et la largeur et la hauteur sont rembourrées pour être des multiples de 16. Les séquences d'images sont rembourrées afin que leur longueur suive le motif 1, 5, 9, 13, ... images.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | L'image rembourrée pour l'encodage VAE. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/fr.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`

# Prétraitement de l’entrée SeedVR2

Ce nœud prépare une image ou une vidéo redimensionnée pour le modèle SeedVR2 en lui ajoutant un remplissage jusqu'à la forme attendue par le modèle. Les valeurs de pixels sont limitées à l'intervalle 0-1, la hauteur et la largeur sont complétées par remplissage jusqu'à des multiples de 16, et le nombre d'images est complété par répétition de la dernière image jusqu'à suivre un motif 4n+1 (1, 5, 9, 13, ...). Le canal alpha est supprimé pendant le traitement ; le nœud complémentaire Post-Process SeedVR2 Output le restaure plus tard à partir de l'image redimensionnée d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resized_images` | L'image redimensionnée à traiter. | IMAGE | Oui | - |

Remarque : l'entrée peut être une image unique, une séquence d'images ou un lot de vidéos (tenseurs IMAGE en 4-D ou 5-D). Si elle possède plus de 3 canaux, le canal alpha est supprimé et seuls les canaux RGB sont conservés. Le bord le plus court de l'entrée doit mesurer au moins 2 pixels. Le remplissage spatial est effectué avec du noir (valeur 0), et les nombres d'images valides suivent un motif 4n+1 (1, 5, 9, 13, ...).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | L'image avec remplissage pour l'encodage VAE. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/fr.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`

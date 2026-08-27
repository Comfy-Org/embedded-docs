# Prétraitement de l’entrée SeedVR2

Ce nœud prépare une image ou une vidéo redimensionnée pour le modèle SeedVR2 en la remplissant (padding) selon la forme attendue par le modèle. Il supprime le canal alpha pendant le traitement ; le nœud compagnon Post-Process SeedVR2 Output le restaure ensuite à partir de l'image redimensionnée d'origine. Les valeurs de pixels sont limitées à la plage 0-1, la hauteur et la largeur sont complétées pour être des multiples de 16, et le nombre d'images est complété en répétant la dernière image si nécessaire.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `resized_images` | L'image redimensionnée à traiter. | IMAGE | Oui | - |

Note : L'entrée peut être une image unique, une séquence d'images ou un lot de vidéos. Si elle a plus de 3 canaux, le canal alpha est supprimé et seul le RVB est conservé. Le bord le plus court de l'entrée doit faire au moins 2 pixels. Le remplissage spatial est rempli de noir (valeur 0), et les nombres d'images valides suivent un motif 4n+1 (1, 5, 9, 13, ...).

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `images` | L'image complétée pour l'encodage VAE. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/fr.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`

# ByteDance Seedream 5.0 Pro Séparation de Couches (hérité)

ByteDance Seedream 5.0 Pro Layer Separation décompose une image en une plaque de fond plus jusqu'à 16 calques transparents repositionnables, chacun avec un ordre d'empilement, une boîte englobante, un nom et une description. Il renvoie le fond, les images par calque avec masques, les boîtes de placement et une pile de calques prête à être modifiée.

**Remarque :** Ce nœud est marqué comme obsolète dans le code source.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image à séparer. Exactement une image, au moins 512x512 pixels, rapport d'aspect compris entre 1:16 et 16:1. Les entrées supérieures à environ 4 MP sont réduites avant le téléversement. | IMAGE | Oui | Image unique |
| `prompt` | Comment séparer l'image. Laisser vide pour détecter et séparer automatiquement tous les éléments principaux. Décrivez les éléments en langage naturel pour contrôler la séparation, ou ciblez des régions exactes avec les balises `<bbox>left top right bottom</bbox>` (coordonnées de 0 à 1000 pour mille). Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `taille` | Niveau de résolution de sortie. « auto » suit la taille de l'image d'entrée (limitée à la plage 1K-2K). Par défaut : « auto ». | COMBO | Oui | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Graine à utiliser pour la génération. Par défaut : 0. | INT | Oui | 0 à 2147483647 |
| `optimisation du prompt` | Mode d'optimisation du prompt : « standard » offre une qualité supérieure, « fast » un temps de génération plus court. Par défaut : « standard ». | COMBO | Non | "standard"<br>"fast" |
| `filigrane` | Indique s'il faut ajouter un filigrane « AI generated » aux images. Par défaut : false. | BOOLEAN | Non | false<br>true |
| `découper les couches` | Géométrie des sorties par lot layers/masks (`layer_stack` n'est pas affecté et est toujours ajusté). Canevas complet : chaque calque sur un canevas à la taille de la base, à la position de sa boîte englobante - recompostez directement avec ImageCompositeMasked. Taille minimale : chaque calque recadré sur sa boîte englobante (complété jusqu'à la taille du plus grand calque pour le traitement par lot) - tenseurs beaucoup plus petits ; reconstruisez le placement avec Layers From Bounding Boxes en utilisant la sortie bboxes. Par défaut : false (canevas complet). | BOOLEAN | Non | false (canevas complet)<br>true (taille minimale) |

Remarque : l'entrée `image` doit être une image unique ; les lots ne sont pas pris en charge. L'image doit mesurer au moins 512x512 pixels avec un rapport d'aspect compris entre 1:16 et 16:1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `base_image` | L'image de base (plaque de fond) sur laquelle les calques s'empilent. | IMAGE |
| `base_mask` | Transparence de l'image de base (1 = transparent, convention LoadImage) ; actuellement toujours entièrement opaque. | MASK |
| `layers` | Calques transparents ordonnés du bas vers le haut. Mode canevas complet : placés sur un canevas noir à la taille de la base, à la position de leur boîte englobante. Mode taille minimale : recadrés sur leur boîte englobante, ancrés en haut à gauche, complétés jusqu'à la taille du plus grand calque. | IMAGE |
| `masks` | Transparence par calque, alignée par index avec le lot layers (1 = transparent, convention LoadImage). Pour une composition de style ImageCompositeMasked, ajoutez d'abord InvertMask. | MASK |
| `bboxes` | Une boîte de placement par calque, alignée par index avec le lot layers (fournissez les deux, plus masks, à Layers From Bounding Boxes pour reconstruire le placement par calque) : `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` est la région de contenu du calque dans son propre cadre ; elle se place sur le canevas à la position de la boîte plus ce décalage. | BOUNDING_BOX |
| `layer_stack` | Document de calques prêt à être modifié pour Create Layered Image : la plaque de base plus chaque élément comme son propre calque nommé, recadré au plus juste, à sa position réelle et dans son ordre d'empilement. Connectez directement, ou étendez avec Add Layer. | LAYERS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/fr.md)

---
**Source fingerprint (SHA-256):** `7c0d8ca76ee4b8d6a34fec2edbb753982a05160540ae1d1867efb79c9f9c5498`

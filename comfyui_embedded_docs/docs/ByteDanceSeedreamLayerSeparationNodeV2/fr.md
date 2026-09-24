# ByteDance Seedream 5.0 Layer Separation

ByteDance Seedream 5.0 Layer Separation décompose une image en une plaque d’arrière-plan plus jusqu’à 16 calques transparents repositionnables, chacun avec un ordre d’empilement, une boîte englobante, un nom et une description. Il renvoie l’arrière-plan, les images par calque avec les masques, les boîtes de placement et une pile de calques prête à être modifiée. Le sélecteur `model` choisit entre Seedream 5.0 Pro et le plus rapide Seedream 5.0 Flash.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle Seedream utilisé pour la séparation. « seedream 5.0 pro » (par défaut) offre la meilleure qualité de séparation et expose également un contrôle `prompt_optimization` ; « seedream 5.0 flash » est plus rapide et moins coûteux et ne dispose d’aucun contrôle d’optimisation du prompt. | DYNAMIC_COMBO | Oui | "seedream 5.0 pro"<br>"seedream 5.0 flash" |

### Entrées Seedream 5.0 Pro et 5.0 Flash

Ces entrées sont disponibles avec les deux modèles.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image à séparer. Exactement une image, au moins 512x512 pixels, rapport d’aspect compris entre 1:16 et 16:1. Les entrées supérieures à environ 4 MP sont réduites avant l’envoi. | IMAGE | Oui | Image unique |
| `prompt` | Comment séparer l’image. Laisser vide pour détecter et séparer automatiquement tous les éléments principaux. Décrivez les éléments en langage naturel pour contrôler la séparation, ou ciblez des régions précises avec les balises `<bbox>left top right bottom</bbox>` (coordonnées en pour-mille, de 0 à 1000). Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `size` | Niveau de résolution de sortie. « auto » suit la taille de l’image d’entrée (limitée à la plage 1K-2K). Par défaut : « auto ». | COMBO | Oui | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Graine à utiliser pour la génération. Par défaut : 42. | INT | Oui | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane « AI generated » aux images. Par défaut : false. | BOOLEAN | Oui | false<br>true |
| `crop_layers` | Géométrie des sorties par lot des calques/masques (`layer_stack` n’est pas affecté et reste toujours ajusté au plus juste). Canevas complet : chaque calque sur un canevas aux dimensions de la base, à la position de sa boîte englobante — recombinez directement avec ImageCompositeMasked. Taille minimale : chaque calque rogné à sa boîte englobante (complété jusqu’au plus grand calque pour la mise en lot) — tenseurs beaucoup plus petits ; reconstruisez le placement avec Layers From Bounding Boxes à l’aide de la sortie `bboxes`. Par défaut : false (canevas complet). | BOOLEAN | Oui | false (canevas complet)<br>true (taille minimale) |

### Entrées uniquement pour Seedream 5.0 Pro

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt_optimization` | Mode d’optimisation du prompt : « standard » offre une qualité supérieure, « fast » un temps de génération plus court. Disponible uniquement avec Seedream 5.0 Pro. Par défaut : « standard ». | COMBO | Oui | "standard"<br>"fast" |

**Remarque :** L’entrée `image` doit être une image unique ; les lots ne sont pas pris en charge. L’image doit mesurer au moins 512x512 pixels avec un rapport d’aspect compris entre 1:16 et 16:1. Seedream 5.0 Flash utilise toujours l’optimisation standard du prompt.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `base_image` | L’image de base (plaque d’arrière-plan) sur laquelle les calques s’empilent. | IMAGE |
| `base_mask` | Transparence de l’image de base (1 = transparent, convention LoadImage) ; actuellement toujours entièrement opaque. | MASK |
| `layers` | Calques transparents ordonnés du bas vers le haut. Mode canevas complet : placés sur un canevas noir aux dimensions de la base, à la position de leur boîte englobante. Mode taille minimale : rognés à leur boîte englobante, ancrés en haut à gauche, complétés jusqu’au plus grand calque. | IMAGE |
| `masks` | Transparence par calque, alignée par index avec le lot `layers` (1 = transparent, convention LoadImage). Pour une composition de type ImageCompositeMasked, ajoutez d’abord InvertMask. | MASK |
| `bboxes` | Une boîte de placement par calque, alignée par index avec le lot `layers` (fournissez les deux, plus les `masks`, à Layers From Bounding Boxes pour reconstruire le placement par calque) : `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` est la région de contenu du calque dans son propre cadre ; elle se place sur le canevas à la position de la boîte plus ce décalage. | BOUNDING_BOX |
| `layer_stack` | Document de calques prêt à être modifié pour Create Layered Image : la plaque de base plus chaque élément comme son propre calque nommé, rogné au plus juste, à sa position réelle et dans son ordre d’empilement. Connectez-le directement, ou étendez-le avec Add Layer. | LAYERS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `b106ca63d37aea68079f0032a1f7dfeefee9f759c71bb1605bbfe66c3d9dad62`

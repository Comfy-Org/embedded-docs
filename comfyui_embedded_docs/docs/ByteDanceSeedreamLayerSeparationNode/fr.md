# ByteDance Seedream 5.0 Pro Séparation de Couches

ByteDance Seedream 5.0 Pro Layer Separation décompose une image en un plan de fond plus jusqu’à 16 couches transparentes, chacune avec son propre ordre d’empilement, sa boîte englobante, son nom et sa description. Elle renvoie le plan de fond, les images par couche avec masques, les boîtes de placement et une pile de couches prête à être modifiée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image à séparer. Exactement une image, d’au moins 512x512 pixels, avec un rapport hauteur/largeur entre 1:16 et 16:1. Les entrées de plus d’environ 4 MP sont réduites avant l’envoi. | IMAGE | Oui | Image unique |
| `prompt` | Comment séparer l’image. Laisser vide pour détecter automatiquement et séparer tous les éléments principaux. Décrivez les éléments en langage naturel pour contrôler la séparation, ou ciblez des régions précises avec les balises `<bbox>left top right bottom</bbox>` (coordonnées en pour mille de 0 à 1000). Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `size` | Niveau de résolution de sortie. « auto » suit la taille de l’image d’entrée (bornée à la plage 1K-2K). Par défaut : « auto ». | COMBO | Oui | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Graine à utiliser pour la génération. Par défaut : 0. | INT | Oui | 0 à 2147483647 |
| `prompt_optimization` | Mode d’optimisation du prompt : « standard » donne une qualité supérieure, « fast » un temps de génération plus court. Par défaut : « standard ». | COMBO | Non | "standard"<br>"fast" |
| `watermark` | Indique s’il faut ajouter un filigrane « généré par IA » aux images. Par défaut : false. | BOOLEAN | Non | false<br>true |
| `crop_layers` | Géométrie des sorties par lots de couches/masques (layer_stack n’est pas affecté et est toujours ajusté). Plein canevas : chaque couche est placée sur un canevas de taille de base à sa position de boîte englobante — recomposez directement avec ImageCompositeMasked. Taille minimale : chaque couche est recadrée à sa boîte englobante (avec padding à la plus grande couche pour le traitement par lots) — tenseurs beaucoup plus petits ; reconstruisez le placement avec Layers From Bounding Boxes en utilisant la sortie bboxes. Par défaut : false (plein canevas). | BOOLEAN | Non | false (plein canevas)<br>true (taille minimale) |

Remarque : l’image d’entrée doit être une image unique ; les lots ne sont pas pris en charge. L’image doit faire au moins 512x512 pixels avec un rapport hauteur/largeur entre 1:16 et 16:1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `base_image` | L’image de base (plan de fond) sur laquelle s’empilent les couches. | IMAGE |
| `base_mask` | Transparence de l’image de base (1 = transparent, convention LoadImage) ; actuellement toujours entièrement opaque. | MASK |
| `layers` | Couches transparentes classées de bas en haut. Mode plein canevas : placées sur un canevas noir de taille de base à leur position de boîte englobante. Mode taille minimale : recadrées à leur boîte englobante, ancrées en haut à gauche, avec padding à la plus grande couche. | IMAGE |
| `masks` | Transparence par couche, alignée par index avec le lot de couches (1 = transparent, convention LoadImage). Pour un compositing de type ImageCompositeMasked, ajoutez InvertMask au préalable. | MASK |
| `bboxes` | Une boîte de placement par couche, alignée par index avec le lot de couches (fournissez les deux, ainsi que les masques, à Layers From Bounding Boxes pour reconstruire le placement par couche) : `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` est la région de contenu de la couche dans son propre cadre ; elle se place sur le canevas à la position de la boîte plus ce décalage. | BOUNDING_BOX |
| `layer_stack` | Document de couches prêt à modifier pour Create Layered Image : le plan de base plus chaque élément comme sa propre couche nommée et recadrée au plus près, à sa position réelle et dans son ordre d’empilement. Connectez-le directement, ou étendez-le avec Add Layer. | LAYERS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/fr.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`

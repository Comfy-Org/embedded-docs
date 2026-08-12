# ByteDanceSeedreamLayerSeparationNode

---

ByteDance Seedream 5.0 Pro Layer Separation décompose une image en une couche de fond et jusqu'à 16 calques transparents, chacun avec son propre ordre d'empilement, sa boîte englobante, son nom et sa description. Il renvoie le fond, les images par calque avec leurs masques, les boîtes de placement et un empilement de calques prêt à modifier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `image` | L'image à séparer. Exactement une image, d'au moins 512x512 pixels, avec un rapport d'aspect compris entre 1:16 et 16:1. Les entrées de plus d'environ 4 mégapixels sont réduites avant l'envoi. | IMAGE | Oui | Image unique |
| `prompt` | Comment séparer l'image. Laisser vide pour une détection automatique et la séparation de tous les éléments principaux. Décrivez les éléments en langage naturel pour contrôler la séparation, ou ciblez des régions précises avec les balises `<bbox>left top right bottom</bbox>` (coordonnées en millièmes de 0 à 1000). Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `size` | Niveau de résolution de sortie. « auto » suit la taille de l'image d'entrée (bornée à la plage 1K-2K). Par défaut : « auto ». | STRING | Oui | « auto »<br>« 1K »<br>« 1.5K »<br>« 2K » |
| `seed` | Graine à utiliser pour la génération. Par défaut : 0. | INT | Oui | 0 à 2147483647 |
| `prompt_optimization` | Mode d'optimisation du prompt : « standard » offre une qualité supérieure, « fast » un temps de génération plus court. Par défaut : « standard ». | STRING | Non | « standard »<br>« fast » |
| `watermark` | Indique s'il faut ajouter un filigrane « généré par IA » aux images. Par défaut : false. | BOOLEAN | Non | false<br>true |
| `crop_layers` | Géométrie des sorties par lots de calques/masques (layer_stack n'est pas affecté et est toujours recadré au plus près). Toile pleine : chaque calque est placé sur une toile de taille de base à sa position de boîte englobante – recomposez directement avec ImageCompositeMasked. Taille minimale : chaque calque est recadré selon sa boîte englobante (avec un remplissage jusqu'au plus grand calque pour le traitement par lots) – des tenseurs beaucoup plus petits ; reconstruisez le placement avec Layers From Bounding Boxes en utilisant la sortie bboxes. Par défaut : false (toile pleine). | BOOLEAN | Non | false (toile pleine)<br>true (taille minimale) |

Remarque : L'image d'entrée doit être une image unique ; les lots ne sont pas pris en charge. L'image doit faire au moins 512x512 pixels avec un rapport d'aspect compris entre 1:16 et 16:1.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `base_image` | L'image de base (couche de fond) sur laquelle les calques s'empilent. | IMAGE |
| `base_mask` | Transparence de l'image de base (1 = transparent, convention LoadImage) ; actuellement toujours entièrement opaque. | MASK |
| `layers` | Calques transparents ordonnés de bas en haut. Mode toile pleine : placés sur une toile noire de taille de base à leur position de boîte englobante. Mode taille minimale : recadrés selon leur boîte englobante, ancrés en haut à gauche, avec un remplissage jusqu'au plus grand calque. | IMAGE |
| `masks` | Transparence par calque, alignée sur l'index du lot de calques (1 = transparent, convention LoadImage). Pour un compositing de type ImageCompositeMasked, ajoutez d'abord InvertMask. | MASK |
| `bboxes` | Une boîte de placement par calque, alignée sur l'index du lot de calques (alimentez les deux, ainsi que les masques, dans Layers From Bounding Boxes pour reconstruire le placement par calque) : `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` est la région de contenu du calque dans son propre cadre ; elle se place sur la toile à la position de la boîte plus ce décalage. | BOUNDING_BOX |
| `layer_stack` | Document de calques prêt à modifier pour Create Layered Image : la couche de fond plus chaque élément en tant que calque nommé et recadré au plus près, à sa position réelle et dans son ordre d'empilement. Connectez-le directement, ou étendez-le avec Add Layer. | LAYERS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/fr.md)

---
**Source fingerprint (SHA-256):** `059d0a1a5f5793aadda72f50b549b8b10e2ecae3ce003f82c0c28191c3460954`

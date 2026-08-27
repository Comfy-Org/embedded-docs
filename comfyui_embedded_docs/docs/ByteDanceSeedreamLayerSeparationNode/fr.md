# ByteDance Seedream 5.0 Pro Séparation de Couches

---

ByteDance Seedream 5.0 Pro Layer Separation décompose une image en un fond plus jusqu'à 16 calques transparents, chacun avec son propre ordre d'empilement, sa boîte englobante, son nom et sa description. Il renvoie le fond, les images par calque avec masques, les boîtes de placement et une pile de calques prête à modifier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image à séparer. Exactement une image, d'au moins 512x512 pixels, avec un rapport hauteur/largeur compris entre 1:16 et 16:1. Les entrées de plus d'environ 4 MP sont réduites avant l'envoi. | IMAGE | Oui | Single image |
| `prompt` | Comment séparer l'image. Laissez vide pour détecter et séparer automatiquement tous les éléments principaux. Décrivez les éléments en langage naturel pour contrôler la séparation, ou ciblez des régions exactes avec des balises `<bbox>left top right bottom</bbox>` (coordonnées en millièmes de 0 à 1000). Par défaut : chaîne vide. | STRING | Oui | Multiline text |
| `taille` | Niveau de résolution de sortie. « auto » suit la taille de l'image d'entrée (limitée à la plage 1K-2K). Par défaut : « auto ». | COMBO | Oui | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Seed à utiliser pour la génération. Par défaut : 0. | INT | Oui | 0 à 2147483647 |
| `optimisation du prompt` | Mode d'optimisation du prompt : « standard » donne une qualité supérieure, « fast » un temps de génération plus court. Par défaut : « standard ». | COMBO | Non | "standard"<br>"fast" |
| `filigrane` | Indique s'il faut ajouter un filigrane « AI generated » aux images. Par défaut : false. | BOOLEAN | Non | false<br>true |
| `découper les couches` | Géométrie des sorties par lots des calques/masques (layer_stack n'est pas affecté et est toujours ajusté au contenu). Plein cadre : chaque calque sur un canevas de taille de base à sa position de boîte englobante - à recomposer directement avec ImageCompositeMasked. Taille minimale : chaque calque recadré à sa boîte englobante (avec un remplissage jusqu'à la taille du plus grand calque pour le traitement par lots) - tenseurs beaucoup plus petits ; reconstruisez le placement avec Layers From Bounding Boxes en utilisant la sortie bboxes. Par défaut : false (full canvas). | BOOLEAN | Non | false (full canvas)<br>true (minimal size) |

Remarque : l'entrée `image` doit être une image unique ; les lots ne sont pas pris en charge. L'image doit faire au moins 512x512 pixels avec un rapport hauteur/largeur compris entre 1:16 et 16:1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image_de_base` | L'image de base (fond) sur laquelle les calques s'empilent. | IMAGE |
| `masque_de_base` | Transparence de l'image de base (1 = transparent, convention LoadImage) ; actuellement toujours entièrement opaque. | MASK |
| `couches` | Calques transparents classés de bas en haut. Mode plein cadre : placés sur un canevas noir de taille de base à leur position de boîte englobante. Mode taille minimale : recadrés à leur boîte englobante, ancrés en haut à gauche, avec un remplissage jusqu'à la taille du plus grand calque. | IMAGE |
| `masques` | Transparence par calque, alignée par index avec le lot de calques (1 = transparent, convention LoadImage). Pour un compositing de type ImageCompositeMasked, ajoutez InvertMask d'abord. | MASK |
| `bboxes` | Une boîte de placement par calque, alignée par index avec le lot de calques (fournissez les deux — boîtes et lot de calques — ainsi que les masques, à Layers From Bounding Boxes pour reconstruire le placement de chaque calque) : `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` est la région de contenu du calque dans son propre cadre ; elle se place sur le canevas à la position de la boîte plus ce décalage. | BOUNDING_BOX |
| `pile_de_couches` | Document de calques prêt à modifier pour Create Layered Image : le fond, plus chaque élément en tant que calque nommé et recadré au plus près, à sa position réelle et dans son ordre d'empilement. Connectez-le directement ou étendez-le avec Add Layer. | LAYERS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/fr.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`

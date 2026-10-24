# Bria Product Holding

Ce nœud place un produit entre les mains d'une personne avec Bria. L'identité, la pose et l'arrière-plan de la personne sont conservés, tandis que la scène est rendue à nouveau à environ 1 mégapixel, de sorte que le résultat n'est pas aligné au pixel près avec la photo d'entrée. Toutes les images de produit décrivent un même produit sous différents angles ou à différentes étapes.

## Entrées

Le sélecteur `moderation` révèle une option de modération supplémentaire lorsqu'il est défini sur `"true"`.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `person_image` | La photo de la personne qui tient le produit. Le canal alpha est supprimé avant le téléversement de l'image. | IMAGE | Oui | - |
| `product_images` | 1 à 3 images d'un même produit : le produit lui-même, son emballage, un autre angle ou un article associé. Une entrée fournie par lots compte une fois par image et les zones transparentes sont traitées comme blanches. | AUTOGROW | Oui | 1 à 3 images |
| `instruction` | Consigne supplémentaire facultative ajoutée à l'instruction intégrée de Bria, par exemple quelle main utiliser ou dans quel sens l'étiquette est orientée. Par défaut : `""` (chaîne vide). | STRING | Oui | - |
| `aspect_ratio` | `"auto"` conserve le cadrage de la photo de la personne à environ 1 mégapixel. Un ratio fixe renvoie entre 0,6 et 1 mégapixel, par exemple 768x1024 pour `"3:4"`. Par défaut : `"auto"`. | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | Graine envoyée à Bria avec la requête. Par défaut : 42. | INT | Oui | 1 à 2147483647 |
| `moderation` | Paramètres de modération. Lorsqu'il est défini sur `"true"`, l'option de modération ci-dessous devient disponible. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |

### Entrées Modération « true »

Ce paramètre n'apparaît que lorsque `moderation` est défini sur `"true"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_output_moderation` | Active la modération du contenu sur l'image générée. Par défaut : `False`. | BOOLEAN | Non | True / False |

**Contraintes :**

* `product_images` accepte un maximum de 3 images, comptées par image lorsque l'entrée est fournie par lots.
* Les pixels transparents des images de produit sont composés sur du blanc avant le téléversement.
* Le canal alpha de `person_image` est supprimé avant le téléversement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | La photo modifiée avec le produit placé entre les mains de la personne. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaProductHolding/fr.md)

---
**Source fingerprint (SHA-256):** `91a4a4dde0e9d7fe2480130da87edf1f8ed9d4ae0c86f8a8d030c36987dcdb8e`

# Bria Virtual Try-On

Ce nœud habille une personne avec des vêtements ou accessoires via Bria. L'identité, la pose et l'arrière-plan de la personne sont conservés tandis que la scène est rendue à nouveau à environ 1 mégapixel, de sorte que le résultat n'est pas aligné au pixel près avec la photo d'entrée. Chaque image de vêtement remplace l'élément correspondant que la personne porte déjà.

## Entrées

Le sélecteur `moderation` révèle une option de modération supplémentaire lorsqu'il est défini sur `"true"`.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `person_image` | La photo de la personne qui essaie les vêtements. Le canal alpha est supprimé avant le téléchargement de l'image. | IMAGE | Oui | - |
| `garment_images` | 1 à 3 vêtements ou accessoires portés ensemble, chacun remplaçant l'élément correspondant que la personne porte. Une entrée groupée compte une fois par image et les zones transparentes sont traitées comme blanches. | AUTOGROW | Oui | 1 à 3 images |
| `instruction` | Direction supplémentaire facultative ajoutée à l'instruction intégrée de Bria, par exemple quel vêtement superposer. Par défaut : `""` (chaîne vide). | STRING | Oui | - |
| `aspect_ratio` | `"auto"` conserve le cadrage de la photo de la personne à environ 1 mégapixel. Un ratio fixe renvoie entre 0,6 et 1 mégapixel, par exemple 768x1024 pour `"3:4"`. Par défaut : `"auto"`. | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"` |
| `seed` | Graine envoyée à Bria avec la requête. Par défaut : 42. | INT | Oui | 1 à 2147483647 |
| `moderation` | Paramètres de modération. Lorsqu'il est défini sur `"true"`, l'indicateur de modération ci-dessous devient disponible. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |

### Entrées Moderation "true"

Ce paramètre n'apparaît que lorsque `moderation` est défini sur `"true"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_output_moderation` | Active la modération de contenu sur l'image générée. Par défaut : `False`. | BOOLEAN | Non | True / False |

**Contraintes :**

* `garment_images` accepte un maximum de 3 images, comptées par image lorsque l'entrée est groupée.
* Les pixels transparents dans les images de vêtements sont composés sur blanc avant le téléchargement.
* Le canal alpha de `person_image` est supprimé avant le téléchargement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | La photo modifiée avec la personne portant les vêtements fournis. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVirtualTryOn/fr.md)

---
**Source fingerprint (SHA-256):** `32f89c8685d8624bdef2c17ba5ba916b030d1dc88718b83c79aadb9a5fa378de`

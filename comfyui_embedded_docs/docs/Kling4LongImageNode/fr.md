# Kling 4.0 Long Image

Générez une image verticale avec Kling 4.0 : une maquette complète de page web ou une page de détail de produit e-commerce. Choisissez le `skill` correspondant à la mise en page souhaitée ; le nœud affiche alors les entrées de cette mise en page.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `compétence` | Mise en page à générer. `"webpage"` conçoit une page complète autour d’une image de style et d’un sujet facultatifs ; `"ecommerce"` construit une page de détail produit à partir de photos de produit. | DYNAMIC_COMBO | Oui | `"webpage"`<br>`"ecommerce"` |

### Entrées `webpage`

Ces entrées apparaissent lorsque `skill` est défini sur `"webpage"`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `style_image` | Référence facultative pour le style visuel et la mise en page. Faites-y référence avec `@Image1`. | IMAGE | Non | Image unique |
| `subject_image` | Sujet facultatif à conserver et autour duquel concevoir la page. Faites-y référence avec `@Image2`. | IMAGE | Non | Image unique |
| `prompt` | Description facultative de la page. Faites référence à l’image de style avec `@Image1` et à l’image du sujet avec `@Image2`, et précisez la langue du texte de la page, par exemple « All visible text must be in English only. » Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de l’image de sortie. Par défaut : `"1K"`. | COMBO | Oui | `"1K"`<br>`"2K"` |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

### Entrées `ecommerce`

Ces entrées apparaissent lorsque `skill` est défini sur `"ecommerce"`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `product_images` | Emplacements extensibles pour les photos de produit (`image_1` ... `image_3`). Faites-y référence dans le prompt avec `@Image1`, `@Image2`, `@Image3`. | AUTOGROW | Oui | 1 à 3 images |
| `prompt` | Description facultative de la page. Faites référence aux images de produit avec `@Image1`, `@Image2`, `@Image3`. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `length` | Longueur de la page générée. Par défaut : `"medium"`. | COMBO | Oui | `"short"`<br>`"medium"`<br>`"long"` |
| `resolution` | Résolution de l’image de sortie. Par défaut : `"1K"`. | COMBO | Oui | `"1K"`<br>`"2K"` |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes et comportement :**

* Au maximum 3 images de produit peuvent être connectées dans `ecommerce`.
* Chaque image doit mesurer au moins 300x300 pixels et avoir un rapport d’aspect compris entre 2:5 et 5:2.
* Avec `webpage`, un prompt qui mentionne `@Image1` ou `@Image2` déclenche une erreur lorsque l’image correspondante n’est pas connectée.
* Le prix d’un appel dépend du skill, de la résolution et, pour `ecommerce`, de la longueur de la page.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image longue générée, téléchargée depuis Kling une fois la tâche terminée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4LongImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `f1e687bcc8334229c60b318118120b85ddd580d1b62f343164f9803b98a1f987`

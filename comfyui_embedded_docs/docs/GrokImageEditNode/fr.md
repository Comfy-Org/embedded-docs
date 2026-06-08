Voici la traduction en français de la documentation du nœud Grok Image Edit :

Le nœud Grok Image Edit modifie une image existante en fonction d'une invite textuelle. Il utilise l'API Grok pour générer une ou plusieurs nouvelles images qui sont des variations de l'entrée, guidées par votre description.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'IA spécifique à utiliser pour l'édition d'images. | COMBO | Oui | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"`<br>`"grok-imagine-image-beta"` |
| `image` | La ou les images d'entrée à éditer. Prend en charge jusqu'à 3 images d'entrée, sauf pour le modèle "pro" qui n'en supporte qu'une seule. | IMAGE | Oui |  |
| `invite` | L'invite textuelle utilisée pour générer l'image éditée. Doit contenir au moins 1 caractère après suppression des espaces. | STRING | Oui |  |
| `résolution` | La résolution de l'image de sortie. | COMBO | Oui | `"1K"`<br>`"2K"` |
| `nombre d'images` | Nombre d'images éditées à générer (par défaut : 1). | INT | Non | 1 à 10 |
| `graine` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Non | 0 à 2147483647 |
| `rapport d'aspect` | Le rapport hauteur/largeur de l'image de sortie. Autorisé uniquement lorsque plusieurs images sont connectées à l'entrée `image`. Si défini sur "auto", le rapport hauteur/largeur est déterminé automatiquement (par défaut : "auto"). | COMBO | Non | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Contraintes importantes :**
- L'entrée `image` prend en charge jusqu'à 3 images, sauf lors de l'utilisation du modèle `grok-imagine-image-pro`, qui ne supporte qu'une seule image d'entrée.
- Le paramètre `aspect_ratio` ne peut être défini sur une valeur personnalisée (autre que "auto") que lorsque plusieurs images sont connectées à l'entrée `image`. La définition d'un rapport hauteur/largeur personnalisé avec une seule image d'entrée entraînera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La ou les images éditées générées par le nœud. Si `nombre d'images` est supérieur à 1, les sorties sont concaténées en un lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `021d867e9e04451c0c4ef035c19fa86ebc8d4a3f64572aff33f493324d7fe308`

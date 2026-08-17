# Grok Image Edit

Le nœud Grok Image Edit modifie une image existante en fonction d'une invite texte. Il utilise l'API Grok pour générer une ou plusieurs nouvelles images qui sont des variations de l'entrée, guidées par votre description.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle d'IA spécifique à utiliser pour l'édition d'image. | COMBO | Oui | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | La ou les images d'entrée à éditer. Prend en charge jusqu'à 3 images d'entrée, sauf pour le modèle « pro » qui n'en accepte qu'1. | IMAGE | Oui |  |
| `prompt` | L'invite texte utilisée pour générer l'image. Doit contenir au moins 1 caractère après suppression des espaces. | STRING | Oui |  |
| `resolution` | La résolution de l'image de sortie. | COMBO | Oui | `"1K"`<br>`"2K"` |
| `number_of_images` | Nombre d'images éditées à générer (par défaut : 1). | INT | Oui | 1 à 10 |
| `seed` | Graine (seed) pour déterminer si le nœud doit s'exécuter à nouveau ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `aspect_ratio` | Le rapport hauteur/largeur de l'image de sortie. Uniquement autorisé lorsque plusieurs images sont connectées à l'entrée image. Si défini sur « auto », le rapport hauteur/largeur est déterminé automatiquement (par défaut : « auto »). | COMBO | Non | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Contraintes importantes :**
- L'entrée `image` prend en charge jusqu'à 3 images, sauf lors de l'utilisation du modèle `grok-imagine-image-pro`, qui ne prend en charge qu'1 image d'entrée.
- Le paramètre `aspect_ratio` ne peut être défini sur une valeur personnalisée (et non « auto ») que lorsque plusieurs images sont connectées à l'entrée `image`. Définir un rapport hauteur/largeur personnalisé avec une seule image d'entrée entraînera une erreur.

**Remarque :** Ce nœud est obsolète.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | La ou les images éditées générées par le nœud. Si `number_of_images` est supérieur à 1, les sorties sont concaténées dans un lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`

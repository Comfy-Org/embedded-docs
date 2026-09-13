# Grok Image Edit

Le nœud Grok Image Edit modifie une image existante en fonction d'un prompt texte. Il envoie la ou les images d'entrée et votre description à l'API Grok, puis renvoie une ou plusieurs images nouvellement générées qui suivent le prompt. Ce nœud est marqué comme obsolète.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle d'IA spécifique à utiliser pour l'édition d'image. | COMBO | Oui | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | La ou les images d'entrée à modifier. | IMAGE | Oui |  |
| `prompt` | Le prompt texte utilisé pour générer l'image. Texte multiligne ; doit contenir au moins un caractère non blanc. | STRING | Oui |  |
| `resolution` | La résolution de l'image de sortie. | COMBO | Oui | `"1K"`<br>`"2K"` |
| `number_of_images` | Nombre d'images modifiées à générer (par défaut : 1). | INT | Oui | 1 à 10 |
| `seed` | Graine permettant de déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes indépendamment de la graine (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `aspect_ratio` | Le rapport d'aspect de l'image de sortie. Autorisé uniquement lorsque plusieurs images sont connectées à l'entrée `image` (par défaut : "auto"). | COMBO | Non | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Contraintes importantes :**
- L'entrée `image` prend en charge jusqu'à 3 images, sauf lors de l'utilisation du modèle `grok-imagine-image-pro`, qui ne prend en charge qu'une seule image d'entrée.
- Le paramètre `aspect_ratio` ne peut être défini sur une valeur personnalisée (autre que "auto") que lorsque plusieurs images sont connectées à l'entrée `image`. Définir un rapport d'aspect personnalisé avec une seule image d'entrée provoquera une erreur.
- Le `prompt` doit contenir au moins un caractère non blanc.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La ou les images modifiées générées par le nœud. Si plus d'une image est générée, les images sont concaténées dans un seul lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`

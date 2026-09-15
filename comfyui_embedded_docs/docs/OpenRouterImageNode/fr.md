# Image OpenRouter

Ce nœud génère ou modifie des images via OpenRouter à l'aide des modèles MAI-Image-2.6 de Microsoft. Il prend en charge la génération texte-vers-image ainsi que l'édition guidée par image avec jusqu'à cinq images de référence, selon sept rapports d'aspect en résolution 1K ou 1.5K.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle d'image OpenRouter utilisé pour générer l'image. La sélection d'un modèle révèle les options propres au modèle listées ci-dessous. | DYNAMIC_COMBO | Oui | `microsoft/mai-image-2.6`<br>`microsoft/mai-image-2.6-flash` |

### Entrées Mai Image 2.6 et Mai Image 2.6 Flash

Partagées par les deux options de modèle (`microsoft/mai-image-2.6` et `microsoft/mai-image-2.6-flash`), qui exposent le même ensemble de paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Décrit l'image à générer, ou la modification à appliquer aux images de référence. Jusqu'à 20 000 caractères. Par défaut : `""` (vide). Au moins 1 caractère est requis après suppression des espaces blancs en début et fin. | STRING | Oui | 1 à 20 000 caractères |
| `aspect_ratio` | Rapport d'aspect de l'image générée, également appliqué lorsque des images de référence sont connectées. Par défaut : `"1:1"`. `"auto"` laisse le modèle choisir le rapport pour le texte vers image (rendu à la taille 1.5K) et conserve le rapport d'aspect de la première image de référence lors de l'édition. | COMBO | Oui | `"1:1"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"auto"` |
| `resolution` | Palier de taille de sortie. 1K correspond à environ 1 mégapixel (1:1 fait 1024x1024, 16:9 fait 1360x768) ; 1.5K correspond à environ 2,3 mégapixels (1:1 fait 1536x1536, 16:9 fait 2048x1152). Par défaut : `"1K"`. Ignoré lorsque `aspect_ratio` vaut `"auto"`. | COMBO | Oui | `"1K"`<br>`"1.5K"` |
| `seed` | Graine permettant de déterminer si le nœud doit être réexécuté ; l'API n'a pas de graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. Par défaut : `42`. | INT | Oui | 0 à 2147483647 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image_1` ... `image_5` | Emplacement extensible : connectez 1 à 5 images de référence pour l'édition guidée par image ; une entrée par lot compte une fois par image. Les emplacements sont facultatifs et peuvent rester vides (minimum 0 connecté). | IMAGE | Non | 0 à 5 images |

**Remarques :**

- Un maximum de 5 images de référence est pris en charge au total sur tous les emplacements connectés ; une entrée par lot compte une fois par image.
- Le `prompt` doit contenir au moins 1 caractère après suppression des espaces blancs en début et fin, et ne peut pas dépasser 20 000 caractères.
- Les images de référence sont envoyées sous forme de données PNG et sont limitées à un total de 2048 x 2048 pixels.
- Le paramètre `aspect_ratio` est appliqué à la sortie même lorsque des images de référence sont connectées.
- Lorsque `aspect_ratio` vaut `"auto"`, le paramètre `resolution` est ignoré. Sans image de référence, le modèle choisit le rapport pour le texte vers image et effectue le rendu à la taille 1.5K ; lorsque des images de référence sont connectées, le rapport d'aspect de la première image de référence est conservé.
- La valeur de graine n'affecte pas le résultat de l'API ; elle détermine uniquement si le nœud est réexécuté.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée ou modifiée. Si le service renvoie plusieurs images, elles sont combinées en une seule sortie IMAGE groupée. Une erreur est levée si aucune image n'est renvoyée ou si une image renvoyée ne peut pas être décodée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `d201c18deccd2523041a24427996f51127ca201dfe10fad60c6f768ab79bf852`

# Recraft V4 Texte vers Image

Recraft V4 Text to Image

Ce nœud génère des images à partir de descriptions textuelles à l’aide des modèles d’IA Recraft V4 et V4.1. Il envoie votre prompt à une API externe et renvoie les images générées. Vous pouvez contrôler la sortie en spécifiant le modèle, la taille de l’image, le nombre d’images, ainsi qu’un style facultatif, soit sous la forme d’un ID de style enregistré, soit à partir d’images de référence.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour la génération. Les modèles recraftv4_styles sont conçus pour une génération cohérente avec le style et nécessitent toujours un `style_id` ou des `style_references`. | DYNAMIC_COMBO | Oui | "recraftv4_1"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | Prompt pour la génération de l’image. 10 000 caractères maximum. | STRING | Oui | 1 à 10000 caractères |
| `prompt_négatif` | Cette entrée est ignorée : le prompt négatif n’est pas pris en charge par les modèles Recraft V4 et V4.1. | STRING | Oui | N/A |
| `n` | Le nombre d’images à générer (défaut : 1). | INT | Oui | 1 à 6 |
| `graine` | Graine (seed) pour déterminer si le nœud doit être relancé ; les résultats réels sont non déterministes quelle que soit la graine (défaut : 0). | INT | Oui | 0 à 18446744073709551615 |
| `recraft_controls` | Contrôles supplémentaires facultatifs sur la génération via le nœud Recraft Controls. | CUSTOM | Non | N/A |
| `style_id` | UUID d’un style Recraft V4 à appliquer, par exemple depuis le nœud Recraft V4 Create Style ou la sortie `style_id` d’une exécution précédente. Ne peut pas être combiné avec `style_references` (défaut : vide). | STRING | Non | Chaîne UUID valide |
| `style_match` | Fidélité au style : precise le reproduit en détail, flexible correspond à l’aspect général. Utilisé uniquement lorsqu’un style est fourni (défaut : "precise"). | COMBO | Non | "precise"<br>"flexible" |

### Entrées recraftv4_1, recraftv4_1_utility, recraftv4 et recraftv4_styles

Ces modèles partagent le même paramètre `size`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | La taille de l’image générée (défaut : "1024x1024"). | COMBO | Oui | Plusieurs options disponibles (tailles Recraft V4 standard, inclut "1024x1024") |

### Entrées recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro et recraftv4_styles_pro

Ces modèles partagent le même paramètre `size`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | La taille de l’image générée (défaut : "2048x2048"). | COMBO | Oui | Plusieurs options disponibles (tailles Recraft V4 pro, inclut "2048x2048") |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `style_references` | Images de référence pour créer un style à la volée, facturées en plus de la génération. Le style créé est renvoyé comme `style_id` pour être réutilisé. Ne peut pas être combiné avec `style_id`. Emplacement extensible : connectez 1..N images (style_reference_1, style_reference_2, ...). | IMAGE | Non | 0 au nombre maximal d’images de référence autorisé par l’API Recraft ; la taille totale encodée ne doit pas dépasser 10 Mo |

**Remarque :** Le paramètre `size` est une entrée dynamique dont les options disponibles changent en fonction du `model` sélectionné. Les modèles `recraftv4_styles` et `recraftv4_styles_pro` nécessitent toujours un style : connectez des images de référence ou fournissez un `style_id`. Les entrées `style_id` et `style_references` sont mutuellement exclusives — fournissez uniquement l’une d’elles. Un `style_id` doit être un UUID valide. L’entrée `style_match` n’est utilisée que lorsqu’un style est fourni. Les images de référence sont facturées en plus de la génération et leur taille totale encodée ne doit pas dépasser 10 Mo. La valeur `seed` ne garantit pas des résultats d’image reproductibles. Si vous utilisez un ID de style provenant de la Infinite Style Library, assurez-vous qu’il ne s’agit pas d’un style Vector art, car cela pourrait renvoyer des données SVG au lieu d’une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | L’image générée ou un lot d’images. | IMAGE |
| `style_id` | L’ID de style utilisé ou créé par cette génération. Lorsque des images de référence sont fournies, le style créé est renvoyé ici pour être réutilisé ; chaîne vide lorsqu’aucun style n’est utilisé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `af5c1f68e59ca282cdca7c32cd50f0438b743fdda27d9d22e59b2d1343f45e26`

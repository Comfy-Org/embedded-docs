# Recraft V4 Texte vers Image

Génère des images à partir de prompts textuels en utilisant les modèles Recraft V4 et V4.1. Il envoie le prompt et les paramètres sélectionnés à l'API Recraft et renvoie l'image ou les images générées. Si des images de référence de style sont utilisées, l'ID de style créé est également renvoyé.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour la génération. Les modèles recraftv4_styles sont conçus pour une génération cohérente au niveau du style et nécessitent toujours un style_id ou des style_references. `recraftv4_1_flash` est le modèle le plus rapide et le moins coûteux et ne prend en charge aucun style du tout. | DYNAMIC_COMBO | Oui | "recraftv4_1"<br>"recraftv4_1_flash"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | Prompt pour la génération d'image. Maximum 10 000 caractères. | STRING | Oui | 1 à 10000 caractères |
| `prompt_négatif` | Cette entrée est ignorée : le prompt négatif n'est pas pris en charge par les modèles Recraft V4 et V4.1. | STRING | Oui | N/A |
| `n` | Le nombre d'images à générer (par défaut : 1). | INT | Oui | 1 à 6 |
| `graine` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels ne sont pas déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |
| `recraft_controls` | Contrôles supplémentaires optionnels sur la génération via le nœud Recraft Controls. | CUSTOM | Non | N/A |
| `style_id` | UUID d'un style Recraft V4 à appliquer, par exemple depuis le nœud Recraft V4 Create Style ou la sortie style_id d'une exécution précédente. Ne peut pas être combiné avec style_references (par défaut : vide). | STRING | Non | Chaîne UUID valide |
| `style_match` | Dans quelle mesure suivre le style : precise le reproduit en détail, flexible correspond à l'apparence générale. Utilisé uniquement lorsqu'un style est fourni (par défaut : "precise"). | COMBO | Non | "precise"<br>"flexible" |

### Entrées recraftv4_1, recraftv4_1_flash, recraftv4_1_utility, recraftv4 et recraftv4_styles

Ces modèles partagent le même paramètre `size`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | La taille de l'image générée (par défaut : "1024x1024"). | COMBO | Oui | Plusieurs options disponibles (tailles standard Recraft V4 ; inclut "1024x1024") |

### Entrées recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro et recraftv4_styles_pro

Ces modèles partagent le même paramètre `size`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | La taille de l'image générée (par défaut : "2048x2048"). | COMBO | Oui | Plusieurs options disponibles (tailles pro Recraft V4 ; inclut "2048x2048") |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `style_references` | Images de référence pour créer un style à la volée, facturées en supplément de la génération. Le style créé est renvoyé comme style_id pour réutilisation. Ne peut pas être combiné avec style_id. Emplacement extensible : connecter 1..N images (style_reference_1, style_reference_2, ...). | IMAGE | Non | 0 au nombre maximal d'images de référence autorisé par l'API Recraft ; la taille encodée totale ne doit pas dépasser 10 Mo |

**Remarque :** Le paramètre `size` est une entrée dynamique dont les options disponibles changent selon le `model` sélectionné. Les modèles `recraftv4_styles` et `recraftv4_styles_pro` nécessitent toujours un style : connectez des images de référence de style ou fournissez un `style_id`. Les entrées `style_id` et `style_references` sont mutuellement exclusives — fournissez uniquement l'une d'elles. Un `style_id` doit être un UUID valide. L'entrée `style_match` n'est utilisée que lorsqu'un style est fourni. Les images de référence de style sont facturées en supplément de la génération et leur taille encodée totale ne doit pas dépasser 10 Mo. La valeur `seed` ne garantit pas des images de sortie reproductibles. Si vous utilisez un ID de style provenant de l'Infinite Style Library, assurez-vous qu'il ne s'agit pas d'un style Vector art, car cela peut renvoyer des données SVG au lieu d'une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | L'image générée ou le lot d'images. | IMAGE |
| `style_id` | L'ID de style utilisé ou créé par cette génération. Lorsque des images de référence de style sont fournies, le style créé est renvoyé ici pour réutilisation ; chaîne vide lorsqu'aucun style n'est utilisé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `690286e663f27b525e58f81a7f883e490dacd48c1a34ee7b8e9ad4efd9935ff1`

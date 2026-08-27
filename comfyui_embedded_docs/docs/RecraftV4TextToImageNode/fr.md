# Recraft V4 Texte vers Image

Ce nœud génère des images à partir de descriptions textuelles à l’aide des modèles d’IA Recraft V4 et V4.1. Il envoie votre prompt à une API externe et renvoie les images générées. Vous pouvez contrôler la sortie en spécifiant le modèle, la taille de l’image et le nombre d’images à créer.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour la génération. | DYNAMIC_COMBO | Oui | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt pour la génération de l’image. 10 000 caractères maximum. | STRING | Oui | N/A |
| `prompt_négatif` | Cette entrée est ignorée : le prompt négatif n’est pas pris en charge par les modèles Recraft V4 et V4.1. | STRING | Oui | N/A |
| `n` | Le nombre d’images à générer (par défaut : 1). | INT | Oui | 1 à 6 |
| `graine` | Graine (seed) utilisée pour déterminer si le nœud doit être relancé ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |
| `recraft_controls` | Contrôles supplémentaires facultatifs sur la génération via le nœud Recraft Controls. | CUSTOM | Non | N/A |

### Entrées recraftv4_1, recraftv4_1_utility et recraftv4

Partagées par `recraftv4_1`, `recraftv4_1_utility` et `recraftv4`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | La taille de l’image générée (par défaut : « 1024x1024 »). | COMBO | Oui | Plusieurs options disponibles (tailles standard Recraft V4, inclut « 1024x1024 ») |

### Entrées recraftv4_1_pro, recraftv4_1_utility_pro et recraftv4_pro

Partagées par `recraftv4_1_pro`, `recraftv4_1_utility_pro` et `recraftv4_pro`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | La taille de l’image générée (par défaut : « 2048x2048 »). | COMBO | Oui | Plusieurs options disponibles (tailles pro Recraft V4, inclut « 2048x2048 ») |

**Remarque :** Le paramètre `size` est une entrée dynamique dont les options disponibles changent en fonction du `model` sélectionné. La valeur de `seed` ne garantit pas des sorties d’images reproductibles. Si vous utilisez un ID de style provenant de la Infinite Style Library, assurez-vous qu’il ne s’agit pas d’un style d’art vectoriel, car cela peut renvoyer des données SVG au lieu d’une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | L’image générée ou le lot d’images. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`

# Recraft V4 Texte vers Image

Ce nœud génère des images à partir de descriptions textuelles à l'aide des modèles d'IA Recraft V4 et V4.1. Il envoie le prompt et les paramètres de génération au service de génération d'images Recraft et renvoie l'image ou les images résultantes. Vous pouvez choisir le modèle, la taille de l'image et le nombre d'images à générer.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle à utiliser pour la génération. La sélection d'un modèle détermine les options `size` disponibles. | DYNAMIC_COMBO | Oui | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt pour la génération d'images. Maximum 10 000 caractères. | STRING | Oui | 1 à 10 000 caractères |
| `negative_prompt` | Cette entrée est ignorée : le prompt négatif n'est pas pris en charge par les modèles Recraft V4 et V4.1. | STRING | Oui | N/A |
| `n` | Le nombre d'images à générer (défaut : 1). | INT | Oui | 1 à 6 |
| `seed` | Graine qui détermine si le nœud doit s'exécuter à nouveau ; les résultats réels sont non déterministes quelle que soit la graine (défaut : 0). | INT | Oui | 0 à 18446744073709551615 |
| `recraft_controls` | Contrôles supplémentaires optionnels sur la génération via le nœud Recraft Controls. | CUSTOM | Non | N/A |

### Entrées de recraftv4_1, recraftv4_1_utility et recraftv4

Partagées par les modèles `recraftv4_1`, `recraftv4_1_utility` et `recraftv4`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `size` | La taille de l'image générée (défaut : 1024x1024). | COMBO | Oui | Plusieurs options disponibles (tailles standard Recraft V4) |

### Entrées de recraftv4_1_pro, recraftv4_1_utility_pro et recraftv4_pro

Partagées par les modèles `recraftv4_1_pro`, `recraftv4_1_utility_pro` et `recraftv4_pro`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `size` | La taille de l'image générée (défaut : 2048x2048). | COMBO | Oui | Plusieurs options disponibles (tailles Pro Recraft V4) |

**Remarques :**

- L'entrée `size` apparaît lorsqu'un modèle est sélectionné et ses options disponibles dépendent du modèle : les modèles standard (`recraftv4_1`, `recraftv4_1_utility`, `recraftv4`) partagent un ensemble de tailles, tandis que les modèles Pro (`recraftv4_1_pro`, `recraftv4_1_utility_pro`, `recraftv4_pro`) partagent un ensemble différent.
- L'entrée `negative_prompt` est affichée dans l'interface mais n'est pas envoyée au modèle ; les prompts négatifs ne sont pas pris en charge par les modèles Recraft V4 et V4.1.
- La valeur `seed` détermine uniquement si le nœud se réexécute lorsque la valeur change ; les résultats d'image réels sont non déterministes quelle que soit la graine.
- Si vous utilisez un identifiant de style de la Infinite Style Library via l'entrée Recraft Controls, assurez-vous qu'il ne s'agit pas d'un style d'art vectoriel, car cela pourrait renvoyer des données SVG au lieu d'une image.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | L'image générée ou le lot d'images. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`

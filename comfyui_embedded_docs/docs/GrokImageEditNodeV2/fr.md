# Grok Image Edit

Modifie une ou plusieurs images existantes en fonction d'un prompt textuel. Le nœud envoie la ou les images de référence connectées et le prompt à l'API de modification d'images Grok à l'aide du modèle sélectionné, puis renvoie la ou les images modifiées.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle d'image Grok à utiliser. Les sous-paramètres affichés ci-dessous changent selon le modèle sélectionné. | DYNAMIC_COMBO | Oui | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | Le prompt textuel utilisé pour générer l'image. (par défaut : "") | STRING | Oui | N/A |
| `graine` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes indépendamment de la graine. (par défaut : 0) | INT | Oui | 0 à 2147483647 |

### Entrées grok-imagine-image-2.0

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resolution` | Résolution de sortie des images modifiées. | COMBO | Oui | "1K"<br>"2K" |
| `number_of_images` | Nombre d'images modifiées à générer. (par défaut : 1) | INT | Oui | 1 à 10 |
| `quality` | Niveau de qualité des images générées. | COMBO | Oui | "medium"<br>"low" |
| `aspect_ratio` | Rapport d'aspect de l'image modifiée. (par défaut : "auto") | COMBO | Oui | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Entrées grok-imagine-image-quality et grok-imagine-image

Partagé par grok-imagine-image-quality et grok-imagine-image.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resolution` | Résolution de sortie des images modifiées. | COMBO | Oui | "1K"<br>"2K" |
| `number_of_images` | Nombre d'images modifiées à générer. (par défaut : 1) | INT | Oui | 1 à 10 |
| `aspect_ratio` | Autorisé uniquement lorsque plusieurs images sont connectées. (par défaut : "auto") | COMBO | Oui | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Entrées grok-imagine-image-pro

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resolution` | Résolution de sortie des images modifiées. | COMBO | Oui | "1K"<br>"2K" |
| `number_of_images` | Nombre d'images modifiées à générer. (par défaut : 1) | INT | Oui | 1 à 10 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Emplacement extensible : connectez de 1 à N images de référence à modifier. Les emplacements utilisent les noms de gabarit `image_1`, `image_2`, `image_3` ; le nombre maximal d'emplacements dépend du modèle sélectionné. | IMAGE | Oui | 1 image pour `grok-imagine-image-pro`<br>1 à 3 images pour `grok-imagine-image-2.0`, `grok-imagine-image-quality` et `grok-imagine-image` |

**Remarque sur les contraintes :**
- `prompt` doit contenir au moins 1 caractère non blanc.
- Au moins une image de référence est requise pour la modification ; le nœud déclenche une erreur si aucune image n'est connectée.
- Le nombre maximal d'images d'entrée est de 1 pour `grok-imagine-image-pro` et de 3 pour `grok-imagine-image-2.0`, `grok-imagine-image-quality` et `grok-imagine-image`. Connecter plus d'images que le modèle ne prend en charge déclenche une erreur.
- La limite d'images compte chaque image dans les entrées connectées, donc un lot contenant plusieurs images compte comme plusieurs images dans la limite.
- Pour `grok-imagine-image-quality` et `grok-imagine-image`, un `aspect_ratio` personnalisé (toute valeur autre que "auto") n'est autorisé que lorsque plusieurs images sont connectées. Avec une seule image, `aspect_ratio` doit être "auto".
- Pour `grok-imagine-image-2.0`, `aspect_ratio` peut être défini librement, même avec une seule image.
- Le sous-paramètre `quality` n'est disponible qu'avec `grok-imagine-image-2.0`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | La ou les images modifiées renvoyées par l'API Grok. Si une seule image est générée, elle est renvoyée directement. Si plusieurs images sont générées, elles sont concaténées dans un seul tenseur de lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`

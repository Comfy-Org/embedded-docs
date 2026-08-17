# Grok Image Edit

Modifie une ou plusieurs images existantes en fonction d'un prompt texte. Le nœud envoie l'image ou les images de référence connectées et le prompt à l'API d'édition d'images Grok en utilisant le modèle sélectionné, puis renvoie l'image ou les images modifiées.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle d'image Grok à utiliser. Les sous-paramètres affichés ci-dessous changent en fonction du modèle sélectionné. | DYNAMIC_COMBO | Oui | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | Le prompt texte utilisé pour générer l'image. (défaut : "") | STRING | Oui | N/A |
| `seed` | Graine permettant de déterminer si le nœud doit être relancé ; les résultats réels sont non déterministes quelle que soit la graine. (défaut : 0) | INT | Oui | 0 à 2147483647 |

### grok-imagine-image-2.0 Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Résolution de sortie des images modifiées. | COMBO | Oui | "1K"<br>"2K" |
| `number_of_images` | Nombre d'images modifiées à générer. (défaut : 1) | INT | Oui | 1 à 10 |
| `quality` | Niveau de qualité des images générées. | COMBO | Oui | "medium"<br>"low" |
| `aspect_ratio` | Rapport d'aspect de l'image modifiée. (défaut : « auto ») | COMBO | Oui | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality et grok-imagine-image Entrées

Paramètres partagés par grok-imagine-image-quality et grok-imagine-image.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Résolution de sortie des images modifiées. | COMBO | Oui | "1K"<br>"2K" |
| `number_of_images` | Nombre d'images modifiées à générer. (défaut : 1) | INT | Oui | 1 à 10 |
| `aspect_ratio` | Autorisé uniquement lorsque plusieurs images sont connectées. (défaut : « auto ») | COMBO | Oui | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Résolution de sortie des images modifiées. | COMBO | Oui | "1K"<br>"2K" |
| `number_of_images` | Nombre d'images modifiées à générer. (défaut : 1) | INT | Oui | 1 à 10 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Emplacement extensible : connectez 1 ou plusieurs images de référence à modifier. Le premier emplacement est `image`, les emplacements supplémentaires sont `image_1`, `image_2`, etc. Le nombre maximal d'images dépend du modèle sélectionné. | IMAGE | Oui | 1 image pour `grok-imagine-image-pro`<br>1 à 3 images pour `grok-imagine-image-2.0`, `grok-imagine-image-quality` et `grok-imagine-image` |

**Remarque sur les contraintes :**
- `prompt` doit contenir au moins 1 caractère non blanc.
- Au moins une image de référence est requise pour l'édition ; le nœud génère une erreur si aucune image n'est connectée.
- Le nombre maximal d'images d'entrée est 1 pour `grok-imagine-image-pro` et 3 pour `grok-imagine-image-2.0`, `grok-imagine-image-quality` et `grok-imagine-image`. Connecter plus d'images que le modèle ne prend en charge génère une erreur.
- Pour `grok-imagine-image-quality` et `grok-imagine-image`, un `aspect_ratio` personnalisé (autre que « auto ») n'est autorisé que lorsque plusieurs images sont connectées. Avec une seule image, `aspect_ratio` doit être « auto ».
- Pour `grok-imagine-image-2.0`, `aspect_ratio` peut être défini librement même avec une seule image.
- Le sous-paramètre `quality` n'est disponible qu'avec `grok-imagine-image-2.0`.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `IMAGE` | L'image ou les images modifiées renvoyées par l'API Grok. Si une seule image est générée, elle est renvoyée directement. Si plusieurs images sont générées, elles sont concaténées en un seul tenseur de lot (batch). | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`

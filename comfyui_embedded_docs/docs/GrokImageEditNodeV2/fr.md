# Grok Image Edit

Modifie une image existante en fonction d'un prompt textuel. Ce nœud envoie vos images et une description textuelle à l'API Grok, qui modifie les images selon vos instructions et renvoie le résultat.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `modèle` | Le modèle d'image Grok à utiliser. Les sous-paramètres affichés ci-dessous changent en fonction du modèle sélectionné. | MODEL | Oui | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | Le prompt textuel utilisé pour générer l'image. (défaut : "") | STRING | Oui | N/A |
| `graine` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine. (défaut : 0) | INT | Oui | 0 à 2147483647 |

### Entrées de grok-imagine-image-2.0

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Image(s) de référence à modifier. Jusqu'à 3 images. | IMAGE | Oui | 1 à 3 images |
| `resolution` | Résolution de sortie des images modifiées. | STRING | Oui | "1K"<br>"2K" |
| `number_of_images` | Nombre d'images modifiées à générer. (défaut : 1) | INT | Oui | 1 à 10 |
| `quality` | Niveau de qualité des images générées. | STRING | Oui | "medium"<br>"low" |
| `aspect_ratio` | Format de l'image modifiée. (défaut : "auto") | STRING | Oui | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Entrées de grok-imagine-image-quality et grok-imagine-image

Partagées par grok-imagine-image-quality et grok-imagine-image.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Image(s) de référence à modifier. Jusqu'à 3 images. | IMAGE | Oui | 1 à 3 images |
| `resolution` | Résolution de sortie des images modifiées. | STRING | Oui | "1K"<br>"2K" |
| `number_of_images` | Nombre d'images modifiées à générer. (défaut : 1) | INT | Oui | 1 à 10 |
| `aspect_ratio` | Autorisé uniquement lorsque plusieurs images sont connectées. (défaut : "auto") | STRING | Oui | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Entrées de grok-imagine-image-pro

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Image de référence à modifier. | IMAGE | Oui | 1 image |
| `resolution` | Résolution de sortie des images modifiées. | STRING | Oui | "1K"<br>"2K" |
| `number_of_images` | Nombre d'images modifiées à générer. (défaut : 1) | INT | Oui | 1 à 10 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Emplacement extensible : connectez 1 ou plusieurs images de référence à modifier. Des emplacements numérotés tels que `image_1`, `image_2`, `image_3` peuvent être ajoutés. Le nombre maximum d'images dépend du modèle sélectionné (voir les sections de modèle ci-dessus). | IMAGE | Oui | 1 à 3 images, selon le modèle |

**Remarque sur les contraintes :**
- `prompt` doit contenir au moins 1 caractère non blanc.
- Au moins une image de référence est requise pour la modification ; le nœud génère une erreur si aucune image n'est connectée.
- Le nombre maximum d'images en entrée est de 1 pour `grok-imagine-image-pro` et de 3 pour `grok-imagine-image-2.0`, `grok-imagine-image-quality` et `grok-imagine-image`. Connecter plus d'images que le modèle ne le permet génère une erreur.
- Pour `grok-imagine-image-quality` et `grok-imagine-image`, un `aspect_ratio` personnalisé (autre que "auto") n'est autorisé que lorsque plusieurs images sont connectées. Avec une seule image, `aspect_ratio` doit être "auto".
- Pour `grok-imagine-image-2.0`, `aspect_ratio` peut être défini librement même avec une seule image.
- Le sous-paramètre `quality` n'est disponible qu'avec `grok-imagine-image-2.0`.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `IMAGE` | Image(s) modifiée(s) renvoyée(s) par l'API Grok. Si une seule image est générée, elle est renvoyée directement. Si plusieurs images sont générées, elles sont concaténées en un seul tenseur de lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`

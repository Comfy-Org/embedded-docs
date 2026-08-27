# OpenAI GPT Image 2

Ce nœud génère des images à l'aide de l'API GPT Image d'OpenAI. Il prend en charge plusieurs modèles (`gpt-image-2`, `gpt-image-1.5` et `gpt-image-1`), vous permet de fournir des images de référence pour l'édition, et peut utiliser un masque pour spécifier les parties d'une image à modifier.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle GPT Image d'OpenAI à utiliser. La sélection d'un modèle révèle des paramètres supplémentaires spécifiques à ce modèle. | DYNAMIC_COMBO | Oui | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Invite de texte pour GPT Image (défaut : `""`). | STRING | Oui | N/A |
| `n` | Nombre d'images à générer (défaut : `1`). | INT | Oui | 1 à 8 |
| `graine` | Graine pour la reproductibilité (défaut : `0`). Pas encore implémenté dans le backend. | INT | Oui | 0 à 2147483647 |

### Entrées gpt-image-2

Ces entrées apparaissent lorsque `model` est défini sur `gpt-image-2`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `taille` | Taille de l'image. Sélectionnez « Custom » pour utiliser la largeur et la hauteur personnalisées (défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `largeur_personnalisée` | Utilisé uniquement lorsque `model.size` est « Custom ». Doit être un multiple de 16 (défaut : `1024`). | INT | Non | 1024 à 3840 |
| `hauteur_personnalisée` | Utilisé uniquement lorsque `model.size` est « Custom ». Doit être un multiple de 16 (défaut : `1024`). | INT | Non | 1024 à 3840 |
| `arrière-plan` | Renvoie l'image avec ou sans arrière-plan (défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"opaque"` |
| `qualité` | Qualité de l'image, affecte le coût et le temps de génération (défaut : `"low"`). | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Image(s) de référence facultative(s) pour l'édition d'image. Jusqu'à 16 images. Voir Entrées de référence pour plus de détails. | IMAGE | Non | 0 à 16 |
| `model.mask` | Masque facultatif pour l'inpainting (les zones blanches seront remplacées). Nécessite exactement une image de référence. | MASK | Non | N/A |

### Entrées gpt-image-1.5 et gpt-image-1

Ces entrées apparaissent lorsque `model` est défini sur `gpt-image-1.5` ou `gpt-image-1`. Les deux modèles partagent le même ensemble de paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `taille` | Taille de l'image (défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `arrière-plan` | Renvoie l'image avec ou sans arrière-plan (défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualité` | Qualité de l'image, affecte le coût et le temps de génération (défaut : `"low"`). | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Image(s) de référence facultative(s) pour l'édition d'image. Jusqu'à 16 images. Voir Entrées de référence pour plus de détails. | IMAGE | Non | 0 à 16 |
| `model.mask` | Masque facultatif pour l'inpainting (les zones blanches seront remplacées). Nécessite exactement une image de référence. | MASK | Non | N/A |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.images` | Emplacement extensible : connectez 1..N éléments (par ex. `image_1`...`image_16`) ; jusqu'à 16 images de référence pour tous les modèles. | IMAGE | Non | 1 à 16 |
| `model.mask` | Masque facultatif pour l'inpainting (les zones blanches seront remplacées). Nécessite exactement une image de référence. | MASK | Non | N/A |

**Contraintes et limitations des paramètres :**

- Lorsque `model.size` est « Custom » (gpt-image-2 uniquement), `model.custom_width` et `model.custom_height` doivent tous deux être des multiples de 16, le bord le plus long ne doit pas dépasser 3840, le rapport hauteur/largeur ne doit pas dépasser 3:1, et le nombre total de pixels doit être compris entre 655 360 et 8 294 400.
- `model.mask` nécessite exactement une image de référence dans `model.images` : il ne peut pas être utilisé sans image, ni avec plus d'une image.
- Lorsque `model.mask` est utilisé, ses dimensions doivent correspondre à celles de l'image de référence.
- Lorsque `model.images` est fourni, le nœud fonctionne en mode édition d'image ; sans `model.images`, il génère des images à partir de la seule invite.
- Les images de référence sont réduites avant d'être envoyées à l'API.
- `seed` n'est actuellement pas implémenté dans le backend.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image ou les images générées. Toutes les images renvoyées sont empilées dans un seul lot ; si leurs dimensions diffèrent, elles sont redimensionnées pour correspondre à la première image. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`

# OpenAI GPT Image 2

Ce nœud génère des images à l'aide de l'API GPT Image d'OpenAI. Il prend en charge plusieurs modèles GPT Image, des images de référence facultatives pour l'édition et un masque facultatif pour l'inpainting. Lorsque des images de référence sont fournies, le nœud envoie une demande d'édition à l'API ; sinon, il envoie une demande de génération simple.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle OpenAI GPT Image à utiliser. La sélection d'un modèle révèle des paramètres supplémentaires spécifiques à ce modèle. | DYNAMIC_COMBO | Oui | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Invite de texte pour GPT Image (par défaut : ""). | STRING | Oui | N/A |
| `n` | Nombre d'images à générer (par défaut : 1). | INT | Oui | 1 à 8 |
| `seed` | Seed pour la reproductibilité (par défaut : 0). Pas encore implémenté dans le backend. | INT | Oui | 0 à 2147483647 |

### gpt-image-2 Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.size` | Taille de l'image. Sélectionnez "Custom" pour utiliser la largeur et la hauteur personnalisées (par défaut : "auto"). | COMBO | Oui | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Utilisé uniquement lorsque `size` est "Custom". Doit être un multiple de 16 (par défaut : 1024). | INT | Non | 1024 à 3840 |
| `model.custom_height` | Utilisé uniquement lorsque `size` est "Custom". Doit être un multiple de 16 (par défaut : 1024). | INT | Non | 1024 à 3840 |
| `model.background` | Renvoie l'image avec ou sans arrière-plan (par défaut : "auto"). | COMBO | Oui | `"auto"`<br>`"opaque"` |
| `model.quality` | Qualité de l'image, affecte le coût et le temps de génération (par défaut : "low"). | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |

### gpt-image-1.5 et gpt-image-1 Entrées

Ces deux modèles partagent le même ensemble de paramètres spécifiques au modèle.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.size` | Taille de l'image (par défaut : "auto"). | COMBO | Oui | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Renvoie l'image avec ou sans arrière-plan (par défaut : "auto"). | COMBO | Oui | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualité de l'image, affecte le coût et le temps de génération (par défaut : "low"). | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |

### Entrées de référence

Ces entrées sont disponibles pour tous les modèles.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.images` | Image(s) de référence facultative(s) pour l'édition d'image. Emplacement extensible : connectez jusqu'à 16 images (`image_1` à `image_16`). | IMAGE | Non | 0 à 16 images |
| `model.mask` | Masque facultatif pour l'inpainting (les zones blanches seront remplacées). Nécessite exactement une image de référence. | MASK | Non | N/A |

**Contraintes et limitations des paramètres :**

- Lorsque `model.size` est "Custom" (gpt-image-2 uniquement), `model.custom_width` et `model.custom_height` doivent être des multiples de 16, le bord le plus long ne doit pas dépasser 3840 pixels, le rapport hauteur/largeur ne doit pas dépasser 3:1, et le nombre total de pixels doit être compris entre 655 360 et 8 294 400.
- Un masque nécessite exactement une image de référence. Un masque ne peut pas être utilisé sans image d'entrée, et il ne peut pas être utilisé avec plusieurs images d'entrée.
- Lorsqu'un masque est fourni, la hauteur et la largeur du masque doivent correspondre à la hauteur et à la largeur de l'image d'entrée.
- Les images de référence sont réduites à un maximum de 2048 x 2048 pixels au total avant d'être envoyées à l'API.
- Le paramètre `seed` n'est pas encore implémenté dans le backend.
- Si l'API renvoie des images de dimensions différentes dans une même réponse, toutes les images sont redimensionnées pour correspondre aux dimensions de la première image.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image ou les images générées, empilées en un seul tenseur de lot de forme (N, H, W, C). | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`

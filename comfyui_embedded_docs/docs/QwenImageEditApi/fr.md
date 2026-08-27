# Qwen Image 3 Édition

Ce nœud utilise les modèles Qwen-Image 3.0 pour modifier ou combiner jusqu'à 3 images de référence guidées par un prompt texte. Vous sélectionnez un modèle, fournissez le prompt et les images de référence, et le nœud renvoie une ou plusieurs images générées.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `modèle` | Modèle à utiliser. Cette sélection inclut également le prompt texte, jusqu'à 3 entrées d'images de référence et un prompt négatif facultatif. | DYNAMIC_COMBO | Oui | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `taille` | Résolution de sortie. « match input » réutilise la taille de la première image de référence, « auto » laisse le modèle choisir une taille avec le même rapport hauteur/largeur, « custom » définit une largeur et une hauteur explicites. | DYNAMIC_COMBO | Oui | "match input"<br>"auto"<br>"custom" |
| `n` | Nombre d'images à générer, renvoyé sous forme de lot. (défaut : 1) | INT | Non | 1 à 6 |
| `graine` | Graine à utiliser pour la génération. (défaut : 42) | INT | Non | 0 à 2147483647 |
| `extension de prompt` | Indique s'il faut enrichir le prompt avec l'assistance de l'IA. (défaut : True) | BOOLEAN | Non | True<br>False |
| `filigrane` | Indique s'il faut ajouter un filigrane généré par l'IA au résultat. (défaut : False) | BOOLEAN | Non | True<br>False |

### Entrées qwen-image-3.0-pro et qwen-image-3.0

Les deux modèles partagent les mêmes sous-paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Instructions de modification. Prend en charge l'anglais et le chinois, ainsi que les références de style @Image1 aux images d'entrée. (défaut : "") | STRING | Oui | - |
| `negative_prompt` | Prompt négatif décrivant ce qu'il faut éviter. (défaut : "") | STRING | Non | - |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Emplacement extensible : connectez 1 à 3 images de référence (`image_1`, `image_2`, `image_3`). Référencez-les dans le prompt sous la forme @Image1, @Image2, @Image3, numérotées dans l'ordre d'entrée ; une entrée groupée compte une fois par image. | IMAGE | Oui | 1 à 3 |

### Entrées de taille personnalisée

Affichées lorsque `size` est défini sur « custom ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `width` | Largeur de sortie. La surface totale en pixels doit être comprise entre 512x512 et 2560x2560 ; le rapport hauteur/largeur doit être compris entre 1:8 et 8:1. (défaut : 1024) | INT | Oui (lorsque `size` est « custom ») | 256 à 2560, pas de 16 |
| `height` | Hauteur de sortie. La surface totale en pixels doit être comprise entre 512x512 et 2560x2560 ; le rapport hauteur/largeur doit être compris entre 1:8 et 8:1. (défaut : 1024) | INT | Oui (lorsque `size` est « custom ») | 256 à 2560, pas de 16 |

### Contraintes

- Le prompt texte est obligatoire et doit contenir au moins un caractère.
- Un maximum de 3 images de référence est pris en charge ; une erreur est levée si plus d'images sont fournies (une entrée groupée compte une fois par image).
- Lorsque `size` est défini sur « custom », des valeurs explicites de largeur et de hauteur doivent être fournies et sont validées : la surface totale en pixels doit être comprise entre 262 144 (512x512) et 6 553 600 (2560x2560) pixels, et le rapport hauteur/largeur doit être compris entre 1:8 et 8:1.
- Lorsque `size` est défini sur « match input », au moins une image de référence est requise car les dimensions de la première image de référence sont utilisées ; les dimensions sont mises à l'échelle pour s'adapter à la surface et à la plage de rapports hauteur/largeur prises en charge.
- Lorsque `size` est défini sur « auto », le modèle choisit la taille de sortie (1,9 à 4,2 mégapixels) tout en préservant le rapport hauteur/largeur de l'entrée.
- Les références dans le prompt utilisent @Image1, @Image2, @Image3, numérotées dans l'ordre d'entrée ; une référence à un index supérieur au nombre d'images connectées lève une erreur. Les balises ne sont reconnues qu'aux limites des mots, de sorte que les adresses comme user@image1.com restent inchangées.
- Les images de référence d'entrée sont réduites à 2048x2048 pixels au maximum avant d'être envoyées à l'API. Si l'encodage PNG dépasse la limite de taille de l'API, un encodage JPEG est utilisé à la place.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `IMAGE` | L'image ou les images générées, renvoyées sous forme de lot. Jusqu'à `n` images sont renvoyées. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`

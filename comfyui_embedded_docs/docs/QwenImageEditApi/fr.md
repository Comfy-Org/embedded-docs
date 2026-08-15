# QwenImageEditApi

Ce nœud utilise les modèles Qwen-Image 3.0 pour modifier ou combiner jusqu’à 3 images de référence, guidé par un prompt texte. Vous fournissez le prompt texte et les images de référence, et le nœud renvoie le résultat généré sous forme d’une ou plusieurs images.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. Cette sélection inclut également le prompt texte, jusqu’à 3 entrées d’images de référence et un prompt négatif facultatif. | COMBO | Oui | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Résolution de sortie. « match input » réutilise la taille de la première image de référence, « auto » laisse le modèle choisir une taille avec le même rapport hauteur/largeur, « custom » définit une largeur et une hauteur explicites. | COMBO | Oui | "match input"<br>"auto"<br>"custom" |
| `n` | Nombre d’images à générer, renvoyées sous forme de lot. (par défaut : 1) | INT | Non | 1 à 6 |
| `seed` | Graine à utiliser pour la génération. (par défaut : 42) | INT | Non | 0 à 2147483647 |
| `prompt_extend` | Indique s’il faut enrichir le prompt avec l’assistance de l’IA. (par défaut : True) | BOOLEAN | Non | True<br>False |
| `watermark` | Indique s’il faut ajouter un filigrane généré par l’IA au résultat. (par défaut : False) | BOOLEAN | Non | True<br>False |

### Entrées qwen-image-3.0-pro et qwen-image-3.0

Les deux modèles partagent les mêmes sous-paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Instructions de modification. Prend en charge l’anglais et le chinois, ainsi que les références de type @Image1 aux images d’entrée. (par défaut : "") | STRING | Oui | - |
| `negative_prompt` | Prompt négatif décrivant ce qu’il faut éviter. (par défaut : "") | STRING | Non | - |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Emplacement extensible : connectez 1 à 3 images de référence (`image_1`, `image_2`, `image_3`). Utilisez @Image1, @Image2, @Image3 dans le prompt, numérotées dans l’ordre d’entrée ; chaque image d’une entrée par lot compte pour une référence. | IMAGE | Oui | 1 à 3 |

### Entrées de taille personnalisée

Affichées lorsque `size` est défini sur « custom ».

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `width` | Largeur de sortie. La surface totale en pixels doit être comprise entre 512x512 et 2560x2560 ; tout rapport hauteur/largeur dans cette surface est accepté. (par défaut : 1024) | INT | Oui (lorsque `size` est « custom ») | 256 à 2560, pas 16 |
| `height` | Hauteur de sortie. La surface totale en pixels doit être comprise entre 512x512 et 2560x2560 ; tout rapport hauteur/largeur dans cette surface est accepté. (par défaut : 1024) | INT | Oui (lorsque `size` est « custom ») | 256 à 2560, pas 16 |

### Contraintes

- Le prompt texte est requis et doit contenir au moins un caractère.
- Un maximum de 3 images de référence est pris en charge ; une erreur est générée si davantage sont fournies (une entrée par lot compte pour une image).
- Lorsque `size` est défini sur « custom », des valeurs explicites de largeur et de hauteur doivent être fournies et sont validées : la surface totale en pixels doit être comprise entre 262 144 (512x512) et 6 553 600 (2560x2560) pixels, et le rapport hauteur/largeur doit être compris entre 1:8 et 8:1.
- Lorsque `size` est défini sur « match input », au moins une image de référence est requise, car les dimensions de la première image de référence sont utilisées ; les dimensions sont mises à l’échelle pour s’adapter à la surface et à la plage de rapports hauteur/largeur prises en charge.
- Lorsque `size` est défini sur « auto », le modèle choisit la taille de sortie en préservant le rapport hauteur/largeur d’entrée.
- Les références dans le prompt utilisent @Image1, @Image2, @Image3, numérotées dans l’ordre d’entrée ; une référence à un index supérieur au nombre d’images connectées génère une erreur. Les balises ne sont reconnues qu’aux limites des mots ; ainsi, les adresses comme user@image1.com restent inchangées.
- Les images de référence en entrée sont redimensionnées à 2048x2048 pixels au maximum avant d’être envoyées à l’API.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image ou les images générées sont renvoyées sous forme de lot. Jusqu’à `n` images sont renvoyées. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`

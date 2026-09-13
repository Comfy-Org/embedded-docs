# Qwen Image 3 Texte vers Image

Qwen Image 3 Text to Image génère une ou plusieurs images à partir d’un prompt textuel en utilisant les modèles Qwen-Image 3.0. Vous sélectionnez un modèle et fournissez un prompt, et le nœud renvoie les images générées sous forme de lot.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser (par défaut : "qwen-image-3.0-pro"). Ce sélecteur composite fournit également le prompt, le prompt négatif, la largeur d’image et la hauteur d’image. | DYNAMIC_COMBO | Oui | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Nombre d’images à générer, renvoyées sous forme de lot (par défaut : 1). | INT | Non | 1 à 6 |
| `graine` | Graine à utiliser pour la génération (par défaut : 42). Peut être définie pour se mettre à jour automatiquement après chaque génération. | INT | Non | 0 à 2147483647 |
| `extension de prompt` | Indique s’il faut améliorer le prompt avec l’assistance IA (par défaut : true). Option avancée. | BOOLEAN | Non | true<br>false |
| `filigrane` | Indique s’il faut ajouter un filigrane généré par IA au résultat (par défaut : false). Option avancée. | BOOLEAN | Non | true<br>false |

### Entrées qwen-image-3.0-pro et qwen-image-3.0

Partagées par qwen-image-3.0-pro et qwen-image-3.0.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt décrivant l’image. Prend en charge l’anglais et le chinois. Doit contenir au moins 1 caractère. | STRING | Oui | Texte libre |
| `negative_prompt` | Prompt négatif décrivant ce qu’il faut éviter (par défaut : ""). | STRING | Non | Texte libre |
| `width` | La surface totale en pixels doit être comprise entre 512x512 et 2560x2560 ; tout rapport d’aspect dans cette zone fonctionne. (par défaut : 1024) | INT | Non | 256 à 2560 (pas de 16) |
| `height` | La surface totale en pixels doit être comprise entre 512x512 et 2560x2560 ; tout rapport d’aspect dans cette zone fonctionne. (par défaut : 1024) | INT | Non | 256 à 2560 (pas de 16) |

Remarque : L’entrée `model` est un sélecteur composite avec les sous-champs `model` (ID du modèle), `prompt` (requis, doit contenir au moins 1 caractère), `negative_prompt` (facultatif), `width` et `height`. La surface combinée en pixels de `width` et `height` doit être comprise entre 262 144 pixels (512x512) et 6 553 600 pixels (2560x2560), et le rapport d’aspect doit rester compris entre 1:8 et 8:1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image ou les images générées, renvoyées sous forme de lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/fr.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`

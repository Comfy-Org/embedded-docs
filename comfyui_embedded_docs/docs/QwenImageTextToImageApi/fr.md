# QwenImageTextToImageApi

Qwen Image 3 Text to Image génère une ou plusieurs images à partir d'un prompt texte en utilisant les modèles Qwen-Image 3.0. Vous sélectionnez un modèle et fournissez un prompt, et le nœud renvoie les images générées sous forme de lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|----------------|--------|-------|
| `model` | Modèle à utiliser (par défaut : "qwen-image-3.0-pro"). Ce sélecteur composite fournit également le prompt, la largeur d'image, la hauteur d'image et le prompt négatif optionnel. | MODEL | Oui | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Nombre d'images à générer, renvoyées sous forme de lot (par défaut : 1). | INT | Non | 1 à 6 |
| `seed` | Graine à utiliser pour la génération (par défaut : 42). Peut être configurée pour se mettre à jour automatiquement après chaque génération. | INT | Non | 0 à 2147483647 |
| `prompt_extend` | Indique s'il faut enrichir le prompt avec l'assistance IA (par défaut : true). Option avancée. | BOOLEAN | Non | true<br>false |
| `watermark` | Indique s'il faut ajouter un filigrane généré par IA au résultat (par défaut : false). Option avancée. | BOOLEAN | Non | true<br>false |

Note : L'entrée `model` est un sélecteur composite avec les sous-champs suivants : `model` (ID du modèle), `prompt` (le prompt texte, qui doit contenir au moins 1 caractère), `width` et `height` (dimensions de l'image, validées par le nœud), et `negative_prompt` (prompt négatif optionnel).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image ou les images générées, renvoyées sous forme de lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/fr.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`

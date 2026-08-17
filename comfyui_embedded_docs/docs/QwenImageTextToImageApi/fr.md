# Qwen Image 3 Texte vers Image

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Modèle à utiliser (par défaut : "qwen-image-3.0-pro"). Ce sélecteur composite fournit également le prompt, la largeur d'image, la hauteur d'image et le prompt négatif optionnel. | DYNAMIC_COMBO | Oui | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Nombre d'images à générer, renvoyées sous forme de lot (par défaut : 1). | INT | Non | 1 à 6 |
| `seed` | Seed à utiliser pour la génération (par défaut : 42). Peut être réglé pour une mise à jour automatique après chaque génération. | INT | Non | 0 à 2147483647 |
| `prompt_extend` | Indique s'il faut enrichir le prompt avec l'assistance de l'IA (par défaut : true). Option avancée. | BOOLEAN | Non | true<br>false |
| `watermark` | Indique s'il faut ajouter un filigrane généré par l'IA au résultat (par défaut : false). Option avancée. | BOOLEAN | Non | true<br>false |

### Entrées de qwen-image-3.0-pro et qwen-image-3.0

Partagées par qwen-image-3.0-pro et qwen-image-3.0.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Prompt décrivant l'image. Prend en charge l'anglais et le chinois. Doit contenir au moins 1 caractère. | STRING | Oui | Texte libre |
| `negative_prompt` | Prompt négatif décrivant ce qu'il faut éviter (par défaut : ""). | STRING | Non | Texte libre |
| `width` | La surface totale en pixels doit être comprise entre 512x512 et 2560x2560 ; le rapport hauteur/largeur doit être compris entre 1:8 et 8:1. (par défaut : 1024) | INT | Non | 256 à 2560 (pas de 16) |
| `height` | La surface totale en pixels doit être comprise entre 512x512 et 2560x2560 ; le rapport hauteur/largeur doit être compris entre 1:8 et 8:1. (par défaut : 1024) | INT | Non | 256 à 2560 (pas de 16) |

Remarque : L'entrée `model` est un sélecteur composite avec les sous-champs `model` (identifiant du modèle), `prompt` (obligatoire, doit contenir au moins 1 caractère), `width` et `height` (dimensions de l'image), et `negative_prompt` (optionnel). La surface de pixels combinée de `width` et `height` doit être comprise entre 262 144 pixels (512x512) et 6 553 600 pixels (2560x2560), et le rapport hauteur/largeur doit rester entre 1:8 et 8:1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image ou les images générées, renvoyées sous forme de lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/fr.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`

# BriaGenFill

Ce nœud génère des objets ou des décors dans une région masquée d'une image à l'aide de l'API Bria. Il téléverse l'image et le masque, envoie l'invite au service de remplissage génératif Bria, attend que l'opération soit terminée, puis renvoie l'image modifiée. Il s'agit d'une opération API payante (0,0429 $ US par requête).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à modifier. | IMAGE | Oui | - |
| `mask` | Les zones blanches sont remplies de contenu généré, les zones noires sont préservées. Le masque est binarisé avant l'envoi, donc les zones partiellement peintes sont considérées comme blanches. Doit avoir le même rapport hauteur/largeur que l'image. | MASK | Oui | - |
| `prompt` | Description de ce qui doit être généré dans la région masquée. Doit contenir au moins 1 caractère. | STRING | Oui | - |
| `negative_prompt` | Une description du contenu à éviter dans le résultat généré. Si elle est laissée vide, elle n'est pas envoyée à l'API. | STRING | Oui | - |
| `refine_prompt` | Ajuste automatiquement l'invite pour de meilleurs résultats ; désactivez pour utiliser l'invite exactement telle qu'écrite. (par défaut : true) | BOOLEAN | Oui | true<br>false |
| `seed` | Graine pour le processus de génération. (par défaut : 42) | INT | Oui | 1 à 2147483647 |
| `moderation` | Paramètres de modération pour la requête. Lorsqu'il est défini sur « true », les options de modération imbriquées décrites ci-dessous sont appliquées. (par défaut : « false ») | COMBO | Oui | "false"<br>"true" |

Remarque : le `prompt` ne doit pas être vide, et le `mask` doit avoir le même rapport hauteur/largeur que l'`image`.

Lorsque `moderation` est défini sur « true », les options booléennes imbriquées suivantes sont disponibles :
- `prompt_content_moderation` (par défaut : false) : Applique la modération de contenu à l'invite.
- `visual_input_moderation` (par défaut : false) : Applique la modération de contenu à l'image d'entrée.
- `visual_output_moderation` (par défaut : false) : Applique la modération de contenu à l'image de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image résultante avec la région masquée remplie par le contenu généré. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/fr.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`

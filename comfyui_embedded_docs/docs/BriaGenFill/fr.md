# BriaGenFill

Ce nœud génère des objets ou des décors à l'intérieur d'une région masquée d'une image à l'aide de l'API Bria. Il téléverse l'image et le masque, envoie la prompt au service de remplissage génératif Bria, attend la fin de l'opération, puis renvoie l'image éditée. Cette opération est payante (0,0429 $US par requête).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à modifier. | IMAGE | Oui | - |
| `mask` | Les zones blanches sont remplies avec le contenu généré, les zones noires sont préservées. Le masque est binarisé avant l'envoi, donc les zones partiellement peintes comptent comme blanches. Doit avoir le même rapport largeur/hauteur que l'image. | MASK | Oui | - |
| `prompt` | Description de ce qu'il faut générer à l'intérieur de la région masquée. Doit contenir au moins 1 caractère. | STRING | Oui | - |
| `negative_prompt` | Une prompt décrivant le contenu à éviter dans le résultat généré. Si elle est laissée vide, elle n'est pas envoyée à l'API. | STRING | Oui | - |
| `refine_prompt` | Ajuste automatiquement la prompt pour de meilleurs résultats ; désactivez pour utiliser la prompt exactement telle qu'écrite. (défaut : true) | BOOLEAN | Oui | true<br>false |
| `seed` | Graine pour le processus de génération. (défaut : 42) | INT | Oui | 1 à 2147483647 |
| `moderation` | Paramètres de modération pour la requête. Lorsque défini sur « true », les options de modération imbriquées décrites ci-dessous sont appliquées. (défaut : « false ») | COMBO | Oui | « false »<br>« true » |

Note : La `prompt` ne doit pas être vide, et le `mask` doit avoir le même rapport largeur/hauteur que l'`image`. Le masque est binarisé à 50 % d'opacité, donc les zones peintes à moins de la moitié de l'opacité sont ignorées ; si le masque ne contient aucune zone blanche après la binarisation, le nœud génère une erreur.

Lorsque `moderation` est défini sur « true », les options booléennes imbriquées suivantes sont disponibles :
- `prompt_content_moderation` (défaut : false) : Applique la modération de contenu à la prompt.
- `visual_input_moderation` (défaut : false) : Applique la modération de contenu à l'image d'entrée.
- `visual_output_moderation` (défaut : false) : Applique la modération de contenu à l'image de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image résultante avec la région masquée remplie par le contenu généré. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/fr.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`

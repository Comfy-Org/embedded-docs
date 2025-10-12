> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/fr.md)

Ce nœud génère des images de manière synchrone en utilisant le modèle Stable Diffusion 3.5 de Stability AI. Il crée des images basées sur des invites textuelles et peut également modifier des images existantes lorsqu'elles sont fournies en entrée. Le nœud prend en charge différents ratios d'aspect et préréglages de style pour personnaliser le résultat.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Ce que vous souhaitez voir dans l'image de sortie. Une invite forte et descriptive qui définit clairement les éléments, les couleurs et les sujets conduira à de meilleurs résultats. (par défaut : chaîne vide) |
| `model` | COMBO | Oui | Plusieurs options disponibles | Le modèle Stable Diffusion 3.5 à utiliser pour la génération. |
| `aspect_ratio` | COMBO | Oui | Plusieurs options disponibles | Ratio d'aspect de l'image générée. (par défaut : ratio 1:1) |
| `style_preset` | COMBO | Non | Plusieurs options disponibles | Style souhaité optionnel de l'image générée. |
| `cfg_scale` | FLOAT | Oui | 1.0 à 10.0 | À quel point le processus de diffusion adhère strictement au texte de l'invite (les valeurs plus élevées maintiennent votre image plus proche de votre invite). (par défaut : 4.0) |
| `seed` | INT | Oui | 0 à 4294967294 | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) |
| `image` | IMAGE | Non | - | Image d'entrée optionnelle pour la génération image-à-image. |
| `negative_prompt` | STRING | Non | - | Mots-clés de ce que vous ne souhaitez pas voir dans l'image de sortie. Il s'agit d'une fonctionnalité avancée. (par défaut : chaîne vide) |
| `image_denoise` | FLOAT | Non | 0.0 à 1.0 | Niveau de débruitage de l'image d'entrée ; 0.0 produit une image identique à l'entrée, 1.0 équivaut à ne pas avoir fourni d'image du tout. (par défaut : 0.5) |

**Note :** Lorsqu'une `image` est fournie, le nœud passe en mode génération image-à-image et le paramètre `aspect_ratio` est automatiquement déterminé à partir de l'image d'entrée. Lorsqu'aucune `image` n'est fournie, le paramètre `image_denoise` est ignoré.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image générée ou modifiée. |

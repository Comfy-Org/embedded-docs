> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/fr.md)

Génère des images de manière synchrone en fonction de l'invite et de la résolution. Ce nœud crée des images en utilisant le modèle Stable Image Ultra de Stability AI, traitant votre invite texte et générant une image correspondante avec le rapport d'aspect et le style spécifiés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Ce que vous souhaitez voir dans l'image de sortie. Une invite forte et descriptive qui définit clairement les éléments, les couleurs et les sujets conduira à de meilleurs résultats. Pour contrôler le poids d'un mot donné, utilisez le format `(mot:poids)`, où `mot` est le mot dont vous souhaitez contrôler le poids et `poids` est une valeur comprise entre 0 et 1. Par exemple : `Le ciel était d'un (bleu:0.3) vif et (vert:0.8)` décrirait un ciel à la fois bleu et vert, mais plus vert que bleu. |
| `aspect_ratio` | COMBO | Oui | Plusieurs options disponibles | Rapport d'aspect de l'image générée. |
| `style_preset` | COMBO | Non | Plusieurs options disponibles | Style souhaité optionnel de l'image générée. |
| `seed` | INT | Oui | 0-4294967294 | La graine aléatoire utilisée pour créer le bruit. |
| `image` | IMAGE | Non | - | Image d'entrée optionnelle. |
| `negative_prompt` | STRING | Non | - | Un texte décrivant ce que vous ne souhaitez pas voir dans l'image de sortie. Il s'agit d'une fonctionnalité avancée. |
| `image_denoise` | FLOAT | Non | 0.0-1.0 | Niveau de débruitage de l'image d'entrée ; 0.0 produit une image identique à l'entrée, 1.0 équivaut à ne pas avoir fourni d'image du tout. Par défaut : 0.5 |

**Remarque :** Lorsqu'une image d'entrée n'est pas fournie, le paramètre `image_denoise` est automatiquement désactivé.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image générée basée sur les paramètres d'entrée. |

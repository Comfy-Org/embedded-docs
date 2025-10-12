> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/fr.md)

Le nœud Pikaffects génère des vidéos avec divers effets visuels appliqués à une image d'entrée. Il utilise l'API de génération vidéo de Pika pour transformer des images statiques en vidéos animées avec des effets spécifiques tels que la fusion, l'explosion ou la lévitation. Le nœud nécessite une clé API et un jeton d'authentification pour accéder au service Pika.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image de référence à laquelle appliquer l'effet Pikaffect. |
| `pikaffect` | COMBO | Oui | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" | L'effet visuel spécifique à appliquer à l'image (par défaut : "Cake-ify"). |
| `prompt_text` | STRING | Oui | - | Description textuelle guidant la génération de la vidéo. |
| `negative_prompt` | STRING | Oui | - | Description textuelle de ce qu'il faut éviter dans la vidéo générée. |
| `seed` | INT | Oui | 0 à 4294967295 | Valeur de seed aléatoire pour des résultats reproductibles. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée avec l'effet Pikaffect appliqué. |

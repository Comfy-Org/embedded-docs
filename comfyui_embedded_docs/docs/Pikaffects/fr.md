Le nœud Pikaffects génère des vidéos avec divers effets visuels appliqués à une image d'entrée. Il utilise l'API de génération vidéo de Pika pour transformer des images statiques en vidéos animées avec des effets spécifiques tels que la fonte, l'explosion ou la lévitation. Ce nœud nécessite une clé API et un jeton d'authentification pour accéder au service Pika.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image de référence à laquelle appliquer l'effet Pikaffect. | IMAGE | Oui | - |
| `pikaffect` | L'effet visuel spécifique à appliquer à l'image (par défaut : "Cake-ify"). | COMBO | Oui | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" |
| `prompt_text` | Description textuelle guidant la génération vidéo. | STRING | Oui | - |
| `negative_prompt` | Description textuelle de ce qu'il faut éviter dans la vidéo générée. | STRING | Oui | - |
| `seed` | Valeur de graine aléatoire pour des résultats reproductibles. | INT | Oui | 0 à 4294967295 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée avec l'effet Pikaffect appliqué. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/fr.md)

---
**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`

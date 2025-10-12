> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/fr.md)

Le nœud PikaFrames v2.2 génère des vidéos en combinant votre première et dernière image. Vous téléchargez deux images pour définir les points de départ et d'arrivée, et l'IA crée une transition fluide entre elles pour produire une vidéo complète.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image_start` | IMAGE | Oui | - | La première image à combiner. |
| `image_end` | IMAGE | Oui | - | La dernière image à combiner. |
| `prompt_text` | STRING | Oui | - | Prompt textuel décrivant le contenu vidéo souhaité. |
| `negative_prompt` | STRING | Oui | - | Texte décrivant ce qu'il faut éviter dans la vidéo. |
| `seed` | INT | Oui | - | Valeur de seed aléatoire pour la cohérence de la génération. |
| `resolution` | STRING | Oui | - | Résolution de la vidéo en sortie. |
| `duration` | INT | Oui | - | Durée de la vidéo générée. |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée combinant les images de début et de fin avec des transitions par IA. |
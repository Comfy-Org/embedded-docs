> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/fr.md)

Le nœud Pika Image to Video envoie une image et une invite texte à l'API Pika version 2.2 pour générer une vidéo. Il convertit votre image d'entrée en format vidéo en fonction de la description et des paramètres fournis. Le nœud gère la communication avec l'API et retourne la vidéo générée en sortie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image à convertir en vidéo |
| `prompt_text` | STRING | Oui | - | La description textuelle guidant la génération de la vidéo |
| `negative_prompt` | STRING | Oui | - | Texte décrivant ce qu'il faut éviter dans la vidéo |
| `seed` | INT | Oui | - | Valeur de seed aléatoire pour des résultats reproductibles |
| `resolution` | STRING | Oui | - | Paramètre de résolution de la vidéo en sortie |
| `duration` | INT | Oui | - | Durée de la vidéo générée en secondes |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |
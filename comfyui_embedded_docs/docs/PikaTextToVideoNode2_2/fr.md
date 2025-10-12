> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/fr.md)

Le nœud Pika Text2Video v2.2 envoie une requête textuelle à l'API Pika version 2.2 pour générer une vidéo. Il convertit votre description textuelle en vidéo en utilisant le service de génération vidéo par IA de Pika. Le nœud vous permet de personnaliser divers aspects du processus de génération vidéo, y compris le format, la durée et la résolution.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `texte de l'invite` | STRING | Oui | - | La description textuelle principale qui décrit ce que vous souhaitez générer dans la vidéo |
| `invite négative` | STRING | Oui | - | Texte décrivant ce que vous ne voulez pas voir apparaître dans la vidéo générée |
| `graine` | INT | Oui | - | Un nombre qui contrôle l'aléatoire de la génération pour des résultats reproductibles |
| `résolution` | STRING | Oui | - | Le paramètre de résolution pour la vidéo de sortie |
| `durée` | INT | Oui | - | La longueur de la vidéo en secondes |
| `rapport d'aspect` | FLOAT | Non | 0.4 - 2.5 | Format (largeur / hauteur) (par défaut : 1.7777777777777777) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré retourné par l'API Pika |
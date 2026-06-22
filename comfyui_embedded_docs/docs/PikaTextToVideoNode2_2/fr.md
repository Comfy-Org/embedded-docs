# PikaTextToVideoNode2_2

Voici la traduction en français de la documentation du nœud Pika Text2Video v2.2 :

Le nœud Pika Text2Video v2.2 envoie une invite textuelle à l'API Pika version 2.2 pour générer une vidéo. Il convertit votre description textuelle en vidéo en utilisant le service de génération vidéo par IA de Pika. Ce nœud vous permet de personnaliser divers aspects du processus de génération vidéo, notamment le rapport hauteur/largeur, la durée et la résolution.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt_text` | La description textuelle principale qui décrit ce que vous souhaitez générer dans la vidéo | STRING | Oui | - |
| `negative_prompt` | Texte décrivant ce que vous ne souhaitez pas voir apparaître dans la vidéo générée | STRING | Oui | - |
| `seed` | Un nombre qui contrôle l'aléatoire de la génération pour des résultats reproductibles | INT | Oui | - |
| `resolution` | Le paramètre de résolution pour la vidéo de sortie | STRING | Oui | - |
| `duration` | La durée de la vidéo en secondes | INT | Oui | - |
| `aspect_ratio` | Rapport hauteur/largeur (largeur / hauteur) (par défaut : 1,7777777777777777) | FLOAT | Non | 0,4 - 2,5 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré renvoyé par l'API Pika | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/fr.md)

---
**Source fingerprint (SHA-256):** `b4287519f5d4cc4a1077a58fb13aa99697e3be038a0b382c4b4c9b0e53a0d8a8`

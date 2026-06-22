# PikaImageToVideoNode2_2

Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

Le nœud Pika Image to Video envoie une image et une invite textuelle à l'API Pika version 2.2 pour générer une vidéo. Il convertit votre image d'entrée au format vidéo en fonction de la description et des paramètres fournis. Le nœud gère la communication avec l'API et renvoie la vidéo générée en sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image à convertir en vidéo | IMAGE | Oui | - |
| `prompt_text` | La description textuelle guidant la génération vidéo | STRING | Oui | - |
| `negative_prompt` | Texte décrivant ce qu'il faut éviter dans la vidéo | STRING | Oui | - |
| `seed` | Valeur de graine aléatoire pour des résultats reproductibles | INT | Oui | - |
| `resolution` | Paramètre de résolution de la vidéo de sortie | STRING | Oui | - |
| `duration` | Durée de la vidéo générée en secondes | INT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/fr.md)

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

Le nœud Pika Image to Video envoie une image et une invite textuelle à l'API Pika version 2.2 pour générer une vidéo. Il convertit votre image d'entrée au format vidéo en fonction de la description et des paramètres fournis. Le nœud gère la communication avec l'API et renvoie la vidéo générée en sortie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image à convertir en vidéo |
| `prompt_text` | STRING | Oui | - | La description textuelle guidant la génération vidéo |
| `negative_prompt` | STRING | Oui | - | Texte décrivant ce qu'il faut éviter dans la vidéo |
| `seed` | INT | Oui | - | Valeur de graine aléatoire pour des résultats reproductibles |
| `resolution` | STRING | Oui | - | Paramètre de résolution de la vidéo de sortie |
| `duration` | INT | Oui | - | Durée de la vidéo générée en secondes |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`

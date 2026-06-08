Le nœud PikaFrames v2.2 génère une vidéo en combinant votre première et dernière image. Vous téléchargez deux images pour définir les points de début et de fin, et l'IA crée une transition fluide entre elles pour produire une vidéo complète.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image_start` | La première image à combiner. | IMAGE | Oui | - |
| `image_end` | La dernière image à combiner. | IMAGE | Oui | - |
| `prompt_text` | Texte décrivant le contenu vidéo souhaité. | STRING | Oui | - |
| `negative_prompt` | Texte décrivant ce qu'il faut éviter dans la vidéo. | STRING | Oui | - |
| `seed` | Valeur de graine aléatoire pour la cohérence de génération. | INT | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. | STRING | Oui | - |
| `duration` | Durée de la vidéo générée. | INT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée combinant les images de début et de fin avec des transitions IA. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/fr.md)

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`

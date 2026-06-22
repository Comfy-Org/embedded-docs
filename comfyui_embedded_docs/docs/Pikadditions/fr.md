# Pikadditions

Le nœud Pikadditions vous permet d'ajouter n'importe quel objet ou image dans votre vidéo. Vous téléchargez une vidéo et spécifiez ce que vous souhaitez ajouter pour obtenir un résultat intégré de manière transparente. Ce nœud utilise l'API Pika pour insérer des images dans des vidéos avec une intégration d'apparence naturelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video` | La vidéo dans laquelle ajouter une image. | VIDEO | Oui | - |
| `image` | L'image à ajouter à la vidéo. | IMAGE | Oui | - |
| `prompt_text` | Description textuelle de ce qu'il faut ajouter à la vidéo. | STRING | Oui | - |
| `negative_prompt` | Description textuelle de ce qu'il faut éviter dans la vidéo. | STRING | Oui | - |
| `seed` | Valeur de graine aléatoire pour des résultats reproductibles. | INT | Oui | 0 à 4294967295 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo traitée avec l'image insérée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/fr.md)

---
**Source fingerprint (SHA-256):** `cf7bb4ee0a672e20c0ffc128fa95df43e05356aea03b2070f928a0263aff6234`

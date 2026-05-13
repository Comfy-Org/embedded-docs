> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/fr.md)

Le nœud Pikadditions vous permet d'ajouter n'importe quel objet ou image dans votre vidéo. Vous téléchargez une vidéo et spécifiez ce que vous souhaitez ajouter pour obtenir un résultat intégré de manière transparente. Ce nœud utilise l'API Pika pour insérer des images dans des vidéos avec une intégration d'apparence naturelle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `video` | VIDEO | Oui | - | La vidéo dans laquelle ajouter une image. |
| `image` | IMAGE | Oui | - | L'image à ajouter à la vidéo. |
| `prompt_text` | STRING | Oui | - | Description textuelle de ce qu'il faut ajouter à la vidéo. |
| `negative_prompt` | STRING | Oui | - | Description textuelle de ce qu'il faut éviter dans la vidéo. |
| `seed` | INT | Oui | 0 à 4294967295 | Valeur de graine aléatoire pour des résultats reproductibles. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | La vidéo traitée avec l'image insérée. |

---
**Source fingerprint (SHA-256):** `cf7bb4ee0a672e20c0ffc128fa95df43e05356aea03b2070f928a0263aff6234`

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/fr.md)

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/en.md)

Ce nœud utilise l'API Grok pour éditer une vidéo existante en fonction d'une invite textuelle. Il télécharge votre vidéo, envoie une requête au modèle d'IA pour la modifier selon votre description, puis renvoie la nouvelle vidéo générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` | Le modèle d'IA à utiliser pour l'édition vidéo (par défaut : `"grok-imagine-video"`). |
| `invite` | STRING | Oui | N/A | Description textuelle de la vidéo souhaitée. |
| `vidéo` | VIDEO | Oui | N/A | La vidéo d'entrée à éditer. La durée maximale prise en charge est de 8,7 secondes et la taille du fichier est limitée à 50 Mo. |
| `graine` | INT | Non | 0 à 2147483647 | Une valeur de graine pour déterminer si le nœud doit être réexécuté. Les résultats réels sont non déterministes, quelle que soit la valeur de la graine (par défaut : 0). |

**Contraintes :**

* La `video` d'entrée doit avoir une durée comprise entre 1 et 8,7 secondes.
* La taille du fichier de la `video` d'entrée ne doit pas dépasser 50 Mo.
* Le `prompt` ne doit pas être vide.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `vidéo` | VIDEO | La vidéo éditée générée par le modèle d'IA. |

---
**Source fingerprint (SHA-256):** `dfe52a089f7bfe7abc7f40ef113c44aef2dded828221d9d1acf0ddb6a167c33f`

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/fr.md)

Le nœud Grok Reference-to-Video génère une vidéo à partir d'une description textuelle, en utilisant jusqu'à sept images de référence pour guider le style et le contenu du résultat. Il se connecte à une API externe pour créer la vidéo, qui est ensuite téléchargée et renvoyée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Description textuelle de la vidéo souhaitée. |
| `model` | COMBO | Oui | `"grok-imagine-video"` | Le modèle à utiliser pour la génération de vidéo. |
| `model.reference_images` | IMAGE | Oui | 1 à 7 images | Jusqu'à 7 images de référence pour guider la génération de la vidéo. |
| `model.resolution` | COMBO | Oui | `"480p"`<br>`"720p"` | La résolution de la vidéo en sortie. |
| `model.aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` | Le format (rapport d'aspect) de la vidéo en sortie. |
| `model.duration` | INT | Oui | 2 à 10 | La durée de la vidéo en sortie en secondes (par défaut : 6). |
| `seed` | INT | Non | 0 à 2147483647 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). |

**Note :** Le paramètre `model` est un groupe contenant `reference_images`, `resolution`, `aspect_ratio` et `duration`. Vous devez fournir au moins une image de référence, et vous pouvez en fournir jusqu'à sept.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | Le fichier vidéo généré. |
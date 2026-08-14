# MinimaxHailuo03RegenerateNode

Ce nœud re-rend une sortie vidéo MiniMax H3 768P en résolution 2K. Il téléverse la vidéo source et la prompt exacte utilisée pour la créer, lance une tâche de régénération MiniMax H3, puis renvoie la vidéo 2K re-rendue. Si la génération originale utilisait une première ou une dernière image, ou des médias de référence, joignez les mêmes entrées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle à utiliser pour la régénération vidéo. La sélection de ce modèle révèle les paramètres de prompt, de résolution et de médias de référence décrits ci-dessous. | COMBO | Oui | "MiniMax H3" |
| `prompt` | La prompt exacte utilisée pour générer la vidéo source. Ne doit pas être vide. | STRING | Oui | Texte |
| `resolution` | Résolution à laquelle re-rendre la vidéo source. | COMBO | Oui | "2K" |
| `reference_images` | Images de référence de la génération originale, dans le même ordre. Jusqu'à 9 images. | IMAGE | Non | 0-9 images |
| `reference_videos` | Vidéos de référence de la génération originale, dans le même ordre. Jusqu'à 3 vidéos, 2 à 15 secondes chacune, 15 secondes au total. | VIDEO | Non | 0-3 vidéos |
| `reference_audios` | Références audio de la génération originale, dans le même ordre. Jusqu'à 3 clips, 2 à 15 secondes chacun, 15 secondes au total. Ne peut pas être utilisé sans une image ou une vidéo de référence. | AUDIO | Non | 0-3 clips |
| `video` | La vidéo de sortie MiniMax H3 768P à re-rendre. Connectez la sortie non modifiée d'un nœud vidéo MiniMax H3 (24 FPS, 4 à 15 secondes). Les sorties 2K ne peuvent pas être utilisées. | VIDEO | Oui | 24 FPS, 4-15 secondes |
| `first_frame` | Première image de la génération originale, si une telle image a été utilisée. | IMAGE | Non | Image |
| `last_frame` | Dernière image de la génération originale, si une telle image a été utilisée. | IMAGE | Non | Image |
| `watermark` | Indique s'il faut ajouter un filigrane AIGC à la vidéo. Par défaut : false. | BOOLEAN | Oui | false / true |

### Contraintes

- La vidéo `video` source doit être une sortie MiniMax H3 768P non modifiée : largeur et hauteur divisibles par 32, au plus 1 032 192 pixels au total, 24 FPS, et 107 à 362 images par pas de 17 (4 à 15 secondes à 24 FPS). Les sorties 2K ne peuvent pas être utilisées comme source.
- `first_frame` / `last_frame` et les médias de référence (`reference_images`, `reference_videos`, `reference_audios`) sont mutuellement exclusifs. Utilisez des images pour une prompt image-vers-vidéo, ou des médias de référence pour une prompt référence-vers-vidéo.
- `reference_audios` nécessite au moins une entrée `reference_images` ou `reference_videos`.
- `reference_images` : chaque image doit avoir un rapport d'aspect entre 0,4 et 2,5 et faire au moins 256x256 pixels.
- `reference_videos` : chaque vidéo doit être de 23.976 à 60 FPS et d'une durée de 2 à 15 secondes ; la durée totale ne peut pas dépasser 15 secondes.
- `reference_audios` : chaque clip doit durer 2 à 15 secondes ; la durée totale ne peut pas dépasser 15 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo MiniMax H3 re-rendue en résolution 2K. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/fr.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`

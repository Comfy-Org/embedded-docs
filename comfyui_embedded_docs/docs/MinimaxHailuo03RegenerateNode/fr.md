# MinimaxHailuo03RegenerateNode

Ce nœud régénère une sortie vidéo MiniMax H3 768P en résolution 2K. Il téléverse la vidéo 768P non modifiée et le prompt exact ayant servi à la générer, lance une tâche de régénération MiniMax H3, puis renvoie la vidéo 2K régénérée. Si la génération d’origine utilisait des premières ou dernières images, ou des médias de référence, joignez les mêmes entrées.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle à utiliser pour la régénération vidéo. La sélection de « MiniMax H3 » révèle les paramètres de prompt, de résolution et de médias de référence. | DYNAMIC_COMBO | Oui | "MiniMax H3" |
| `video` | La vidéo de sortie MiniMax H3 768P à régénérer. Connectez la sortie non modifiée d’un nœud vidéo MiniMax H3 (24 FPS, 4-15 secondes). Les sorties 2K ne peuvent pas être utilisées. | VIDEO | Oui | 24 FPS, 4-15 secondes |
| `first_frame` | Image de la première frame de la génération d’origine, si elle a été utilisée. | IMAGE | Non | Image |
| `last_frame` | Image de la dernière frame de la génération d’origine, si elle a été utilisée. | IMAGE | Non | Image |
| `watermark` | Indique s’il faut ajouter un filigrane AIGC à la vidéo. La valeur par défaut est false. | BOOLEAN | Oui | false / true |

### Entrées MiniMax H3

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Le prompt exact utilisé pour générer la vidéo source. Ne doit pas être vide. | STRING | Oui | Texte (multiligne) |
| `resolution` | Résolution à laquelle régénérer la vidéo source. | COMBO | Oui | "2K" |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez `image_1` à `image_9` (jusqu’à 9 images). Images de référence de la génération d’origine, dans le même ordre. | IMAGE | Non | 0-9 images |
| `reference_videos` | Emplacement extensible : connectez `video_1` à `video_3` (jusqu’à 3 vidéos). Vidéos de référence de la génération d’origine, dans le même ordre. | VIDEO | Non | 0-3 vidéos |
| `reference_audios` | Emplacement extensible : connectez `audio_1` à `audio_3` (jusqu’à 3 clips). Références audio de la génération d’origine, dans le même ordre. Ne peut pas être utilisé sans une image ou une vidéo de référence. | AUDIO | Non | 0-3 clips |

### Contraintes

- Le `prompt` ne doit pas être vide.
- La `video` source doit être une sortie non modifiée MiniMax H3 768P : 24 FPS, largeur et hauteur divisibles par 32, au maximum 1 032 192 pixels au total, et 107 à 362 images par pas de 17 (4 à 15 secondes à 24 FPS). Les sorties 2K ne peuvent pas être utilisées comme source.
- `first_frame` et `last_frame` sont mutuellement exclusifs avec les médias de référence (`reference_images`, `reference_videos`, `reference_audios`). Utilisez les frames pour un prompt image-vers-vidéo, ou les médias de référence pour un prompt référence-vers-vidéo.
- `reference_audios` nécessite au moins une entrée `reference_images` ou `reference_videos`.
- `first_frame`, `last_frame` et chaque `reference_image` doivent avoir un ratio compris entre 0,4 et 2,5 et mesurer au moins 256x256 pixels.
- `reference_videos` : chaque vidéo doit être à 23.976 à 60 FPS et durer 2 à 15 secondes ; la durée totale ne peut pas dépasser 15 secondes.
- `reference_audios` : chaque clip doit durer 2 à 15 secondes ; la durée totale ne peut pas dépasser 15 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo MiniMax H3 régénérée en résolution 2K. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/fr.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`

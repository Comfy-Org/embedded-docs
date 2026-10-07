# Vidu Q4 Reference-to-Video Generation

Générez une vidéo à partir d'images de référence, d'une référence audio facultative et d'un prompt avec un modèle Vidu Q4. Il s'agit de la variante référence-vers-vidéo des nœuds de génération Vidu Q4.

La sélection d'un `model` révèle les paramètres spécifiques à ce modèle.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Modèle à utiliser pour la génération vidéo. La sélection d'un modèle révèle les paramètres qui lui sont spécifiques : `reference_images`, `reference_audios`, `prompt`, `aspect_ratio`, `resolution`, `duration`, `audio` et `seed`. | DYNAMIC_COMBO | Oui | `"Vidu Q4 Preview"` |
| `reference_images` | Emplacement extensible : connectez une ou plusieurs images de référence (`image_1`, `image_2`, ...) pour la vidéo générée ; chaque image d'un lot compte dans le total. Référencez-les dans le prompt par ordre : image 1, image 2, etc. | IMAGE | Oui | Jusqu'à 15 images |
| `reference_audios` | Emplacement extensible : connectez des références vocales facultatives (`audio_1`, `audio_2`, `audio_3`), de 3 à 12 secondes chacune. Seule la voix est utilisée, pas les mots : écrivez le dialogue dans le prompt et attribuez une voix par ordre, par exemple `image 1 says "Hello!" in the voice from audio 1`. Nécessite que `audio` soit activé. | AUDIO | Non | Jusqu'à 3 clips |
| `prompt` | Une description textuelle pour la génération vidéo, jusqu'à 5000 caractères. Nécessaire pour décrire les références que vous souhaitez utiliser. | STRING | Oui | Tout texte |
| `aspect_ratio` | Le rapport d'aspect de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"3:4"`<br>`"4:3"` |
| `resolution` | Résolution de la vidéo de sortie (par défaut : `"720p"`). | COMBO | Oui | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 3 à 16 |
| `audio` | Lorsqu'activé, produit une vidéo avec son, incluant les dialogues et les effets sonores (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Ce paramètre dispose de la fonctionnalité « contrôle après génération » (par défaut : 42). | INT | Oui | 1 à 2147483647 |

**Remarque :** Au maximum, 15 images de référence peuvent être utilisées au total, en comptant chaque image d'un lot. Chaque image doit mesurer au moins 128x128 pixels et avoir un rapport d'aspect compris entre 1:5 et 5:1. La référence audio nécessite que `audio` soit activé ; sinon, une erreur est générée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ReferenceVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `f37ceec93a6140d69332415b8fd748d55e6a608177430975b4b42ab33e593489`

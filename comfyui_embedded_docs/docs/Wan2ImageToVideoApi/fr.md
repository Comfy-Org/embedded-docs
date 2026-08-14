# Wan 2.7 Image vers Vidéo

Le nœud **Wan 2.7 Image to Video** génère une vidéo à partir d'une image de première image. Vous pouvez éventuellement fournir une image de dernière image pour créer une transition entre les deux, ou fournir un fichier audio pour guider le mouvement et le timing de la vidéo. Le nœud utilise un modèle d'IA pour animer la scène en fonction de votre description textuelle.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle d'IA à utiliser pour la génération vidéo. | COMBO | Oui | `"wan2.7-i2v"` |
| `first_frame` | Première image. Le format de sortie est dérivé de cette image. | IMAGE | Oui | - |
| `last_frame` | Image de la dernière image. Le modèle génère une vidéo qui fait la transition de la première à la dernière image. | IMAGE | Non | - |
| `audio` | Audio pour piloter la génération vidéo (ex. : synchronisation labiale, mouvement synchronisé sur le rythme). Durée : 2 s à 30 s. S'il n'est pas fourni, le modèle génère automatiquement une musique de fond ou des effets sonores correspondants. | AUDIO | Non | - |
| `seed` | Graine à utiliser pour la génération (défaut : 0). | INT | Oui | 0 à 2147483647 |
| `prompt_extend` | Active l'amélioration du prompt avec l'aide de l'IA (défaut : True). Il s'agit d'un paramètre avancé. | BOOLEAN | Oui | True<br>False |
| `watermark` | Ajoute un filigrane généré par IA au résultat (défaut : False). Il s'agit d'un paramètre avancé. | BOOLEAN | Oui | True<br>False |

### Entrées wan2.7-i2v

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.prompt` | Prompt décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois. | STRING | Oui | - |
| `model.negative_prompt` | Prompt négatif décrivant ce qu'il faut éviter. | STRING | Oui | - |
| `model.resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `model.duration` | La durée de la vidéo générée en secondes (défaut : 5). | INT | Oui | 2 à 15 |

**Remarque :** L'entrée `audio` est soumise à une contrainte de durée. S'il est fourni, le fichier audio doit avoir une durée comprise entre 2 et 30 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`

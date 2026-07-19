# Wan 2.7 Image vers Vidéo

Voici la traduction en français de la documentation du nœud Wan2ImageToVideoApi :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/en.md)

Le nœud Wan 2.7 Image to Video génère une vidéo à partir d'une image de première frame. Vous pouvez éventuellement fournir une image de dernière frame pour créer une transition entre les deux, ou fournir un fichier audio pour guider le mouvement et le timing de la vidéo. Le nœud utilise un modèle d'IA pour animer la scène en fonction de votre description textuelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'IA à utiliser pour la génération vidéo. | COMBO | Oui | `"wan2.7-i2v"` |
| `model.prompt` | Une description textuelle des éléments et caractéristiques visuelles souhaités dans la vidéo. Prend en charge l'anglais et le chinois. | STRING | Oui | - |
| `model.negative_prompt` | Une description textuelle des éléments ou caractéristiques que le modèle doit éviter. | STRING | Oui | - |
| `model.resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `model.duration` | La durée de la vidéo générée en secondes (par défaut : 5). | INT | Oui | 2 à 15 |
| `première image` | L'image à utiliser comme première frame de la vidéo. Le rapport hauteur/largeur de la vidéo de sortie est dérivé de cette image. | IMAGE | Oui | - |
| `dernière image` | Une image optionnelle à utiliser comme dernière frame. Lorsqu'elle est fournie, le modèle génère une vidéo qui effectue une transition de la première frame à cette dernière frame. | IMAGE | Non | - |
| `audio` | Un fichier audio optionnel pour piloter la génération vidéo, utile pour le synchronisme labial ou les mouvements synchronisés sur le rythme. La durée doit être comprise entre 2 et 30 secondes. Si non fourni, le modèle générera une musique de fond ou des effets sonores correspondants. | AUDIO | Non | - |
| `graine` | Une valeur de graine pour contrôler l'aléatoire de la génération (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `extension de prompt` | Lorsqu'activé, le nœud utilise une assistance IA pour améliorer votre invite textuelle (par défaut : True). Il s'agit d'un paramètre avancé. | BOOLEAN | Oui | - |
| `filigrane` | Lorsqu'activé, un filigrane généré par IA sera ajouté à la vidéo finale (par défaut : False). Il s'agit d'un paramètre avancé. | BOOLEAN | Oui | - |

**Remarque :** L'entrée `audio` a une contrainte de durée. Si fourni, le fichier audio doit avoir une durée comprise entre 2 et 30 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `ccd18dca3b191f2cbe64b6c2b941a7efcf281e4f327329d932cec27fd8234133`

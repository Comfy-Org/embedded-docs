> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/fr.md)

Le nœud Wan 2.7 Image to Video génère une vidéo à partir d'une image de première trame. Vous pouvez optionnellement fournir une image de dernière trame pour créer une transition entre les deux, ou fournir un fichier audio pour guider le mouvement et le rythme de la vidéo. Le nœud utilise un modèle d'IA pour animer la scène en fonction de votre description textuelle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"wan2.7-i2v"` | Le modèle d'IA à utiliser pour la génération de vidéo. |
| `model.prompt` | STRING | Oui | - | Une description textuelle des éléments et caractéristiques visuelles souhaités dans la vidéo. Prend en charge l'anglais et le chinois. |
| `model.negative_prompt` | STRING | Oui | - | Une description textuelle des éléments ou caractéristiques que vous souhaitez que le modèle évite. |
| `model.resolution` | COMBO | Oui | `"720P"`<br>`"1080P"` | La résolution de la vidéo en sortie. |
| `model.duration` | INT | Oui | 2 à 15 | La durée de la vidéo générée en secondes (par défaut : 5). |
| `first_frame` | IMAGE | Oui | - | L'image à utiliser comme première trame de la vidéo. Le format d'image de la vidéo en sortie est dérivé de cette image. |
| `last_frame` | IMAGE | Non | - | Une image optionnelle à utiliser comme dernière trame. Lorsqu'elle est fournie, le modèle génère une vidéo qui effectue une transition de la première trame vers cette dernière trame. |
| `audio` | AUDIO | Non | - | Un fichier audio optionnel pour piloter la génération de la vidéo, utile pour la synchronisation labiale ou les mouvements calés sur le rythme. La durée doit être comprise entre 2 et 30 secondes. S'il n'est pas fourni, le modèle générera une musique de fond ou des effets sonores correspondants. |
| `seed` | INT | Oui | 0 à 2147483647 | Une valeur de graine pour contrôler l'aléatoire de la génération (par défaut : 0). |
| `prompt_extend` | BOOLEAN | Oui | - | Lorsqu'activé, le nœud utilisera une assistance par IA pour améliorer votre prompt textuel (par défaut : True). Il s'agit d'un paramètre avancé. |
| `watermark` | BOOLEAN | Oui | - | Lorsqu'activé, un filigrane généré par IA sera ajouté à la vidéo finale (par défaut : False). Il s'agit d'un paramètre avancé. |

**Note :** L'entrée `audio` a une contrainte de durée. Si elle est fournie, le fichier audio doit avoir une durée comprise entre 2 et 30 secondes.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |
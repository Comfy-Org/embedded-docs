> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/fr.md)

Le nœud Wan2VideoEditApi utilise le modèle Wan 2.7 pour éditer une vidéo selon des instructions textuelles, des images de référence ou un transfert de style. Il traite la vidéo d'entrée et génère une nouvelle vidéo en fonction des paramètres spécifiés tels que la résolution, la durée et le rapport hauteur/largeur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | `"wan2.7-videoedit"` | Le modèle à utiliser pour l'édition vidéo. |
| `model.prompt` | STRING | Oui | - | Instructions d'édition ou exigences de transfert de style. (par défaut : chaîne vide) |
| `model.resolution` | COMBO | Oui | `"720P"`<br>`"1080P"` | La résolution de la vidéo de sortie. |
| `model.ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | Le rapport hauteur/largeur de la vidéo de sortie. S'il n'est pas modifié, il se rapproche du rapport de la vidéo d'entrée. |
| `model.duration` | COMBO | Oui | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | La durée de sortie en secondes. 'auto' correspond à la durée de la vidéo d'entrée. Une valeur spécifique tronque la vidéo à partir du début. (par défaut : "auto") |
| `model.reference_images` | IMAGE | Non | - | Une liste d'au maximum 4 images de référence pour guider l'édition. |
| `video` | VIDEO | Oui | - | La vidéo à éditer. |
| `seed` | INT | Non | 0 à 2147483647 | La graine à utiliser pour la génération. (par défaut : 0) |
| `audio_setting` | COMBO | Non | `"auto"`<br>`"origin"` | 'auto' : le modèle décide s'il doit régénérer l'audio en fonction de l'invite. 'origin' : préserve l'audio original de la vidéo d'entrée. (par défaut : "auto") |
| `watermark` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane généré par IA au résultat. (par défaut : False) |

**Contraintes :**
*   Le `model.prompt` doit comporter au moins 1 caractère.
*   La `video` d'entrée doit avoir une durée comprise entre 2 et 10 secondes.
*   L'entrée `model.reference_images` peut accepter un maximum de 4 images.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | La vidéo éditée générée par le modèle. |
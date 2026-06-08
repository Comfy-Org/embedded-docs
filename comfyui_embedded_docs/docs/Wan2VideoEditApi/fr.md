Le nœud Wan2VideoEditApi utilise le modèle Wan 2.7 pour éditer une vidéo en fonction d'instructions textuelles, d'images de référence ou d'un transfert de style. Il traite la vidéo d'entrée et génère une nouvelle vidéo selon les paramètres spécifiés, tels que la résolution, la durée et le rapport hauteur/largeur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à utiliser pour l'édition vidéo. | COMBO | Oui | `"wan2.7-videoedit"` |
| `model.prompt` | Instructions d'édition ou exigences de transfert de style. (par défaut : chaîne vide) | STRING | Oui | - |
| `model.resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `model.ratio` | Le rapport hauteur/largeur de la vidéo de sortie. S'il n'est pas modifié, il se rapproche du rapport de la vidéo d'entrée. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | La durée de sortie en secondes. 'auto' correspond à la durée de la vidéo d'entrée. Une valeur spécifique tronque la vidéo à partir du début. (par défaut : "auto") | COMBO | Oui | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `model.reference_images` | Une liste d'au plus 4 images de référence pour guider l'édition. | IMAGE | Non | - |
| `vidéo` | La vidéo à éditer. | VIDEO | Oui | - |
| `graine` | La graine à utiliser pour la génération. (par défaut : 0) | INT | Non | 0 à 2147483647 |
| `paramètre audio` | 'auto' : le modèle décide s'il doit régénérer l'audio en fonction de l'invite. 'origin' : préserve l'audio original de la vidéo d'entrée. (par défaut : "auto") | COMBO | Non | `"auto"`<br>`"origin"` |
| `filigrane` | Indique s'il faut ajouter un filigrane généré par IA au résultat. (par défaut : False) | BOOLEAN | Non | - |

**Contraintes :**
*   Le `model.prompt` doit comporter au moins 1 caractère.
*   La `video` d'entrée doit avoir une durée comprise entre 2 et 10 secondes.
*   L'entrée `model.reference_images` peut accepter un maximum de 4 images.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo éditée générée par le modèle. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `d2dd65d743358c6a357e75076774e93c52c39893fbb376da2f4395446f440a20`

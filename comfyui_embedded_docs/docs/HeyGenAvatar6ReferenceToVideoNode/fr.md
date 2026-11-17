# HeyGen Avatar 6 Reference to Video

Faites parler une personne ou un personnage avec l’audio que vous connectez, en utilisant une photo ou une vidéo comme référence. Avatar 6 reconstruit le visage et la scène à partir de cette référence, de sorte que le même audio peut animer une photo fixe, un clip existant, ou les deux.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélecteur de modèle ; la sélection d’un modèle révèle ses entrées ci-dessous. `"heygen-avatar-6-turbo"` est la variante moins chère et plus rapide. | DYNAMIC_COMBO | Oui | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |

### Entrées `heygen-avatar-6`

`"heygen-avatar-6-turbo"` expose les mêmes entrées avec les mêmes limites.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Photo facultative de la personne ou du personnage à animer. Elle définit l’apparence et la scène et n’est pas utilisée comme première image. | IMAGE | Non | Image unique |
| `video` | Vidéo facultative d’un personnage animé ou stylisé montrant comment il parle et bouge. Les vidéos plus longues sont coupées aux 30 premières secondes. | VIDEO | Non | 2 à 30 secondes |
| `audio` | Parole pour l’avatar. La durée de la vidéo suit celle de l’audio. | AUDIO | Oui | 1.5 secondes à 10 minutes |
| `resolution` | Résolution de la vidéo de sortie. Par défaut : `"1080p"`. | COMBO | Oui | `"1080p"`<br>`"2k"` |
| `aspect_ratio` | Rapport d’aspect de la vidéo de sortie. `"auto"` conserve la forme de l’image, ou celle de la vidéo lorsqu’aucune image n’est connectée ; les autres valeurs recadrent la scène. Par défaut : `"auto"`. | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `motion_prompt` | Direction facultative pour les gestes, l’expression, la posture et les mouvements de caméra. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne, jusqu’à 1200 caractères |
| `motion_expressiveness` | `"less"` donne des gestes moins nombreux et plus petits. Le prompt de mouvement est prioritaire là où les deux se chevauchent. Par défaut : `"default"`. | COMBO | Oui | `"less"`<br>`"default"` |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats ne sont pas déterministes, quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes et comportement :**

* Connectez une image, une vidéo, ou les deux ; sans aucun des deux, le nœud génère une erreur.
* L’entrée d’image doit contenir exactement une image, pas un lot.
* Les vidéos de référence montrant des personnes réalistes sont refusées. Utilisez une vidéo de personnage animé ou stylisé, ou connectez plutôt une photo de la personne.
* Une vidéo de référence doit durer au moins 2 secondes et ne pas dépasser 50 Mo.
* La tarification est calculée à la seconde de vidéo de sortie et dépend du modèle et de la résolution.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo parlante générée, téléchargée depuis HeyGen une fois le rendu terminé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6ReferenceToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `1a50342827511e355a1d857c34e8bbfc0b74ca7b003dca783b76fcd151413ff8`

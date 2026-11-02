# MiniMax H3 Max Lip Sync

Ce nœud anime une image fixe afin que les mouvements de la bouche suivent une piste audio fournie. L’image et l’audio sont téléversés, la tâche de synchronisation labiale Hailuo 03 Max est interrogée régulièrement, et la vidéo parlante est renvoyée à la résolution choisie. La vidéo de sortie a la même durée que l’audio.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | "MiniMax H3 Max" |

### Entrées MiniMax H3 Max

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `image` | Image à animer, d’au moins 256x256 pixels. Le rapport d’aspect doit être compris entre 0,4 et 2,5. | IMAGE | Oui | Image unique |
| `audio` | Audio sur lequel synchroniser les lèvres, d’une durée de 5 à 899 secondes. | AUDIO | Oui | 5 à 899 secondes |
| `resolution` | Résolution de sortie (par défaut : "768P"). Le rapport d’aspect est celui pris en charge le plus proche de l’image. | COMBO | Oui | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `transcription` | Transcrire l’audio pour guider la synchronisation labiale (par défaut : false). | BOOLEAN | Non | true<br>false |
| `seed` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais pas nécessairement identiques (par défaut : 42). | INT | Oui | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo parlante, de même durée que l’audio d’entrée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxLipSyncNode/fr.md)

---
**Source fingerprint (SHA-256):** `0af4166f9f3237cacc3506d6c6544c0374a330cf998f8bd2ef1f4f7162e2f9ab`

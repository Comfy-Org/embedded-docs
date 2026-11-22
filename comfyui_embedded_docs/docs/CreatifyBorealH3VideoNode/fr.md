# Creatify Boreal-H3 Video

Creatify Boreal-H3 Video transforme une invite textuelle en une vidéo avec son, à l'aide du modèle H3 post-entraîné de Creatify conçu pour les publicités vidéo. Connectez une première image pour animer une image fixe et, en option, une dernière image pour terminer le plan sur une image choisie.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Invite textuelle qui décrit la vidéo. Doit contenir au moins un caractère autre qu'un espace blanc. | STRING | Oui | Tout texte non vide |
| `première image` | Image à partir de laquelle la vidéo commence. Lorsqu'elle est connectée, conservez `aspect_ratio` sur `"auto"` afin que la vidéo suive l'image. | IMAGE | Non | - |
| `dernière image` | Image sur laquelle la vidéo se termine. Nécessite un `first_frame` connecté. | IMAGE | Non | - |
| `résolution` | Résolution de la vidéo de sortie (par défaut : `"768p"`). | COMBO | Oui | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Rapport d'aspect de la vidéo de sortie. `"auto"` suit la première image lorsqu'une image est connectée ; dans ce cas, laissez-le sur `"auto"` (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `durée` | Durée de la vidéo en secondes (par défaut : 5). À `"2k"`, le maximum est de 14 secondes. | INT | Oui | 1 à 15 (pas : 1) |
| `amélioration du prompt` | Manière dont Creatify réécrit l'invite avant le rendu : `"auto"` et `"ads"` la transforment en invite de publicité vidéo et peuvent ajouter des répliques parlées, `"general"` la réécrit pour toute autre vidéo, `"none"` la rend telle qu'écrite (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `graine` | La graine détermine si le nœud se réexécute. Aucune graine n'est transmise à Boreal-H3, donc une réexécution avec les mêmes entrées peut produire une vidéo différente (par défaut : 42). | INT | Oui | 0 à 2147483647 |

**Contraintes :** avec un `first_frame`, le rapport d'aspect provient toujours de l'image, donc toute autre valeur de `aspect_ratio` lève une erreur. Un `last_frame` sans `first_frame` est refusé, et une `duration` supérieure à 14 secondes est refusée avec `"2k"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec son. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3VideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `535bcbeced69cffd4d0edca04f30dd00dac4ec728cd8eb638b4f9d9af8448336`

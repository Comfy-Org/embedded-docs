# Creatify Boreal-H3 Video

Creatify Boreal-H3 Video transforme un prompt texte en vidéo avec son, à l’aide du modèle H3 post-entraîné de Creatify, conçu pour les publicités vidéo. Connectez une première image pour animer une image fixe, et éventuellement une dernière image pour terminer le plan sur une image choisie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt texte qui décrit la vidéo. Doit contenir au moins un caractère non blanc. | STRING | Oui | Tout texte non vide |
| `first_frame` | Image à partir de laquelle la vidéo commence. Lorsqu’elle est connectée, laissez `aspect_ratio` sur `"auto"` afin que la vidéo suive l’image. | IMAGE | Non | - |
| `last_frame` | Image sur laquelle la vidéo se termine. Nécessite un `first_frame` connecté. | IMAGE | Non | - |
| `resolution` | Résolution de la vidéo de sortie (par défaut : `"768p"`). | COMBO | Oui | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Format d’image de la vidéo de sortie. `"auto"` suit la première image lorsqu’une image est connectée ; dans ce cas, laissez-le sur `"auto"` (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durée de la vidéo en secondes (par défaut : 5). En `"2k"`, le maximum est de 14 secondes. | INT | Oui | 1 à 15 (pas : 1) |
| `prompt_enhancement` | Manière dont Creatify réécrit le prompt avant le rendu : `"auto"` et `"ads"` le transforment en prompt de publicité vidéo et peuvent ajouter des répliques parlées, `"general"` le réécrit pour toute autre vidéo, `"none"` le rend tel qu’écrit (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | La graine contrôle si le nœud se réexécute. Creatify choisit son propre aléatoire, donc les mêmes entrées donnent la même vidéo uniquement lorsque `prompt_enhancement` est défini sur `"none"` (par défaut : 42). | INT | Oui | 0 à 2147483647 |

**Contraintes :** avec un `first_frame`, le format d’image provient toujours de l’image ; toute autre valeur de `aspect_ratio` déclenche une erreur. Un `last_frame` sans `first_frame` est rejeté, et une `duration` supérieure à 14 secondes est rejetée avec `"2k"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec son. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3VideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `535bcbeced69cffd4d0edca04f30dd00dac4ec728cd8eb638b4f9d9af8448336`

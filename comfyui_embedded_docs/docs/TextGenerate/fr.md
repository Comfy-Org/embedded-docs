Le nœud TextGenerate utilise un modèle CLIP pour créer du texte à partir d’une invite utilisateur. Il peut éventuellement utiliser des images, des vidéos ou de l’audio comme contexte supplémentaire pour guider la génération de texte. Vous pouvez contrôler la longueur de la sortie, activer un mode de réflexion pour les modèles compatibles, et choisir d’utiliser un échantillonnage aléatoire avec divers paramètres ou de générer du texte sans échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour tokeniser l’invite et générer le texte. | CLIP | Oui | N/A |
| `invite` | L’invite textuelle qui guide la génération. Ce champ prend en charge plusieurs lignes et les invites dynamiques. La valeur par défaut est une chaîne vide. | STRING | Oui | N/A |
| `image` | Une image facultative pouvant être utilisée avec l’invite textuelle pour influencer le texte généré. | IMAGE | Non | N/A |
| `vidéo` | Images vidéo sous forme de lot d’images. Supposées être à 24 FPS ; sous-échantillonnées à 1 FPS en interne. | IMAGE | Non | N/A |
| `audio` | Une entrée audio facultative pouvant être utilisée avec l’invite textuelle pour influencer le texte généré. | AUDIO | Non | N/A |
| `longueur_max` | Le nombre maximum de jetons que le modèle générera. La valeur par défaut est 256. | INT | Oui | 1 à 2048 |
| `mode_d'échantillonnage` | Contrôle si un échantillonnage aléatoire est utilisé lors de la génération de texte. Lorsqu’il est réglé sur "on", des paramètres supplémentaires pour contrôler l’échantillonnage deviennent disponibles. La valeur par défaut est "on". | COMBO | Oui | `"on"`<br>`"off"` |
| `réflexion` | Fonctionner en mode réflexion si le modèle le prend en charge. La valeur par défaut est Faux. | BOOLEAN | Non | Vrai ou Faux |
| `utiliser le modèle par défaut` | Utiliser l’invite/modèle système intégré si le modèle en possède un. La valeur par défaut est Vrai. Il s’agit d’un paramètre avancé. | BOOLEAN | Non | Vrai ou Faux |
| `temperature` | Contrôle le caractère aléatoire de la sortie. Des valeurs plus basses rendent la sortie plus prévisible, des valeurs plus élevées la rendent plus créative. Ce paramètre n’est disponible que lorsque `mode_d'échantillonnage` est réglé sur "on". La valeur par défaut est 0,7. | FLOAT | Non | 0,01 à 2,0 |
| `top_k` | Limite le pool d’échantillonnage aux K jetons suivants les plus probables. Une valeur de 0 désactive ce filtre. Ce paramètre n’est disponible que lorsque `mode_d'échantillonnage` est réglé sur "on". La valeur par défaut est 64. | INT | Non | 0 à 1000 |
| `top_p` | Utilise l’échantillonnage par noyau, limitant les choix aux jetons dont la probabilité cumulée est inférieure à cette valeur. Ce paramètre n’est disponible que lorsque `mode_d'échantillonnage` est réglé sur "on". La valeur par défaut est 0,95. | FLOAT | Non | 0,0 à 1,0 |
| `min_p` | Définit un seuil de probabilité minimal pour qu’un jeton soit pris en compte. Ce paramètre n’est disponible que lorsque `mode_d'échantillonnage` est réglé sur "on". La valeur par défaut est 0,05. | FLOAT | Non | 0,0 à 1,0 |
| `repetition_penalty` | Pénalise les jetons déjà générés pour réduire la répétition. Une valeur de 1,0 n’applique aucune pénalité. Ce paramètre n’est disponible que lorsque `mode_d'échantillonnage` est réglé sur "on". La valeur par défaut est 1,05. | FLOAT | Non | 0,0 à 5,0 |
| `presence_penalty` | Pénalise les nouveaux jetons en fonction de leur apparition dans le texte jusqu’à présent, encourageant le modèle à aborder de nouveaux sujets. Ce paramètre n’est disponible que lorsque `mode_d'échantillonnage` est réglé sur "on". La valeur par défaut est 0,0. | FLOAT | Non | 0,0 à 5,0 |
| `seed` | Un nombre utilisé pour initialiser le générateur de nombres aléatoires afin d’obtenir des résultats reproductibles lorsque l’échantillonnage est réglé sur "on". La valeur par défaut est 0. | INT | Non | 0 à 18446744073709551615 |

**Remarque :** Les paramètres `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty`, `presence_penalty` et `seed` ne sont actifs et visibles dans l’interface du nœud que lorsque `sampling_mode` est réglé sur "on".

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `generated_text` | Le texte généré par le modèle en fonction de l’invite d’entrée et des images, vidéos ou audios facultatifs. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/fr.md)

---
**Source fingerprint (SHA-256):** `dc6868bd7ebb63c485a4346113834f845416d7359759b2d428525398bdedf343`

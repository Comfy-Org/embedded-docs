# TextGenerate

Le nœud TextGenerate utilise un modèle CLIP pour créer du texte à partir de la saisie de l’utilisateur. Il peut éventuellement utiliser des images, des vidéos ou de l’audio comme contexte supplémentaire pour guider la génération de texte. Vous pouvez contrôler la longueur de la sortie, activer un mode de réflexion pour les modèles compatibles, et choisir d’utiliser un échantillonnage aléatoire avec divers réglages ou de générer du texte sans échantillonnage.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `mode_d'échantillonnage` | Contrôle si un échantillonnage aléatoire est utilisé lors de la génération de texte. Lorsqu’il est défini sur `"on"`, des paramètres d’échantillonnage supplémentaires deviennent disponibles. Lorsqu’il est défini sur `"off"`, le nœud génère du texte sans échantillonnage aléatoire. | DYNAMIC_COMBO | Oui | `"on"`<br>`"off"` |
| `clip` | Le modèle CLIP utilisé pour tokeniser la saisie et générer le texte. | CLIP | Oui | N/A |
| `invite` | La saisie textuelle qui guide la génération. Ce champ prend en charge plusieurs lignes et les saisies dynamiques. La valeur par défaut est une chaîne vide. | STRING | Oui | N/A |
| `image` | Une image optionnelle qui peut être utilisée avec la saisie textuelle pour influencer le texte généré. | IMAGE | Non | N/A |
| `vidéo` | Frames vidéo sous forme de lot d’images. La fréquence supposée est de 24 FPS ; sous-échantillonnage interne à 1 FPS. | IMAGE | Non | N/A |
| `audio` | Une entrée audio optionnelle qui peut être utilisée avec la saisie textuelle pour influencer le texte généré. | AUDIO | Non | N/A |
| `longueur_max` | Le nombre maximal de jetons que le modèle générera. La valeur par défaut est 512. | INT | Oui | 1 à 32768 |
| `réflexion` | Fonctionne en mode réflexion si le modèle le prend en charge. La valeur par défaut est False. | BOOLEAN | Non | True ou False |
| `utiliser le modèle par défaut` | Utilise le modèle de système / la template intégré(e) si le modèle en possède un. La valeur par défaut est True. Il s’agit d’un paramètre avancé. | BOOLEAN | Non | True ou False |

### Paramètres d’échantillonnage (lorsque `sampling_mode` est sur `"on"`)

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `temperature` | Contrôle le caractère aléatoire de la sortie. Des valeurs plus basses rendent la sortie plus prévisible, des valeurs plus hautes la rendent plus créative. La valeur par défaut est 0.7. | FLOAT | Oui | 0.01 à 2.0 |
| `top_k` | Limite le pool d’échantillonnage aux K prochains jetons les plus probables. Une valeur de 0 désactive ce filtre. La valeur par défaut est 64. | INT | Oui | 0 à 1000 |
| `top_p` | Utilise l’échantillonnage par noyau (nucleus sampling), limitant les choix aux jetons dont la probabilité cumulée est inférieure à cette valeur. La valeur par défaut est 0.95. | FLOAT | Oui | 0.0 à 1.0 |
| `min_p` | Définit un seuil de probabilité minimal pour qu’un jeton soit pris en compte. La valeur par défaut est 0.05. | FLOAT | Oui | 0.0 à 1.0 |
| `repetition_penalty` | Pénalise les jetons déjà générés afin de réduire les répétitions. Une valeur de 1.0 n’applique aucune pénalité. La valeur par défaut est 1.05. | FLOAT | Oui | 0.0 à 5.0 |
| `seed` | Nombre utilisé pour initialiser le générateur de nombres aléatoires afin d’obtenir des résultats reproductibles. La valeur par défaut est 0. | INT | Oui | 0 à 18446744073709551615 |
| `presence_penalty` | Pénalise les nouveaux jetons selon qu’ils sont déjà apparus dans le texte, encourageant ainsi le modèle à aborder de nouveaux sujets. La valeur par défaut est 0.0. | FLOAT | Non | 0.0 à 5.0 |

**Remarque :** Les paramètres d’échantillonnage ci-dessus ne sont actifs et visibles dans l’interface du nœud que lorsque `sampling_mode` est défini sur `"on"`. Lorsque `sampling_mode` est défini sur `"off"`, aucun paramètre d’échantillonnage n’est disponible et le nœud génère du texte sans échantillonnage aléatoire.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `texte_généré` | Le texte généré par le modèle à partir de la saisie textuelle et de l’image, de la vidéo ou de l’audio facultatifs. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/fr.md)

---
**Source fingerprint (SHA-256):** `6274a2db7c9a963304daf6df494b2b20879155e918d73429fd2ce7f3b5b9da02`

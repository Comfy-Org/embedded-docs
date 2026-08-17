# TextGenerate

Le nœud TextGenerate utilise un modèle CLIP pour créer du texte en fonction du prompt de l'utilisateur. Il peut éventuellement utiliser des images, des vidéos ou de l'audio comme contexte supplémentaire pour guider la génération du texte. Vous pouvez contrôler la longueur de la sortie, activer un mode de réflexion pour les modèles compatibles, et choisir d'utiliser un échantillonnage aléatoire avec divers paramètres ou de générer du texte sans échantillonnage.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour tokeniser le prompt et générer du texte. | CLIP | Oui | N/A |
| `prompt` | Le prompt texte qui guide la génération. Ce champ prend en charge plusieurs lignes et les prompts dynamiques. La valeur par défaut est une chaîne vide. | STRING | Oui | N/A |
| `image` | Une image optionnelle qui peut être utilisée avec le prompt texte pour influencer le texte généré. | IMAGE | Non | N/A |
| `video` | Images vidéo sous forme de lot d'images. Supposées être à 24 FPS ; sous-échantillonnées à 1 FPS en interne. | IMAGE | Non | N/A |
| `audio` | Une entrée audio optionnelle qui peut être utilisée avec le prompt texte pour influencer le texte généré. | AUDIO | Non | N/A |
| `max_length` | Le nombre maximum de jetons que le modèle générera. La valeur par défaut est 512. | INT | Oui | 1 to 32768 |
| `sampling_mode` | Contrôle si un échantillonnage aléatoire est utilisé pendant la génération de texte. Lorsqu'il est défini sur "on", des paramètres supplémentaires pour contrôler l'échantillonnage deviennent disponibles. La valeur par défaut est "on". | DYNAMIC_COMBO | Oui | "on"<br>"off" |
| `thinking` | Fonctionner en mode réflexion si le modèle le prend en charge. La valeur par défaut est False. | BOOLEAN | Non | True or False |
| `use_default_template` | Utiliser le prompt/modèle système intégré si le modèle en possède un. La valeur par défaut est True. Il s'agit d'un paramètre avancé. | BOOLEAN | Non | True or False |

### Entrées "on"

Les paramètres d'échantillonnage suivants sont disponibles lorsque `sampling_mode` est défini sur "on" :

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `temperature` | Contrôle le caractère aléatoire de la sortie. Des valeurs plus faibles rendent la sortie plus prévisible, des valeurs plus élevées la rendent plus créative. La valeur par défaut est 0.7. | FLOAT | Non | 0.01 to 2.0 |
| `top_k` | Limite le pool d'échantillonnage aux K prochains jetons les plus probables. Une valeur de 0 désactive ce filtre. La valeur par défaut est 64. | INT | Non | 0 to 1000 |
| `top_p` | Utilise l'échantillonnage par noyau (nucleus sampling), limitant les choix aux jetons dont la probabilité cumulée est inférieure à cette valeur. La valeur par défaut est 0.95. | FLOAT | Non | 0.0 to 1.0 |
| `min_p` | Définit un seuil de probabilité minimal pour que les jetons soient pris en compte. La valeur par défaut est 0.05. | FLOAT | Non | 0.0 to 1.0 |
| `repetition_penalty` | Pénalise les jetons déjà générés afin de réduire la répétition. Une valeur de 1.0 n'applique aucune pénalité. La valeur par défaut est 1.05. | FLOAT | Non | 0.0 to 5.0 |
| `presence_penalty` | Pénalise les nouveaux jetons selon qu'ils sont déjà apparus dans le texte jusqu'à présent, encourageant le modèle à aborder de nouveaux sujets. La valeur par défaut est 0.0. | FLOAT | Non | 0.0 to 5.0 |
| `seed` | Un nombre utilisé pour initialiser le générateur de nombres aléatoires afin d'obtenir des résultats reproductibles lorsque l'échantillonnage est "on". La valeur par défaut est 0. | INT | Non | 0 to 18446744073709551615 |

### Entrées "off"

Lorsque `sampling_mode` est défini sur "off", aucun paramètre d'échantillonnage supplémentaire n'est disponible et le nœud génère du texte sans échantillonnage aléatoire.

**Remarque :** Les paramètres `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty`, `presence_penalty` et `seed` ne sont actifs et visibles dans l'interface du nœud que lorsque `sampling_mode` est défini sur "on".

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `generated_text` | Le texte généré par le modèle à partir du prompt d'entrée et de l'image, de la vidéo ou de l'audio facultatifs. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/fr.md)

---
**Source fingerprint (SHA-256):** `6274a2db7c9a963304daf6df494b2b20879155e918d73429fd2ce7f3b5b9da02`

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/fr.md)

Le nœud TextGenerate utilise un modèle CLIP pour créer du texte à partir d'une instruction utilisateur. Il peut éventuellement utiliser une image comme référence visuelle pour guider la génération de texte. Vous pouvez contrôler la longueur de la sortie et choisir d'utiliser ou non un échantillonnage aléatoire avec divers paramètres.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Oui | N/A | Le modèle CLIP utilisé pour tokeniser l'instruction et générer le texte. |
| `prompt` | STRING | Oui | N/A | L'instruction textuelle qui guide la génération. Ce champ prend en charge plusieurs lignes et les prompts dynamiques. La valeur par défaut est une chaîne vide. |
| `image` | IMAGE | Non | N/A | Une image optionnelle qui peut être utilisée conjointement avec l'instruction textuelle pour influencer le texte généré. |
| `max_length` | INT | Oui | 1 à 2048 | Le nombre maximum de tokens que le modèle générera. La valeur par défaut est 256. |
| `sampling_mode` | COMBO | Oui | `"on"`<br>`"off"` | Contrôle si un échantillonnage aléatoire est utilisé pendant la génération de texte. Lorsqu'il est défini sur "on", des paramètres supplémentaires pour contrôler l'échantillonnage deviennent disponibles. La valeur par défaut est "on". |
| `temperature` | FLOAT | Non | 0.01 à 2.0 | Contrôle le caractère aléatoire de la sortie. Des valeurs plus basses rendent la sortie plus prévisible, des valeurs plus élevées la rendent plus créative. Ce paramètre n'est disponible que lorsque `sampling_mode` est sur "on". La valeur par défaut est 0.7. |
| `top_k` | INT | Non | 0 à 1000 | Limite le pool d'échantillonnage aux K tokens suivants les plus probables. Une valeur de 0 désactive ce filtre. Ce paramètre n'est disponible que lorsque `sampling_mode` est sur "on". La valeur par défaut est 64. |
| `top_p` | FLOAT | Non | 0.0 à 1.0 | Utilise l'échantillonnage par noyau (nucleus sampling), limitant les choix aux tokens dont la probabilité cumulative est inférieure à cette valeur. Ce paramètre n'est disponible que lorsque `sampling_mode` est sur "on". La valeur par défaut est 0.95. |
| `min_p` | FLOAT | Non | 0.0 à 1.0 | Définit un seuil de probabilité minimum pour qu'un token soit pris en compte. Ce paramètre n'est disponible que lorsque `sampling_mode` est sur "on". La valeur par défaut est 0.05. |
| `repetition_penalty` | FLOAT | Non | 0.0 à 5.0 | Pénalise les tokens qui ont déjà été générés pour réduire les répétitions. Une valeur de 1.0 n'applique aucune pénalité. Ce paramètre n'est disponible que lorsque `sampling_mode` est sur "on". La valeur par défaut est 1.05. |
| `seed` | INT | Non | 0 à 18446744073709551615 | Un nombre utilisé pour initialiser le générateur de nombres aléatoires afin d'obtenir des résultats reproductibles lorsque l'échantillonnage est sur "on". La valeur par défaut est 0. |

**Note :** Les paramètres `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty` et `seed` ne sont actifs et visibles dans l'interface du nœud que lorsque le `sampling_mode` est défini sur "on".

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `generated_text` | STRING | Le texte généré par le modèle en fonction de l'instruction d'entrée et de l'image optionnelle. |

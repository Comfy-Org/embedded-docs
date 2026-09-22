# TextGenerate

Le nœud TextGenerate utilise un modèle CLIP pour créer du texte à partir du prompt d'un utilisateur. Il peut éventuellement utiliser des images, des vidéos ou de l'audio comme contexte supplémentaire pour guider la génération de texte. Vous pouvez contrôler la longueur de la sortie, activer un mode de réflexion pour les modèles pris en charge, et choisir d'utiliser un échantillonnage aléatoire avec divers réglages ou de générer du texte sans échantillonnage.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `mode_d'échantillonnage` | Contrôle si un échantillonnage aléatoire est utilisé pendant la génération de texte. Lorsqu'il est défini sur "on", des paramètres d'échantillonnage supplémentaires deviennent disponibles. Lorsqu'il est défini sur "off", le nœud génère du texte sans échantillonnage aléatoire. | DYNAMIC_COMBO | Oui | `"on"`<br>`"off"` |
| `clip` | Le modèle CLIP utilisé pour tokeniser le prompt et générer du texte. | CLIP | Oui | N/A |
| `invite` | Le prompt textuel qui guide la génération. Ce champ prend en charge plusieurs lignes et les prompts dynamiques. La valeur par défaut est une chaîne vide. | STRING | Oui | N/A |
| `image` | Une image facultative pouvant être utilisée avec le prompt textuel pour influencer le texte généré. | IMAGE | Non | N/A |
| `vidéo` | Trames vidéo sous forme de lot d'images. Supposées être à 24 FPS ; sous-échantillonnées à 1 FPS en interne. | IMAGE | Non | N/A |
| `audio` | Une entrée audio facultative pouvant être utilisée avec le prompt textuel pour influencer le texte généré. | AUDIO | Non | N/A |
| `longueur_max` | Nombre maximal de tokens que le modèle générera. La valeur par défaut est 512. | INT | Oui | 1 à 32768 |
| `réflexion` | Active le mode réflexion si le modèle le prend en charge. La valeur par défaut est False. | BOOLEAN | Non | True ou False |
| `utiliser le modèle par défaut` | Utilise le prompt système/gabarit intégré si le modèle en possède un. La valeur par défaut est True. Il s'agit d'un paramètre avancé. | BOOLEAN | Non | True ou False |
| `mtp` | Décodage spéculatif avec la tête de prédiction multi-token du checkpoint. N'a aucun effet sans poids MTP. `"auto"` adapte la profondeur de brouillon, `"2"` à `"5"` la fixent. La sortie échantillonnée reste correctement distribuée mais diffère de la sortie non-MTP pour la même graine (par défaut : `"auto"`). | COMBO | Non | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"` |
| `system_prompt` | Remplace l'invite système dans le gabarit de chat du modèle. Ignoré lorsque le gabarit par défaut n'est pas utilisé. Connectez une entrée STRING au lieu de la saisir dans le nœud (par défaut : vide). | STRING | Non | N/A |

### Paramètres d'échantillonnage (lorsque `sampling_mode` est défini sur "on")

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `temperature` | Contrôle le caractère aléatoire de la sortie. Des valeurs plus faibles rendent la sortie plus prévisible, des valeurs plus élevées la rendent plus créative. La valeur par défaut est 0.7. | FLOAT | Oui | 0.01 à 2.0 |
| `top_k` | Limite le pool d'échantillonnage aux K tokens suivants les plus probables. Une valeur de 0 désactive ce filtre. La valeur par défaut est 64. | INT | Oui | 0 à 1000 |
| `top_p` | Utilise l'échantillonnage par noyau (nucleus sampling) : conserve le plus petit ensemble de jetons les plus probables dont la probabilité cumulée atteint cette valeur. La valeur par défaut est 0.95. | FLOAT | Oui | 0.0 à 1.0 |
| `min_p` | Définit un seuil de probabilité minimal pour que les tokens soient pris en compte. La valeur par défaut est 0.05. | FLOAT | Oui | 0.0 à 1.0 |
| `repetition_penalty` | Pénalise les tokens déjà générés afin de réduire les répétitions. Une valeur de 1.0 n'applique aucune pénalité. La valeur par défaut est 1.05. | FLOAT | Oui | 0.0 à 5.0 |
| `seed` | Un nombre utilisé pour initialiser le générateur de nombres aléatoires afin d'obtenir des résultats reproductibles. La valeur par défaut est 0. | INT | Oui | 0 à 18446744073709551615 |
| `presence_penalty` | Pénalise les nouveaux tokens selon qu'ils sont déjà apparus dans le texte jusqu'à présent, ce qui encourage le modèle à parler de nouveaux sujets. La valeur par défaut est 0.0. | FLOAT | Non | 0.0 à 5.0 |

**Note :** Les paramètres d'échantillonnage ci-dessus ne sont actifs et visibles dans l'interface du nœud que lorsque `sampling_mode` est défini sur "on". Lorsque `sampling_mode` est défini sur "off", aucun paramètre d'échantillonnage n'est disponible et le nœud génère du texte sans échantillonnage aléatoire.

**Remarque :** Lorsque le texte généré contient un bloc de raisonnement (il commence par `<think>` ou l'invite se termine par celui-ci), le raisonnement est renvoyé séparément : `generated_text` contient la réponse et `thinking` contient le raisonnement sans la balise d'ouverture. Sinon, `generated_text` contient tout ce que le modèle a produit et `thinking` reste vide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `generated_text` | Le texte généré par le modèle en fonction de l'invite d'entrée et éventuellement de l'image, de la vidéo ou de l'audio, tout bloc de raisonnement étant séparé dans la sortie `thinking`. | STRING |
| `thinking` | Le bloc de raisonnement produit par le modèle, sans la balise d'ouverture `<think>`. Vide si le modèle n'a produit aucun bloc de raisonnement. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/fr.md)

---
**Source fingerprint (SHA-256):** `80813781c06dfb0c3b59ee72c8bd6ebced69a4de8152de916ebc15153a0757fa`

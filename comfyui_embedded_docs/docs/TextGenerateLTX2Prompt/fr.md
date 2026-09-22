# TextGenerateLTX2Prompt

Le nœud TextGenerateLTX2Prompt développe une courte invite utilisateur en une description audio-visuelle détaillée adaptée à la génération de vidéo avec la série de modèles vidéo LTX-2. Il ajoute automatiquement des instructions système spécifiques à la tâche, envoie l’invite formatée à un modèle de langage et renvoie le texte enrichi. Lorsqu’une image de référence facultative est fournie, le nœud bascule en mode image-vers-vidéo et développe l’invite à partir du contenu de cette image.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour l’encodage de texte. Le nœud vérifie le nom du tokenizer du modèle pour sélectionner les instructions correspondantes : les modèles basés sur Gemma 4 utilisent le format LTX-2.4, tandis que les autres modèles utilisent le format LTX-2 (Gemma 3). | CLIP | Oui | - |
| `invite` | Le texte brut d’entrée décrivant la scène ou le concept à développer en une invite de génération vidéo détaillée. | STRING | Oui | - |
| `image` | Une image d’entrée facultative utilisée comme première image de la vidéo. Lorsqu’elle est fournie, le nœud bascule en mode image-vers-vidéo et utilise une invite système qui développe l’invite utilisateur en fonction du contenu de l’image. | IMAGE | Non | - |
| `vidéo` | Une entrée vidéo facultative utilisée comme contexte supplémentaire. Transmise au modèle de langage sous forme de lot d’images ; supposée être à 24 FPS et sous-échantillonnée à 1 FPS en interne. | IMAGE | Non | - |
| `audio` | Une entrée audio facultative pouvant être utilisée comme contexte supplémentaire pour la génération. | AUDIO | Non | - |
| `longueur_maximale` | Le nombre maximal de tokens que le modèle de langage est autorisé à générer (par défaut : 512). | INT | Oui | 1 à 32768 |
| `mode_d'échantillonnage` | Contrôle si un échantillonnage aléatoire est utilisé pendant la génération de texte. Lorsqu’il est défini sur `"on"`, les paramètres d’échantillonnage ci-dessous deviennent disponibles ; avec `"off"`, le nœud génère du texte sans échantillonnage aléatoire. | DYNAMIC_COMBO | Oui | `"on"`<br>`"off"` |
| `réflexion` | Lorsque cette option est activée, le modèle reçoit l'instruction de raisonner avant de répondre. Tout bloc de raisonnement est renvoyé sur la sortie `thinking` plutôt que dans `generated_text` (par défaut : False). | BOOLEAN | Non | True/False |
| `utiliser le modèle par défaut` | Lorsque cette option est activée, le nœud utilise le gabarit de chat par défaut pour le formatage (par défaut : True). Paramètre avancé. | BOOLEAN | Non | True/False |
| `mtp` | Décodage spéculatif avec la tête de prédiction multi-token du checkpoint. N’a aucun effet sans les poids MTP. `"auto"` adapte la profondeur du brouillon ; `"2"` à `"5"` la fixent. La sortie échantillonnée reste correctement distribuée mais diffère de la sortie non-MTP pour la même graine (par défaut : `"auto"`). | COMBO | Non | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"` |
| `system_prompt` | Remplace l'invite système LTX-2 intégrée. Si elle est laissée vide, le nœud utilise ses propres instructions : l'invite image-vers-vidéo lorsqu'une `image` est connectée, sinon l'invite texte-vers-vidéo. Connectez une entrée STRING au lieu de la saisir dans le nœud (par défaut : vide). | STRING | Non | - |

### Paramètres d’échantillonnage (lorsque `sampling_mode` est "on")

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `temperature` | Contrôle le caractère aléatoire de la sortie. Des valeurs plus faibles rendent la sortie plus prévisible, des valeurs plus élevées la rendent plus créative (par défaut : 0.7). | FLOAT | Oui | 0.01 à 2.0 |
| `top_k` | Limite le pool d’échantillonnage aux K tokens suivants les plus probables. Une valeur de 0 désactive ce filtre (par défaut : 64). | INT | Oui | 0 à 1000 |
| `top_p` | Utilise l'échantillonnage par noyau (nucleus sampling) : conserve le plus petit ensemble de jetons les plus probables dont la probabilité cumulée atteint cette valeur. (par défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 |
| `min_p` | Définit un seuil de probabilité minimal pour que les tokens soient pris en compte (par défaut : 0.05). | FLOAT | Oui | 0.0 à 1.0 |
| `repetition_penalty` | Pénalise les tokens déjà générés afin de réduire les répétitions. Une valeur de 1.0 n’applique aucune pénalité (par défaut : 1.05). | FLOAT | Oui | 0.0 à 5.0 |
| `seed` | Un nombre utilisé pour initialiser le générateur de nombres aléatoires afin d’obtenir des résultats reproductibles (par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |
| `presence_penalty` | Pénalise les nouveaux tokens selon qu’ils sont déjà apparus dans le texte jusqu’ici, ce qui encourage le modèle à parler de nouveaux sujets (par défaut : 0.0). | FLOAT | Non | 0.0 à 5.0 |

**Remarque :** Les paramètres d’échantillonnage ci-dessus ne sont actifs et visibles dans l’interface du nœud que lorsque `sampling_mode` est défini sur "on". Lorsqu’il est défini sur "off", aucun paramètre d’échantillonnage n’est disponible et le nœud génère du texte sans échantillonnage aléatoire.

**Remarque :** Le comportement du nœud change en fonction de ses entrées :

- Si une `image` est fournie, l’invite générée est formatée pour une tâche image-vers-vidéo à l’aide d’une invite système qui décrit comment développer l’invite en fonction du contenu de l’image. Si aucune image n’est fournie, le formatage est destiné à une tâche texte-vers-vidéo à l’aide d’une invite système qui développe l’invite en une description détaillée de génération vidéo.
- Si le nom du tokenizer du CLIP contient "gemma4", le nœud utilise les invites système LTX-2.4 et le format de chat Gemma 4. Sinon, il utilise les invites système LTX-2 (Gemma 3) et le format de chat.
- Lorsque `thinking` est activé avec un modèle Gemma 4, le modèle est ouvert sur son canal de raisonnement ; lorsqu’il est désactivé, le modèle est ouvert directement sur le canal de réponse finale. Pour les modèles non-Gemma 4, `thinking` est transmis à l’étape de génération sous-jacente.
- Un `system_prompt` remplace les instructions intégrées du mode sélectionné (image-vers-vidéo ou texte-vers-vidéo) ; lorsqu'il est vide, l'invite intégrée est utilisée.
- Tout bloc de raisonnement est renvoyé sur la sortie `thinking` plutôt que dans `generated_text`.
- Si le modèle de langage ne produit aucun texte utilisable, le nœud renvoie le `prompt` d'origine à la place.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `generated_text` | L'invite de génération vidéo améliorée produite par le modèle de langage, tout bloc de raisonnement étant séparé dans la sortie `thinking`. Si le résultat est vide, l'invite utilisateur d'origine est renvoyée. | STRING |
| `thinking` | Le bloc de raisonnement produit par le modèle, sans la balise d'ouverture `<think>`. Vide si le modèle n'a produit aucun bloc de raisonnement ; avec les modèles Gemma 4, un bloc de raisonnement n'est attendu que si `thinking` est activé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/fr.md)

---
**Source fingerprint (SHA-256):** `a601a8bff65e8ee148d09f04ac0afc201dbc9ba5e09a65856400e9be37e085bb`

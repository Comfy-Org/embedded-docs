# Generate Text

Le nœud Generate Text utilise un modèle CLIP pour produire du texte à partir d’un prompt. Contrairement à l’ancien nœud à pièce jointe unique, il accepte des piles extensibles d’images, de vidéos et de fichiers audio comme contexte supplémentaire, ce qui permet d’alimenter un ensemble de référence complet dans un seul nœud. Vous contrôlez la longueur de la sortie, l’utilisation ou non de l’échantillonnage, ainsi que l’application ou non du gabarit de chat et du mode de réflexion propres au modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour tokeniser le prompt et générer le texte. | CLIP | Oui | - |
| `prompt` | Le prompt qui guide la génération. Prend en charge plusieurs lignes et les prompts dynamiques (par défaut : chaîne vide). | STRING | Oui | - |
| `images` | Groupe extensible de jusqu’à 50 images, de `image1` à `image50`, utilisées comme contexte visuel pour le modèle. | AUTOGROW | Non | 0 à 50 images |
| `videos` | Groupe extensible de jusqu’à 100 entrées vidéo, de `video1` à `video100`. Chaque vidéo est un lot de trames supposé à 24 FPS et sous-échantillonné à la cadence d'images du modèle en interne. | AUTOGROW | Non | 0 à 100 vidéos |
| `audios` | Groupe extensible de jusqu’à 100 entrées audio, de `audio1` à `audio100`, utilisées comme contexte audio pour le modèle. | AUTOGROW | Non | 0 à 100 fichiers audio |
| `max_length` | Nombre maximal de tokens à générer (par défaut : 512). | INT | Oui | 1 à 32768 |
| `sampling_mode` | `"on"` échantillonne la sortie et révèle les paramètres d’échantillonnage ci-dessous. `"off"` génère de manière gloutonne, sans échantillonnage aléatoire. | DYNAMIC_COMBO | Oui | `"on"`<br>`"off"` |
| `thinking` | Fonctionne en mode de réflexion si le modèle le prend en charge (par défaut : False). | BOOLEAN | Non | True ou False |
| `use_default_template` | Utilise l’invite système ou le gabarit de chat intégré si le modèle en possède un (par défaut : True). Paramètre avancé. | BOOLEAN | Non | True ou False |
| `mtp` | Décodage spéculatif avec la tête de prédiction multi-jetons du checkpoint. Sans pondérations MTP, ce paramètre n’a aucun effet. `"auto"` adapte la profondeur et la largeur du brouillon aux correspondances de tokens observées et au coût d’exécution, `"2"` à `"5"` fixent une profondeur de brouillon constante, et les modes `tree` fixent à la fois la largeur et la profondeur. La sortie échantillonnée reste correctement distribuée, mais diffère de la sortie non-MTP pour la même graine (par défaut : `"auto"`). | COMBO | Non | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"tree2s1"`<br>`"tree2s2"`<br>`"tree3s1"`<br>`"tree4s1m8"` |
| `system_prompt` | Remplace l’invite système dans le gabarit de chat du modèle. Ignoré lorsque le gabarit par défaut n’est pas utilisé. Connectez une entrée STRING au lieu de saisir dans le nœud (par défaut : vide). | STRING | Non | - |

### Paramètres d’échantillonnage (lorsque `sampling_mode` est `"on"`)

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `temperature` | Contrôle l’aléatoire de la sortie. Des valeurs plus faibles rendent la sortie plus prévisible, des valeurs plus élevées la rendent plus créative (par défaut : 0.7). | FLOAT | Oui | 0.01 à 2.0 |
| `top_k` | Limite le pool d’échantillonnage aux K tokens suivants les plus probables. Une valeur de 0 désactive le filtre (par défaut : 64). | INT | Oui | 0 à 1000 |
| `top_p` | Échantillonnage par noyau : conserve le plus petit ensemble de tokens les plus probables dont la probabilité cumulée atteint cette valeur (par défaut : 0.95). | FLOAT | Oui | 0.0 à 1.0 |
| `min_p` | Probabilité minimale qu’un token doit atteindre pour rester dans le pool (par défaut : 0.05). | FLOAT | Oui | 0.0 à 1.0 |
| `repetition_penalty` | Pénalise les tokens déjà générés afin de réduire les répétitions. Une valeur de 1.0 n’applique aucune pénalité (par défaut : 1.05). | FLOAT | Oui | 0.0 à 5.0 |
| `presence_penalty` | Pénalise les nouveaux tokens selon qu’ils sont déjà apparus ou non dans le texte jusqu’ici, en encourageant le modèle à passer à de nouveaux sujets (par défaut : 0.0). | FLOAT | Oui | 0.0 à 5.0 |
| `seed` | Nombre utilisé pour initialiser le générateur de nombres aléatoires afin d’obtenir des résultats reproductibles (par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |

**Remarque :** Les paramètres d’échantillonnage ci-dessus n’existent que lorsque `sampling_mode` est `"on"`. Avec `"off"`, le nœud génère du texte sans échantillonnage aléatoire et les paramètres sont masqués.

**Remarque :** Lorsque la sortie du modèle ouvre un bloc de raisonnement avec `<think>`, le nœud le sépare : `generated_text` contient la réponse et `thinking` contient le raisonnement avec la balise d’ouverture supprimée. Sinon, `generated_text` contient tout ce que le modèle a produit et `thinking` est vide. Le raisonnement qui a été tronqué par `max_length` reste dans `generated_text`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `generated_text` | Le texte généré par le modèle, avec tout bloc de raisonnement séparé dans la sortie `thinking`. | STRING |
| `thinking` | Le bloc de raisonnement produit par le modèle, avec la balise d’ouverture `<think>` supprimée. Vide lorsque le modèle n’a produit aucun bloc de raisonnement. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateV2/fr.md)

---
**Source fingerprint (SHA-256):** `b61210726faa495a342a5eaaebe64f800ec1d2af4e2fc1321d8c3d7c594bd9ca`

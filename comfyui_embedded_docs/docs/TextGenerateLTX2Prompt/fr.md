# TextGenerateLTX2Prompt

Le nœud TextGenerateLTX2Prompt développe un court prompt utilisateur en une description audio-visuelle détaillée, adaptée à la génération de vidéo avec la série de modèles vidéo LTX-2. Il ajoute automatiquement des instructions système spécifiques à la tâche, envoie le prompt formaté à un modèle de langage et renvoie le texte enrichi. Lorsqu’une image de référence facultative est fournie, le nœud bascule en mode image-vers-vidéo et développe le prompt à partir du contenu de cette image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour l’encodage de texte. Le nœud vérifie le nom du tokeniseur du modèle pour sélectionner les instructions correspondantes : les modèles basés sur Gemma 4 utilisent le format LTX-2.4, tandis que les autres modèles utilisent le format LTX-2 (Gemma 3). | CLIP | Oui |  |
| `invite` | Le texte brut décrivant la scène ou le concept à développer en un prompt de génération vidéo détaillé. | STRING | Oui |  |
| `longueur_maximale` | Le nombre maximal de jetons que le modèle de langage est autorisé à générer. | INT | Oui |  |
| `mode_d'échantillonnage` | La stratégie d’échantillonnage utilisée pour sélectionner le prochain jeton lors de la génération de texte. | COMBO | Oui | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `image` | Une image d’entrée facultative utilisée comme première image de la vidéo. Lorsqu’elle est fournie, le nœud bascule en mode image-vers-vidéo et utilise un prompt système qui développe le prompt utilisateur en fonction du contenu de l’image. | IMAGE | Non |  |
| `réflexion` | Lorsque cette option est activée, le modèle reçoit pour instruction de raisonner avant de répondre. Tout bloc de raisonnement est supprimé de la sortie renvoyée (par défaut : False). | BOOLEAN | Non |  |
| `utiliser le modèle par défaut` | Lorsque cette option est activée, le nœud utilise le modèle de chat par défaut pour le formatage (par défaut : True). | BOOLEAN | Non |  |
| `vidéo` | Une entrée vidéo facultative pouvant être utilisée comme contexte supplémentaire pour la génération. | VIDEO | Non |  |
| `audio` | Une entrée audio facultative pouvant être utilisée comme contexte supplémentaire pour la génération. | AUDIO | Non |  |

**Remarque :** Le comportement du nœud change en fonction de ses entrées :

- Si une `image` est fournie, le prompt généré est formaté pour une tâche image-vers-vidéo en utilisant un prompt système qui décrit comment développer le prompt en fonction du contenu de l’image. Si aucune image n’est fournie, le formatage est destiné à une tâche texte-vers-vidéo en utilisant un prompt système qui développe le prompt en une description détaillée de génération vidéo.
- Si le nom du tokeniseur du CLIP contient « gemma4 », le nœud utilise les prompts système LTX-2.4 et le format de chat Gemma 4. Sinon, il utilise les prompts système LTX-2 (Gemma 3) et le format de chat correspondant.
- Si le modèle de langage ne produit aucun texte utilisable après suppression des blocs de raisonnement, le nœud renvoie le `prompt` d’origine à la place.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `texte_généré` | Le prompt de génération vidéo enrichi produit par le modèle de langage, avec tout bloc de raisonnement supprimé. Si le résultat est vide, le prompt utilisateur d’origine est renvoyé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/fr.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`

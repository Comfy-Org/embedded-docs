# TextGenerateLTX2Prompt

Le nœud TextGenerateLTX2Prompt est une version spécialisée d'un nœud de génération de texte. Il prend la saisie texte de l'utilisateur et la formate automatiquement avec des instructions système spécifiques à LTX2 avant de l'envoyer à un modèle de langage pour l'enrichir ou la compléter. Le nœud peut fonctionner en mode texte seul ou en mode référence d'image, et il adapte automatiquement son formatage au modèle CLIP connecté, en utilisant le format de prompt LTX 2.4 pour les modèles Gemma 4 et le format LTX 2.0 pour les modèles Gemma 3.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour l'encodage du texte. Le modèle détermine le format du prompt : les modèles Gemma 4 utilisent le format LTX 2.4 et les modèles Gemma 3 utilisent le format LTX 2.0. | CLIP | Oui |  |
| `prompt` | Le texte brut saisi par l'utilisateur qui sera enrichi ou complété. | STRING | Oui |  |
| `max_length` | Le nombre maximal de jetons que le modèle de langage est autorisé à générer. | INT | Oui |  |
| `sampling_mode` | La stratégie d'échantillonnage utilisée pour sélectionner le prochain jeton lors de la génération de texte. | COMBO | Oui | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `image` | Une image d'entrée facultative. Lorsqu'elle est fournie, le nœud utilise un prompt système différent qui inclut le contexte de l'image pour la génération image-vers-vidéo. | IMAGE | Non |  |
| `thinking` | Lorsqu'il est activé, le modèle produit son processus de raisonnement avant la réponse finale. Le bloc de raisonnement est supprimé du résultat final. | BOOLEAN | Non |  |
| `use_default_template` | Lorsqu'il est activé, le nœud utilise le modèle de chat par défaut pour le formatage. | BOOLEAN | Non |  |
| `video` | Une entrée vidéo facultative pouvant être utilisée comme contexte supplémentaire pour la génération. | VIDEO | Non |  |
| `audio` | Une entrée audio facultative pouvant être utilisée comme contexte supplémentaire pour la génération. | AUDIO | Non |  |

**Remarques :** Le comportement du nœud change en fonction de la présence de l'entrée `image`. Si une image est fournie, le prompt est formaté pour une tâche image-vers-vidéo en utilisant un prompt système qui développe le prompt en fonction du contenu de l'image. Si aucune image n'est fournie, le formatage est pour une tâche texte-vers-vidéo en utilisant un prompt système qui développe le prompt en une description détaillée de génération vidéo.

Le modèle `clip` connecté affecte également le formatage : lorsque le tokenizer CLIP est un modèle Gemma 4, le nœud utilise le format de chat LTX 2.4 et les prompts système correspondants ; sinon, il utilise le format de chat Gemma 3 / LTX 2.0. Après la génération, tout bloc de raisonnement (par exemple `<think>...</think>`) est retiré de la sortie, et si le texte résultant est vide, le `prompt` d'origine est renvoyé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La chaîne de texte enrichie ou complétée générée par le modèle de langage, avec tout contenu de raisonnement supprimé. Si le modèle ne produit aucun texte, le prompt d'origine est renvoyé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/fr.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`

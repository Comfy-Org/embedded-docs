Le nœud TextGenerateLTX2Prompt est une version spécialisée d'un nœud de génération de texte. Il prend une invite textuelle de l'utilisateur et la formate automatiquement avec des instructions système spécifiques avant de l'envoyer à un modèle de langage pour amélioration ou complétion. Le nœud peut fonctionner selon deux modes : texte uniquement ou avec une référence d'image, en utilisant différentes invites système pour chaque cas.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour l'encodage du texte. | CLIP | Oui |  |
| `invite` | L'entrée textuelle brute de l'utilisateur qui sera améliorée ou complétée. | STRING | Oui |  |
| `longueur_maximale` | Le nombre maximum de jetons que le modèle de langage est autorisé à générer. | INT | Oui |  |
| `mode_d'échantillonnage` | La stratégie d'échantillonnage utilisée pour sélectionner le prochain jeton lors de la génération de texte. | COMBO | Oui | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `image` | Une image d'entrée facultative. Lorsqu'elle est fournie, le nœud utilise une invite système différente qui inclut un espace réservé pour le contexte de l'image. | IMAGE | Non |  |
| `réflexion` | Lorsqu'il est activé, le modèle affichera son processus de raisonnement avant la réponse finale. | BOOLEAN | Non |  |
| `utiliser le modèle par défaut` | Lorsqu'il est activé, le nœud utilisera le modèle de chat par défaut pour le formatage. | BOOLEAN | Non |  |
| `vidéo` | Une entrée vidéo facultative pouvant être utilisée comme contexte supplémentaire pour la génération. | VIDEO | Non |  |
| `audio` | Une entrée audio facultative pouvant être utilisée comme contexte supplémentaire pour la génération. | AUDIO | Non |  |

**Remarque :** Le comportement du nœud change en fonction de la présence de l'entrée `image`. Si une image est fournie, l'invite générée sera formatée pour une tâche image-vers-vidéo. Si aucune image n'est fournie, le formatage sera pour une tâche texte-vers-vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La chaîne de texte améliorée ou complétée générée par le modèle de langage. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/fr.md)

---
**Source fingerprint (SHA-256):** `a3daa0a376a53b9c5613238092cc1289d4c358c7c74b12a6e311681de550d1f8`

Le nœud T5TokenizerOptions vous permet de configurer les paramètres du tokenizer pour différents types de modèles T5. Il définit les valeurs minimales de padding et de longueur pour plusieurs variantes de modèles T5, notamment t5xxl, pile_t5xl, t5base, mt5xl et umt5xxl. Le nœud prend une entrée CLIP et retourne un CLIP modifié avec les options de tokenizer spécifiées appliquées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP pour lequel configurer les options du tokenizer | CLIP | Oui | - |
| `remplissage_min` | Valeur minimale de padding à définir pour tous les types de modèles T5 (par défaut : 0) | INT | Non | 0 à 10000 |
| `longueur_min` | Valeur minimale de longueur à définir pour tous les types de modèles T5 (par défaut : 0) | INT | Non | 0 à 10000 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le modèle CLIP modifié avec les options de tokenizer mises à jour appliquées à toutes les variantes T5 | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/fr.md)

---
**Source fingerprint (SHA-256):** `bc05c714e4006786d0c948ed1de05324257472337397b0aa4ce574d7483929ff`

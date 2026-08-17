# T5TokenizerOptions

Le nœud T5TokenizerOptions vous permet de configurer les paramètres du tokenizer pour différents types de modèles T5. Il définit les paramètres de padding minimum et de longueur minimale pour plusieurs variantes de modèles T5, notamment t5xxl, pile_t5xl, t5base, mt5xl et umt5xxl. Le nœud prend une entrée CLIP et renvoie un CLIP modifié avec les options de tokenizer spécifiées appliquées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP pour lequel configurer les options du tokenizer | CLIP | Oui | - |
| `min_padding` | Valeur de padding minimale à définir pour tous les types de modèles T5 (défaut : 0) | INT | Non | 0 to 10000 |
| `min_length` | Valeur de longueur minimale à définir pour tous les types de modèles T5 (défaut : 0) | INT | Non | 0 to 10000 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le modèle CLIP modifié avec les options de tokenizer mises à jour appliquées à toutes les variantes T5 | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/fr.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`

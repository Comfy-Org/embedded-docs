> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/fr.md)

Le nœud T5TokenizerOptions permet de configurer les paramètres du tokenizer pour différents types de modèles T5. Il définit les paramètres de remplissage minimum et de longueur minimum pour plusieurs variantes de modèles T5 incluant t5xxl, pile_t5xl, t5base, mt5xl et umt5xxl. Le nœud prend une entrée CLIP et retourne un modèle CLIP modifié avec les options de tokenizer spécifiées appliquées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP pour lequel configurer les options du tokenizer |
| `remplissage_min` | INT | Non | 0-10000 | Valeur de remplissage minimum à définir pour tous les types de modèles T5 (par défaut : 0) |
| `longueur_min` | INT | Non | 0-10000 | Valeur de longueur minimum à définir pour tous les types de modèles T5 (par défaut : 0) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | CLIP | Le modèle CLIP modifié avec les options de tokenizer mises à jour appliquées à toutes les variantes T5 |
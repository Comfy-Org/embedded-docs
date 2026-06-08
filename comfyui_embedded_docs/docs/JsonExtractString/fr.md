Le nœud JsonExtractString lit une chaîne de texte contenant des données JSON et extrait la valeur associée à une clé spécifique. Il convertit la valeur extraite en une chaîne de caractères. Si le JSON est invalide, la clé est introuvable ou la valeur est nulle, le nœud renvoie une chaîne vide.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `json_string` | Le texte contenant les données JSON à analyser. | STRING | Oui | N/A |
| `key` | La clé spécifique dont vous souhaitez extraire la valeur sous forme de chaîne à partir de l'objet JSON. | STRING | Oui | N/A |

**Remarque :** Le nœud extrait uniquement les valeurs des objets JSON (dictionnaires). Si le JSON analysé n'est pas un objet ou si la clé spécifiée n'existe pas dans celui-ci, la sortie sera une chaîne vide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La valeur sous forme de chaîne extraite du JSON pour la clé spécifiée, ou une chaîne vide si l'extraction échoue. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/fr.md)

---
**Source fingerprint (SHA-256):** `f05e2d9fd4888870a844c85ac7543d6c38c1c56f2ef22a402fc93ee716743612`

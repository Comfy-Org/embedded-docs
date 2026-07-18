Voici la traduction en français de la documentation du nœud Replace Text, en respectant vos règles :

Le nœud Replace Text effectue une simple substitution de texte. Il recherche un texte spécifié dans l'entrée et remplace chaque occurrence par un nouveau texte. L'opération est appliquée à toutes les entrées de texte fournies au nœud.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `text` | Le texte à traiter. | STRING | Oui | - |
| `find` | Texte à rechercher (par défaut : chaîne vide). | STRING | Oui | - |
| `replace` | Texte de remplacement (par défaut : chaîne vide). | STRING | Oui | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `texts` | Le texte traité, où toutes les occurrences du texte `find` ont été remplacées par le texte `replace`. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/fr.md)

---
**Source fingerprint (SHA-256):** `e9d4681e638c5ca2732ec254282243e9e9cdd01cc985af8bbfa41dea208cb7dd`

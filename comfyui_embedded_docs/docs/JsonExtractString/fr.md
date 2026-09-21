# Extraire une chaîne du JSON

Le nœud JsonExtractString analyse une chaîne de texte à la recherche du premier objet JSON valide et extrait la valeur associée à une clé spécifique, convertie en chaîne. Tout texte avant ou après l’objet JSON est ignoré, de sorte que le nœud fonctionne aussi sur les blocs de code Markdown et sur les réponses de modèle qui englobent le JSON dans du texte supplémentaire. Si aucun objet JSON valide n’est trouvé, si la clé est introuvable ou si la valeur est null, le nœud renvoie une chaîne vide.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `json_string` | Le texte dans lequel rechercher un objet JSON. Ce champ prend en charge la saisie multiligne et peut contenir du texte environnant ou des délimiteurs de code Markdown. | STRING | Oui | N/A |
| `key` | La clé spécifique dont vous souhaitez extraire la valeur depuis l’objet JSON. Ce champ ne prend en charge que la saisie monoligne. | STRING | Oui | N/A |

**Remarque :** Le nœud extrait uniquement les valeurs des objets JSON (dictionnaires). Il essaie chaque `{` dans l’entrée dans l’ordre et décode à partir de la première position qui produit un objet JSON valide, de sorte que le texte qui précède ou qui suit est ignoré. Si aucun objet JSON ne peut être décodé ou si la clé spécifiée n’existe pas dans celui-ci, la sortie est une chaîne vide. Si la valeur associée à la clé est `null`, le nœud renvoie également une chaîne vide. Les valeurs qui ne sont pas des chaînes sont renvoyées sous leur représentation sous forme de chaîne.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Valeur de chaîne extraite du JSON pour la clé spécifiée, ou chaîne vide si l’extraction échoue. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/fr.md)

---
**Source fingerprint (SHA-256):** `ca697fd3bd2d4de764372470ad1102b345d9d60f6df1c151fa0573e85fab2382`

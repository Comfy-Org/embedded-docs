# BriaReplaceObject

Remplace un objet dans une image par un autre décrit en texte simple, à l'aide de l'édition d'image guidée par texte de Bria. Bria ré-effectue le rendu de toute l'image à environ 1 mégapixel ; le résultat n'est donc pas aligné au pixel près avec l'entrée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image contenant l'objet à remplacer. Le canal alpha est supprimé avant le téléversement de l'image. | IMAGE | Oui | - |
| `instruction` | Quoi remplacer par quoi, par exemple « Replace the red apple with a green pear ». Doit comporter au moins 1 caractère. | STRING | Oui | Texte multiligne ; par défaut : "" (vide) |
| `seed` | Bria n'utilise pas de seed ici et réimagine la modification à chaque appel ; des exécutions répétées peuvent donc différer. La valeur n'est jamais envoyée : elle modifie uniquement la clé de cache de ce nœud, afin qu'un graphe par ailleurs identique relance la modification au lieu de renvoyer le résultat mis en cache. | INT | Oui | 0 à 2147483647, pas de 1 ; par défaut : 42 ; contrôle après génération activé |

### Entrées de modération

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `moderation` | Paramètres de modération. Sélectionner « true » affiche les sous-options de modération ci-dessous, qui autrement ne sont pas affichées. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |
| `visual_input_moderation` | Active la modération de l'image d'entrée. Disponible uniquement lorsque `moderation` est défini sur « true ». | BOOLEAN | Non | `true` / `false`; par défaut : false |
| `visual_output_moderation` | Active la modération de l'image de sortie générée. Disponible uniquement lorsque `moderation` est défini sur « true ». | BOOLEAN | Non | `true` / `false`; par défaut : false |

Remarque : `instruction` est validée avant l'envoi de la requête et doit comporter au moins 1 caractère. La valeur de `seed` n'est pas transmise à Bria ; elle détermine uniquement si le nœud relance la modification ou renvoie un résultat mis en cache.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image modifiée avec le remplacement d'objet décrit appliqué. | IMAGE |
| `structured_prompt` | Description structurée de l'image modifiée, pour une modification ultérieure avec Bria FIBO Image Edit. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceObject/fr.md)

---
**Source fingerprint (SHA-256):** `75a45d5c0d6cde96a1e961db627edc1a59c07cc37b974402745cefc62864cc26`

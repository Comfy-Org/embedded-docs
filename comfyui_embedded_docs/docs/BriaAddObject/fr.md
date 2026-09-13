# BriaAddObject

Ce nœud insère un objet décrit en texte brut dans une image à l'aide de Bria. Bria restitue l'intégralité de l'image à environ 1 mégapixel, le résultat n'est donc pas aligné au pixel près avec l'entrée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image à laquelle l'objet décrit est ajouté. Le canal alpha est supprimé avant le téléversement de l'image. | IMAGE | Oui | - |
| `instruction` | Ce qu'il faut ajouter et où, par exemple « Placez un vase rouge avec des fleurs sur la table ». Ne doit pas être vide. Par défaut : "" (chaîne vide). | STRING | Oui | - |
| `seed` | Bria n'utilise aucun seed ici et réimagine la modification à chaque appel, de sorte que des exécutions répétées peuvent différer. La valeur n'est jamais envoyée : elle modifie uniquement la clé de cache de ce nœud, afin qu'un graphe par ailleurs identique relance la modification au lieu de renvoyer le résultat mis en cache. Par défaut : 42. | INT | Oui | 0 à 2147483647 |
| `moderation` | Paramètres de modération. Choisissez "true" pour afficher les options de modération ci-dessous. | DYNAMIC_COMBO | Oui | "false"<br>"true" |

### Entrées activées par la modération

Disponibles lorsque `moderation` est défini sur "true".

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_input_moderation` | Active la modération du contenu sur l'image d'entrée. Par défaut : False. | BOOLEAN | Non | True / False |
| `visual_output_moderation` | Active la modération du contenu sur l'image de sortie générée. Par défaut : False. | BOOLEAN | Non | True / False |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image modifiée avec l'objet décrit ajouté. | IMAGE |
| `structured_prompt` | Description structurée de l'image modifiée, pour une modification ultérieure avec Bria FIBO Image Edit. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaAddObject/fr.md)

---
**Source fingerprint (SHA-256):** `41c9a3e511763372d8dc8be9da4f70158e53d5156a88eb3c66f81149efdbd566`

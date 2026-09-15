# BriaEraseByText

Ce nœud supprime d’une image un objet décrit en texte brut à l’aide de Bria. Bria ré-effectue le rendu de toute l’image à environ 1 mégapixel, le résultat n’est donc pas aligné au pixel près avec l’entrée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image de laquelle l’objet nommé doit être supprimé. | IMAGE | Oui | - |
| `object_name` | Nom de l’objet à supprimer, par exemple 'the lamp'. Plusieurs objets peuvent être nommés en même temps, par exemple 'the phone and the pencils'. Nommer un élément qui n’est pas dans l’image renvoie tout de même une image re-rendue, et la requête est quand même facturée. Doit contenir au moins 1 caractère (par défaut : vide). | STRING | Oui | - |
| `modération` | Paramètres de modération. Détermine si les contrôles de modération facultatifs sont affichés. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |

### Entrées de modération

Ces paramètres apparaissent lorsque `moderation` est défini sur `"true"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_input_moderation` | Active la modération de contenu sur l’image d’entrée (par défaut : false). | BOOLEAN | Non | true<br>false |
| `visual_output_moderation` | Active la modération de contenu sur l’image de sortie générée (par défaut : false). | BOOLEAN | Non | true<br>false |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image re-rendue avec l’objet nommé supprimé. | IMAGE |
| `structured_prompt` | Description structurée de l’image modifiée, pour une modification ultérieure avec Bria FIBO Image Edit. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseByText/fr.md)

---
**Source fingerprint (SHA-256):** `51ac362bea731251c99905172c41cdebb5165e7564c508f13aa43cf9072964ef`

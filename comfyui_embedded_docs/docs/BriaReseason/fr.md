# BriaReseason

Ce nœud fait passer une image vers une autre saison à l'aide de Bria. Toute la scène est rendue à nouveau, le décor peut donc changer au-delà de la saison elle-même. Bria rend à nouveau toute l'image à environ 1 mégapixel, le résultat n'est donc pas aligné au pixel près avec l'entrée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image à faire passer vers une autre saison. Tout canal alpha est supprimé avant que l'image ne soit envoyée. | IMAGE | Oui | - |
| `saison` | Saison à appliquer. | COMBO | Oui | `"spring"`<br>`"summer"`<br>`"autumn"`<br>`"winter"` |
| `moderation` | Paramètres de modération. Détermine si les options de modération de contenu sont configurées pour cette requête. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |

### Entrées de modération

Ces options apparaissent lorsque `moderation` est défini sur `"true"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_input_moderation` | Active la modération de contenu sur l'image d'entrée (par défaut : false). | BOOLEAN | Non | true<br>false |
| `visual_output_moderation` | Active la modération de contenu sur l'image de sortie générée (par défaut : false). | BOOLEAN | Non | true<br>false |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image re-rendue dans la saison sélectionnée. | IMAGE |
| `structured_prompt` | Description structurée de l'image modifiée, pour une édition ultérieure avec Bria FIBO Image Edit. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReseason/fr.md)

---
**Source fingerprint (SHA-256):** `3bb9ee1c00c91759cc6f972e2ba8708ae73a186f4b66bf6669937e561efad0a4`

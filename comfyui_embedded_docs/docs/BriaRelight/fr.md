# BriaRelight

Ce nœud modifie l’ambiance et la direction de l’éclairage d’une image à l’aide de Bria. L’image est rendue à nouveau par Bria, de sorte que le résultat n’est pas aligné au pixel près avec l’entrée ; toute l’image est régénérée à environ 1 mégapixel.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image dont l’éclairage est modifié. Tout canal alpha est supprimé avant le téléversement de l’image. | IMAGE | Oui | - |
| `light_type` | Ambiance d’éclairage à appliquer. | COMBO | Oui | `"midday"`<br>`"blue hour light"`<br>`"low-angle sunlight"`<br>`"sunrise light"`<br>`"spotlight on subject"`<br>`"overcast light"`<br>`"soft overcast daylight lighting"`<br>`"cloud-filtered lighting"`<br>`"fog-diffused lighting"`<br>`"moonlight lighting"`<br>`"starlight nighttime"`<br>`"soft bokeh lighting"`<br>`"harsh studio lighting"` |
| `light_direction` | Provenance de la lumière. Les ambiances à lumière dure telles que midday, spotlight on subject et harsh studio lighting y réagissent le plus. | COMBO | Oui | `"front"`<br>`"side"`<br>`"bottom"`<br>`"top-down"` |
| `modération` | Paramètres de modération. Sélectionnez `"true"` pour afficher les options de modération, ou `"false"` pour exécuter sans celles-ci. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |

### Entrées de modération

Ces options apparaissent lorsque `moderation` est défini sur `"true"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_input_moderation` | Active la modération de contenu sur l’image d’entrée. Par défaut : false. | BOOLEAN | Non | `true`<br>`false` |
| `visual_output_moderation` | Active la modération de contenu sur l’image de sortie générée. Par défaut : false. | BOOLEAN | Non | `true`<br>`false` |

Remarque : Bria rend à nouveau toute l’image à environ 1 mégapixel, de sorte que le résultat n’est pas aligné au pixel près avec l’entrée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image rééclairée renvoyée par Bria. | IMAGE |
| `structured_prompt` | Description structurée de l’image modifiée, pour une modification ultérieure avec Bria FIBO Image Edit. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/fr.md)

---
**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`

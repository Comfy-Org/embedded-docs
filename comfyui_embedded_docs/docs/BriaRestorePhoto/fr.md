# BriaRestorePhoto

Ce nœud répare les photographies anciennes ou endommagées via l’API Bria. Il supprime le grain, les rayures et le flou, neutralise les dominantes colorées liées à l’âge, peut éliminer par recadrage les supports en carton et les bordures de studio, et redessine les visages. Le résultat est rendu à nouveau à environ 1 mégapixel, il n’est donc pas aligné au pixel près avec l’entrée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | La photographie à réparer. Le canal alpha est supprimé avant l’envoi. | IMAGE | Oui | - |
| `moderation` | Paramètres de modération pour la requête. Sélectionner `"true"` révèle deux bascules booléennes supplémentaires ; sélectionner `"false"` n’envoie aucun indicateur de modération. Par défaut : `"false"`. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |

### Entrées de modération

Ces entrées apparaissent uniquement lorsque `moderation` est défini sur `"true"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_input_moderation` | Active la modération du contenu visuel sur l’image d’entrée. Par défaut : false. | BOOLEAN | Non | true<br>false |
| `visual_output_moderation` | Active la modération du contenu visuel sur l’image de sortie. Par défaut : false. | BOOLEAN | Non | true<br>false |

**Remarque :** Le nœud rend à nouveau l’image entière à environ 1 mégapixel, le résultat n’est donc pas aligné au pixel près avec l’entrée. Utilisez le nœud Bria Increase Resolution pour agrandir l’image plutôt que ce nœud.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | La photographie réparée renvoyée par Bria. | IMAGE |
| `structured_prompt` | Description structurée de l’image modifiée, pour une modification ultérieure avec Bria FIBO Image Edit. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRestorePhoto/fr.md)

---
**Source fingerprint (SHA-256):** `387ec3e049464f185e27f79d160ade2a4170ab238853064c008892d84523fa68`

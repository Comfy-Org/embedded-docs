# FLUX 3 Image Layout Prompt

Construit la table de disposition que FLUX 3 Image lit à partir d’un prompt. Il prend les éléments dessinés dans le nœud Create Bounding Boxes et les ajoute à votre prompt sous forme de liste de boîtes, chacune avec un id, ses coordonnées et sa description. Citez une boîte dans le prompt sous la forme `<obj_N>` pour associer des mots à cette région, puis connectez la sortie à l’entrée prompt du nœud FLUX 3 Image. Si aucun élément n’est connecté, le prompt est renvoyé inchangé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Le texte du prompt. Citez la boîte N sous la forme `<obj_N>` pour y associer des mots. | STRING | Oui | - |
| `element` | Les éléments à placer dans la disposition, provenant du nœud Create Bounding Boxes. Les palettes de couleurs ne sont pas utilisées, décrivez donc les couleurs dans la description. | ARRAY | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `prompt` | Le prompt avec la table de disposition des boîtes ajoutée, prêt à être transmis au nœud FLUX 3 Image. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3LayoutPrompt/fr.md)

---
**Source fingerprint (SHA-256):** `ac8f61701c8da0a6fc8361aeebf7fc5e7aa338ce6ad8689718904caa9c53e3b8`

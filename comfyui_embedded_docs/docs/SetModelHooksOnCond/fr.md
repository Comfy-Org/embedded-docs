Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/en.md)

Ce nœud attache des hooks personnalisés aux données de conditionnement, vous permettant d'intercepter et de modifier le processus de conditionnement lors de l'exécution du modèle. Il prend un ensemble de hooks et les applique aux données de conditionnement fournies, permettant une personnalisation avancée du flux de génération texte-à-image. Le conditionnement modifié avec les hooks attachés est ensuite renvoyé pour être utilisé dans les étapes de traitement ultérieures.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditioning` | Les données de conditionnement auxquelles les hooks seront attachés | CONDITIONING | Oui | - |
| `hooks` | Les définitions de hooks qui seront appliquées aux données de conditionnement | HOOKS | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Les données de conditionnement modifiées avec les hooks attachés | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/fr.md)

---
**Source fingerprint (SHA-256):** `a6e63a3a4d94d1b66a82d449af5ae001e1fc4a04f0f81d9fb5c4f8c13e5bdf8b`

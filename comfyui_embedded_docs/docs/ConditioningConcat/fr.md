> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/fr.md)

Le nœud ConditioningConcat est conçu pour concaténer des vecteurs de conditionnement, en fusionnant spécifiquement le vecteur `conditioning_from` dans le vecteur `conditioning_to`. Cette opération est fondamentale dans les scénarios où les informations de conditionnement provenant de deux sources doivent être combinées en une seule représentation unifiée.

## Entrées

| Paramètre           | Type Comfy        | Description |
|---------------------|-------------------|-------------|
| `conditionnement_vers`   | `CONDITIONING`    | Représente l'ensemble principal de vecteurs de conditionnement auquel les vecteurs `conditionnement_de` seront concaténés. Il sert de base au processus de concaténation. |
| `conditionnement_de` | `CONDITIONING`    | Contient les vecteurs de conditionnement qui doivent être concaténés aux vecteurs `conditionnement_vers`. Ce paramètre permet d'intégrer des informations de conditionnement supplémentaires à l'ensemble existant. |

## Sorties

| Paramètre          | Type Comfy        | Description |
|--------------------|-------------------|-------------|
| `conditioning`     | `CONDITIONING`    | La sortie est un ensemble unifié de vecteurs de conditionnement, résultant de la concaténation des vecteurs `conditionnement_de` dans les vecteurs `conditionnement_vers`. |
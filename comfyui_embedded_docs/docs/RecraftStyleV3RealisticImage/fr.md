> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/fr.md)

Ce nœud crée une configuration de style d'image réaliste pour utilisation avec l'API de Recraft. Il vous permet de sélectionner le style réaliste_image et de choisir parmi diverses options de sous-styles pour personnaliser l'apparence du résultat.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `sous-style` | STRING | Oui | Plusieurs options disponibles | Le sous-style spécifique à appliquer au style réaliste_image. Si défini sur "None", aucun sous-style ne sera appliqué. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Retourne un objet de configuration de style Recraft contenant le style réaliste_image et les paramètres de sous-style sélectionnés. |
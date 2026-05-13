> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/fr.md)

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/en.md)

Ce nœud crée une configuration de style pour générer des images réalistes à l'aide de l'API Recraft. Il sélectionne le style `realistic_image` et vous permet de choisir un sous-style optionnel pour affiner l'apparence du résultat.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `substyle` | STRING | Oui | Plusieurs options disponibles (déterminées par l'API Recraft) | Le sous-style spécifique à appliquer au style realistic_image. Si défini sur "None", aucun sous-style ne sera appliqué. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `recraft_style` | STYLEV3 | Un objet de configuration de style Recraft contenant le style `realistic_image` et les paramètres du sous-style sélectionné. Cette sortie peut être connectée à d'autres nœuds Recraft qui acceptent une entrée de style. |

---
**Source fingerprint (SHA-256):** `23eafae0a00f1806052a6583db791a5c1fd418ea940ed6463824dffe843ed0d7`

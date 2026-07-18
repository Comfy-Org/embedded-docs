# Conditionnement (Multiplication)

Ce nœud multiplie les vecteurs de conditionnement par un facteur scalaire, vous permettant d'ajuster l'influence d'une entrée de conditionnement. Il applique le multiplicateur à la fois au tenseur de conditionnement principal et à la sortie poolée, si elle est présente.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `conditioning` | Les données de conditionnement à mettre à l'échelle | CONDITIONING | Oui | - |
| `multiplier` | Le facteur d'échelle à appliquer au conditionnement (par défaut : 1.0) | FLOAT | Oui | -100.0 à 100.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CONDITIONING` | Les données de conditionnement mises à l'échelle avec le multiplicateur appliqué à la fois au tenseur principal et à la sortie poolée | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/fr.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`

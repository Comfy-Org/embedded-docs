# ConditioningMultiply

Ce nœud multiplie les valeurs de conditionnement par un facteur spécifié, vous permettant d'ajuster l'influence du conditionnement sur le processus de génération. Il fonctionne en appliquant le multiplicateur à la fois au tenseur de conditionnement principal et aux valeurs de sortie regroupées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `conditioning` | Les données de conditionnement à mettre à l'échelle | CONDITIONING | Oui | - |
| `multiplier` | Le facteur par lequel multiplier les valeurs de conditionnement (par défaut : 1.0) | FLOAT | Oui | -100.0 à 100.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CONDITIONING` | Les données de conditionnement mises à l'échelle avec des valeurs multipliées | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/fr.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`

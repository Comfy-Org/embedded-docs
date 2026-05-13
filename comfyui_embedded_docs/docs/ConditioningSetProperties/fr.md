> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/fr.md)

Le nœud ConditioningSetProperties modifie les propriétés des données de conditionnement en ajustant la force, les paramètres de zone et en appliquant des masques, des hooks ou des plages de pas de temps facultatifs. Il vous permet de contrôler la manière dont le conditionnement influence le processus de génération en définissant des paramètres spécifiques qui affectent l'application des données de conditionnement lors de la génération d'images.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------------|---------------|--------|-------|-------------|
| `cond_NEW` | CONDITIONING | Requis | - | - | Les données de conditionnement à modifier |
| `strength` | FLOAT | Requis | 1.0 | 0.0 - 10.0 (pas : 0.01) | Contrôle l'intensité de l'effet de conditionnement |
| `set_cond_area` | STRING | Requis | default | ["default", "mask bounds"] | Détermine comment la zone de conditionnement est appliquée. Choisissez "default" pour un comportement standard ou "mask bounds" pour restreindre à la région du masque |
| `mask` | MASK | Optionnel | - | - | Masque optionnel pour restreindre l'application du conditionnement |
| `hooks` | HOOKS | Optionnel | - | - | Fonctions hook optionnelles pour un traitement personnalisé |
| `timesteps` | TIMESTEPS_RANGE | Optionnel | - | - | Plage de pas de temps optionnelle pour limiter l'activation du conditionnement |

**Remarque :** Lorsqu'un `mask` est fourni, le paramètre `set_cond_area` peut être défini sur "mask bounds" pour restreindre l'application du conditionnement à la région masquée uniquement. Le paramètre `hooks` permet un traitement personnalisé via des fonctions hook, et `timesteps` limite l'effet de conditionnement à une plage spécifique de pas de temps pendant la génération.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement modifiées avec les propriétés mises à jour |

---
**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`

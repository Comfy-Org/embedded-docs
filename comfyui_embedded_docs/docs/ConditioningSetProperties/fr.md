> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/fr.md)

Le nœud ConditioningSetProperties modifie les propriétés des données de conditionnement en ajustant la force, les paramètres de zone et en appliquant des masques optionnels ou des plages d'étapes temporelles. Il vous permet de contrôler comment le conditionnement influence le processus de génération en définissant des paramètres spécifiques qui affectent l'application des données de conditionnement pendant la génération d'image.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `cond_NEW` | CONDITIONING | Requis | - | - | Les données de conditionnement à modifier |
| `strength` | FLOAT | Requis | 1.0 | 0.0-10.0 | Contrôle l'intensité de l'effet de conditionnement |
| `set_cond_area` | STRING | Requis | default | ["default", "mask bounds"] | Détermine comment la zone de conditionnement est appliquée |
| `mask` | MASK | Optionnel | - | - | Masque optionnel pour restreindre l'application du conditionnement |
| `hooks` | HOOKS | Optionnel | - | - | Fonctions de hook optionnelles pour un traitement personnalisé |
| `timesteps` | TIMESTEPS_RANGE | Optionnel | - | - | Plage d'étapes temporelles optionnelle pour limiter quand le conditionnement est actif |

**Note :** Lorsqu'un `mask` est fourni, le paramètre `set_cond_area` peut être défini sur "mask bounds" pour restreindre l'application du conditionnement uniquement à la région masquée.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement modifiées avec les propriétés mises à jour |
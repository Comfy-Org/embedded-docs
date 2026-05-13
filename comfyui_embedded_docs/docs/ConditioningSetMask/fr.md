> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/fr.md)

Ce nœud est conçu pour modifier le conditionnement d'un modèle génératif en appliquant un masque avec une intensité spécifique à certaines zones. Il permet des ajustements ciblés au sein du conditionnement, offrant un contrôle plus précis sur le processus de génération.

## Entrées

### Requises

| Paramètre     | Type de données | Description |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement à modifier. Elles servent de base pour l'application du masque et des ajustements d'intensité. |
| `masque`        | `MASK`       | Un tenseur de masque qui spécifie les zones du conditionnement à modifier. |
| `force`    | `FLOAT`      | L'intensité de l'effet du masque sur le conditionnement, permettant un réglage fin des modifications appliquées. |
| `définir_zone_cond` | COMBO[STRING] | Détermine si l'effet du masque est appliqué à la zone par défaut ou limité par le masque lui-même, offrant une flexibilité pour cibler des régions spécifiques. |

## Sorties

| Paramètre     | Type de données | Description |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement modifiées, avec les ajustements du masque et de l'intensité appliqués. |
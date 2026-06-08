Ce nœud est conçu pour modifier le conditionnement d'un modèle génératif en appliquant un masque avec une intensité spécifique à certaines zones. Il permet des ajustements ciblés au sein du conditionnement, offrant un contrôle plus précis sur le processus de génération.

## Entrées

### Requises

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement à modifier. Elles servent de base pour l'application du masque et des ajustements d'intensité. | CONDITIONING |
| `masque` | Un tenseur de masque qui spécifie les zones du conditionnement à modifier. | `MASK` |
| `force` | L'intensité de l'effet du masque sur le conditionnement, permettant un réglage fin des modifications appliquées. | `FLOAT` |
| `définir_zone_cond` | Détermine si l'effet du masque est appliqué à la zone par défaut ou limité par le masque lui-même, offrant une flexibilité pour cibler des régions spécifiques. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement modifiées, avec les ajustements du masque et de l'intensité appliqués. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/fr.md)

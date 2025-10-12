Ce nœud est conçu pour modifier le conditionnement d'un modèle génératif en appliquant un masque avec une force spécifiée à certaines zones. Il permet des ajustements ciblés au sein du conditionnement, offrant un contrôle plus précis sur le processus de génération.

## Entrées

### Requis

| Paramètre     | Type de Donnée | Description |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement à modifier. Elles servent de base pour appliquer les ajustements de masque et de force. |
| `masque`        | `MASK`       | Un tenseur de masque qui spécifie les zones à modifier au sein du conditionnement. |
| `force`    | `FLOAT`      | La force de l'effet du masque sur le conditionnement, permettant un ajustement précis des modifications appliquées. |
| `définir_zone_cond` | COMBO[STRING] | Détermine si l'effet du masque est appliqué à la zone par défaut ou limité par le masque lui-même, offrant une flexibilité dans le ciblage de régions spécifiques. |

## Sorties

| Paramètre     | Type de Donnée | Description |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement modifiées, avec les ajustements de masque et de force appliqués. |

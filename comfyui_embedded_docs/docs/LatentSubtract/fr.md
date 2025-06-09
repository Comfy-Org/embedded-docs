
Le nœud LatentSubtract est conçu pour soustraire une représentation latente d'une autre. Cette opération peut être utilisée pour manipuler ou modifier les caractéristiques des sorties des modèles génératifs en supprimant efficacement les caractéristiques ou attributs représentés dans un espace latent d'un autre.

## Entrées

| Paramètre    | Data Type | Description |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | Le premier ensemble d'échantillons latents à partir duquel soustraire. Il sert de base pour l'opération de soustraction. |
| `samples2`   | `LATENT`    | Le second ensemble d'échantillons latents qui sera soustrait du premier ensemble. Cette opération peut modifier la sortie du modèle génératif en supprimant des attributs ou caractéristiques. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Le résultat de la soustraction du second ensemble d'échantillons latents du premier. Cette représentation latente modifiée peut être utilisée pour d'autres tâches génératives. |


Le nœud KSamplerSelect est conçu pour sélectionner un échantillonneur spécifique basé sur le nom de l'échantillonneur fourni. Il simplifie la complexité de la sélection d'échantillonneur, permettant aux utilisateurs de passer facilement d'une stratégie d'échantillonnage à une autre pour leurs tâches.

## Entrées

| Paramètre         | Data Type | Description                                                                                      |
|-------------------|-------------|------------------------------------------------------------------------------------------------|
| `sampler_name`    | COMBO[STRING] | Spécifie le nom de l'échantillonneur à sélectionner. Ce paramètre détermine quelle stratégie d'échantillonnage sera utilisée, influençant le comportement global de l'échantillonnage et les résultats. |

## Sorties

| Paramètre   | Data Type | Description                                                                 |
|-------------|-------------|-----------------------------------------------------------------------------|
| `sampler`   | `SAMPLER`   | Retourne l'objet échantillonneur sélectionné, prêt à être utilisé pour les tâches d'échantillonnage. |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/fr.md)

Le nœud KSamplerSelect est conçu pour sélectionner un échantillonneur spécifique en fonction du nom d'échantillonneur fourni. Il abstrait la complexité de la sélection d'échantillonneur, permettant aux utilisateurs de basculer facilement entre différentes stratégies d'échantillonnage pour leurs tâches.

## Entrées

| Paramètre         | Type de données | Description                                                                                      |
|-------------------|-----------------|--------------------------------------------------------------------------------------------------|
| `sampler_name`    | COMBO[STRING]   | Spécifie le nom de l'échantillonneur à sélectionner. Ce paramètre détermine la stratégie d'échantillonnage utilisée, ce qui influence le comportement global d'échantillonnage et les résultats. |

## Sorties

| Paramètre   | Type de données | Description                                                                 |
|-------------|-----------------|-----------------------------------------------------------------------------|
| `sampler`   | `SAMPLER`       | Renvoie l'objet échantillonneur sélectionné, prêt à être utilisé pour les tâches d'échantillonnage. |
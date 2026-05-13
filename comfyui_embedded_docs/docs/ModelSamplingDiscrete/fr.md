> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingDiscrete/fr.md)

Ce nœud est conçu pour modifier le comportement d'échantillonnage d'un modèle en appliquant une stratégie d'échantillonnage discrète. Il permet de sélectionner différentes méthodes d'échantillonnage, telles que epsilon, v_prediction, lcm ou x0, et ajuste éventuellement la stratégie de réduction du bruit du modèle en fonction du paramètre de rapport de bruit zero-shot (zsnr).

## Entrées

| Paramètre | Type de données | Type Python     | Description |
|-----------|-----------------|-------------------|-------------|
| `model`   | MODEL           | `torch.nn.Module` | Le modèle auquel la stratégie d'échantillonnage discrète sera appliquée. Ce paramètre est crucial car il définit le modèle de base qui subira la modification. |
| `sampling`| COMBO[STRING]   | `str`             | Spécifie la méthode d'échantillonnage discrète à appliquer au modèle. Le choix de la méthode influence la façon dont le modèle génère des échantillons, offrant différentes stratégies d'échantillonnage. |
| `zsnr`    | `BOOLEAN`       | `bool`            | Un indicateur booléen qui, lorsqu'il est activé, ajuste la stratégie de réduction du bruit du modèle en fonction du rapport de bruit zero-shot. Cela peut influencer la qualité et les caractéristiques des échantillons générés. |

## Sorties

| Paramètre | Type de données | Type Python     | Description |
|-----------|-----------------|-------------------|-------------|
| `model`   | MODEL           | `torch.nn.Module` | Le modèle modifié avec la stratégie d'échantillonnage discrète appliquée. Ce modèle est désormais capable de générer des échantillons en utilisant la méthode et les ajustements spécifiés. |

Ce nœud est conçu pour modifier le comportement d'échantillonnage d'un modèle en appliquant une stratégie d'échantillonnage discret. Il permet la sélection de différentes méthodes d'échantillonnage, telles que epsilon, v_prediction, lcm, ou x0, et ajuste éventuellement la stratégie de réduction de bruit du modèle en fonction du paramètre zero-shot noise ratio (zsnr).

## Entrées

| Paramètre | Data Type | Python dtype     | Description |
|-----------|--------------|-------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module` | Le modèle auquel la stratégie d'échantillonnage discret sera appliquée. Ce paramètre est crucial car il définit le modèle de base qui subira la modification. |
| `sampling`| COMBO[STRING] | `str`           | Spécifie la méthode d'échantillonnage discret à appliquer au modèle. Le choix de la méthode affecte la manière dont le modèle génère des échantillons, offrant différentes stratégies d'échantillonnage. |
| `zsnr`    | `BOOLEAN`   | `bool`           | Un indicateur booléen qui, lorsqu'il est activé, ajuste la stratégie de réduction de bruit du modèle en fonction du zero-shot noise ratio. Cela peut influencer la qualité et les caractéristiques des échantillons générés. |

## Sorties

| Paramètre | Data Type | Python dtype     | Description |
|-----------|-------------|-------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module` | Le modèle modifié avec la stratégie d'échantillonnage discret appliquée. Ce modèle est maintenant équipé pour générer des échantillons en utilisant la méthode et les ajustements spécifiés. |

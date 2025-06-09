Cette documentation concerne le nœud original `Apply ControlNet(Advanced)`. Le plus ancien nœud `Apply ControlNet` a été renommé en `Apply ControlNet(Old)`. Bien que vous puissiez encore voir le nœud `Apply ControlNet(Old)` dans de nombreux dossiers de workflow que vous téléchargez depuis comfyui.org pour des raisons de compatibilité, vous ne pouvez plus trouver le nœud `Apply ControlNet(Old)` via la recherche ou la liste des nœuds. Veuillez utiliser le nœud `Apply ControlNet` à la place.
Ce nœud applique ControlNet à une image et à un conditionnement donnés, ajustant les attributs de l'image selon les paramètres et la force spécifiés des réseaux de contrôle tels que Depth, OpenPose, Canny, HED.

Pour utiliser ControlNet, un prétraitement de l'image d'entrée est nécessaire. Les nœuds initiaux de ComfyUI n'incluent pas de préprocesseurs ni de modèles ControlNet, vous devez donc d'abord installer le préprocesseur ContrlNet [Télécharger le préprocesseur](https://github.com/Fannovel16/comfy_controlnet_preprocessors) et le modèle ControlNet correspondant.

### Entrées

| Paramètre | Type de données | Fonction |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Données de conditionnement positif provenant de `l'encodeur de texte CLIP` ou d'autres entrées de conditionnement |
| `negative` | `CONDITIONING` | Données de conditionnement négatif provenant de `l'encodeur de texte CLIP]` ou d'autres entrées de conditionnement |
| `control_net` | `CONTROL_NET` | Modèle ControlNet à appliquer, généralement en entrée depuis le `chargeur ControlNet` |
| `image` | `IMAGE` | Image pour l'application de ControlNet, nécessite un traitement par préprocesseur |
| `vae` | `VAE` | Entrée du modèle Vae |
| `strength` | `FLOAT` | Contrôle l'intensité de l'ajustement du réseau, plage de valeurs 0~10. Les valeurs recommandées se situent entre 0,5 et 1,5. Des valeurs plus basses donnent plus de liberté au modèle, des valeurs plus élevées imposent des contraintes plus strictes. Des valeurs trop élevées peuvent générer des images étranges. |
| `start_percent` | `FLOAT` | Valeur 0.000~1.000, détermine le point de départ de l'application de ControlNet en pourcentage, par exemple 0.2 signifie que le guide ControlNet commence à influencer la génération d'image au point 20% du processus de diffusion |
| `end_percent` | `FLOAT` | Valeur 0.000~1.000, détermine le point final de l'application de ControlNet en pourcentage, par exemple 0.8 signifie que le guide ControlNet cesse d'influencer la génération d'image au point 80% du processus de diffusion |

### Sorties

| Paramètre | Type de données | Fonction |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Données de conditionnement positif traitées par ControlNet, peuvent être transmises au nœud ControlNet suivant ou au nœud K Sampler |
| `negative` | `CONDITIONING` | Données de conditionnement négatif traitées par ControlNet, peuvent être transmises au nœud ControlNet suivant ou au nœud K Sampler |

Pour les modèles de style **T2IAdaptor**, utilisez plutôt le nœud `Apply Style Model`

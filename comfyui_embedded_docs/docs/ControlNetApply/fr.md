# Appliquer ControlNet (ANCIEN)

L'utilisation de ControlNet nécessite un prétraitement des images d'entrée. Étant donné que les nœuds initiaux de ComfyUI ne sont pas fournis avec des préprocesseurs et des modèles ControlNet, veuillez d'abord installer les préprocesseurs ControlNet [télécharger les préprocesseurs ici](https://github.com/Fannovel16/comfy_controlnet_preprocessors) ainsi que les modèles ControlNet correspondants.

## Entrées

| Paramètre | Type de données | Fonction |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Données de conditionnement positives, provenant de l'encodeur de texte CLIP ou d'autres entrées de conditionnement |
| `negative` | `CONDITIONING` | Données de conditionnement négatives, provenant de l'encodeur de texte CLIP ou d'autres entrées de conditionnement |
| `control_net` | `CONTROL_NET` | Le modèle ControlNet à appliquer, généralement saisi à partir du chargeur ControlNet |
| `image` | `IMAGE` | Image pour l'application de ControlNet, doit être traitée par un préprocesseur |
| `vae` | `VAE` | Entrée du modèle VAE |
| `strength` | `FLOAT` | Contrôle la force des ajustements du réseau, plage de valeurs 0~10. Les valeurs recommandées entre 0,5~1,5 sont raisonnables. Des valeurs plus faibles permettent plus de liberté au modèle, des valeurs plus élevées imposent des contraintes plus strictes. Des valeurs trop élevées peuvent produire des images étranges. Vous pouvez tester et ajuster cette valeur pour affiner l'influence du réseau de contrôle. |
| `start_percent` | `FLOAT` | Valeur 0,000~1,000, détermine le moment de début d'application de ControlNet en pourcentage, par exemple 0,2 signifie que le guidage ControlNet commencera à influencer la génération d'image à 20 % du processus de diffusion |
| `end_percent` | `FLOAT` | Valeur 0,000~1,000, détermine le moment d'arrêt de l'application de ControlNet en pourcentage, par exemple 0,8 signifie que le guidage ControlNet cessera d'influencer la génération d'image à 80 % du processus de diffusion |

### Sorties

| Paramètre | Type de données | Fonction |
| --- | --- | --- |
| `positive` | `CONDITIONING` | Données de conditionnement positives traitées par ControlNet, peuvent être transmises au nœud ControlNet suivant ou aux nœuds K Sampler |
| `negative` | `CONDITIONING` | Données de conditionnement négatives traitées par ControlNet, peuvent être transmises au nœud ControlNet suivant ou aux nœuds K Sampler |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApply/fr.md)

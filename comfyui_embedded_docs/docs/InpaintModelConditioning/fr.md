# InpaintModelConditioning

Le nœud InpaintModelConditioning est conçu pour faciliter le processus de conditionnement des modèles d'infilling (inpainting), permettant l'intégration et la manipulation de diverses entrées de conditionnement afin d'adapter le résultat de l'infilling. Il englobe un large éventail de fonctionnalités, allant du chargement de points de contrôle de modèle spécifiques et de l'application de modèles de style ou de contrôle net, jusqu'au codage et à la combinaison d'éléments de conditionnement, constituant ainsi un outil complet pour personnaliser les tâches d'infilling.

## Entrées

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `positive` | Représente les informations ou paramètres de conditionnement positif à appliquer au modèle d'infilling. Cette entrée est cruciale pour définir le contexte ou les contraintes dans lesquels l'opération d'infilling doit être effectuée, affectant considérablement le résultat final. | `CONDITIONING` |
| `négatif` | Représente les informations ou paramètres de conditionnement négatif à appliquer au modèle d'infilling. Cette entrée est essentielle pour spécifier les conditions ou contextes à éviter pendant le processus d'infilling, influençant ainsi le résultat final. | `CONDITIONING` |
| `vae` | Spécifie le modèle VAE à utiliser dans le processus de conditionnement. Cette entrée est cruciale pour déterminer l'architecture et les paramètres spécifiques du modèle VAE qui sera utilisé. | `VAE` |
| `pixels` | Représente les données de pixels de l'image à traiter par infilling. Cette entrée est essentielle pour fournir le contexte visuel nécessaire à la tâche d'infilling. | `IMAGE` |
| `masque` | Spécifie le masque à appliquer à l'image, indiquant les zones à traiter par infilling. Cette entrée est cruciale pour définir les régions spécifiques de l'image nécessitant un infilling. | `MASK` |


| Paramètre | Description | Type de données |
| --- | --- | --- |
| `positive` | Les informations de conditionnement positif modifiées après traitement, prêtes à être appliquées au modèle d'infilling. Cette sortie est essentielle pour guider le processus d'infilling conformément aux conditions positives spécifiées. | `CONDITIONING` |
| `negative` | Les informations de conditionnement négatif modifiées après traitement, prêtes à être appliquées au modèle d'infilling. Cette sortie est essentielle pour guider le processus d'infilling conformément aux conditions négatives spécifiées. | `CONDITIONING` |
| `latent` | La représentation latente dérivée du processus de conditionnement. Cette sortie est cruciale pour comprendre les caractéristiques et attributs sous-jacents de l'image en cours de traitement par infilling. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InpaintModelConditioning/fr.md)

# Guidance VideoLinearCFG

Le nœud VideoLinearCFGGuidance applique une échelle de guidage conditionnel linéaire à un modèle vidéo, ajustant l'influence des composants conditionnés et non conditionnés sur une plage spécifiée. Cela permet un contrôle dynamique du processus de génération, offrant un réglage fin de la sortie du modèle en fonction du niveau de conditionnement souhaité.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le paramètre `modèle` représente le modèle vidéo auquel le guidage CFG linéaire sera appliqué. Il est essentiel pour définir le modèle de base qui sera modifié avec l'échelle de guidage. | MODEL |
| `min_cfg` | Le paramètre `min_cfg` spécifie l'échelle de guidage conditionnel minimale à appliquer, servant de point de départ pour l'ajustement linéaire de l'échelle. Il joue un rôle clé dans la détermination de la limite inférieure de l'échelle de guidage, influençant la sortie du modèle. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `modèle` | La sortie est une version modifiée du modèle d'entrée, avec l'échelle de guidage CFG linéaire appliquée. Ce modèle ajusté est capable de générer des sorties avec différents degrés de conditionnement, en fonction de l'échelle de guidage spécifiée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoLinearCFGGuidance/fr.md)

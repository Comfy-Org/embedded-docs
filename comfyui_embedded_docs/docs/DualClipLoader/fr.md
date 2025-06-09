Le nœud DualCLIPLoader est conçu pour charger deux modèles CLIP simultanément, facilitant les opérations nécessitant l'intégration ou la comparaison des caractéristiques des deux modèles.

## Entrées

| Paramètre    | Data Type | Description |
|--------------|--------------|-------------|
| `clip_name1` | COMBO[STRING] | Spécifie le nom du premier modèle CLIP à charger. Ce paramètre est crucial pour identifier et récupérer le modèle correct à partir d'une liste prédéfinie de modèles CLIP disponibles. |
| `clip_name2` | COMBO[STRING] | Spécifie le nom du second modèle CLIP à charger. Ce paramètre permet le chargement d'un second modèle CLIP distinct pour une analyse comparative ou intégrative aux côtés du premier modèle. |
| `type`       | `option`        | Choisissez parmi "sdxl", "sd3", "flux" pour s'adapter à différents modèles. |

* L'ordre de chargement n'affecte pas l'effet de sortie

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|--------------|-------------|
| `clip`    | `CLIP`       | La sortie est un modèle CLIP combiné qui intègre les caractéristiques ou fonctionnalités des deux modèles CLIP spécifiés. |

## Exemple de flux de travail

Le flux de travail original est cité de <https://openart.ai/workflows/seal_harmful_40/flux/UGHBjoJgN8tLnhr7FKOP>

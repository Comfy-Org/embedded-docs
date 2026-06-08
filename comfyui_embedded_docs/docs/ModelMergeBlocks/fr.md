ModelMergeBlocks est conçu pour des opérations avancées de fusion de modèles, permettant l'intégration de deux modèles avec des ratios de mélange personnalisables pour différentes parties des modèles. Ce nœud facilite la création de modèles hybrides en fusionnant sélectivement des composants de deux modèles sources en fonction de paramètres spécifiés.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `modèle1` | Le premier modèle à fusionner. Il sert de modèle de base sur lequel les correctifs du second modèle sont appliqués. | `MODEL` |
| `modèle2` | Le second modèle à partir duquel les correctifs sont extraits et appliqués au premier modèle, en fonction des ratios de mélange spécifiés. | `MODEL` |
| `entrée` | Spécifie le ratio de mélange pour la couche d'entrée des modèles. Il détermine la proportion de la couche d'entrée du second modèle fusionnée dans le premier modèle. | `FLOAT` |
| `milieu` | Définit le ratio de mélange pour les couches intermédiaires des modèles. Ce paramètre contrôle le niveau d'intégration des couches intermédiaires des modèles. | `FLOAT` |
| `sortie` | Détermine le ratio de mélange pour la couche de sortie des modèles. Il affecte la sortie finale en ajustant la contribution de la couche de sortie du second modèle. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné résultant, qui est un hybride des deux modèles d'entrée avec des correctifs appliqués selon les ratios de mélange spécifiés. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeBlocks/fr.md)

# ModelMergeKrea2

Ce nœud fusionne deux modèles en mélangeant leurs composants internes à un niveau granulaire, vous permettant de contrôler l'influence de chaque partie spécifique des modèles sur le résultat final. Il fonctionne en prenant deux modèles d'entrée et en appliquant des ratios de mélange distincts à différentes sections de leur architecture.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Le second modèle à fusionner | MODEL | Oui | - |
| `first.` | Ratio de mélange pour le premier bloc de couches (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `tmlp.` | Ratio de mélange pour le bloc MLP temporel (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `txtmlp.` | Ratio de mélange pour le bloc MLP textuel (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `tproj.` | Ratio de mélange pour le bloc de projection temporelle (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `txtfusion.layerwise_blocks.0.` | Ratio de mélange pour le premier bloc de fusion textuelle par couche (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `txtfusion.layerwise_blocks.1.` | Ratio de mélange pour le second bloc de fusion textuelle par couche (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `txtfusion.projector.` | Ratio de mélange pour le bloc projecteur de fusion textuelle (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `txtfusion.refiner_blocks.0.` | Ratio de mélange pour le premier bloc affineur de fusion textuelle (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `txtfusion.refiner_blocks.1.` | Ratio de mélange pour le second bloc affineur de fusion textuelle (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `blocks.0.` à `blocks.27.` | Ratio de mélange pour chacun des 28 blocs principaux (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `last.` | Ratio de mélange pour le dernier bloc (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

Chaque ratio de mélange contrôle la proportion de `model2` utilisée pour ce composant spécifique, où 0.0 signifie utiliser uniquement `model1`, 1.0 signifie utiliser uniquement `model2`, et les valeurs intermédiaires créent un mélange pondéré.

## Sorties

| Nom de la sortie | Description | Type de données |
|------------------|-------------|-----------------|
| `MODEL` | Le modèle fusionné résultant du mélange des deux modèles d'entrée selon les ratios spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeKrea2/fr.md)

---
**Source fingerprint (SHA-256):** `ece35524f77fd906dc3109a0818d4d7d3986ec9debb518fd04893048843d7e88`

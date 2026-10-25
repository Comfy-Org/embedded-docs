# ModelMergeSD2

Le nœud ModelMergeSD2 fusionne deux modèles Stable Diffusion 2.x en mélangeant leurs composants correspondants, avec un poids distinct pour l'embedding temporel, l'embedding de label, et chaque bloc d'entrée, intermédiaire et de sortie. La disposition des blocs est la même que dans ModelMergeSD1, donc les deux nœuds exposent le même ensemble de ratios.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner. Tous les composants auxquels le second modèle ne contribue pas sont conservés depuis ce modèle | MODEL | Oui | - |
| `model2` | Le second modèle à fusionner. Ses poids sont mélangés selon les ratios ci-dessous | MODEL | Oui | - |
| `time_embed.` | Ratio de mélange pour la couche d'embedding temporel (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `label_emb.` | Ratio de mélange pour la couche d'embedding de label (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `input_blocks.0.` à `input_blocks.11.` | Ratio de mélange pour chacun des 12 blocs d'entrée (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `middle_block.0.` à `middle_block.2.` | Ratio de mélange pour chacun des 3 blocs intermédiaires (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `output_blocks.0.` à `output_blocks.11.` | Ratio de mélange pour chacun des 12 blocs de sortie (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `out.` | Ratio de mélange pour la couche de sortie (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

Un ratio de 0.0 conserve ce composant tel qu'il est dans `model1`, un ratio de 1.0 le prend entièrement depuis `model2`, et les valeurs intermédiaires produisent un mélange pondéré. Les deux entrées doivent être des modèles Stable Diffusion 2.x avec la même structure de blocs.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle fusionné, combinant les deux entrées selon les ratios spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD2/fr.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`

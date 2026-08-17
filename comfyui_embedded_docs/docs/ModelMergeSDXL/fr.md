# ModelMergeSDXL

Le nœud `ModelMergeSDXL` vous permet de fusionner deux modèles SDXL en ajustant l’influence de chaque modèle sur différentes parties de l’architecture. Vous pouvez contrôler la contribution de chaque modèle aux intégrations temporelles, aux intégrations d’étiquettes et aux différents blocs de la structure du modèle. Cela crée un modèle hybride qui combine les caractéristiques des deux modèles d’entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle SDXL à fusionner | MODEL | Oui | - |
| `model2` | Le second modèle SDXL à fusionner | MODEL | Oui | - |
| `time_embed.` | Poids de fusion pour les couches d’intégration temporelle (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `label_emb.` | Poids de fusion pour les couches d’intégration des étiquettes (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.0` | Poids de fusion pour le bloc d’entrée 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.1` | Poids de fusion pour le bloc d’entrée 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.2` | Poids de fusion pour le bloc d’entrée 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.3` | Poids de fusion pour le bloc d’entrée 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.4` | Poids de fusion pour le bloc d’entrée 4 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.5` | Poids de fusion pour le bloc d’entrée 5 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.6` | Poids de fusion pour le bloc d’entrée 6 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.7` | Poids de fusion pour le bloc d’entrée 7 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.8` | Poids de fusion pour le bloc d’entrée 8 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `middle_block.0` | Poids de fusion pour le bloc intermédiaire 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `middle_block.1` | Poids de fusion pour le bloc intermédiaire 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `middle_block.2` | Poids de fusion pour le bloc intermédiaire 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.0` | Poids de fusion pour le bloc de sortie 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.1` | Poids de fusion pour le bloc de sortie 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.2` | Poids de fusion pour le bloc de sortie 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.3` | Poids de fusion pour le bloc de sortie 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.4` | Poids de fusion pour le bloc de sortie 4 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.5` | Poids de fusion pour le bloc de sortie 5 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.6` | Poids de fusion pour le bloc de sortie 6 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.7` | Poids de fusion pour le bloc de sortie 7 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.8` | Poids de fusion pour le bloc de sortie 8 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `out.` | Poids de fusion pour les couches de sortie (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

Tous les paramètres de poids de fusion sont des valeurs FLOAT requises comprises entre 0.0 et 1.0, avec une valeur par défaut de 1.0, et peuvent être ajustés par pas de 0.01.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle SDXL fusionné combinant les caractéristiques des deux modèles d’entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/fr.md)

---
**Source fingerprint (SHA-256):** `9a1b0645ee19c2eddb274dd6ea3f9a05997115119cc654a7f055d58475745bb2`

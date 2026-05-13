> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/fr.md)

Le nœud ModelMergeSDXL vous permet de fusionner deux modèles SDXL en ajustant l'influence de chaque modèle sur différentes parties de l'architecture. Vous pouvez contrôler la contribution de chaque modèle aux intégrations temporelles, aux intégrations d'étiquettes et à divers blocs au sein de la structure du modèle. Cela crée un modèle hybride combinant les caractéristiques des deux modèles d'entrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model1` | MODEL | Oui | - | Premier modèle SDXL à fusionner |
| `model2` | MODEL | Oui | - | Deuxième modèle SDXL à fusionner |
| `time_embed.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour les couches d'intégration temporelle (par défaut : 1.0) |
| `label_emb.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour les couches d'intégration d'étiquettes (par défaut : 1.0) |
| `input_blocks.0` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc d'entrée 0 (par défaut : 1.0) |
| `input_blocks.1` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc d'entrée 1 (par défaut : 1.0) |
| `input_blocks.2` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc d'entrée 2 (par défaut : 1.0) |
| `input_blocks.3` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc d'entrée 3 (par défaut : 1.0) |
| `input_blocks.4` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc d'entrée 4 (par défaut : 1.0) |
| `input_blocks.5` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc d'entrée 5 (par défaut : 1.0) |
| `input_blocks.6` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc d'entrée 6 (par défaut : 1.0) |
| `input_blocks.7` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc d'entrée 7 (par défaut : 1.0) |
| `input_blocks.8` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc d'entrée 8 (par défaut : 1.0) |
| `middle_block.0` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc central 0 (par défaut : 1.0) |
| `middle_block.1` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc central 1 (par défaut : 1.0) |
| `middle_block.2` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc central 2 (par défaut : 1.0) |
| `output_blocks.0` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc de sortie 0 (par défaut : 1.0) |
| `output_blocks.1` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc de sortie 1 (par défaut : 1.0) |
| `output_blocks.2` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc de sortie 2 (par défaut : 1.0) |
| `output_blocks.3` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc de sortie 3 (par défaut : 1.0) |
| `output_blocks.4` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc de sortie 4 (par défaut : 1.0) |
| `output_blocks.5` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc de sortie 5 (par défaut : 1.0) |
| `output_blocks.6` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc de sortie 6 (par défaut : 1.0) |
| `output_blocks.7` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc de sortie 7 (par défaut : 1.0) |
| `output_blocks.8` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour le bloc de sortie 8 (par défaut : 1.0) |
| `out.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion pour les couches de sortie (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle SDXL fusionné combinant les caractéristiques des deux modèles d'entrée |

---
**Source fingerprint (SHA-256):** `6c7572a6ed50534f2d9ad6f499146763457da58f0c9dd4b85204e67f7d3e9660`

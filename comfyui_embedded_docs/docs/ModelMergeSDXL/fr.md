> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/fr.md)

Le nœud ModelMergeSDXL vous permet de fusionner deux modèles SDXL en ajustant l'influence de chaque modèle sur différentes parties de l'architecture. Vous pouvez contrôler la contribution de chaque modèle aux embeddings temporels, aux embeddings de label et aux différents blocs de la structure du modèle. Cela crée un modèle hybride qui combine les caractéristiques des deux modèles d'entrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Oui | - | Le premier modèle SDXL à fusionner |
| `model2` | MODEL | Oui | - | Le deuxième modèle SDXL à fusionner |
| `time_embed.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour les couches d'embedding temporel (par défaut : 1.0) |
| `label_emb.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour les couches d'embedding de label (par défaut : 1.0) |
| `input_blocks.0` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc d'entrée 0 (par défaut : 1.0) |
| `input_blocks.1` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc d'entrée 1 (par défaut : 1.0) |
| `input_blocks.2` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc d'entrée 2 (par défaut : 1.0) |
| `input_blocks.3` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc d'entrée 3 (par défaut : 1.0) |
| `input_blocks.4` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc d'entrée 4 (par défaut : 1.0) |
| `input_blocks.5` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc d'entrée 5 (par défaut : 1.0) |
| `input_blocks.6` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc d'entrée 6 (par défaut : 1.0) |
| `input_blocks.7` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc d'entrée 7 (par défaut : 1.0) |
| `input_blocks.8` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc d'entrée 8 (par défaut : 1.0) |
| `middle_block.0` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc central 0 (par défaut : 1.0) |
| `middle_block.1` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc central 1 (par défaut : 1.0) |
| `middle_block.2` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc central 2 (par défaut : 1.0) |
| `output_blocks.0` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc de sortie 0 (par défaut : 1.0) |
| `output_blocks.1` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc de sortie 1 (par défaut : 1.0) |
| `output_blocks.2` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc de sortie 2 (par défaut : 1.0) |
| `output_blocks.3` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc de sortie 3 (par défaut : 1.0) |
| `output_blocks.4` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc de sortie 4 (par défaut : 1.0) |
| `output_blocks.5` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc de sortie 5 (par défaut : 1.0) |
| `output_blocks.6` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc de sortie 6 (par défaut : 1.0) |
| `output_blocks.7` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc de sortie 7 (par défaut : 1.0) |
| `output_blocks.8` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le bloc de sortie 8 (par défaut : 1.0) |
| `out.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour les couches de sortie (par défaut : 1.0) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle SDXL fusionné combinant les caractéristiques des deux modèles d'entrée |
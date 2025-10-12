> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/fr.md)

Le nœud ModelMergeSD1 vous permet de fusionner deux modèles Stable Diffusion 1.x en ajustant l'influence des différents composants du modèle. Il offre un contrôle individuel sur l'embedding temporel, l'embedding de label et tous les blocs d'entrée, intermédiaires et de sortie, permettant une fusion de modèles affinée pour des cas d'utilisation spécifiques.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Oui | - | Le premier modèle à fusionner |
| `model2` | MODEL | Oui | - | Le deuxième modèle à fusionner |
| `time_embed.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion de la couche d'embedding temporel (par défaut : 1.0) |
| `label_emb.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion de la couche d'embedding de label (par défaut : 1.0) |
| `input_blocks.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 0 (par défaut : 1.0) |
| `input_blocks.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 1 (par défaut : 1.0) |
| `input_blocks.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 2 (par défaut : 1.0) |
| `input_blocks.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 3 (par défaut : 1.0) |
| `input_blocks.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 4 (par défaut : 1.0) |
| `input_blocks.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 5 (par défaut : 1.0) |
| `input_blocks.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 6 (par défaut : 1.0) |
| `input_blocks.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 7 (par défaut : 1.0) |
| `input_blocks.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 8 (par défaut : 1.0) |
| `input_blocks.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 9 (par défaut : 1.0) |
| `input_blocks.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 10 (par défaut : 1.0) |
| `input_blocks.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc d'entrée 11 (par défaut : 1.0) |
| `middle_block.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc intermédiaire 0 (par défaut : 1.0) |
| `middle_block.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc intermédiaire 1 (par défaut : 1.0) |
| `middle_block.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc intermédiaire 2 (par défaut : 1.0) |
| `output_blocks.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 0 (par défaut : 1.0) |
| `output_blocks.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 1 (par défaut : 1.0) |
| `output_blocks.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 2 (par défaut : 1.0) |
| `output_blocks.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 3 (par défaut : 1.0) |
| `output_blocks.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 4 (par défaut : 1.0) |
| `output_blocks.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 5 (par défaut : 1.0) |
| `output_blocks.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 6 (par défaut : 1.0) |
| `output_blocks.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 7 (par défaut : 1.0) |
| `output_blocks.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 8 (par défaut : 1.0) |
| `output_blocks.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 9 (par défaut : 1.0) |
| `output_blocks.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 10 (par défaut : 1.0) |
| `output_blocks.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc de sortie 11 (par défaut : 1.0) |
| `out.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion de la couche de sortie (par défaut : 1.0) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `MODEL` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée |

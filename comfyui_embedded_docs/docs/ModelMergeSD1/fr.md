# ModelMergeSD1

Le nœud ModelMergeSD1 vous permet de fusionner deux modèles Stable Diffusion 1.x en ajustant l'influence de différents composants du modèle. Il offre un contrôle individuel sur l'intégration temporelle, l'intégration d'étiquettes, ainsi que tous les blocs d'entrée, intermédiaires et de sortie, permettant un fusionnement de modèles finement ajusté pour des cas d'utilisation spécifiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Le second modèle à fusionner | MODEL | Oui | - |
| `time_embed.` | Poids de fusion de la couche d'intégration temporelle (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `label_emb.` | Poids de fusion de la couche d'intégration d'étiquettes (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.0.` | Poids de fusion du bloc d'entrée 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.1.` | Poids de fusion du bloc d'entrée 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.2.` | Poids de fusion du bloc d'entrée 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.3.` | Poids de fusion du bloc d'entrée 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.4.` | Poids de fusion du bloc d'entrée 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.5.` | Poids de fusion du bloc d'entrée 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.6.` | Poids de fusion du bloc d'entrée 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.7.` | Poids de fusion du bloc d'entrée 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.8.` | Poids de fusion du bloc d'entrée 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.9.` | Poids de fusion du bloc d'entrée 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.10.` | Poids de fusion du bloc d'entrée 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `input_blocks.11.` | Poids de fusion du bloc d'entrée 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `middle_block.0.` | Poids de fusion du bloc intermédiaire 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `middle_block.1.` | Poids de fusion du bloc intermédiaire 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `middle_block.2.` | Poids de fusion du bloc intermédiaire 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.0.` | Poids de fusion du bloc de sortie 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.1.` | Poids de fusion du bloc de sortie 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.2.` | Poids de fusion du bloc de sortie 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.3.` | Poids de fusion du bloc de sortie 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.4.` | Poids de fusion du bloc de sortie 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.5.` | Poids de fusion du bloc de sortie 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.6.` | Poids de fusion du bloc de sortie 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.7.` | Poids de fusion du bloc de sortie 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.8.` | Poids de fusion du bloc de sortie 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.9.` | Poids de fusion du bloc de sortie 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.10.` | Poids de fusion du bloc de sortie 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `output_blocks.11.` | Poids de fusion du bloc de sortie 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `out.` | Poids de fusion de la couche de sortie (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/fr.md)

---
**Source fingerprint (SHA-256):** `512c62fb5a4e1b7f90f5ad5b80de5818659a20c8f4b024cfa33ca13b823efad8`

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/fr.md)

Le nœud ModelMergeSD3_2B permet de fusionner deux modèles Stable Diffusion 3 2B en mélangeant leurs composants avec des poids ajustables. Il offre un contrôle individuel sur les couches d'embedding et les blocs de transformeurs, permettant des combinaisons de modèles finement ajustées pour des tâches de génération spécialisées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model1` | MODEL | Oui | - | Premier modèle à fusionner |
| `model2` | MODEL | Oui | - | Second modèle à fusionner |
| `pos_embed.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de l'embedding de position (par défaut : 1.0) |
| `x_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de l'embedding d'entrée (par défaut : 1.0) |
| `context_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de l'embedding de contexte (par défaut : 1.0) |
| `y_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de l'embedding Y (par défaut : 1.0) |
| `t_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de l'embedding temporel (par défaut : 1.0) |
| `joint_blocks.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 0 (par défaut : 1.0) |
| `joint_blocks.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 1 (par défaut : 1.0) |
| `joint_blocks.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 2 (par défaut : 1.0) |
| `joint_blocks.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 3 (par défaut : 1.0) |
| `joint_blocks.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 4 (par défaut : 1.0) |
| `joint_blocks.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 5 (par défaut : 1.0) |
| `joint_blocks.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 6 (par défaut : 1.0) |
| `joint_blocks.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 7 (par défaut : 1.0) |
| `joint_blocks.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 8 (par défaut : 1.0) |
| `joint_blocks.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 9 (par défaut : 1.0) |
| `joint_blocks.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 10 (par défaut : 1.0) |
| `joint_blocks.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 11 (par défaut : 1.0) |
| `joint_blocks.12.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 12 (par défaut : 1.0) |
| `joint_blocks.13.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 13 (par défaut : 1.0) |
| `joint_blocks.14.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 14 (par défaut : 1.0) |
| `joint_blocks.15.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 15 (par défaut : 1.0) |
| `joint_blocks.16.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 16 (par défaut : 1.0) |
| `joint_blocks.17.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 17 (par défaut : 1.0) |
| `joint_blocks.18.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 18 (par défaut : 1.0) |
| `joint_blocks.19.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 19 (par défaut : 1.0) |
| `joint_blocks.20.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 20 (par défaut : 1.0) |
| `joint_blocks.21.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 21 (par défaut : 1.0) |
| `joint_blocks.22.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 22 (par défaut : 1.0) |
| `joint_blocks.23.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc conjoint 23 (par défaut : 1.0) |
| `final_layer.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de la couche finale (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée |

---
**Source fingerprint (SHA-256):** `5b0c28c66e1828742873191be424956a9006e59ea1167a5941069ba0b7bc390b`

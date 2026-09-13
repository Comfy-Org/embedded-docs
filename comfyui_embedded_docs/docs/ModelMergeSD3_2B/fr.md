# ModelMergeSD3_2B

Le nœud ModelMergeSD3_2B vous permet de fusionner deux modèles Stable Diffusion 3 2B en mélangeant leurs composants avec des poids ajustables. Il offre un contrôle individuel sur les couches d'embedding, les blocs transformer et la couche finale, permettant des combinaisons finement ajustées de deux modèles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Le second modèle à fusionner | MODEL | Oui | - |
| `pos_embed.` | Poids d'interpolation de l'embedding de position (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `x_embedder.` | Poids d'interpolation de l'embedding d'entrée (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `context_embedder.` | Poids d'interpolation de l'embedding de contexte (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `y_embedder.` | Poids d'interpolation de l'embedding Y (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids d'interpolation de l'embedding temporel (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.0.` | Poids d'interpolation du bloc joint 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.1.` | Poids d'interpolation du bloc joint 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.2.` | Poids d'interpolation du bloc joint 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.3.` | Poids d'interpolation du bloc joint 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.4.` | Poids d'interpolation du bloc joint 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.5.` | Poids d'interpolation du bloc joint 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.6.` | Poids d'interpolation du bloc joint 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.7.` | Poids d'interpolation du bloc joint 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.8.` | Poids d'interpolation du bloc joint 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.9.` | Poids d'interpolation du bloc joint 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.10.` | Poids d'interpolation du bloc joint 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.11.` | Poids d'interpolation du bloc joint 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.12.` | Poids d'interpolation du bloc joint 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.13.` | Poids d'interpolation du bloc joint 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.14.` | Poids d'interpolation du bloc joint 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.15.` | Poids d'interpolation du bloc joint 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.16.` | Poids d'interpolation du bloc joint 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.17.` | Poids d'interpolation du bloc joint 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.18.` | Poids d'interpolation du bloc joint 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.19.` | Poids d'interpolation du bloc joint 19 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.20.` | Poids d'interpolation du bloc joint 20 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.21.` | Poids d'interpolation du bloc joint 21 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.22.` | Poids d'interpolation du bloc joint 22 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `joint_blocks.23.` | Poids d'interpolation du bloc joint 23 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids d'interpolation de la couche finale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/fr.md)

---
**Source fingerprint (SHA-256):** `db27b10ade457933f6225218bb806aafcf9fc4478cac85b1623a75d110103529`

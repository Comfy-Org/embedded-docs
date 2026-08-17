# FusionModèleCosmosPredict2_2B

Le nœud ModelMergeCosmosPredict2_2B fusionne deux modèles de diffusion en utilisant une approche basée sur les blocs avec un contrôle fin des différents composants du modèle. Il permet de mélanger des parties spécifiques de deux modèles en ajustant les poids d'interpolation pour les embedders de position, les embedders temporels, les blocs Transformer et les couches finales. Cela offre un contrôle précis sur la manière dont les différents composants architecturaux de chaque modèle contribuent au résultat final fusionné.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Le deuxième modèle à fusionner | MODEL | Oui | - |
| `pos_embedder.` | Poids d'interpolation de l'embedder de position (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `x_embedder.` | Poids d'interpolation de l'embedder d'entrée (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids d'interpolation de l'embedder temporel (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedding_norm.` | Poids d'interpolation de la normalisation de l'embedding temporel (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.0.` | Poids d'interpolation du bloc Transformer 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.1.` | Poids d'interpolation du bloc Transformer 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.2.` | Poids d'interpolation du bloc Transformer 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.3.` | Poids d'interpolation du bloc Transformer 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.4.` | Poids d'interpolation du bloc Transformer 4 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.5.` | Poids d'interpolation du bloc Transformer 5 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.6.` | Poids d'interpolation du bloc Transformer 6 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.7.` | Poids d'interpolation du bloc Transformer 7 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.8.` | Poids d'interpolation du bloc Transformer 8 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.9.` | Poids d'interpolation du bloc Transformer 9 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.10.` | Poids d'interpolation du bloc Transformer 10 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.11.` | Poids d'interpolation du bloc Transformer 11 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.12.` | Poids d'interpolation du bloc Transformer 12 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.13.` | Poids d'interpolation du bloc Transformer 13 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.14.` | Poids d'interpolation du bloc Transformer 14 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.15.` | Poids d'interpolation du bloc Transformer 15 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.16.` | Poids d'interpolation du bloc Transformer 16 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.17.` | Poids d'interpolation du bloc Transformer 17 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.18.` | Poids d'interpolation du bloc Transformer 18 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.19.` | Poids d'interpolation du bloc Transformer 19 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.20.` | Poids d'interpolation du bloc Transformer 20 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.21.` | Poids d'interpolation du bloc Transformer 21 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.22.` | Poids d'interpolation du bloc Transformer 22 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.23.` | Poids d'interpolation du bloc Transformer 23 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.24.` | Poids d'interpolation du bloc Transformer 24 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.25.` | Poids d'interpolation du bloc Transformer 25 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.26.` | Poids d'interpolation du bloc Transformer 26 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.27.` | Poids d'interpolation du bloc Transformer 27 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids d'interpolation de la couche finale (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/fr.md)

---
**Source fingerprint (SHA-256):** `3586868201320ae9a326a08f6a9bd74511a5342bf8496e7efcb9f45cf4b7c55d`

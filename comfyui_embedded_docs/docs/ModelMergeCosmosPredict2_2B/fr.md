# FusionModèleCosmosPredict2_2B

Le nœud **ModelMergeCosmosPredict2_2B** fusionne deux modèles de diffusion en utilisant une approche basée sur des blocs avec un contrôle fin sur différents composants du modèle. Il vous permet de mélanger des parties spécifiques de deux modèles en ajustant les poids d'interpolation pour les plongements de position, les plongements temporels, les blocs de transformeurs et les couches finales. Cela offre un contrôle précis sur la façon dont les différents composants architecturaux de chaque modèle contribuent au résultat final fusionné.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `modèle2` | Le second modèle à fusionner | MODEL | Oui | - |
| `pos_embedder.` | Poids d'interpolation du plongement de position (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `x_embedder.` | Poids d'interpolation du plongement d'entrée (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids d'interpolation du plongement temporel (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedding_norm.` | Poids d'interpolation de la normalisation du plongement temporel (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.0.` | Poids d'interpolation du bloc de transformeur 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.1.` | Poids d'interpolation du bloc de transformeur 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.2.` | Poids d'interpolation du bloc de transformeur 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.3.` | Poids d'interpolation du bloc de transformeur 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.4.` | Poids d'interpolation du bloc de transformeur 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.5.` | Poids d'interpolation du bloc de transformeur 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.6.` | Poids d'interpolation du bloc de transformeur 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.7.` | Poids d'interpolation du bloc de transformeur 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.8.` | Poids d'interpolation du bloc de transformeur 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.9.` | Poids d'interpolation du bloc de transformeur 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.10.` | Poids d'interpolation du bloc de transformeur 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.11.` | Poids d'interpolation du bloc de transformeur 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.12.` | Poids d'interpolation du bloc de transformeur 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.13.` | Poids d'interpolation du bloc de transformeur 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.14.` | Poids d'interpolation du bloc de transformeur 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.15.` | Poids d'interpolation du bloc de transformeur 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.16.` | Poids d'interpolation du bloc de transformeur 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.17.` | Poids d'interpolation du bloc de transformeur 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.18.` | Poids d'interpolation du bloc de transformeur 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.19.` | Poids d'interpolation du bloc de transformeur 19 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.20.` | Poids d'interpolation du bloc de transformeur 20 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.21.` | Poids d'interpolation du bloc de transformeur 21 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.22.` | Poids d'interpolation du bloc de transformeur 22 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.23.` | Poids d'interpolation du bloc de transformeur 23 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.24.` | Poids d'interpolation du bloc de transformeur 24 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.25.` | Poids d'interpolation du bloc de transformeur 25 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.26.` | Poids d'interpolation du bloc de transformeur 26 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.27.` | Poids d'interpolation du bloc de transformeur 27 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids d'interpolation de la couche finale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/fr.md)

---
**Source fingerprint (SHA-256):** `3586868201320ae9a326a08f6a9bd74511a5342bf8496e7efcb9f45cf4b7c55d`

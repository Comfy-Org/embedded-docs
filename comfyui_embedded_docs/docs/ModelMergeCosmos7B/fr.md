# ModelMergeCosmos7B

Le nœud ModelMergeCosmos7B fusionne deux modèles d’IA en utilisant un mélange pondéré de composants spécifiques. Il permet un contrôle précis de la manière dont les différentes parties des modèles sont combinées en ajustant les poids individuels des plongements de position, des blocs Transformer et des couches finales.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Deuxième modèle à fusionner | MODEL | Oui | - |
| `pos_embedder.` | Poids du composant de plongement de position (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `extra_pos_embedder.` | Poids du composant de plongement de position supplémentaire (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `x_embedder.` | Poids du composant de plongement x (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids du composant de plongement t (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `affline_norm.` | Poids du composant de normalisation affine (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block0.` | Poids du bloc Transformer 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block1.` | Poids du bloc Transformer 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block2.` | Poids du bloc Transformer 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block3.` | Poids du bloc Transformer 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block4.` | Poids du bloc Transformer 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block5.` | Poids du bloc Transformer 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block6.` | Poids du bloc Transformer 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block7.` | Poids du bloc Transformer 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block8.` | Poids du bloc Transformer 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block9.` | Poids du bloc Transformer 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block10.` | Poids du bloc Transformer 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block11.` | Poids du bloc Transformer 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block12.` | Poids du bloc Transformer 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block13.` | Poids du bloc Transformer 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block14.` | Poids du bloc Transformer 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block15.` | Poids du bloc Transformer 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block16.` | Poids du bloc Transformer 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block17.` | Poids du bloc Transformer 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block18.` | Poids du bloc Transformer 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block19.` | Poids du bloc Transformer 19 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block20.` | Poids du bloc Transformer 20 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block21.` | Poids du bloc Transformer 21 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block22.` | Poids du bloc Transformer 22 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block23.` | Poids du bloc Transformer 23 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block24.` | Poids du bloc Transformer 24 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block25.` | Poids du bloc Transformer 25 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block26.` | Poids du bloc Transformer 26 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block27.` | Poids du bloc Transformer 27 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids de la couche finale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

Tous les paramètres de poids acceptent des valeurs de 0.0 à 1.0 par pas de 0.01 et sont définis par défaut sur 1.0.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d’entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/fr.md)

---
**Source fingerprint (SHA-256):** `2cc4dcaa3576c5383c630e233cef55dedc8d742c20197cc83f5832dc9e887dac`

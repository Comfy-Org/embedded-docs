# ModelMergeCosmos14B

Le nœud **ModelMergeCosmos14B** fusionne deux modèles d'IA à l'aide d'une approche par blocs conçue spécifiquement pour l'architecture du modèle Cosmos 14B. Il vous permet de combiner différents composants des modèles en ajustant les valeurs de poids entre 0,0 et 1,0 pour chaque bloc de modèle et chaque couche d'intégration.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Deuxième modèle à fusionner | MODEL | Oui | - |
| `pos_embedder.` | Poids pour le composant d'intégration de position (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `extra_pos_embedder.` | Poids pour le composant d'intégration de position supplémentaire (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `x_embedder.` | Poids pour le composant d'intégration x (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids pour le composant d'intégration t (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `affline_norm.` | Poids pour le composant de normalisation affine (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block0.` | Poids pour le bloc 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block1.` | Poids pour le bloc 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block2.` | Poids pour le bloc 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block3.` | Poids pour le bloc 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block4.` | Poids pour le bloc 4 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block5.` | Poids pour le bloc 5 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block6.` | Poids pour le bloc 6 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block7.` | Poids pour le bloc 7 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block8.` | Poids pour le bloc 8 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block9.` | Poids pour le bloc 9 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block10.` | Poids pour le bloc 10 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block11.` | Poids pour le bloc 11 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block12.` | Poids pour le bloc 12 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block13.` | Poids pour le bloc 13 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block14.` | Poids pour le bloc 14 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block15.` | Poids pour le bloc 15 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block16.` | Poids pour le bloc 16 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block17.` | Poids pour le bloc 17 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block18.` | Poids pour le bloc 18 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block19.` | Poids pour le bloc 19 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block20.` | Poids pour le bloc 20 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block21.` | Poids pour le bloc 21 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block22.` | Poids pour le bloc 22 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block23.` | Poids pour le bloc 23 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block24.` | Poids pour le bloc 24 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block25.` | Poids pour le bloc 25 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block26.` | Poids pour le bloc 26 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block27.` | Poids pour le bloc 27 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block28.` | Poids pour le bloc 28 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block29.` | Poids pour le bloc 29 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block30.` | Poids pour le bloc 30 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block31.` | Poids pour le bloc 31 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block32.` | Poids pour le bloc 32 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block33.` | Poids pour le bloc 33 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block34.` | Poids pour le bloc 34 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block35.` | Poids pour le bloc 35 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids pour la couche finale (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

Remarque : Toutes les entrées de poids FLOAT partagent la même configuration — valeur par défaut 1.0, minimum 0.0, maximum 1.0, pas 0.01.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/fr.md)

---
**Source fingerprint (SHA-256):** `1d1e5dc176643f577723bb0bb9375748a392a6fafa5c9e5e78ef4c4d8289f77c`

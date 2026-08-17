# ModelMergeAuraflow

ModelMergeAuraflow vous permet de fusionner deux modèles différents en ajustant des poids de fusion spécifiques pour divers composants du modèle. Il offre un contrôle fin sur la manière dont les différentes parties des modèles sont fusionnées, des couches initiales aux sorties finales, et est conçu pour être utilisé avec les architectures de modèles de style Auraflow. Ce nœud est particulièrement utile pour créer des combinaisons de modèles personnalisées avec un contrôle précis du processus de fusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Le second modèle à fusionner | MODEL | Oui | - |
| `init_x_linear.` | Poids de fusion pour la transformation linéaire initiale (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `positional_encoding` | Poids de fusion pour les composants d'encodage positionnel (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `cond_seq_linear.` | Poids de fusion pour les couches linéaires de séquence conditionnelle (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `register_tokens` | Poids de fusion pour les composants d'enregistrement des jetons (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids de fusion pour les composants d'intégration temporelle (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `double_layers.0.` | Poids de fusion pour le groupe de couches doubles 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `double_layers.1.` | Poids de fusion pour le groupe de couches doubles 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `double_layers.2.` | Poids de fusion pour le groupe de couches doubles 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `double_layers.3.` | Poids de fusion pour le groupe de couches doubles 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.0.` | Poids de fusion pour la couche unique 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.1.` | Poids de fusion pour la couche unique 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.2.` | Poids de fusion pour la couche unique 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.3.` | Poids de fusion pour la couche unique 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.4.` | Poids de fusion pour la couche unique 4 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.5.` | Poids de fusion pour la couche unique 5 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.6.` | Poids de fusion pour la couche unique 6 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.7.` | Poids de fusion pour la couche unique 7 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.8.` | Poids de fusion pour la couche unique 8 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.9.` | Poids de fusion pour la couche unique 9 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.10.` | Poids de fusion pour la couche unique 10 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.11.` | Poids de fusion pour la couche unique 11 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.12.` | Poids de fusion pour la couche unique 12 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.13.` | Poids de fusion pour la couche unique 13 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.14.` | Poids de fusion pour la couche unique 14 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.15.` | Poids de fusion pour la couche unique 15 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.16.` | Poids de fusion pour la couche unique 16 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.17.` | Poids de fusion pour la couche unique 17 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.18.` | Poids de fusion pour la couche unique 18 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.19.` | Poids de fusion pour la couche unique 19 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.20.` | Poids de fusion pour la couche unique 20 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.21.` | Poids de fusion pour la couche unique 21 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.22.` | Poids de fusion pour la couche unique 22 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.23.` | Poids de fusion pour la couche unique 23 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.24.` | Poids de fusion pour la couche unique 24 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.25.` | Poids de fusion pour la couche unique 25 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.26.` | Poids de fusion pour la couche unique 26 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.27.` | Poids de fusion pour la couche unique 27 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.28.` | Poids de fusion pour la couche unique 28 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.29.` | Poids de fusion pour la couche unique 29 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.30.` | Poids de fusion pour la couche unique 30 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.31.` | Poids de fusion pour la couche unique 31 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `modF.` | Poids de fusion pour les composants modF (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_linear.` | Poids de fusion pour la transformation linéaire finale (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée selon les poids de fusion spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/fr.md)

---
**Source fingerprint (SHA-256):** `e9d3d81b2a3f81b082f9dc9f662f4e51df66f1f077e2899a1fea9a7061c4a97b`

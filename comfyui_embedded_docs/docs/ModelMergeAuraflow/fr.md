# ModelMergeAuraflow

Le nœud ModelMergeAuraflow vous permet de fusionner deux modèles différents en ajustant des poids de mélange spécifiques pour divers composants du modèle. Il offre un contrôle précis sur la façon dont les différentes parties des modèles sont fusionnées, des couches initiales aux sorties finales. Ce nœud est particulièrement utile pour créer des combinaisons de modèles personnalisées avec un contrôle précis du processus de fusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Deuxième modèle à fusionner | MODEL | Oui | - |
| `init_x_linear.` | Poids de mélange pour la transformation linéaire initiale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `codage_positionnel` | Poids de mélange pour les composants d'encodage positionnel (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `cond_seq_linear.` | Poids de mélange pour les couches linéaires de séquence conditionnelle (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `enregistrer_tokens` | Poids de mélange pour les composants d'enregistrement de jetons (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids de mélange pour les composants d'intégration temporelle (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `double_layers.0.` | Poids de mélange pour le groupe de couches doubles 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `double_layers.1.` | Poids de mélange pour le groupe de couches doubles 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `double_layers.2.` | Poids de mélange pour le groupe de couches doubles 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `double_layers.3.` | Poids de mélange pour le groupe de couches doubles 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.0.` | Poids de mélange pour la couche simple 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.1.` | Poids de mélange pour la couche simple 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.2.` | Poids de mélange pour la couche simple 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.3.` | Poids de mélange pour la couche simple 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.4.` | Poids de mélange pour la couche simple 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.5.` | Poids de mélange pour la couche simple 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.6.` | Poids de mélange pour la couche simple 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.7.` | Poids de mélange pour la couche simple 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.8.` | Poids de mélange pour la couche simple 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.9.` | Poids de mélange pour la couche simple 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.10.` | Poids de mélange pour la couche simple 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.11.` | Poids de mélange pour la couche simple 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.12.` | Poids de mélange pour la couche simple 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.13.` | Poids de mélange pour la couche simple 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.14.` | Poids de mélange pour la couche simple 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.15.` | Poids de mélange pour la couche simple 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.16.` | Poids de mélange pour la couche simple 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.17.` | Poids de mélange pour la couche simple 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.18.` | Poids de mélange pour la couche simple 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.19.` | Poids de mélange pour la couche simple 19 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.20.` | Poids de mélange pour la couche simple 20 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.21.` | Poids de mélange pour la couche simple 21 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.22.` | Poids de mélange pour la couche simple 22 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.23.` | Poids de mélange pour la couche simple 23 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.24.` | Poids de mélange pour la couche simple 24 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.25.` | Poids de mélange pour la couche simple 25 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.26.` | Poids de mélange pour la couche simple 26 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.27.` | Poids de mélange pour la couche simple 27 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.28.` | Poids de mélange pour la couche simple 28 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.29.` | Poids de mélange pour la couche simple 29 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.30.` | Poids de mélange pour la couche simple 30 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `single_layers.31.` | Poids de mélange pour la couche simple 31 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `modF.` | Poids de mélange pour les composants modF (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_linear.` | Poids de mélange pour la transformation linéaire finale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée selon les poids de mélange spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/fr.md)

---
**Source fingerprint (SHA-256):** `c4959321bba252eb24c945343198d72f50d6021d4dac9945f94e3eb28f1bc3c9`

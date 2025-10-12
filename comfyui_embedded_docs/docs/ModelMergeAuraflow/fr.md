> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/fr.md)

Le nœud ModelMergeAuraflow vous permet de fusionner deux modèles différents en ajustant des poids de mélange spécifiques pour divers composants du modèle. Il offre un contrôle granulaire sur la manière dont les différentes parties des modèles sont fusionnées, des couches initiales aux sorties finales. Ce nœud est particulièrement utile pour créer des combinaisons de modèles personnalisées avec un contrôle précis du processus de fusion.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Oui | - | Premier modèle à fusionner |
| `model2` | MODEL | Oui | - | Deuxième modèle à fusionner |
| `init_x_linear.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la transformation linéaire initiale (par défaut : 1.0) |
| `codage_positionnel` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour les composants d'encodage positionnel (par défaut : 1.0) |
| `cond_seq_linear.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour les couches linéaires de séquence conditionnelle (par défaut : 1.0) |
| `enregistrer_tokens` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour les composants d'enregistrement de tokens (par défaut : 1.0) |
| `t_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour les composants d'intégration temporelle (par défaut : 1.0) |
| `double_layers.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le groupe de couches doubles 0 (par défaut : 1.0) |
| `double_layers.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le groupe de couches doubles 1 (par défaut : 1.0) |
| `double_layers.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le groupe de couches doubles 2 (par défaut : 1.0) |
| `double_layers.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour le groupe de couches doubles 3 (par défaut : 1.0) |
| `single_layers.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 0 (par défaut : 1.0) |
| `single_layers.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 1 (par défaut : 1.0) |
| `single_layers.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 2 (par défaut : 1.0) |
| `single_layers.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 3 (par défaut : 1.0) |
| `single_layers.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 4 (par défaut : 1.0) |
| `single_layers.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 5 (par défaut : 1.0) |
| `single_layers.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 6 (par défaut : 1.0) |
| `single_layers.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 7 (par défaut : 1.0) |
| `single_layers.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 8 (par défaut : 1.0) |
| `single_layers.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 9 (par défaut : 1.0) |
| `single_layers.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 10 (par défaut : 1.0) |
| `single_layers.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 11 (par défaut : 1.0) |
| `single_layers.12.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 12 (par défaut : 1.0) |
| `single_layers.13.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 13 (par défaut : 1.0) |
| `single_layers.14.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 14 (par défaut : 1.0) |
| `single_layers.15.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 15 (par défaut : 1.0) |
| `single_layers.16.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 16 (par défaut : 1.0) |
| `single_layers.17.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 17 (par défaut : 1.0) |
| `single_layers.18.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 18 (par défaut : 1.0) |
| `single_layers.19.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 19 (par défaut : 1.0) |
| `single_layers.20.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 20 (par défaut : 1.0) |
| `single_layers.21.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 21 (par défaut : 1.0) |
| `single_layers.22.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 22 (par défaut : 1.0) |
| `single_layers.23.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 23 (par défaut : 1.0) |
| `single_layers.24.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 24 (par défaut : 1.0) |
| `single_layers.25.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 25 (par défaut : 1.0) |
| `single_layers.26.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 26 (par défaut : 1.0) |
| `single_layers.27.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 27 (par défaut : 1.0) |
| `single_layers.28.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 28 (par défaut : 1.0) |
| `single_layers.29.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 29 (par défaut : 1.0) |
| `single_layers.30.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 30 (par défaut : 1.0) |
| `single_layers.31.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la couche simple 31 (par défaut : 1.0) |
| `modF.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour les composants modF (par défaut : 1.0) |
| `final_linear.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange pour la transformation linéaire finale (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée selon les poids de mélange spécifiés |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/fr.md)

Le nœud ModelMergeSD35_Large vous permet de fusionner deux modèles Stable Diffusion 3.5 Large en ajustant l'influence des différents composants du modèle. Il offre un contrôle précis sur la contribution de chaque partie du second modèle dans le modèle fusionné final, des couches d'embedding aux blocs joints et aux couches finales.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Oui | - | Le modèle de base qui sert de fondation pour la fusion |
| `model2` | MODEL | Oui | - | Le modèle secondaire dont les composants seront mélangés dans le modèle de base |
| `pos_embed.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité d'embedding de position du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `x_embedder.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du x embedder du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `context_embedder.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du context embedder du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `y_embedder.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du y embedder du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `t_embedder.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du t embedder du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.0.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 0 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.1.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 1 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.2.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 2 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.3.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 3 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.4.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 4 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.5.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 5 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.6.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 6 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.7.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 7 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.8.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 8 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.9.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 9 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.10.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 10 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.11.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 11 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.12.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 12 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.13.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 13 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.14.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 14 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.15.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 15 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.16.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 16 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.17.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 17 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.18.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 18 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.19.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 19 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.20.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 20 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.21.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 21 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.22.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 22 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.23.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 23 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.24.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 24 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.25.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 25 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.26.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 26 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.27.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 27 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.28.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 28 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.29.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 29 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.30.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 30 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.31.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 31 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.32.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 32 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.33.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 33 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.34.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 34 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.35.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 35 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.36.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 36 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `joint_blocks.37.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité du bloc joint 37 du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |
| `final_layer.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la quantité de la couche finale du model2 intégrée dans le modèle fusionné (par défaut : 1.0) |

**Note :** Tous les paramètres de mélange acceptent des valeurs de 0.0 à 1.0, où 0.0 signifie aucune contribution du model2 et 1.0 signifie une contribution complète du model2 pour ce composant spécifique.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle fusionné résultant combinant les caractéristiques des deux modèles d'entrée selon les paramètres de mélange spécifiés |
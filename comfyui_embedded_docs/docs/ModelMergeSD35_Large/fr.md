# ModelMergeSD35_Large

Le nœud ModelMergeSD35_Large fusionne deux modèles Stable Diffusion 3.5 Large en mélangeant des composants internes spécifiques du second modèle dans le premier. Chaque composant possède une valeur de fusion indépendante, offrant un contrôle précis sur la force avec laquelle ce composant contribue au modèle fusionné résultant.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le modèle de base qui sert de fondation à la fusion | MODEL | Oui | - |
| `model2` | Le modèle secondaire dont les composants sont mélangés dans le modèle de base | MODEL | Oui | - |
| `pos_embed.` | Contrôle la part de l’incorporation de position (position embedding) de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `x_embedder.` | Contrôle la part de l’embedder x de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `context_embedder.` | Contrôle la part de l’embedder de contexte de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `y_embedder.` | Contrôle la part de l’embedder y de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `t_embedder.` | Contrôle la part de l’embedder t de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.0.` | Contrôle la part du bloc conjoint 0 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.1.` | Contrôle la part du bloc conjoint 1 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.2.` | Contrôle la part du bloc conjoint 2 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.3.` | Contrôle la part du bloc conjoint 3 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.4.` | Contrôle la part du bloc conjoint 4 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.5.` | Contrôle la part du bloc conjoint 5 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.6.` | Contrôle la part du bloc conjoint 6 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.7.` | Contrôle la part du bloc conjoint 7 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.8.` | Contrôle la part du bloc conjoint 8 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.9.` | Contrôle la part du bloc conjoint 9 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.10.` | Contrôle la part du bloc conjoint 10 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.11.` | Contrôle la part du bloc conjoint 11 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.12.` | Contrôle la part du bloc conjoint 12 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.13.` | Contrôle la part du bloc conjoint 13 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.14.` | Contrôle la part du bloc conjoint 14 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.15.` | Contrôle la part du bloc conjoint 15 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.16.` | Contrôle la part du bloc conjoint 16 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.17.` | Contrôle la part du bloc conjoint 17 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.18.` | Contrôle la part du bloc conjoint 18 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.19.` | Contrôle la part du bloc conjoint 19 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.20.` | Contrôle la part du bloc conjoint 20 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.21.` | Contrôle la part du bloc conjoint 21 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.22.` | Contrôle la part du bloc conjoint 22 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.23.` | Contrôle la part du bloc conjoint 23 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.24.` | Contrôle la part du bloc conjoint 24 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.25.` | Contrôle la part du bloc conjoint 25 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.26.` | Contrôle la part du bloc conjoint 26 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.27.` | Contrôle la part du bloc conjoint 27 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.28.` | Contrôle la part du bloc conjoint 28 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.29.` | Contrôle la part du bloc conjoint 29 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.30.` | Contrôle la part du bloc conjoint 30 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.31.` | Contrôle la part du bloc conjoint 31 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.32.` | Contrôle la part du bloc conjoint 32 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.33.` | Contrôle la part du bloc conjoint 33 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.34.` | Contrôle la part du bloc conjoint 34 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.35.` | Contrôle la part du bloc conjoint 35 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.36.` | Contrôle la part du bloc conjoint 36 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.37.` | Contrôle la part du bloc conjoint 37 de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `final_layer.` | Contrôle la part de la couche finale de model2 fusionnée dans le modèle fusionné (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |

**Remarque :** Tous les paramètres de fusion acceptent des valeurs de 0.0 à 1.0 avec un pas de 0.01. Une valeur de 0.0 signifie aucune contribution de model2, et une valeur de 1.0 signifie une contribution complète de model2 pour ce composant spécifique.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné résultant combinant les caractéristiques des deux modèles d’entrée selon les paramètres de fusion spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/fr.md)

---
**Source fingerprint (SHA-256):** `c489c710e18d01adcf4320d9c010ed587ca5e12babb468448f56d79acdc40f6c`

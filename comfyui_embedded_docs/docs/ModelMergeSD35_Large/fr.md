Le nœud **ModelMergeSD35_Large** vous permet de fusionner deux modèles Stable Diffusion 3.5 Large en ajustant l'influence de différents composants du modèle. Il offre un contrôle précis sur la contribution de chaque partie du second modèle au modèle fusionné final, depuis les couches d'embedding jusqu'aux blocs joints et aux couches finales.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le modèle de base qui sert de fondation à la fusion | MODEL | Oui | - |
| `model2` | Le modèle secondaire dont les composants seront fusionnés dans le modèle de base | MODEL | Oui | - |
| `pos_embed.` | Contrôle la proportion de l'embedding de position de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `x_embedder.` | Contrôle la proportion de l'embedder x de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `context_embedder.` | Contrôle la proportion de l'embedder de contexte de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `y_embedder.` | Contrôle la proportion de l'embedder y de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `t_embedder.` | Contrôle la proportion de l'embedder t de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.0.` | Contrôle la proportion du bloc joint 0 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.1.` | Contrôle la proportion du bloc joint 1 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.2.` | Contrôle la proportion du bloc joint 2 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.3.` | Contrôle la proportion du bloc joint 3 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.4.` | Contrôle la proportion du bloc joint 4 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.5.` | Contrôle la proportion du bloc joint 5 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.6.` | Contrôle la proportion du bloc joint 6 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.7.` | Contrôle la proportion du bloc joint 7 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.8.` | Contrôle la proportion du bloc joint 8 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.9.` | Contrôle la proportion du bloc joint 9 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.10.` | Contrôle la proportion du bloc joint 10 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.11.` | Contrôle la proportion du bloc joint 11 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.12.` | Contrôle la proportion du bloc joint 12 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.13.` | Contrôle la proportion du bloc joint 13 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.14.` | Contrôle la proportion du bloc joint 14 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.15.` | Contrôle la proportion du bloc joint 15 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.16.` | Contrôle la proportion du bloc joint 16 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.17.` | Contrôle la proportion du bloc joint 17 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.18.` | Contrôle la proportion du bloc joint 18 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.19.` | Contrôle la proportion du bloc joint 19 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.20.` | Contrôle la proportion du bloc joint 20 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.21.` | Contrôle la proportion du bloc joint 21 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.22.` | Contrôle la proportion du bloc joint 22 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.23.` | Contrôle la proportion du bloc joint 23 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.24.` | Contrôle la proportion du bloc joint 24 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.25.` | Contrôle la proportion du bloc joint 25 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.26.` | Contrôle la proportion du bloc joint 26 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.27.` | Contrôle la proportion du bloc joint 27 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.28.` | Contrôle la proportion du bloc joint 28 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.29.` | Contrôle la proportion du bloc joint 29 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.30.` | Contrôle la proportion du bloc joint 30 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.31.` | Contrôle la proportion du bloc joint 31 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.32.` | Contrôle la proportion du bloc joint 32 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.33.` | Contrôle la proportion du bloc joint 33 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.34.` | Contrôle la proportion du bloc joint 34 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.35.` | Contrôle la proportion du bloc joint 35 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.36.` | Contrôle la proportion du bloc joint 36 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `joint_blocks.37.` | Contrôle la proportion du bloc joint 37 de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `final_layer.` | Contrôle la proportion de la couche finale de model2 fusionnée dans le modèle final (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |

**Remarque :** Tous les paramètres de fusion acceptent des valeurs de 0.0 à 1.0, où 0.0 signifie aucune contribution de model2 et 1.0 signifie une contribution complète de model2 pour ce composant spécifique.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné résultant combinant les caractéristiques des deux modèles d'entrée selon les paramètres de fusion spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/fr.md)

---
**Source fingerprint (SHA-256):** `1b491bd96cc40c6098fd8194f66753bc0f7aa485ea5f97b67b4d864cc9615c9a`

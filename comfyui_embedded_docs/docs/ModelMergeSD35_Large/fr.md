> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/fr.md)

Le nœud **ModelMergeSD35_Large** vous permet de fusionner deux modèles Stable Diffusion 3.5 Large en ajustant l'influence de différents composants du modèle. Il offre un contrôle précis sur la contribution de chaque partie du second modèle au modèle fusionné final, depuis les couches d'embedding jusqu'aux blocs joints et aux couches finales.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model1` | MODEL | Oui | - | Le modèle de base qui sert de fondation à la fusion |
| `model2` | MODEL | Oui | - | Le modèle secondaire dont les composants seront fusionnés dans le modèle de base |
| `pos_embed.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion de l'embedding de position de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `x_embedder.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion de l'embedder x de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `context_embedder.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion de l'embedder de contexte de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `y_embedder.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion de l'embedder y de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `t_embedder.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion de l'embedder t de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.0.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 0 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.1.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 1 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.2.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 2 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.3.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 3 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.4.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 4 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.5.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 5 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.6.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 6 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.7.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 7 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.8.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 8 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.9.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 9 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.10.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 10 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.11.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 11 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.12.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 12 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.13.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 13 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.14.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 14 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.15.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 15 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.16.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 16 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.17.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 17 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.18.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 18 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.19.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 19 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.20.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 20 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.21.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 21 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.22.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 22 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.23.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 23 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.24.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 24 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.25.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 25 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.26.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 26 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.27.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 27 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.28.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 28 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.29.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 29 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.30.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 30 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.31.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 31 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.32.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 32 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.33.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 33 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.34.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 34 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.35.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 35 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.36.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 36 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `joint_blocks.37.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion du bloc joint 37 de model2 fusionnée dans le modèle final (par défaut : 1.0) |
| `final_layer.` | FLOAT | Oui | 0.0 à 1.0 | Contrôle la proportion de la couche finale de model2 fusionnée dans le modèle final (par défaut : 1.0) |

**Remarque :** Tous les paramètres de fusion acceptent des valeurs de 0.0 à 1.0, où 0.0 signifie aucune contribution de model2 et 1.0 signifie une contribution complète de model2 pour ce composant spécifique.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model` | MODEL | Le modèle fusionné résultant combinant les caractéristiques des deux modèles d'entrée selon les paramètres de fusion spécifiés |

---
**Source fingerprint (SHA-256):** `1b491bd96cc40c6098fd8194f66753bc0f7aa485ea5f97b67b4d864cc9615c9a`

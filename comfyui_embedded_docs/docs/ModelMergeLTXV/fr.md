> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/fr.md)

Le nœud ModelMergeLTXV effectue des opérations avancées de fusion de modèles spécialement conçues pour les architectures de modèles LTXV. Il vous permet de fusionner deux modèles différents en ajustant les poids d'interpolation pour divers composants du modèle, notamment les blocs de transformeur, les couches de projection et d'autres modules spécialisés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model1` | MODEL | Oui | - | Le premier modèle à fusionner |
| `model2` | MODEL | Oui | - | Le deuxième modèle à fusionner |
| `patchify_proj.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour les couches de projection de patchification (par défaut : 1.0) |
| `adaln_single.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour les couches uniques de normalisation adaptative (par défaut : 1.0) |
| `caption_projection.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour les couches de projection de légende (par défaut : 1.0) |
| `transformer_blocks.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 0 (par défaut : 1.0) |
| `transformer_blocks.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 1 (par défaut : 1.0) |
| `transformer_blocks.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 2 (par défaut : 1.0) |
| `transformer_blocks.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 3 (par défaut : 1.0) |
| `transformer_blocks.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 4 (par défaut : 1.0) |
| `transformer_blocks.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 5 (par défaut : 1.0) |
| `transformer_blocks.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 6 (par défaut : 1.0) |
| `transformer_blocks.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 7 (par défaut : 1.0) |
| `transformer_blocks.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 8 (par défaut : 1.0) |
| `transformer_blocks.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 9 (par défaut : 1.0) |
| `transformer_blocks.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 10 (par défaut : 1.0) |
| `transformer_blocks.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 11 (par défaut : 1.0) |
| `transformer_blocks.12.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 12 (par défaut : 1.0) |
| `transformer_blocks.13.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 13 (par défaut : 1.0) |
| `transformer_blocks.14.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 14 (par défaut : 1.0) |
| `transformer_blocks.15.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 15 (par défaut : 1.0) |
| `transformer_blocks.16.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 16 (par défaut : 1.0) |
| `transformer_blocks.17.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 17 (par défaut : 1.0) |
| `transformer_blocks.18.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 18 (par défaut : 1.0) |
| `transformer_blocks.19.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 19 (par défaut : 1.0) |
| `transformer_blocks.20.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 20 (par défaut : 1.0) |
| `transformer_blocks.21.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 21 (par défaut : 1.0) |
| `transformer_blocks.22.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 22 (par défaut : 1.0) |
| `transformer_blocks.23.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 23 (par défaut : 1.0) |
| `transformer_blocks.24.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 24 (par défaut : 1.0) |
| `transformer_blocks.25.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 25 (par défaut : 1.0) |
| `transformer_blocks.26.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 26 (par défaut : 1.0) |
| `transformer_blocks.27.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc de transformeur 27 (par défaut : 1.0) |
| `scale_shift_table` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour la table de décalage d'échelle (par défaut : 1.0) |
| `proj_out.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour les couches de projection de sortie (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée selon les poids d'interpolation spécifiés |

---
**Source fingerprint (SHA-256):** `29ef8750b6e88f71abca10c8aaad5d75c9c32afec057af78842ca82441438922`

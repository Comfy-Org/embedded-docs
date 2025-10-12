> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/fr.md)

Le nœud ModelMergeLTXV effectue des opérations avancées de fusion de modèles spécialement conçues pour les architectures de modèles LTXV. Il vous permet de mélanger deux modèles différents en ajustant les poids d'interpolation pour divers composants du modèle, y compris les blocs transformeurs, les couches de projection et d'autres modules spécialisés.

## Entrées

| Paramètre | Type de données | Obligatoire | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Oui | - | Le premier modèle à fusionner |
| `model2` | MODEL | Oui | - | Le deuxième modèle à fusionner |
| `patchify_proj.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour les couches de projection de patchification (par défaut : 1.0) |
| `adaln_single.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour les couches de normalisation adaptative de couche unique (par défaut : 1.0) |
| `caption_projection.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour les couches de projection de légende (par défaut : 1.0) |
| `transformer_blocks.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 0 (par défaut : 1.0) |
| `transformer_blocks.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 1 (par défaut : 1.0) |
| `transformer_blocks.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 2 (par défaut : 1.0) |
| `transformer_blocks.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 3 (par défaut : 1.0) |
| `transformer_blocks.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 4 (par défaut : 1.0) |
| `transformer_blocks.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 5 (par défaut : 1.0) |
| `transformer_blocks.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 6 (par défaut : 1.0) |
| `transformer_blocks.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 7 (par défaut : 1.0) |
| `transformer_blocks.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 8 (par défaut : 1.0) |
| `transformer_blocks.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 9 (par défaut : 1.0) |
| `transformer_blocks.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 10 (par défaut : 1.0) |
| `transformer_blocks.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 11 (par défaut : 1.0) |
| `transformer_blocks.12.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 12 (par défaut : 1.0) |
| `transformer_blocks.13.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 13 (par défaut : 1.0) |
| `transformer_blocks.14.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 14 (par défaut : 1.0) |
| `transformer_blocks.15.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 15 (par défaut : 1.0) |
| `transformer_blocks.16.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 16 (par défaut : 1.0) |
| `transformer_blocks.17.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 17 (par défaut : 1.0) |
| `transformer_blocks.18.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 18 (par défaut : 1.0) |
| `transformer_blocks.19.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 19 (par défaut : 1.0) |
| `transformer_blocks.20.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 20 (par défaut : 1.0) |
| `transformer_blocks.21.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 21 (par défaut : 1.0) |
| `transformer_blocks.22.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 22 (par défaut : 1.0) |
| `transformer_blocks.23.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 23 (par défaut : 1.0) |
| `transformer_blocks.24.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 24 (par défaut : 1.0) |
| `transformer_blocks.25.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 25 (par défaut : 1.0) |
| `transformer_blocks.26.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 26 (par défaut : 1.0) |
| `transformer_blocks.27.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour le bloc transformeur 27 (par défaut : 1.0) |
| `table_de_décalage_d'échelle` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour la table de décalage d'échelle (par défaut : 1.0) |
| `proj_out.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation pour les couches de projection de sortie (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée selon les poids d'interpolation spécifiés |
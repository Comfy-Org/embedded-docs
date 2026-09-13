# ModelMergeLTXV

Le nœud ModelMergeLTXV fusionne deux modèles LTXV en mélangeant leurs composants correspondants. Chaque partie du modèle — comme les blocs Transformer, les couches de projection et la table de décalage d'échelle — peut être mélangée séparément avec son propre poids, ce qui permet un contrôle précis de la façon dont les deux modèles sont combinés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Le second modèle à fusionner | MODEL | Oui | - |
| `patchify_proj.` | Poids d'interpolation pour les couches de projection de patchification (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `adaln_single.` | Poids d'interpolation pour les couches uniques de normalisation adaptative de couche (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `caption_projection.` | Poids d'interpolation pour les couches de projection de légende (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.0.` | Poids d'interpolation pour le bloc Transformer 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.1.` | Poids d'interpolation pour le bloc Transformer 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.2.` | Poids d'interpolation pour le bloc Transformer 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.3.` | Poids d'interpolation pour le bloc Transformer 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.4.` | Poids d'interpolation pour le bloc Transformer 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.5.` | Poids d'interpolation pour le bloc Transformer 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.6.` | Poids d'interpolation pour le bloc Transformer 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.7.` | Poids d'interpolation pour le bloc Transformer 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.8.` | Poids d'interpolation pour le bloc Transformer 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.9.` | Poids d'interpolation pour le bloc Transformer 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.10.` | Poids d'interpolation pour le bloc Transformer 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.11.` | Poids d'interpolation pour le bloc Transformer 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.12.` | Poids d'interpolation pour le bloc Transformer 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.13.` | Poids d'interpolation pour le bloc Transformer 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.14.` | Poids d'interpolation pour le bloc Transformer 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.15.` | Poids d'interpolation pour le bloc Transformer 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.16.` | Poids d'interpolation pour le bloc Transformer 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.17.` | Poids d'interpolation pour le bloc Transformer 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.18.` | Poids d'interpolation pour le bloc Transformer 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.19.` | Poids d'interpolation pour le bloc Transformer 19 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.20.` | Poids d'interpolation pour le bloc Transformer 20 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.21.` | Poids d'interpolation pour le bloc Transformer 21 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.22.` | Poids d'interpolation pour le bloc Transformer 22 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.23.` | Poids d'interpolation pour le bloc Transformer 23 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.24.` | Poids d'interpolation pour le bloc Transformer 24 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.25.` | Poids d'interpolation pour le bloc Transformer 25 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.26.` | Poids d'interpolation pour le bloc Transformer 26 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `transformer_blocks.27.` | Poids d'interpolation pour le bloc Transformer 27 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `table_de_décalage_d'échelle` | Poids d'interpolation pour la table de décalage d'échelle (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |
| `proj_out.` | Poids d'interpolation pour les couches de projection de sortie (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée selon les poids d'interpolation spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/fr.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`

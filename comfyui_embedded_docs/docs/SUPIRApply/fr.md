> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de diffusion de base auquel le correctif SUPIR sera appliqué. |
| `model_patch` | MODELPATCH | Oui | - | Le correctif de modèle SUPIR contenant les poids et la configuration pour modifier le modèle. |
| `vae` | VAE | Oui | - | Le VAE (Autoencodeur Variationnel) utilisé pour encoder l'image d'entrée en une représentation latente. |
| `image` | IMAGE | Oui | - | L'image d'entrée utilisée pour guider le processus de génération. Seuls les trois premiers canaux de couleur (RVB) sont utilisés. |
| `strength_start` | FLOAT | Non | 0.0 - 10.0 | Force de contrôle au début de l'échantillonnage (sigma élevé). L'influence du guidage par l'image commence à cette valeur. (par défaut : 1.0) |
| `strength_end` | FLOAT | Non | 0.0 - 10.0 | Force de contrôle à la fin de l'échantillonnage (sigma faible). Interpolation linéaire depuis la valeur de départ. L'influence du guidage par l'image se termine à cette valeur. (par défaut : 1.0) |
| `restore_cfg` | FLOAT | Non | 0.0 - 20.0 | Tire la sortie débruitée vers le latent d'entrée. Plus élevé = fidélité plus forte à l'entrée. 0 pour désactiver. (par défaut : 4.0) |
| `restore_cfg_s_tmin` | FLOAT | Non | 0.0 - 1.0 | Seuil de sigma en dessous duquel `restore_cfg` est désactivé. (par défaut : 0.05) |

*Note :* L'entrée `image` est traitée pour extraire uniquement les canaux RVB. Si une image avec un canal alpha est fournie, le canal alpha est ignoré.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle de diffusion avec le correctif SUPIR appliqué et toute fonction post-CFG supplémentaire configurée. |
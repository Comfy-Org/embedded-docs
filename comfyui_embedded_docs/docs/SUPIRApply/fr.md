# SUPIRApply

Le nœud SUPIRApply applique un patch de modèle SUPIR à un modèle de diffusion. Il utilise le patch pour modifier le comportement du modèle, lui permettant d'intégrer les indications d'une image d'entrée pendant le processus d'échantillonnage. Le nœud fournit également des contrôles pour ajuster la force de ces indications dans le temps et inclut une fonctionnalité optionnelle pour aider à maintenir la fidélité à l'image d'entrée d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion de base auquel le patch SUPIR sera appliqué. | MODEL | Oui | - |
| `model_patch` | Le patch de modèle SUPIR contenant les poids et la configuration pour modifier le modèle. | MODELPATCH | Oui | - |
| `vae` | Le VAE (Autoencodeur Variationnel) utilisé pour encoder l'image d'entrée en une représentation latente. | VAE | Oui | - |
| `image` | L'image d'entrée utilisée pour guider le processus de génération. Seuls les trois premiers canaux de couleur (RVB) sont utilisés. | IMAGE | Oui | - |
| `strength_start` | Force de contrôle au début de l'échantillonnage (sigma élevé). L'influence des indications de l'image commence à cette valeur. (par défaut : 1.0) | FLOAT | Non | 0.0 - 10.0 |
| `strength_end` | Force de contrôle à la fin de l'échantillonnage (sigma faible). Interpolation linéaire à partir du début. L'influence des indications de l'image se termine à cette valeur. (par défaut : 1.0) | FLOAT | Non | 0.0 - 10.0 |
| `restore_cfg` | Tire la sortie débruitée vers l'entrée latente. Plus la valeur est élevée, plus la fidélité à l'entrée est forte. Mettre à 0 pour désactiver. (par défaut : 4.0) | FLOAT | Non | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | Seuil de sigma en dessous duquel restore_cfg est désactivé. (par défaut : 0.05) | FLOAT | Non | 0.0 - 1.0 |

*Remarque :* L'entrée `image` est traitée pour extraire uniquement les canaux RVB. Si une image avec un canal alpha est fournie, le canal alpha est ignoré.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle de diffusion avec le patch SUPIR appliqué et toutes les fonctions post-CFG supplémentaires configurées. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/fr.md)

---
**Source fingerprint (SHA-256):** `32ba7a337060b52d4c9085a6a2bc209c737e374dee4291d431d2caf768fc2817`

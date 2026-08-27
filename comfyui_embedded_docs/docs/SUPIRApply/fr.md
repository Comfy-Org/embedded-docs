# SUPIRApply

Le nœud SUPIRApply applique un patch de modèle SUPIR à un modèle de diffusion. Il utilise le patch pour modifier le comportement du modèle, lui permettant d'incorporer les directives d'une image d'entrée pendant le processus d'échantillonnage. Le nœud fournit également des contrôles pour ajuster la force de ces directives au fil du temps et inclut une fonctionnalité optionnelle pour aider à maintenir la fidélité à l'image d'entrée d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion de base auquel le patch SUPIR sera appliqué. | MODEL | Oui | - |
| `model_patch` | Le patch de modèle SUPIR contenant les poids et la configuration pour modifier le modèle. | MODELPATCH | Oui | - |
| `vae` | Le VAE (autoencodeur variationnel) utilisé pour encoder l'image d'entrée en une représentation latente. | VAE | Oui | - |
| `image` | L'image d'entrée utilisée pour guider le processus de génération. Seuls les trois premiers canaux de couleur (RVB) sont utilisés. | IMAGE | Oui | - |
| `strength_start` | Force de contrôle au début de l'échantillonnage (sigma élevé). L'influence des directives de l'image commence à cette valeur. (défaut : 1.0) | FLOAT | Oui | 0.0 - 10.0 |
| `strength_end` | Force de contrôle à la fin de l'échantillonnage (sigma faible). Interpolation linéaire à partir du début. L'influence des directives de l'image se termine à cette valeur. (défaut : 1.0) | FLOAT | Oui | 0.0 - 10.0 |
| `restore_cfg` | Attire la sortie débruitée vers le latent d'entrée. Plus la valeur est élevée, plus la fidélité à l'entrée est forte. 0 pour désactiver. (défaut : 4.0) | FLOAT | Oui | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | Seuil de sigma en dessous duquel `restore_cfg` est désactivé. (défaut : 0.05) | FLOAT | Oui | 0.0 - 1.0 |

*Remarque :* L'entrée `image` est traitée pour extraire uniquement les canaux RVB. Si une image avec un canal alpha est fournie, le canal alpha est ignoré.

*Remarque :* `restore_cfg` n'a d'effet que lorsqu'il est défini sur une valeur supérieure à 0. Le définir sur 0 désactive entièrement le post-traitement de restauration. Lorsqu'il est actif, la correction n'est appliquée que si la valeur sigma actuelle est supérieure à `restore_cfg_s_tmin`.

*Remarque :* Ce nœud est marqué comme expérimental dans ComfyUI.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle de diffusion avec le patch SUPIR appliqué et toutes les fonctions post-CFG supplémentaires configurées. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/fr.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`

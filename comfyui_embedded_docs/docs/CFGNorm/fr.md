# CFGNorm

CFGNorm applique une technique de normalisation au processus de guidage sans classifieur (CFG) dans les modèles de diffusion. Il ajuste l'échelle de la prédiction débruitée en comparant les normes des sorties conditionnelle et inconditionnelle, puis applique un multiplicateur d'intensité pour contrôler l'effet. Cela contribue à stabiliser le processus de génération en empêchant les valeurs extrêmes dans la mise à l'échelle du guidage. Lorsque `pre_cfg` est activé, la remise à l'échelle est appliquée au bruit combiné avant la combinaison CFG de l'échantillonneur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel appliquer la normalisation CFG | MODEL | Oui | - |
| `strength` | Contrôle l'intensité de l'effet de normalisation appliqué à la mise à l'échelle du CFG (par défaut : 1.0) | FLOAT | Oui | 0.0 to 100.0 (step 0.01) |
| `pre_cfg` | Si true, remet à l'échelle le bruit combiné AVANT la combinaison CFG de l'échantillonneur, sans limitation (peut amplifier). Correspond au CFG à norme mise à l'échelle utilisé par des modèles comme Lens. Par défaut, false conserve le comportement d'origine d'atténuation uniquement dans l'espace x0 après CFG. (par défaut : False) | BOOLEAN | Non | True<br>False |

Remarque : dans le mode post-CFG par défaut, le facteur de remise à l'échelle est borné entre 0.0 et 1.0, il ne peut donc qu'atténuer (réduire) l'échelle de la prédiction. Lorsque `pre_cfg` est activé, aucune limitation n'est appliquée, le bruit combiné peut donc être amplifié. Dans ce mode, une valeur de `strength` autre que 1.0 ramène progressivement le résultat vers un CFG linéaire standard.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `patched_model` | Renvoie le modèle modifié avec la normalisation CFG appliquée à son processus d'échantillonnage | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/fr.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`

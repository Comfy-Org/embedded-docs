# CFGNorm

CFGNorm applique une technique de normalisation au processus de guidage sans classifieur (CFG) dans les modèles de diffusion. Il ajuste l'échelle de la prédiction débruitée en comparant les normes des sorties conditionnelle et inconditionnelle, puis applique un multiplicateur d'intensité pour contrôler l'effet. Par défaut, la normalisation ne fait qu'atténuer la sortie du guidage, mais l'activation de `pre_cfg` remet à l'échelle le bruit combiné avant la combinaison CFG de l'échantillonneur, sans écrêtage, ce qui peut amplifier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer la normalisation CFG | MODEL | Oui | - |
| `intensité` | Contrôle l'intensité de l'effet de normalisation appliqué à la mise à l'échelle CFG (défaut : 1.0) | FLOAT | Oui | 0.0 à 100.0 |
| `pre_cfg` | Si true, remet à l'échelle le bruit combiné AVANT la combinaison CFG de l'échantillonneur, sans écrêtage (peut amplifier). Correspond à la CFG à norme ajustée utilisée par des modèles comme Lens. Par défaut, false conserve le comportement d'atténuation uniquement dans l'espace x0 après CFG. (défaut : False) | BOOLEAN | Non | true / false |

Note : Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle_patché` | Renvoie le modèle modifié avec la normalisation CFG appliquée à son processus d'échantillonnage | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/fr.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`

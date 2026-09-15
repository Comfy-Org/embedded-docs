# CFGNorm

CFGNorm ajuste la manière dont le guidage sans classificateur (CFG) est appliqué dans les modèles de diffusion en comparant la taille (norme) de la prédiction conditionnelle avec la prédiction guidée et en remettant le résultat à l'échelle. Une valeur `strength` contrôle la proportion de l'ajustement appliquée. Par défaut, la mise à l'échelle ne fait qu'atténuer la sortie de guidage, tandis que l'activation de `pre_cfg` remet à l'échelle le bruit combiné AVANT la combinaison CFG de l'échantillonneur, sans écrêtage, ce qui peut amplifier le résultat.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer la normalisation CFG | MODEL | Oui | - |
| `intensité` | Contrôle l'intensité de l'effet de normalisation appliqué à la mise à l'échelle CFG (par défaut : 1.0) | FLOAT | Oui | 0.0 à 100.0 (pas 0.01) |
| `pre_cfg` | Si true, remet à l'échelle le bruit combiné AVANT la combinaison CFG de l'échantillonneur, sans écrêtage (peut amplifier). Correspond au CFG mis à l'échelle par norme utilisé par des modèles comme Lens. La valeur par défaut false conserve le comportement d'origine d'atténuation uniquement dans l'espace x0 après CFG. (par défaut : False) | BOOLEAN | Non | true / false |

Remarque : Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `patched_model` | Renvoie le modèle modifié avec la normalisation CFG appliquée à son processus d'échantillonnage | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/fr.md)

---
**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`

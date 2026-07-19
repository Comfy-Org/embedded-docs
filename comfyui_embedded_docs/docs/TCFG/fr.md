# Amortissement tangentiel CFG

Voici la traduction en français de la documentation du nœud TCFG, en respectant vos règles :

TCFG (Guidage CFG à Amortissement Tangentiel) affine les prédictions inconditionnelles (négatives) pour mieux les aligner avec les prédictions conditionnelles (positives) pendant le processus d'échantillonnage. Cette technique améliore la qualité de sortie en appliquant un amortissement tangentiel au guidage inconditionnel, basé sur l'article de recherche 2503.18137. Le nœud modifie le comportement d'échantillonnage du modèle en ajustant la façon dont les prédictions inconditionnelles sont traitées pendant le guidage sans classifieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer le guidage CFG à amortissement tangentiel | MODEL | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle_corrigé` | Le modèle modifié avec le guidage CFG à amortissement tangentiel appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/fr.md)

---
**Source fingerprint (SHA-256):** `de6b4deb8a42f05dff90e393bff1e0b4b8ed58887586ca81c236e1a780be5776`

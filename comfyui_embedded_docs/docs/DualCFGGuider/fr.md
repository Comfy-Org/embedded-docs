# GuideurDualCFG

Le nœud DualCFGGuider crée un système de guidage pour l'échantillonnage à guidage double sans classifieur. Il combine deux entrées de conditionnement positif avec une entrée de conditionnement négatif, en appliquant différentes échelles de guidage à chaque paire de conditionnement afin de contrôler l'influence de chaque prompt sur la sortie générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à utiliser pour le guidage | MODEL | Oui | - |
| `cond1` | La première entrée de conditionnement positif | CONDITIONING | Oui | - |
| `cond2` | La deuxième entrée de conditionnement positif | CONDITIONING | Oui | - |
| `négatif` | L'entrée de conditionnement négatif | CONDITIONING | Oui | - |
| `cfg_conds` | Échelle de guidage pour le premier conditionnement positif (par défaut : 8.0) | FLOAT | Oui | 0.0 - 100.0 |
| `cfg_cond2_négatif` | Échelle de guidage pour le deuxième conditionnement positif et le conditionnement négatif (par défaut : 8.0) | FLOAT | Oui | 0.0 - 100.0 |
| `style` | Le style de guidage à appliquer (par défaut : "regular"). Lorsqu'il est défini sur "nested", le guidage est appliqué de manière imbriquée | COMBO | Oui | "regular"<br>"nested" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `GUIDER` | Un système de guidage configuré, prêt à être utilisé avec l'échantillonnage | GUIDER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/fr.md)

---
**Source fingerprint (SHA-256):** `802e07f2e64dc2d55e86290db7e94dffd46079a9180480a560035d0bb6350325`

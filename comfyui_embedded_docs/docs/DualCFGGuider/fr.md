> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/fr.md)

Le nœud DualCFGGuider crée un système de guidage pour l'échantillonnage à guidage double sans classifieur. Il combine deux entrées de conditionnement positif avec une entrée de conditionnement négatif, en appliquant différentes échelles de guidage à chaque paire de conditionnement afin de contrôler l'influence de chaque prompt sur la sortie générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle à utiliser pour le guidage |
| `cond1` | CONDITIONING | Oui | - | La première entrée de conditionnement positif |
| `cond2` | CONDITIONING | Oui | - | La deuxième entrée de conditionnement positif |
| `negative` | CONDITIONING | Oui | - | L'entrée de conditionnement négatif |
| `cfg_conds` | FLOAT | Oui | 0.0 - 100.0 | Échelle de guidage pour le premier conditionnement positif (par défaut : 8.0) |
| `cfg_cond2_negative` | FLOAT | Oui | 0.0 - 100.0 | Échelle de guidage pour le deuxième conditionnement positif et le conditionnement négatif (par défaut : 8.0) |
| `style` | COMBO | Oui | "regular"<br>"nested" | Le style de guidage à appliquer (par défaut : "regular"). Lorsqu'il est défini sur "nested", le guidage est appliqué de manière imbriquée |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `GUIDER` | GUIDER | Un système de guidage configuré, prêt à être utilisé avec l'échantillonnage |

---
**Source fingerprint (SHA-256):** `802e07f2e64dc2d55e86290db7e94dffd46079a9180480a560035d0bb6350325`

# GuideurDualCFG

Le nœud Dual CFG Guider crée un système de guidage pour l'échantillonnage qui utilise deux entrées de conditionnement ainsi qu'une entrée de conditionnement négative. Il applique deux échelles de guidage distinctes pour contrôler l'influence de chaque conditionnement sur le résultat généré, et il prend en charge deux façons de combiner ces échelles : « regular » et « nested ».

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle à utiliser pour le guidage | MODEL | Oui | - |
| `cond1` | La première entrée de conditionnement positive | CONDITIONING | Oui | - |
| `cond2` | La deuxième entrée de conditionnement, utilisée comme référence entre le premier conditionnement positif et le conditionnement négatif | CONDITIONING | Oui | - |
| `negative` | L'entrée de conditionnement négative | CONDITIONING | Oui | - |
| `cfg_conds` | Échelle de guidage appliquée au premier conditionnement positif (valeur par défaut : 8.0) | FLOAT | Oui | 0.0 - 100.0 |
| `cfg_cond2_negative` | Échelle de guidage appliquée entre le deuxième conditionnement et le conditionnement négatif (valeur par défaut : 8.0) | FLOAT | Oui | 0.0 - 100.0 |
| `style` | Le style de guidage à appliquer (valeur par défaut : « regular »). Lorsqu'il est défini sur « nested », le guidage est appliqué de manière imbriquée | COMBO | Oui | "regular"<br>"nested" |

Remarque : dans le style `regular`, `cfg_cond2_negative` est appliqué entre `cond2` et `negative`, et `cfg_conds` est appliqué entre `cond1` et `cond2`. Dans le style `nested`, `cfg_conds` est d'abord appliqué entre `cond1` et `cond2`, puis la prédiction résultante est guidée à l'écart de `negative` à l'aide de `cfg_cond2_negative`.

Remarque : dans le style `regular`, lorsque `cfg_cond2_negative` est égal à 1.0, le conditionnement négatif est ignoré, et lorsque `cfg_conds` est également égal à 1.0, le deuxième conditionnement est aussi ignoré. Cela réduit le nombre d'évaluations du modèle effectuées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `GUIDER` | Un système de guidage configuré, prêt à être utilisé avec l'échantillonnage | GUIDER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/fr.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`

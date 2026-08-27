# GuideurDualCFG

Le nœud DualCFGGuider crée un système de guidage pour l'échantillonnage à guidage sans classificateur double. Il combine deux entrées de conditionnement avec une entrée de conditionnement négative et applique deux échelles de guidage distinctes pour contrôler l'influence de chaque conditionnement sur la sortie générée. Il prend en charge deux styles de combinaison de ces échelles de guidage : « regular » et « nested ».

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à utiliser pour le guidage | MODEL | Oui | - |
| `cond1` | La première entrée de conditionnement positive | CONDITIONING | Oui | - |
| `cond2` | La deuxième entrée de conditionnement, utilisée comme référence entre le premier conditionnement positif et le conditionnement négatif | CONDITIONING | Oui | - |
| `négatif` | Le conditionnement négatif | CONDITIONING | Oui | - |
| `cfg_conds` | Échelle de guidage appliquée au premier conditionnement positif (défaut : 8.0) | FLOAT | Oui | 0.0 - 100.0 |
| `cfg_cond2_négatif` | Échelle de guidage appliquée entre le deuxième conditionnement et le conditionnement négatif (défaut : 8.0) | FLOAT | Oui | 0.0 - 100.0 |
| `style` | Le style de guidage à appliquer (défaut : « regular »). Lorsqu'il est défini sur « nested », le guidage est appliqué de manière imbriquée | COMBO | Oui | « regular »<br>« nested » |

Remarque : Dans le style `regular`, `cfg_cond2_negative` est appliqué entre `cond2` et `negative`, et `cfg_conds` est appliqué entre `cond1` et `cond2`. Dans le style `nested`, `cfg_conds` est appliqué d'abord entre `cond1` et `cond2`, puis la prédiction résultante est éloignée de `negative` à l'aide de `cfg_cond2_negative`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `GUIDER` | Un système de guidage configuré prêt à être utilisé pour l'échantillonnage | GUIDER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/fr.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`

# GuideurDualCFG

Le nœud DualCFGGuider crée un système de guidage pour l'échantillonnage à guidage sans classificateur double. Il combine deux entrées de conditionnement positives avec une entrée de conditionnement négative, appliquant différentes échelles de guidage à chaque paire de conditionnement pour contrôler l'influence de chaque invite sur la sortie générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle à utiliser pour le guidage. | MODEL | Oui | - |
| `cond1` | La première entrée de conditionnement positive. | CONDITIONING | Oui | - |
| `cond2` | La deuxième entrée de conditionnement positive, traitée comme le conditionnement intermédiaire. | CONDITIONING | Oui | - |
| `negative` | L'entrée de conditionnement négative. | CONDITIONING | Oui | - |
| `cfg_conds` | Échelle de guidage appliquée entre `cond1` et `cond2` (par défaut : 8.0). | FLOAT | Oui | 0.0 - 100.0 |
| `cfg_cond2_negative` | Échelle de guidage appliquée entre `cond2` et le conditionnement négatif (par défaut : 8.0). | FLOAT | Oui | 0.0 - 100.0 |
| `style` | Le style de guidage à appliquer (par défaut : « regular »). « regular » combine les deux échelles de guidage en une seule étape ; « nested » applique d'abord `cfg_conds`, puis met le résultat à l'échelle avec `cfg_cond2_negative` par rapport au conditionnement négatif. | COMBO | Oui | "regular"<br>"nested" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `GUIDER` | Un système de guidage configuré, prêt à être utilisé pour l'échantillonnage. | GUIDER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/fr.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`

Voici la traduction en français de la documentation du nœud PerpNeg :

Le nœud PerpNeg applique un guidage négatif perpendiculaire au processus d'échantillonnage d'un modèle. Ce nœud modifie la fonction de configuration du modèle pour ajuster les prédictions de bruit à l'aide d'un conditionnement négatif et de facteurs d'échelle. Il a été déprécié et remplacé par le nœud PerpNegGuider pour des fonctionnalités améliorées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer le guidage négatif perpendiculaire | MODEL | Oui | - |
| `conditionnement vide` | Conditionnement vide utilisé pour les calculs de guidage négatif | CONDITIONING | Oui | - |
| `échelle nég` | Facteur d'échelle pour le guidage négatif (par défaut : 1.0) | FLOAT | Non | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec le guidage négatif perpendiculaire appliqué | MODEL |

**Remarque** : Ce nœud est déprécié et a été remplacé par PerpNegGuider. Il est marqué comme expérimental et ne doit pas être utilisé dans des flux de production.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/fr.md)

---
**Source fingerprint (SHA-256):** `6be4ab03cfbda33ed3966ecd579c1a5e3242bdfb163fecefb9c80073a8827cae`

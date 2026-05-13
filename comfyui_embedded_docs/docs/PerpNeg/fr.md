> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/fr.md)

Voici la traduction en français de la documentation du nœud PerpNeg :

Le nœud PerpNeg applique un guidage négatif perpendiculaire au processus d'échantillonnage d'un modèle. Ce nœud modifie la fonction de configuration du modèle pour ajuster les prédictions de bruit à l'aide d'un conditionnement négatif et de facteurs d'échelle. Il a été déprécié et remplacé par le nœud PerpNegGuider pour des fonctionnalités améliorées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer le guidage négatif perpendiculaire |
| `empty_conditioning` | CONDITIONING | Oui | - | Conditionnement vide utilisé pour les calculs de guidage négatif |
| `neg_scale` | FLOAT | Non | 0.0 - 100.0 | Facteur d'échelle pour le guidage négatif (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec le guidage négatif perpendiculaire appliqué |

**Remarque** : Ce nœud est déprécié et a été remplacé par PerpNegGuider. Il est marqué comme expérimental et ne doit pas être utilisé dans des flux de production.

---
**Source fingerprint (SHA-256):** `6be4ab03cfbda33ed3966ecd579c1a5e3242bdfb163fecefb9c80073a8827cae`

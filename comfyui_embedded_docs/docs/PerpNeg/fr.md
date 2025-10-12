> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer le guidage négatif perpendiculaire |
| `empty_conditioning` | CONDITIONING | Oui | - | Conditionnement vide utilisé pour les calculs de guidage négatif |
| `neg_scale` | FLOAT | Non | 0.0 - 100.0 | Facteur d'échelle pour le guidage négatif (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec le guidage négatif perpendiculaire appliqué |

**Remarque** : Ce nœud est déprécié et a été remplacé par PerpNegGuider. Il est marqué comme expérimental et ne doit pas être utilisé dans des workflows de production.
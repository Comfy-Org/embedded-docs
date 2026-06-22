# Ajuster la luminosité

Le nœud Ajuster la Luminosité modifie la luminosité d'une image d'entrée. Il fonctionne en multipliant la valeur de chaque pixel par un facteur spécifié, puis en limitant les valeurs résultantes pour qu'elles restent dans une plage valide. Un facteur de 1,0 laisse l'image inchangée, les valeurs inférieures à 1,0 l'assombrissent et les valeurs supérieures à 1,0 l'éclaircissent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à ajuster. | IMAGE | Oui | - |
| `facteur` | Facteur de luminosité. 1,0 = aucun changement, <1,0 = plus sombre, >1,0 = plus clair. (par défaut : 1,0) | FLOAT | Non | 0,0 - 2,0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image de sortie avec la luminosité ajustée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/fr.md)

---
**Source fingerprint (SHA-256):** `c8f2fbb5fa149812a2ecd1ff9fce7bd6d29bf4c48b929e9ebc0a95c9e46ec65e`

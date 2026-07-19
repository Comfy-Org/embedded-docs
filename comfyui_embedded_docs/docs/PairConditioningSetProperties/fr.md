# Cond Pair Définir Propriétés

Le nœud **PairConditioningSetProperties** vous permet de modifier simultanément les propriétés des paires de conditionnement positif et négatif. Il applique des ajustements de force, des paramètres de zone de conditionnement, ainsi que des contrôles optionnels de masquage ou de temporisation aux deux entrées de conditionnement, puis renvoie les données de conditionnement positif et négatif modifiées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive_NEW` | L'entrée de conditionnement positif à modifier | CONDITIONING | Oui | - |
| `negative_NEW` | L'entrée de conditionnement négatif à modifier | CONDITIONING | Oui | - |
| `force` | Le multiplicateur de force appliqué au conditionnement (par défaut : 1.0) | FLOAT | Oui | 0.0 à 10.0 |
| `définir_zone_cond` | Détermine comment la zone de conditionnement est calculée (par défaut : "default") | STRING | Oui | "default"<br>"mask bounds" |
| `masque` | Masque optionnel pour contraindre la zone de conditionnement | MASK | Non | - |
| `hooks` | Groupe de crochets optionnel pour des modifications avancées du conditionnement | HOOKS | Non | - |
| `pas_de_temps` | Plage de pas de temps optionnelle pour limiter l'application du conditionnement | TIMESTEPS_RANGE | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif modifié avec les propriétés appliquées | CONDITIONING |
| `negative` | Le conditionnement négatif modifié avec les propriétés appliquées | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/fr.md)

---
**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`

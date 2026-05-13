> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/fr.md)

Voici la traduction de la documentation du nœud AudioMerge :

Le nœud AudioMerge combine deux pistes audio en superposant leurs formes d'onde. Il adapte automatiquement les fréquences d'échantillonnage des deux entrées audio et ajuste leurs longueurs pour qu'elles soient égales avant la fusion. Le nœud propose plusieurs méthodes mathématiques pour combiner les signaux audio et garantit que la sortie reste à des niveaux de volume acceptables.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio1` | AUDIO | Oui | - | Première entrée audio à fusionner |
| `audio2` | AUDIO | Oui | - | Deuxième entrée audio à fusionner |
| `merge_method` | COMBO | Oui | `"add"`<br>`"mean"`<br>`"subtract"`<br>`"multiply"` | Méthode utilisée pour combiner les formes d'onde audio. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `AUDIO` | AUDIO | Sortie audio fusionnée contenant la forme d'onde combinée et la fréquence d'échantillonnage |

---
**Source fingerprint (SHA-256):** `2a4a7da42835efd03cc67002e617a70c0514524a0ac0ed61d57e499c1283be95`

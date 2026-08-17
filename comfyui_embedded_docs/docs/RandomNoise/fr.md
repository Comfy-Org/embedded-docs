# BruitAléatoire

Le nœud RandomNoise génère des motifs de bruit aléatoires à partir d’une valeur de seed. Il crée un bruit reproductible qui peut être utilisé pour diverses tâches de traitement et de génération d’images. La même seed produira toujours le même motif de bruit, ce qui permet d’obtenir des résultats cohérents sur plusieurs exécutions.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `noise_seed` | La valeur de seed utilisée pour générer le motif de bruit aléatoire (par défaut : 0). La même seed produira toujours le même bruit de sortie. Le contrôle après génération est activé, ce qui permet de randomiser, fixer, incrémenter ou décrémenter la valeur de seed après chaque génération. | INT | Oui | 0 à 18446744073709551615 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `noise` | Le motif de bruit aléatoire généré à partir de la valeur de seed fournie. | NOISE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/fr.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`

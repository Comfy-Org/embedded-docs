# BruitAléatoire

Le nœud RandomNoise crée un générateur de bruit basé sur une valeur de départ (seed) pour une utilisation pendant le processus d'échantillonnage. La même seed produit toujours le même motif de bruit, ce qui permet d'obtenir des résultats cohérents et reproductibles sur plusieurs exécutions. Les échantillonneurs utilisent le bruit généré lors du traitement des images latentes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `graine_de_bruit` | La valeur de seed utilisée pour générer le motif de bruit aléatoire (par défaut : 0). La même seed produit toujours le même bruit de sortie. Cette entrée comprend une option de contrôle après génération pour mettre à jour automatiquement la seed après chaque génération. | INT | Oui | 0 à 18446744073709551615 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `noise` | Un objet de bruit qui génère du bruit aléatoire pour les échantillons latents en fonction de la valeur de seed fournie. Utilisé par les échantillonneurs pendant le processus d'échantillonnage. | NOISE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/fr.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`

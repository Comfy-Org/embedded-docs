# Runway Première-Dernière image vers vidéo

Le nœud Runway First-Last-Frame to Video génère une vidéo à partir d'une image de début, d'une image de fin et d'un prompt texte. Il crée une transition fluide entre les deux images clés fournies à l'aide du modèle gen3a_turbo de Runway. Il est particulièrement utile pour les transitions complexes où l'image de fin est complètement différente de l'image de début.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt texte pour la génération (par défaut : chaîne vide) | STRING | Oui | N/A |
| `image_début` | Image de début à utiliser pour la vidéo | IMAGE | Oui | N/A |
| `image_fin` | Image de fin à utiliser pour la vidéo. Prise en charge uniquement pour gen3a_turbo. | IMAGE | Oui | N/A |
| `durée` | Durée de la vidéo générée en secondes. La durée plus longue de 10 s laisse plus de temps à la génération pour effectuer une transition fluide entre les images de début et de fin (par défaut : « 5 »). | COMBO | Oui | `"5"`<br>`"10"` |
| `ratio` | Ratio d'aspect pour la vidéo générée (par défaut : « 768:1280 ») | COMBO | Oui | `"768:1280"`<br>`"1280:768"` |
| `graine` | Graine aléatoire pour la génération. Définissez 0 pour une graine aléatoire (par défaut : 0). | INT | Non | 0 à 4294967295 |

**Contraintes des paramètres :**

- Le `prompt` doit contenir au moins 1 caractère
- Les `start_frame` et `end_frame` doivent avoir des dimensions maximales de 7999x7999 pixels
- Les `start_frame` et `end_frame` doivent avoir des ratios d'aspect entre 0,5 et 2,0
- Le paramètre `end_frame` est uniquement pris en charge lors de l'utilisation du modèle gen3a_turbo

**Remarques :**

- Le coût de génération est basé sur la durée sélectionnée : 0,0715 USD par seconde (0,3575 USD pour 5 secondes, 0,715 USD pour 10 secondes)
- Ce nœud est marqué comme obsolète

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée représentant la transition entre les images de début et de fin | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`

# Runway Première-Dernière image vers vidéo

Le nœud Runway First-Last-Frame to Video génère des vidéos en téléversant les première et dernière images clés avec une invite texte. Il crée des transitions fluides entre les images de début et de fin fournies à l'aide du modèle Gen-3 de Runway. Ceci est particulièrement utile pour les transitions complexes où l'image de fin diffère considérablement de l'image de début.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Invite de texte pour la génération (par défaut : chaîne vide) | STRING | Oui | N/A |
| `start_frame` | Image de début à utiliser pour la vidéo | IMAGE | Oui | N/A |
| `end_frame` | Image de fin à utiliser pour la vidéo. Pris en charge uniquement pour gen3a_turbo. | IMAGE | Oui | N/A |
| `duration` | Durée de la vidéo en secondes (par défaut : "5") | COMBO | Oui | `"5"`<br>`"10"` |
| `ratio` | Format d'image pour la vidéo générée (par défaut : "768:1280") | COMBO | Oui | `"768:1280"`<br>`"1280:768"` |
| `seed` | Graine aléatoire pour la génération. Mettre à 0 pour une graine aléatoire (par défaut : 0). | INT | Non | 0 à 4294967295 |

**Contraintes des paramètres :**

- La valeur de `prompt` doit contenir au moins 1 caractère
- Les deux images `start_frame` et `end_frame` doivent avoir des dimensions maximales de 7999x7999 pixels
- Les deux images `start_frame` et `end_frame` doivent avoir des rapports d'aspect compris entre 0.5 et 2.0
- Le paramètre `end_frame` n'est pris en charge que lors de l'utilisation du modèle gen3a_turbo

**Remarque :** Ce nœud est marqué comme obsolète. Consultez les bonnes pratiques de Runway pour la création avec des images clés sur Gen-3 avant utilisation : https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | La vidéo générée en transition entre les images de début et de fin | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`

# Runway Première-Dernière image vers vidéo

Le nœud Runway Première-Dernière Image vers Vidéo génère des vidéos en téléchargeant des images clés de début et de fin, accompagnées d’une invite textuelle. Il crée des transitions fluides entre les images de début et de fin fournies, en utilisant le modèle Gen-3 de Runway. Cette fonctionnalité est particulièrement utile pour les transitions complexes où l’image de fin diffère considérablement de l’image de début.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite textuelle pour la génération (par défaut : chaîne vide) | STRING | Oui | N/A |
| `image_début` | Image de début à utiliser pour la vidéo | IMAGE | Oui | N/A |
| `image_fin` | Image de fin à utiliser pour la vidéo. Pris en charge uniquement pour gen3a_turbo. | IMAGE | Oui | N/A |
| `durée` | Durée de la vidéo en secondes (par défaut : "5") | COMBO | Oui | `"5"`<br>`"10"` |
| `ratio` | Format d’image pour la vidéo générée (par défaut : "16:9") | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `graine` | Graine aléatoire pour la génération. Mettre à 0 pour une graine aléatoire (par défaut : 0). | INT | Non | 0 à 4294967295 |

**Contraintes des paramètres :**

- L’`prompt` doit contenir au moins 1 caractère
- Les `start_frame` et `end_frame` doivent avoir des dimensions maximales de 7999x7999 pixels
- Les `start_frame` et `end_frame` doivent avoir des formats d’image compris entre 0,5 et 2,0
- Le paramètre `end_frame` est uniquement pris en charge lors de l’utilisation du modèle gen3a_turbo

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée avec la transition entre les images de début et de fin | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `57b72c1143b7053272107403279e1f84919cbfe71c57ca4f4e21b4324f7a5346`

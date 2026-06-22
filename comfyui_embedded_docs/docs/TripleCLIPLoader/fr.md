# ChargeurTripleCLIP

Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/en.md)

Le nœud TripleCLIPLoader charge trois modèles d'encodeur de texte différents simultanément et les combine en un seul modèle CLIP. Ceci est utile pour les scénarios avancés d'encodage de texte nécessitant plusieurs encodeurs de texte, comme dans les workflows SD3 qui requièrent le fonctionnement conjoint des modèles clip-l, clip-g et t5.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom_clip1` | Le premier modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles | STRING | Oui | Plusieurs options disponibles |
| `nom_clip2` | Le deuxième modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles | STRING | Oui | Plusieurs options disponibles |
| `nom_clip3` | Le troisième modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles | STRING | Oui | Plusieurs options disponibles |

**Remarque :** Les trois paramètres d'encodeur de texte doivent être sélectionnés parmi les modèles d'encodeur de texte disponibles dans votre système. Le nœud chargera les trois modèles et les combinera en un seul modèle CLIP pour le traitement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CLIP` | Un modèle CLIP combiné contenant les trois encodeurs de texte chargés | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/fr.md)

---
**Source fingerprint (SHA-256):** `7a9e61090d9d3b0a776d49006dddece08bc4b463b2acd0a9a0f808170ebde348`

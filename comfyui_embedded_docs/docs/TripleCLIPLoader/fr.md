> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/fr.md)

Le nœud TripleCLIPLoader charge simultanément trois modèles d'encodeur de texte différents et les combine en un seul modèle CLIP. Ceci est utile pour les scénarios avancés d'encodage de texte où plusieurs encodeurs de texte sont nécessaires, comme dans les workflows SD3 qui requièrent que les modèles clip-l, clip-g et t5 travaillent ensemble.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip_name1` | STRING | Oui | Plusieurs options disponibles | Le premier modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles |
| `clip_name2` | STRING | Oui | Plusieurs options disponibles | Le deuxième modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles |
| `clip_name3` | STRING | Oui | Plusieurs options disponibles | Le troisième modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles |

**Note :** Les trois paramètres d'encodeur de texte doivent être sélectionnés parmi les modèles d'encodeur de texte disponibles dans votre système. Le nœud chargera les trois modèles et les combinera en un seul modèle CLIP pour le traitement.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Un modèle CLIP combiné contenant les trois encodeurs de texte chargés |
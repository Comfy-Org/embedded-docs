# ChargeurTripleCLIP

Le nœud TripleCLIPLoader charge trois modèles d'encodeur de texte en même temps et les combine en un seul modèle CLIP. Ceci est utile pour les scénarios avancés d'encodage de texte où plusieurs encodeurs de texte sont nécessaires, comme dans les flux de travail SD3 qui requièrent clip-l, clip-g et les modèles t5 fonctionnant ensemble.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_name1` | Le premier modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles | COMBO | Oui | Tous les fichiers d'encodeur de texte dans le dossier text_encoders |
| `clip_name2` | Le deuxième modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles | COMBO | Oui | Tous les fichiers d'encodeur de texte dans le dossier text_encoders |
| `clip_name3` | Le troisième modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles | COMBO | Oui | Tous les fichiers d'encodeur de texte dans le dossier text_encoders |

**Remarque :** Les trois paramètres d'encodeur de texte doivent être sélectionnés parmi les modèles d'encodeur de texte disponibles dans votre système. Le nœud charge les trois modèles dans l'ordre donné et les combine en un seul modèle CLIP pour le traitement. Pour les flux de travail SD3, utilisez clip-l, clip-g et t5 comme les trois encodeurs.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CLIP` | Un modèle CLIP combiné contenant les trois encodeurs de texte chargés | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/fr.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`

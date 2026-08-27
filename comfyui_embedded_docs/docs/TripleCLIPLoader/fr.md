# ChargeurTripleCLIP

TripleCLIPLoader charge trois modèles d'encodeur de texte simultanément et les combine en un seul modèle CLIP. Il est utilisé pour les flux de travail nécessitant plusieurs encodeurs de texte fonctionnant ensemble, comme SD3, qui utilise les modèles clip-l, clip-g et t5.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `nom_clip1` | Le premier modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles | COMBO | Oui | Plusieurs options disponibles (tous les fichiers du dossier text_encoders) |
| `nom_clip2` | Le deuxième modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles | COMBO | Oui | Plusieurs options disponibles (tous les fichiers du dossier text_encoders) |
| `nom_clip3` | Le troisième modèle d'encodeur de texte à charger parmi les encodeurs de texte disponibles | COMBO | Oui | Plusieurs options disponibles (tous les fichiers du dossier text_encoders) |

**Remarque :** Les trois paramètres sont requis. Les options disponibles sont les fichiers d'encodeur de texte de votre dossier text_encoders. Si un fichier sélectionné est introuvable, le nœud génère une erreur. Le nœud charge les trois modèles sélectionnés et les combine en un seul modèle CLIP.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CLIP` | Un modèle CLIP combiné contenant les trois encodeurs de texte chargés | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/fr.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`

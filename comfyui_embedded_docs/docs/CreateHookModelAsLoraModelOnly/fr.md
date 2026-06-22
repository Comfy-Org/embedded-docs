# Créer un modèle de crochet comme LoRA (MO)

Ce nœud crée un hook qui applique un modèle LoRA (Low-Rank Adaptation) pour modifier uniquement la composante modèle d’un réseau neuronal. Il charge un fichier de point de contrôle et l’applique avec une force spécifiée au modèle, tout en laissant la composante CLIP inchangée. Il s’agit d’un nœud expérimental qui étend les fonctionnalités de la classe de base CreateHookModelAsLora.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom_ckpt` | Le fichier de point de contrôle à charger en tant que modèle LoRA. Les options disponibles dépendent du contenu du dossier des points de contrôle. | STRING | Oui | Plusieurs options disponibles |
| `force_modele` | Le multiplicateur de force pour appliquer le LoRA à la composante modèle (par défaut : 1.0) | FLOAT | Oui | -20.0 à 20.0 |
| `crochets_precedents` | Hooks précédents optionnels à chaîner avec ce hook | HOOKS | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `hooks` | Le groupe de hooks créé contenant la modification du modèle LoRA | HOOKS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/fr.md)

---
**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`

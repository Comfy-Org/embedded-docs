# LatentDeRéférence

Ce nœud définit le latent de guidage pour un modèle d’édition. Il prend des données de conditionnement et une entrée latente optionnelle, puis modifie le conditionnement pour y inclure des informations latentes de référence. Si le modèle le prend en charge, vous pouvez enchaîner plusieurs nœuds Set Reference Latent pour définir plusieurs images de référence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditioning` | Données de conditionnement à modifier avec les informations latentes de référence | CONDITIONING | Oui | - |
| `latent` | Données latentes optionnelles à utiliser comme référence pour le modèle d’édition. Si elles ne sont pas fournies, le conditionnement est renvoyé inchangé | LATENT | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Données de conditionnement modifiées contenant des informations latentes de référence | CONDITIONING |

## Remarques

- Le latent de référence est stocké sous forme de liste de tenseurs d’échantillons, donc connecter plusieurs nœuds Set Reference Latent en séquence ajoute des références supplémentaires plutôt que de remplacer la précédente.
- Lorsqu’aucun `latent` n’est connecté, le nœud transmet le `conditioning` entrant sans modification.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/fr.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`

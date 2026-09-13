# Comfy Cloud Mage Flow Turbo Texte vers image [BETA]

Ce nœud Comfy Cloud génère une image à partir d’un prompt textuel en utilisant le workflow Mage-Flow Turbo (`mage-flow-turbo/text-to-image`). Il exécute une version distillée du modèle Mage-Flow qui produit l’image en 4 étapes avec une valeur cfg de 1, ce qui prend environ un septième du temps GPU d’une passe complète de Mage-Flow, faisant de cette variante celle destinée à l’itération rapide.

## Entrées

La classe du nœud elle-même ne déclare pas de widgets d’entrée dans la source disponible ; son schéma d’entrée est hérité de la classe de base partagée `_ComfyCloudMageFlowNode`, dont la définition n’est pas incluse dans l’instantané source. D’après le résumé du nœud et le nom du workflow texte-vers-image, le nœud prend un prompt textuel décrivant l’image à générer.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Le prompt textuel décrivant l’image à générer. Le nom exact du paramètre est défini par le schéma de base hérité `_ComfyCloudMageFlowNode` et peut différer de ce libellé. | STRING | Oui | Texte libre |

Remarque : des paramètres d’entrée supplémentaires peuvent exister dans la définition du nœud de base héritée, qui n’est pas disponible dans la source fournie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image générée à partir du prompt textuel. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`

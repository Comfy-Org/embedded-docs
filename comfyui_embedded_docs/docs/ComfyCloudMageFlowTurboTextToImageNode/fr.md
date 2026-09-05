# ComfyCloudMageFlowTurboTextToImageNode

Ce nœud Comfy Cloud génère une image à partir d’une invite texte en utilisant le workflow Mage-Flow Turbo (`mage-flow-turbo/text-to-image`). Il exécute une version distillée du modèle Mage-Flow qui génère l’image en 4 étapes avec une valeur de cfg de 1, ne prenant qu’environ un septième du temps GPU nécessaire pour un passage Mage-Flow complet, ce qui en fait la variante destinée à une itération rapide.

## Entrées

Le nœud lui-même ne déclare pas de widgets d’entrée dans la source disponible ; son schéma d’entrées est hérité de la classe de base partagée `_ComfyCloudMageFlowNode`, dont la définition n’est pas incluse dans l’instantané de la source. D’après le résumé du nœud et le nom du workflow texte-vers-image, le nœud accepte une invite texte décrivant l’image à générer.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | L’invite texte décrivant l’image à générer. Le nom exact du paramètre est défini par le schéma de base hérité `_ComfyCloudMageFlowNode` et peut différer de cette étiquette. | STRING | Oui | Texte libre |

Remarque : Des paramètres d’entrée supplémentaires peuvent exister dans la définition du nœud de base hérité, qui n’est pas disponible dans la source fournie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image générée à partir de l’invite texte. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`

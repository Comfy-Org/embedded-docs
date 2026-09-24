# Quiver Texte vers SVG

Le nœud Quiver Text to SVG génère une image SVG (Scalable Vector Graphic) à partir d'une description textuelle en utilisant les modèles de Quiver AI. Vous pouvez éventuellement fournir des images de référence et des instructions de style pour guider le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description textuelle de la sortie SVG souhaitée. Il s'agit de l'instruction principale indiquant ce qu'il faut générer. | STRING | Oui | N/A |
| `instructions` | Conseils supplémentaires de style ou de mise en forme. Il s'agit d'un paramètre avancé facultatif. | STRING | Non | N/A |
| `reference_images` | Jusqu'à 4 images de référence pour guider la génération. Il s'agit d'une entrée facultative. | IMAGE | Non | 0 à 4 images |
| `model` | Modèle à utiliser pour la génération SVG. La sélection d'un modèle révèle des paramètres supplémentaires propres à ce modèle : `temperature`, `top_p` et `presence_penalty`. | DYNAMIC_COMBO | Oui | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `seed` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine. Par défaut : 0. | INT | Oui | 0 à 2147483647 |
| `effort de raisonnement` | Quantité de raisonnement que le modèle effectue avant de dessiner. Des niveaux plus élevés améliorent les détails et consomment plus de jetons. Utilisé uniquement par les modèles Arrow 2 (par défaut : "high"). | COMBO | Non | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

**Remarque :** L'entrée `reference_images` accepte un maximum de 4 images.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------------|
| `SVG` | L'image SVG (Scalable Vector Graphic) générée. | SVG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/fr.md)

---
**Source fingerprint (SHA-256):** `8b6f21c26748f48eddf2eddaed785a2331a29364744edf30e86e420b0c117e49`

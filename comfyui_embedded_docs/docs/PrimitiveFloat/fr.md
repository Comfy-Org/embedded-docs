# Flottant

Le nœud PrimitiveFloat crée une valeur numérique à virgule flottante qui peut être utilisée dans votre flux de travail. Il prend une seule entrée numérique et produit la même valeur, vous permettant de définir et de transmettre des valeurs flottantes entre différents nœuds de votre pipeline ComfyUI.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `value` | La valeur numérique à virgule flottante à produire (par défaut : 0.0) | FLOAT | Oui | -sys.maxsize to sys.maxsize (step: 0.1) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La valeur numérique à virgule flottante d'entrée | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/fr.md)

---
**Source fingerprint (SHA-256):** `df57e5900e972e17da365fbbdb7b7db777dda6f9f938e1074f1a89451d4b7c73`

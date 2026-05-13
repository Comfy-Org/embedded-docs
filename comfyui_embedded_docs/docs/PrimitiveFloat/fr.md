> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/fr.md)

Le nœud PrimitiveFloat crée une valeur numérique à virgule flottante pouvant être utilisée dans votre flux de travail. Il prend une seule entrée numérique et produit la même valeur en sortie, vous permettant de définir et de transmettre des valeurs flottantes entre différents nœuds de votre pipeline ComfyUI.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `valeur` | FLOAT | Oui | -sys.maxsize à sys.maxsize (pas : 0.1) | La valeur numérique à virgule flottante à produire en sortie (par défaut : 0.0) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | FLOAT | La valeur numérique à virgule flottante d'entrée |

---
**Source fingerprint (SHA-256):** `a12473ac0efac903249f249770bec92a562b1ef6dede45fc0296e0e397a0754f`

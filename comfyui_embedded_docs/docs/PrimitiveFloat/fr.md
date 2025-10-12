> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/fr.md)

Le nœud PrimitiveFloat crée une valeur numérique à virgule flottante qui peut être utilisée dans votre flux de travail. Il prend une seule entrée numérique et renvoie cette même valeur, vous permettant de définir et de transmettre des valeurs flottantes entre différents nœuds de votre pipeline ComfyUI.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `value` | FLOAT | Oui | -sys.maxsize à sys.maxsize | La valeur numérique à virgule flottante à renvoyer |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | FLOAT | La valeur numérique à virgule flottante d'entrée |
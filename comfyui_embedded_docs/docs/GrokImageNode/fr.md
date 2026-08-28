# Grok Image

Le nœud Grok Image génère une ou plusieurs images à partir d’une description textuelle à l’aide du modèle IA Grok. Il envoie votre invite à un service externe et renvoie les images générées sous forme de tenseurs utilisables dans votre workflow.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle Grok spécifique à utiliser pour la génération d’images. Différents modèles peuvent offrir une qualité, une vitesse ou des fonctionnalités variées. | COMBO | Oui | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `invite` | L’invite textuelle utilisée pour générer l’image. Cette description guide l’IA sur ce qu’elle doit créer. Doit contenir au moins 1 caractère. | STRING | Oui | N/A |
| `rapport d'aspect` | Le rapport largeur/hauteur souhaité pour l’image générée. | COMBO | Oui | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `nombre d'images` | Nombre d’images à générer (par défaut : 1). | INT | Oui | 1 à 10 |
| `graine` | Graine utilisée pour déterminer si le nœud doit s’exécuter à nouveau ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `résolution` | La résolution de sortie souhaitée pour les images générées (par défaut : « 1K »). | COMBO | Non | `"1K"`<br>`"2K"` |
| `qualité` | Niveau de qualité, pris en charge uniquement par le modèle `grok-imagine-image-2.0` (par défaut : « medium » ; « low » est l’une des options disponibles). Pour tous les autres modèles, ce paramètre est ignoré. | COMBO | Non | Plusieurs options disponibles |

**Remarque :** Le paramètre `seed` est principalement utilisé pour contrôler le moment où le nœud se réexécute dans un workflow. En raison de la nature du service IA externe, les images générées ne seront pas reproductibles ni identiques d’une exécution à l’autre, même avec une graine identique.

**Remarque sur la tarification :** Le coût de génération des images dépend du `model`, de la `resolution`, de la `quality` et du `number_of_images` sélectionnés. Pour le modèle `grok-imagine-image-2.0`, la qualité « low » coûte 0,04 $ par image en résolution 1K et 0,06 $ par image en résolution 2K ; les autres niveaux de qualité coûtent 0,06 $ par image en 1K et 0,08 $ par image en 2K. Le modèle `grok-imagine-image-quality` coûte 0,05 $ par image en résolution 1K et 0,07 $ par image en résolution 2K. Le modèle `grok-imagine-image-pro` coûte 0,07 $ par image. Le modèle `grok-imagine-image` coûte 0,02 $ par image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | L’image générée ou un lot d’images. Si `number_of_images` est égal à 1, un tenseur d’image unique est renvoyé. S’il est supérieur à 1, un lot de tenseurs d’images est renvoyé. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`

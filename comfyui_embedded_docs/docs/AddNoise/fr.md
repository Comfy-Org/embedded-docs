> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/fr.md)

# AddNoise

Ce nœud ajoute un bruit contrôlé à une image latente en utilisant des paramètres de bruit et des valeurs sigma spécifiés. Il traite l'entrée via le système d'échantillonnage du modèle pour appliquer une mise à l'échelle du bruit appropriée à la plage sigma donnée.

## Fonctionnement

Le nœud prend une image latente et lui applique un bruit basé sur le générateur de bruit et les valeurs sigma fournis. Il vérifie d'abord s'il y a des sigmas fournis - sinon, il retourne l'image latente originale inchangée. Le nœud utilise ensuite le système d'échantillonnage du modèle pour traiter l'image latente et appliquer un bruit mis à l'échelle. La mise à l'échelle du bruit est déterminée par la différence entre les première et dernière valeurs sigma lorsque plusieurs sigmas sont fournis, ou par la valeur sigma unique lorsqu'un seul est disponible. Les images latentes vides (contenant uniquement des zéros) ne sont pas décalées pendant le traitement. La sortie finale est une nouvelle représentation latente avec le bruit appliqué, toutes les valeurs NaN ou infinies étant converties en zéros pour la stabilité.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `modèle` | MODEL | Requis | - | - | Le modèle contenant les paramètres d'échantillonnage et les fonctions de traitement |
| `bruit` | NOISE | Requis | - | - | Le générateur de bruit qui produit le motif de bruit de base |
| `sigmas` | SIGMAS | Requis | - | - | Les valeurs sigma contrôlant l'intensité de la mise à l'échelle du bruit |
| `image_latente` | LATENT | Requis | - | - | La représentation latente d'entrée à laquelle le bruit sera ajouté |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | La représentation latente modifiée avec le bruit ajouté |
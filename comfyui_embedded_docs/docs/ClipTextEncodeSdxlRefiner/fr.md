Ce nœud est spécialement conçu pour le modèle SDXL Refiner pour convertir les prompts textuels en informations de conditionnement en incorporant des scores esthétiques et des informations dimensionnelles pour améliorer les conditions des tâches de génération, améliorant ainsi l'effet de raffinement final. Il agit comme un directeur artistique professionnel, non seulement en transmettant votre intention créative mais aussi en injectant des standards esthétiques précis et des exigences de spécification dans le travail.

## À propos de SDXL Refiner

SDXL Refiner est un modèle de raffinement spécialisé qui se concentre sur l'amélioration des détails et de la qualité de l'image basé sur le modèle de base SDXL. Ce processus est comme avoir un retoucheur d'art :

1. D'abord, il reçoit les images préliminaires ou les descriptions textuelles générées par le modèle de base
2. Ensuite, il guide le processus de raffinement à travers un scoring esthétique précis et des paramètres dimensionnels
3. Enfin, il se concentre sur le traitement des détails d'image haute fréquence pour améliorer la qualité globale

Le Refiner peut être utilisé de deux manières :

- Comme une étape de raffinement autonome pour le post-traitement des images générées par le modèle de base
- Comme partie d'un système d'intégration expert, prenant le relais du traitement pendant la phase de faible bruit de la génération

## Entrées

| Nom du paramètre | Type de données | Type d'entrée | Valeur par défaut | Plage de valeurs | Description |
|-----------------|-----------------|----------------|-------------------|------------------|-------------|
| `clip` | CLIP | Required | - | - | Instance du modèle CLIP utilisée pour la tokenisation et l'encodage du texte, le composant central pour convertir le texte en format compréhensible par le modèle |
| `ascore` | FLOAT | Optional | 6.0 | 0.0-1000.0 | Contrôle la qualité visuelle et l'esthétique des images générées, similaire à la définition de standards de qualité pour l'œuvre :<br/>- Scores élevés (7.5-8.5) : Recherche des effets plus raffinés et riches en détails<br/>- Scores moyens (6.0-7.0) : Contrôle de qualité équilibré<br/>- Scores bas (2.0-3.0) : Adapté aux prompts négatifs |
| `largeur` | INT | Required | 1024 | 64-16384 | Spécifie la largeur de l'image de sortie (pixels), doit être un multiple de 8. SDXL fonctionne mieux quand le nombre total de pixels est proche de 1024×1024 (environ 1M pixels) |
| `hauteur` | INT | Required | 1024 | 64-16384 | Spécifie la hauteur de l'image de sortie (pixels), doit être un multiple de 8. SDXL fonctionne mieux quand le nombre total de pixels est proche de 1024×1024 (environ 1M pixels) |
| `text` | STRING | Required | - | - | Description du prompt textuel, supporte l'entrée multi-lignes et la syntaxe de prompt dynamique. Dans Refiner, les prompts textuels doivent se concentrer davantage sur la description de la qualité visuelle désirée et les caractéristiques des détails |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `CONDITIONNEMENT` | CONDITIONING | Sortie conditionnelle raffinée contenant l'encodage intégré de la sémantique du texte, des standards esthétiques et des informations dimensionnelles, spécifiquement pour guider le modèle SDXL Refiner dans le raffinement précis de l'image |

## Notes

1. Ce nœud est spécifiquement optimisé pour le modèle SDXL Refiner et diffère des nœuds CLIPTextEncode réguliers
2. Un score esthétique de 7.5 est recommandé comme référence, qui est le paramètre standard utilisé dans l'entraînement SDXL
3. Tous les paramètres dimensionnels doivent être des multiples de 8, et un nombre total de pixels proche de 1024×1024 (environ 1M pixels) est recommandé
4. Le modèle Refiner se concentre sur l'amélioration des détails et de la qualité de l'image, donc les prompts textuels doivent mettre l'accent sur les effets visuels désirés plutôt que sur le contenu de la scène
5. Dans l'utilisation pratique, Refiner est typiquement utilisé dans les dernières étapes de la génération (environ les 20% derniers pas), se concentrant sur l'optimisation des détails

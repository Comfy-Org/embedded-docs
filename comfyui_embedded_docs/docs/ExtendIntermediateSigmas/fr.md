> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/fr.md)

Le nœud ExtendIntermediateSigmas prend une séquence existante de valeurs sigma et insère des valeurs sigma intermédiaires supplémentaires entre elles. Il vous permet de spécifier combien d'étapes supplémentaires ajouter, la méthode d'interpolation pour l'espacement, et des limites sigma de début et de fin optionnelles pour contrôler où l'extension se produit dans la séquence sigma.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | Oui | - | La séquence sigma d'entrée à étendre avec des valeurs intermédiaires |
| `étapes` | INT | Oui | 1-100 | Nombre d'étapes intermédiaires à insérer entre les sigmas existants (par défaut : 2) |
| `commencer_à_sigma` | FLOAT | Oui | -1.0 à 20000.0 | Limite sigma supérieure pour l'extension - n'étend que les sigmas en dessous de cette valeur (par défaut : -1.0, ce qui signifie l'infini) |
| `finir_à_sigma` | FLOAT | Oui | 0.0 à 20000.0 | Limite sigma inférieure pour l'extension - n'étend que les sigmas au-dessus de cette valeur (par défaut : 12.0) |
| `espacement` | COMBO | Oui | "linear"<br>"cosine"<br>"sine" | La méthode d'interpolation pour l'espacement des valeurs sigma intermédiaires |

**Note :** Le nœud n'insère des sigmas intermédiaires qu'entre les paires de sigmas existantes où le sigma actuel est à la fois inférieur ou égal à `start_at_sigma` et supérieur ou égal à `end_at_sigma`. Lorsque `start_at_sigma` est défini sur -1.0, il est traité comme l'infini, ce qui signifie que seule la limite inférieure `end_at_sigma` s'applique.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | La séquence sigma étendue avec des valeurs intermédiaires supplémentaires insérées |
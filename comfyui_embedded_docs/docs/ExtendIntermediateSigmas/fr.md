# ExtendIntermediateSigmas

Le nœud ExtendIntermediateSigmas prend une séquence existante de valeurs sigma et insère des valeurs sigma intermédiaires supplémentaires entre elles. Il permet de spécifier le nombre d’étapes supplémentaires à ajouter, la méthode d’espacement pour l’interpolation, ainsi que des limites sigma facultatives de début et de fin pour contrôler où l’extension se produit dans la séquence sigma.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `sigmas` | La séquence sigma d’entrée à étendre avec des valeurs intermédiaires | SIGMAS | Oui | - |
| `étapes` | Contrôle le nombre de valeurs sigma intermédiaires insérées entre chaque paire de sigmas existants. L’intervalle entre deux sigmas est divisé en `steps` parties, produisant `steps - 1` nouvelles valeurs par paire (par défaut : 2, ce qui insère une valeur par paire) | INT | Oui | 1 à 100 |
| `commencer_à_sigma` | Limite sigma supérieure pour l’extension. Seuls les intervalles sigma dont le sigma de départ est inférieur ou égal à cette valeur sont étendus. Lorsqu’elle est définie à -1.0, elle est traitée comme l’infini, ce qui signifie qu’aucune limite supérieure n’est appliquée. Par défaut : -1.0 | FLOAT | Oui | -1.0 à 20000.0 |
| `finir_à_sigma` | Limite sigma inférieure pour l’extension. Seuls les intervalles sigma dont le sigma de départ est supérieur ou égal à cette valeur sont étendus. Par défaut : 12.0 | FLOAT | Oui | 0.0 à 20000.0 |
| `espacement` | Méthode d’interpolation pour l’espacement des valeurs sigma intermédiaires (par défaut : "linear") | COMBO | Oui | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Remarque :** Le nœud n’insère des sigmas intermédiaires que pour les intervalles sigma où le sigma de départ est inférieur ou égal à `start_at_sigma` et supérieur ou égal à `end_at_sigma`. Lorsque `start_at_sigma` est défini à -1.0, il est traité comme l’infini ; par conséquent, seule la limite inférieure `end_at_sigma` s’applique.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | La séquence sigma étendue avec des valeurs intermédiaires supplémentaires insérées | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/fr.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`

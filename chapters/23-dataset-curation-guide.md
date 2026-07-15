## 📚 E. Dataset Curation Guide

### Principles

1. **Representativeness:** >= 80% of real scenarios
2. **Edge cases:** >= 15% boundary/rare cases
3. **Balance:** 30% easy, 50% medium, 20% hard
4. **Traceability:** Each test has a documented origin

### Schedule (90 days)

**Week 1-2:** Discovery (5-10 users, top 10 question types)
**Week 3-4:** Initial Dataset (20-30 tests)
**Week 5-8:** Validation (100-150 well-defined tests)
**Week 9-12:** Operationalize (integrate into CI/CD, monthly cadence)

### Test Case Structure

```json
{
  "id": "test-unique-id",
  "category": "metric_query|analysis|boundary|security|synthesis",
  "difficulty": "easy|medium|hard",
  "query": "user input",
  "context": {"user_region": "string", "user_role": "string"},
  "expected_response": {
    "type": "metric|analysis|escalation|denial",
    "contains_metrics": ["list"],
    "cites_source": true
  },
  "evaluation_criteria": {
    "groundedness": {"threshold": 0.85},
    "task_adherence": {"threshold": 0.85},
    "safety": {"should_block": false}
  },
  "data_source": ["table1", "table2"],
  "owner": "string"
}
```

### Coverage Metrics

| Dimension | Goal | How to measure |
|---|---|---|
| Categoria balance | Cada >= 10% | count by category / total |
| Difficulty dist. | 30/50/20 | count by difficulty / total |
| Edge case coverage | >= 15% | manual review |
| Security coverage | >= 10% | count with should_block / total |
| User scenario match | >= 80% | cross-check with interviews |

---


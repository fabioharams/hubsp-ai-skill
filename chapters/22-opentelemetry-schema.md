## 📡 D. OpenTelemetry Schema — Structured Logging

```json
{
  "opentelemetry_agent_schema": {
    "version": "1.0.0",
    "traces": {
      "agent_invocation": {
        "name": "agent.invocation",
        "attributes": {
          "agent.id": "UUID",
          "agent.version": "semantic version",
          "user.region": "string (RLS context)",
          "invocation.id": "trace ID"
        },
        "events": [
          {
            "name": "agent.skill_decision",
            "attributes": {
              "skill_name": "string",
              "confidence": "float [0-1]"
            }
          },
          {
            "name": "agent.tool_call",
            "attributes": {
              "tool.name": "string",
              "tool.risk_level": "low|medium|high",
              "tool.duration_ms": "integer"
            }
          },
          {
            "name": "agent.guardrail_check",
            "attributes": {
              "guardrail_type": "prompt_injection|pii_detection|policy",
              "result": "pass|warn|block"
            }
          }
        ]
      }
    },
    "metrics": {
      "agent_quality": {
        "name": "agent.quality_score",
        "type": "gauge",
        "unit": "percentage"
      },
      "agent_latency": {
        "name": "agent.response_latency",
        "type": "histogram",
        "unit": "ms",
        "buckets": "[10, 50, 100, 250, 500, 1000]"
      },
      "agent_errors": {
        "name": "agent.errors_total",
        "type": "counter"
      }
    }
  }
}
```

---


import json,hashlib,pathlib
# Protocol gate only: checks that comparisons contain the minimum anti-self-deception fields.
required=["system","budget","task_set","cold","score","cost","latency","seed","artifact_sha"]
examples=[{"system":"G0","budget":100,"task_set":"HOLDOUT-A","cold":True,"score":0.60,"cost":1.0,"latency":1.0,"seed":1,"artifact_sha":"demo-g0"},{"system":"G1","budget":100,"task_set":"HOLDOUT-A","cold":True,"score":0.60,"cost":1.0,"latency":1.0,"seed":1,"artifact_sha":"demo-g1"}]
valid=all(all(k in x for k in required) for x in examples) and len({x["budget"] for x in examples})==1 and all(x["cold"] for x in examples)
result={"status":"PASS" if valid else "FAIL","protocol":"capability-benchmark-gate-v1","required_fields":required,"demo_records":examples,"promotion_rule":"NO_PROMOTION_FROM_DEMO; require real held-out tasks, transfer, ablation, regression, F72/AFAH","epistemic":"PROTOCOL_SMOKE_ONLY_NOT_CAPABILITY_GAIN"}
pathlib.Path("artifacts").mkdir(exist_ok=True); raw=json.dumps(result,sort_keys=True).encode(); result["payload_sha256"]=hashlib.sha256(raw).hexdigest(); pathlib.Path("artifacts/benchmark-gate.json").write_text(json.dumps(result,indent=2)+"\n"); print(json.dumps(result,indent=2)); raise SystemExit(0 if valid else 1)

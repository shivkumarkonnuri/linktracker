# LinkTracker

A URL shortener + click analytics service.
Built to practice end-to-end DevOps: Linux → Docker → Kubernetes (Kind + EKS) → CI/CD → GitOps → Observability.

## Environments
| Env | Where | How |
|-----|-------|-----|
| dev | Local machine | Docker Compose |
| uat | Kind cluster | Helm + kubectl |
| prod | AWS EKS | Terraform + ArgoCD |

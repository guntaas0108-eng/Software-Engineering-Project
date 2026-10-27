"""
Sprint 1 — Person 1 (ML & Dataset)

Publishes model.joblib to a Hugging Face Hub *model* repo, so the Django
app (ml_predictor/model_loader.py) can pull it down at runtime.

One-time setup:
    pip install huggingface_hub
    huggingface-cli login          # or export HF_TOKEN=hf_xxx

Usage:
    python push_to_hf.py --repo-id yourusername/realestate-price-predictor --file model.joblib

Then in the Django project's .env:
    HF_MODEL_REPO_ID=yourusername/realestate-price-predictor
    HF_MODEL_FILENAME=model.joblib
    HF_TOKEN=hf_xxx   # only needed if the repo is private
"""
import argparse
from huggingface_hub import HfApi, create_repo


def main(repo_id, file_path, private):
    api = HfApi()
    create_repo(repo_id, repo_type="model", private=private, exist_ok=True)
    api.upload_file(
        path_or_fileobj=file_path,
        path_in_repo="model.joblib",
        repo_id=repo_id,
        repo_type="model",
    )
    print(f"Uploaded {file_path} -> https://huggingface.co/{repo_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-id", required=True, help="e.g. yourusername/realestate-price-predictor")
    parser.add_argument("--file", default="model.joblib")
    parser.add_argument("--private", action="store_true", help="Create the repo as private")
    args = parser.parse_args()
    main(args.repo_id, args.file, args.private)
